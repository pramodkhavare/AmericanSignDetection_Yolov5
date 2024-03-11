from src.SignDetection.entity.config_entity import DataIngestionConfig 
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





obj = ConfigurationManager()
obj.get_data_ingestion_config()