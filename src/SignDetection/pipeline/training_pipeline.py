from src.SignDetection.logger import logging 
from src.SignDetection.exception import CustomException
import os ,sys 
from src.SignDetection.config.configuration import ConfigurationManager
from src.SignDetection.components.data_validation import DataValidation 
from src.SignDetection.components.data_ingestion import DataIngestion
from src.SignDetection.components.model_trainer import ModelTrainer 
from src.SignDetection.components.model_pusher import ModelPusher
from src.SignDetection.entity.artifact_entity import DataIngestionArtifacts ,DataValidationArtifacts ,ModelTrainerArtifact ,ModelPusherArtifacts
from src.SignDetection.config.s3_operations import S3Operation
    
class Pipeline:
    def __init__(self ,config : ConfigurationManager ):
        try:
            os.makedirs(config.get_training_pipeline_config().artifact_dir ,exist_ok=True) 
            self.config = config 
        except Exception as e:
            raise CustomException(e ,sys) from e
        
    def start_data_ingestion(self) ->DataIngestionArtifacts:
        try:
            
            data_ingestion_config = self.config.get_data_ingestion_config() 

            data_ingestion = DataIngestion(config=data_ingestion_config)
            
            data_ingestion_artifacts = data_ingestion.initiate_data_ingestion()

            print('Data Ingestion Completed\n')

            return data_ingestion_artifacts
            
        except Exception as e:
            raise CustomException(e ,sys) from e 
    def start_data_validation(self ,data_ingestion_artifacts :DataIngestionArtifacts) ->DataValidationArtifacts:
        try:
            
            data_validation_config = self.config.get_data_validation_config()

            data_ingestion_artifacts = data_ingestion_artifacts
            data_validation = DataValidation(config=data_validation_config,
                                             data_ingestion_artifacts= data_ingestion_artifacts)
            data_validation_artifacts = data_validation.initiate_data_validation()
            return data_validation_artifacts
        except Exception as e:
            raise CustomException(e ,sys) from e 
        
    def start_model_training(self ,data_validation_artifacts : DataValidationArtifacts) ->ModelTrainerArtifact:
        try:
            model_training_config = self.config.get_model_training_config() 
            
            data_validation_artifacts = data_validation_artifacts
            
            model_trainer = ModelTrainer(
                config= model_training_config ,
                data_validation_artifacts= data_validation_artifacts
            )
            
            model_training_artifacts = model_trainer.initiate_model_trainer()
            
            return model_training_artifacts
        except Exception as e:
            raise CustomException(e ,sys) from e 
        
    def start_model_pusher(self, model_training_artifacts :ModelTrainerArtifact ,
                           s3: S3Operation)->ModelPusherArtifacts:
        try:
            model_pusher_config = self.config.get_model_pusher_config()
            self.model_training_artifacts = model_training_artifacts
            model_pusher = ModelPusher(
                model_training_artifact= self.model_training_artifacts,
                model_pusher_config= model_pusher_config ,
                s3= s3
            ) 
            model_pusher_artifacts = model_pusher.initiate_model_pusher()
            return model_pusher_artifacts
        except Exception as e:
            raise CustomException(e ,sys) from e 
        
    def run_pipeline(self):
        try:
            data_ingestion_artifacts = self.start_data_ingestion() 
            data_validation_artifacts = self.start_data_validation(data_ingestion_artifacts= data_ingestion_artifacts)
            
            if data_validation_artifacts.data_validation_status :
                model_training_artifacts = self.start_model_training(data_validation_artifacts= data_validation_artifacts)
                # model_pusher_artifacts = self.start_model_pusher(model_training_artifacts= model_training_artifacts,
                #                                                  s3= S3Operation())
            else:
                raise Exception ('Unable to Train model due to data is not available in necessary format')
        except Exception as e:
            raise CustomException(e ,sys) from e
    
    def run(self):
        try:
            self.run_pipeline()  
        except Exception as e:
            raise CustomException(e ,sys) from e
    