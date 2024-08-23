from src.SignDetection.entity.config_entity import DataIngestionConfig ,DataValidationConfig ,ModelTrainingConfig ,TrainingPipelineConfig ,ModelPusherConfig
from src.SignDetection.constant import *
from src.SignDetection.utils import *
import os ,sys
from src.SignDetection.logger import logging 
from src.SignDetection.exception import CustomException

class ConfigurationManager():
    def __init__(self,
                 config_file_path = CONFIG_FILE_PATH ,
                 current_time_stamp = CURRENT_TIME_STAMP):
        try:
            self.config_file_path = config_file_path
            self.time_stamp = current_time_stamp 
            self.config_info = read_yaml(CONFIG_FILE_PATH)
            self.training_pipeline_config = self.get_training_pipeline_config()
        except Exception as e:
            raise CustomException(e,sys)
    
    def get_training_pipeline_config(self) ->TrainingPipelineConfig:
        try:
            config = self.config_info[TRAINING_PIPELINE_CONFIG]
            artifact_dir  = os.path.join(ROOT_DIR 
                                         ,config[TRAINING_PIPELINE_CONFIG_ARTIFACTS_DIR] ,
                                         self.time_stamp)
            
            training_pipeline_config = TrainingPipelineConfig(artifact_dir=artifact_dir)
            return training_pipeline_config

        except Exception as e:
            raise CustomException (e ,sys) from e

    def get_data_ingestion_config(self) ->DataIngestionConfig:
        
        try:
            config = self.config_info[DATA_INGESTION_CONFIG_KEY]
            data_ingestion_dir = os.path.join(
                self.training_pipeline_config.artifact_dir ,
                config[DATA_INGESTION_DIR_KEY]
            )
            
            feature_store_file_path = os.path.join(
                self.training_pipeline_config.artifact_dir ,
                data_ingestion_dir ,
                config[INGESTED_DIR_KEY] 
            )
            
            data_download_url = config[DATASET_DOWNLOAD_URL_KEY]
            
            data_ingestion_config = DataIngestionConfig(
                data_ingestion_dir= data_ingestion_dir,
                feature_store_file_path= feature_store_file_path,
                data_download_url= data_download_url
            )
            
            return data_ingestion_config
        except Exception as e:
            raise CustomException (e ,sys) from e
 
    
    def get_data_validation_config(self)->DataValidationConfig:
        try:
            config = self.config_info[DATA_VALIDATION_CONFIG_KEY]

            data_validation_dir = os.path.join(
                self.training_pipeline_config.artifact_dir ,
                config[DATA_VALIDATION_DIR_KEY]
            ) 
            
            data_validation_status_file = os.path.join(
                data_validation_dir ,
                config[DATA_VALIDATION_REPORT_FILE_NAME_KEY]
                
            )
            accepted_data_dir = os.path.join(
                data_validation_dir ,
                config[ACCEPTED_DATA_DIR_NAME]
            )
            rejected_data_dir = os.path.join(
                data_validation_dir , config[REJECTED_DATA_DIR_NAME]
            )

            data_validation_config = DataValidationConfig(
                data_validation_dir = data_validation_dir,
                data_validation_status_file = data_validation_status_file ,
                accepted_data_dir= accepted_data_dir,
                rejected_data_dir= rejected_data_dir
            )

            return data_validation_config
        except Exception as e:
            raise CustomException (e ,sys) from e
 
    def get_model_training_config(self)->ModelTrainingConfig:
        try:
            config = self.config_info[MODEL_TRAINING_CONFIG_KEY]
            model_trainer_dir = os.path.join(
                self.training_pipeline_config.artifact_dir ,
                config[TRAINED_MODEL_DIR_NAME_KEY],
                config[TRAINED_MODEL_ARTIFACTS_KEY]
            )
            weight_name = config[PRETRAINED_MODEL_WEIGHT_NAME]
            batch_size = config[BATCH_SIZE]
            no_epochs = config[EPOCHS]
            
            model_training_config = ModelTrainingConfig(
                model_trainer_dir= model_trainer_dir,
                weight_name= weight_name,
                no_epochs= no_epochs ,
                batch_size= batch_size
            ) 

            return model_training_config
        
        except Exception as e:
            raise CustomException (e ,sys) from e
        
    def get_model_pusher_config(self ):
        try:
            config = self.config_info[MODEL_PUSHER_CONFIG_KEY] 
            bucket_name = config[BUCKET_NAME_KEY] 
            s3_model_path = config[MODEL_NAME_KEY]
            model_pusher_config = ModelPusherConfig(
                bucket_name = bucket_name ,
                s3_model_path=  s3_model_path
            )
            return model_pusher_config
        except Exception as e:
            raise CustomException (e ,sys) from e
  