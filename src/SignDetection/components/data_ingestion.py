from src.SignDetection.utils import * 
from src.SignDetection.logger import logging 
from src.SignDetection.exception import CustomException 
import os ,sys 
from src.SignDetection.config.configuration import ConfigurationManager
from src.SignDetection.entity.artifact_entity import DataIngestionArtifacts
import gdown
from zipfile import ZipFile
class DataIngestion:
    def __init__(self , config :ConfigurationManager):
        try:
            self.config = config

        except Exception as e:
            raise CustomException( e,sys )
      
    def download_data(self):
        try:
            

            dataset_url = self.config.data_download_url
            zip_download_dir = self.config.data_ingestion_dir 
            
            os.makedirs(zip_download_dir ,exist_ok= True)
            data_file_name = 'Data.zip'
            zip_file_path = os.path.join(zip_download_dir ,data_file_name)

            gdown.download(dataset_url,zip_file_path)
            logging.info(f"Downloaded Data from {dataset_url} and stored into {zip_file_path}")

            
            return zip_file_path

        except Exception as e:
            logging.info(f'Unable to download file using url {self.config.data_download_url}')
            raise CustomException(e ,sys)
        
    def extract_zip_file(self ,zip_file_path):

        try:
            feature_store_path = self.config.feature_store_file_path 

            os.makedirs(feature_store_path ,exist_ok=True)

            with ZipFile(zip_file_path ,'r') as zip_ref:
                zip_ref.extractall(feature_store_path)

            logging.info(f"Extracted zip file at {feature_store_path}")

            return feature_store_path 

        except Exception as e:
            logging.info(f"Unable to unzip file at location {zip_file_path}")
            raise(CustomException(e ,sys))
        

    def initiate_data_ingestion(self):
        try:
            zip_file_path = self.download_data()
            feature_store_path = self.extract_zip_file(zip_file_path=zip_file_path)

            data_ingestion_artifacts = DataIngestionArtifacts(
                zip_file_path = zip_file_path ,
                feature_store_file_path = feature_store_path
            )

            return data_ingestion_artifacts
            
        except Exception as e:
            logging.info("Unable tp start data ingestion")
            raise CustomException( e ,sys)