from src.SignDetection.config.configuration import ConfigurationManager 
from src.SignDetection.entity.artifact_entity import ModelTrainerArtifact
from src.SignDetection.utils import read_yaml 
from src.SignDetection.logger import logging 
from src.SignDetection.exception import CustomException 
import os ,sys ,zipfile 
import yaml 


class ModelTrainer:
    def __init__(self ,config:ConfigurationManager ):
        self.config = config 

    def initiate_model_trainer(self)->ModelTrainerArtifact :
        logging.info("Model Training step started")
        try:

            #for bash us -
            logging.info("Unzipping data")
            os.system("unzip Data.zip")
            os.system("rm Data.zip")

            #for powershell(windows)
            # with zipfile.ZipFile('Data.zip', 'r') as zip: 
            #     zip.extractall()
            # os.system("del Data.zip")

            with open("data.yaml" , 'r') as file:
                num_classes = str(yaml.safe_load(file)['nc'])



            model_config_file_name = self.config.weight_name.split(".")[0]
            print(model_config_file_name)

            
            configs = read_yaml(f"yolov5/models/{model_config_file_name}.yaml")
            configs['nc'] = int(num_classes)

            with open(f"yolov5/models/custom_{model_config_file_name}.yaml" ,'w') as f:
                yaml.dump(configs ,f)

            #copy for windows
            os.system(f"cd yolov5/ && python train.py --img 416 --batch {self.config.batch_size} --epochs {self.config.no_epochs} --data ../data.yaml --cfg ./models/custom_yolov5s.yaml --weights {self.config.weight_name} --name yolov5s_results  --cache")
            os.system("cp yolov5/runs/train/yolov5s_results/weights/best.pt yolov5/")
            os.makedirs(self.config.model_trainer_dir, exist_ok=True)


            print("***********************")
            print(self.config.model_trainer_dir)
            print("***********************")
            print(os.getcwd())
            print("***********************")


            # os.system(f"cp yolov5/runs/train/yolov5s_results/weights/best.pt {self.config.model_trainer_dir}/")
            os.system(f"cp yolov5/runs/train/yolov5s_results/weights/best.pt ../{self.config.model_trainer_dir}/")


            # os.system("del yolov5/runs")
            # os.system("del train")
            # os.system("del valid")
            # os.system("del data.yaml")
            os.system("rm -rf yolov5/runs")
            os.system("rm -rf train")
            os.system("rm -rf test")
            os.system("rm -rf data.yaml")


            model_trainer_artifact = ModelTrainerArtifact(
                trained_model_file_path="yolov5/best.pt"
            )

            logging.info("Exited initiate_model_trainer method of ModelTrainer class")
            logging.info(f"Model trainer artifact: {model_trainer_artifact}")
            print(self.config.model_trainer_dir)

            
            return model_trainer_artifact


        except Exception as e:
            logging.info('Unable to train model')
            raise CustomException( e ,sys)

