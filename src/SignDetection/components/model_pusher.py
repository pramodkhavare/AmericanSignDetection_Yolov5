from src.SignDetection.utils import * 
from src.SignDetection.logger import logging 
from src.SignDetection.exception import CustomException 
import os ,sys 
from src.SignDetection.config.configuration import ConfigurationManager
from src.SignDetection.entity.artifact_entity import ModelPusherArtifacts ,ModelTrainerArtifact
from src.SignDetection.entity.config_entity import ModelPusherConfig
import gdown
from zipfile import ZipFile 
from src.SignDetection.config.s3_operations import S3Operation 


class ModelPusher:
    def __init__(self ,model_training_artifact: ModelTrainerArtifact ,
                 model_pusher_config : ModelPusherConfig ,
                 s3 : S3Operation):
        try:
            self.model_training_artifact = model_training_artifact 
            self.model_pusher_config = model_pusher_config 
            self.s3 = s3 
        except Exception as e:
            raise CustomException( e,sys ) 
        
    def initiate_model_pusher(self)->ModelPusherArtifacts:
        try:
            """
            Method name : initiate_model_pusher .
            Description : This method will Push Model file into AWS
            Output : ModelPusherArtifact
            """ 
            logging.info('Model pusher step initiated and entered into initiate_model_pusher function')
            
            self.s3.upload_file(
                self.model_training_artifact.trained_model_file_path ,
                self.model_pusher_config.s3_model_path ,    #its only s3_model_name not path
                self.model_pusher_config.bucket_name ,
                remove= False
            )
            logging.info('MOdel is uploaded in S3 Bucket successfully')
            
            model_pusher_artifacts = ModelPusherArtifacts(
                bucket_name= self.model_pusher_config.bucket_name ,
                s3_model_path= self.model_pusher_config.s3_model_path
            )
            print('Model Pushed')
            return model_pusher_artifacts
        except Exception as e:
            raise CustomException( e,sys ) from e
      