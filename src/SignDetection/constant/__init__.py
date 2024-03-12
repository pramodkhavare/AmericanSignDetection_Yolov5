import os ,sys 
from datetime import datetime

def get_time_stamp():
    return datetime.now().strftime('%Y-%m-%d-%H-%M-%S')

ROOT_DIR = os.getcwd()

ARTIFACT_DIR :str = 'artifacts'


#Constatn related with data ingestion
DATA_INGESTION_DIR:str = 'DataIngestion'
DATA_INGESTION_FEATURE_STORE:str = "feature_store"
DATA_DOWNLOAD_URL :str = "https://github.com/entbappy/Branching-tutorial/raw/master/Sign_language_data.zip"



#Constant related with Data Validation
DATA_VALIDATION_DIR_NAME :str ="data_validation"
DATA_VALIDATION_STATUS_FILE :str ='status.txt'
DATA_VALIDATION_ALL_FILE_REQUIRED :list= ['train' ,'test' ,'data.yaml']



#Constant related with Model Trainer
MODEL_TRAINER_DIR_NAME :str = "Model_Trainer"
MODEL_TRAINER_PRETRAINED_WEIGHT_NAME :str = "yolov5s.pt"
MODEL_TRAINER_NO_EPOCHS :int =1 
MODEL_TRAINER_BATCH_SIZE :int =16 



#constant related to flask api
APP_HOST = "0.0.0.0"
APP_PORT = 8000