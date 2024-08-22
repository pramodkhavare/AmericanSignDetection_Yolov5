from src.SignDetection.config.configuration import ConfigurationManager 
from src.SignDetection.entity.artifact_entity import ModelTrainerArtifact ,DataValidationArtifacts
from src.SignDetection.utils import read_yaml 
from src.SignDetection.logger import logging 
from src.SignDetection.exception import CustomException 
import os ,sys ,zipfile 
import yaml 
import shutil


class ModelTrainer:
    def __init__(self ,config:ConfigurationManager ,
                 data_validation_artifacts : DataValidationArtifacts):
        self.model_training_config = config 
        self.data_validation_artifacts = data_validation_artifacts
        
    def data_preparation(self):
        try:
            input_folder_path = self.data_validation_artifacts.accepted_folder_path
            current_working_directory = os.getcwd()
            for item in os.listdir(input_folder_path):
                source = os.path.join(input_folder_path, item)
                destination = os.path.join(current_working_directory, item)
                if os.path.isdir(source):
                    shutil.copytree(source, destination, dirs_exist_ok=True)  # Copy subdirectories
                else:
                    shutil.copy2(source, destination)  # Copy files
        except Exception as e:
            raise (CustomException (e ,sys)) from e  
        
        
    def find_num_of_classes(self):
        try:
            yaml_file = os.path.join(self.data_validation_artifacts.accepted_folder_path,'data.yaml')
            with open(yaml_file , 'r') as file:
                num_classes = str(yaml.safe_load(file)['nc'])
                
            return num_classes
        except Exception as e:
            raise (CustomException (e ,sys)) from e  
        
    def update_existing_code(self,number_of_classes):
        try:
            model_config_file_name = self.model_training_config.weight_name.split(".")[0] #You will get yolov5s from these line
            
            updated_model_yaml_file_path = f"yolov5/models/{model_config_file_name}.yaml" #yolov5/models/yolov5s.yaml
            configs = read_yaml(updated_model_yaml_file_path)  
            configs['nc'] = number_of_classes   #update nc in yolov5/models/yolov5s.yaml and save in config
            
            with open(f"yolov5/models/custom_{model_config_file_name}.yaml" ,'w') as f:
                yaml.dump(configs ,f) #dump config in yolov5/models/custom_yolov5s.yaml
                
            return updated_model_yaml_file_path
        except Exception as e:
            raise (CustomException (e ,sys)) from e 
        
    def train_model(self ):
        try:
            data = self.data_preparation()
            # data_yaml_file = os.path.join(self.data_validation_artifacts.accepted_folder_path ,'data.yaml')
            os.system(f"cd yolov5/ && python train.py --img 416 --batch {self.model_training_config.batch_size} --epochs {self.model_training_config.no_epochs} --data ../data.yaml --cfg ./models/custom_yolov5s.yaml --weights {self.model_training_config.weight_name} --name yolov5s_results  --cache")
            os.system(f"cp yolov5/runs/train/yolov5s_results/weights/best.pt yolov5/") 

        except Exception as e:
            raise (CustomException (e ,sys)) from e 
    def clean_(self):
        try:
            os.system("rm -rf yolov5/runs")
            os.system("rm -rf train")
            os.system("rm -rf test")
            os.system("rm -rf data.yaml")
        
        except Exception as e:
            raise (CustomException (e ,sys)) from e  
    def initiate_model_trainer(self)->ModelTrainerArtifact :
        try:
            logging.info("Model Training step started") 
            num_classes = self.find_num_of_classes()
            updated_model_yaml_file_path = self.update_existing_code(
                number_of_classes= num_classes
            )
            
            trained_model = self.train_model()
            
            
            
            os.makedirs(self.model_training_config.model_trainer_dir, exist_ok=True)
 
            source = f"yolov5/runs/train/yolov5s_results/weights/best.pt"
            destination = self.model_training_config.model_trainer_dir
            shutil.copy(source ,destination)
            
            trained_model_file_path = os.path.join(self.model_training_config.model_trainer_dir , 'best.pt')
            
            model_trainer_artifacts = ModelTrainerArtifact(
                trained_model_file_path = trained_model_file_path
            )
            logging.info(f"Model trainer artifact: {model_trainer_artifacts}")
            logging.info("Model Training step completed") 
            self.clean_()
            return model_trainer_artifacts
            
        
        except Exception as e:
            raise (CustomException (e ,sys)) from e 

    

