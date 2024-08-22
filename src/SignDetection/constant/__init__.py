import os ,sys 
from datetime import datetime

def get_time_stamp():
    return datetime.now().strftime('%Y-%m-%d-%H-%M-%S')

ROOT_DIR = os.getcwd()


CURRENT_TIME_STAMP = f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}"
ROOT_DIR = os.getcwd()  

CONFIG_DIR = "config"
CONFIG_FILE_NAME = "config.yaml"
SCHEMA_FILE_NAME = 'schema.yaml'
CONFIG_FILE_PATH = os.path.join(ROOT_DIR , CONFIG_DIR ,CONFIG_FILE_NAME)
SCHEMA_FILE_PATH = os.path.join(ROOT_DIR , CONFIG_DIR ,SCHEMA_FILE_NAME)

#Hard Coded variable related with training pipeline
TRAINING_PIPELINE_CONFIG = 'training_pipeline_config' 
TRAINING_PIPELINE_CONFIG_PIPELINE_NAME = 'pipeline_name' 
TRAINING_PIPELINE_CONFIG_ARTIFACTS_DIR = 'artifact_dir'


#VARIABLE RELATED WITH DATA INGESTION
DATA_INGESTION_CONFIG_KEY = 'data_ingestion_config'
DATA_INGESTION_DIR_KEY = 'data_ingestion_dir'
DATASET_DOWNLOAD_URL_KEY = 'dataset_download_url'
INGESTED_DIR_KEY = 'ingested_dir'


#VARIABLE RELATED WITH DATA VALIDATION
DATA_VALIDATION_CONFIG_KEY = 'data_validation_config'
DATA_VALIDATION_DIR_KEY = 'data_validation_dir'
DATA_VALIDATION_SCHEMA_DIR_KEY = 'schema_dir'
DATA_VALIDATION_SCHEMA_FILE_KEY = 'schema_file_name'
DATA_VALIDATION_REPORT_FILE_NAME_KEY = 'report_file_name' 
ACCEPTED_DATA_DIR_NAME = 'accepted_data_dir_name'
REJECTED_DATA_DIR_NAME = 'rejected_data_dir_name'



#VARIABLE RELATED WITH DEFINING MODEL 
MODEL_TRAINING_CONFIG_KEY = "model_training_config"
TRAINED_MODEL_DIR_NAME_KEY = "trained_model_main_dir_name"
TRAINED_MODEL_ARTIFACTS_KEY = "trained_model_dir"
PRETRAINED_MODEL_WEIGHT_NAME = 'pretrained_model_weight_name'
EPOCHS = "epochs" 
BATCH_SIZE = "batch_size"


#constant related to flask api
APP_HOST = "0.0.0.0"
APP_PORT = 8000