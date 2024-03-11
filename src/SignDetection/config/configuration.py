from src.SignDetection.entity.config_entity import DataIngestionConfig ,DataValidationConfig ,ModelTrainingConfig
from src.SignDetection.constant import *
from src.SignDetection.utils import *
import os ,sys

class ConfigurationManager():
    def __init__(self):
        create_directory([os.path.join(ROOT_DIR ,ARTIFACT_DIR)])

    def get_data_ingestion_config(self):
        data_ingestion_config = DataIngestionConfig(
            data_ingestion_dir= os.path.join(
                ROOT_DIR , ARTIFACT_DIR ,DATA_INGESTION_DIR
            ) ,
            feature_store_file_path= os.path.join(
                ROOT_DIR ,ARTIFACT_DIR ,DATA_INGESTION_DIR ,DATA_INGESTION_FEATURE_STORE
            ) ,
            data_download_url= DATA_DOWNLOAD_URL
        )

        return data_ingestion_config
    
    def get_data_validation_config(self):
        data_validation_config = DataValidationConfig(
            data_validation_dir_name=os.path.join(
                ROOT_DIR ,ARTIFACT_DIR ,DATA_VALIDATION_DIR_NAME
            ) ,
            data_validation_status_file= os.path.join(
                ROOT_DIR , ARTIFACT_DIR ,DATA_VALIDATION_DIR_NAME ,DATA_VALIDATION_STATUS_FILE
            ) ,
            data_validation_file_required=DATA_VALIDATION_ALL_FILE_REQUIRED
        )
        return data_validation_config
    
    def get_model_training_config(self):
        model_training_config = ModelTrainingConfig(
            model_trainer_dir= os.path.join(ROOT_DIR ,ARTIFACT_DIR ,MODEL_TRAINER_DIR_NAME ),
            weight_name= MODEL_TRAINER_PRETRAINED_WEIGHT_NAME ,
            no_epochs= MODEL_TRAINER_NO_EPOCHS ,
            batch_size= MODEL_TRAINER_BATCH_SIZE
        )

        return model_training_config