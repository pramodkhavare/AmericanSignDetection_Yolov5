from src.SignDetection.utils import * 
from src.SignDetection.logger import logging 
from src.SignDetection.exception import CustomException 
import os ,sys 
from src.SignDetection.config.configuration import ConfigurationManager
from src.SignDetection.utils import *
from src.SignDetection.entity.artifact_entity import DataValidationArtifacts ,DataIngestionArtifacts
import shutil



class DataValidation:
    def __init__(self ,config :ConfigurationManager  ,
                 data_ingestion_artifacts :DataIngestionArtifacts):
        try:
            self.config = config
            self.data_ingestion_artifacts = data_ingestion_artifacts
        except Exception as e:
            raise CustomException(e,sys)
        
    def validation_all_files_exist(self)->bool :
        try:
            validation_status = None 
            all_files = os.listdir(
                self.data_ingestion_artifacts.feature_store_file_path
            )

            for file in all_files:
                if file not in self.config.data_validation_file_required:
                    validation_status = False 
                    os.makedirs(self.config.data_validation_dir_name ,exist_ok=True)
                    with open(self.config.data_validation_status_file , 'w') as f:
                        f.write(f"Validation status : {validation_status}")

                else :
                    validation_status = True 
                    os.makedirs(self.config.data_validation_dir_name ,exist_ok=True)
                    with open(self.config.data_validation_status_file , 'w') as f:
                        f.write(f"Validation status : {validation_status}")
            return validation_status


        except Exception as e:
            logging.info("Unable to validate data")
            raise (CustomException (e ,sys))
    

    def initiate_data_validation(self)->ConfigurationManager:
        logging.info("Data Validation process started")
        try:
            status = self.validation_all_files_exist()
            logging.info(f"Validation status is {status}")

            data_validation_artifacts = DataValidationArtifacts(
                data_validation_status = status
            )

            if status :
                shutil.copy(self.data_ingestion_artifacts.zip_file_path ,os.getcwd())
                
            return data_validation_artifacts

        except Exception as e:
            raise CustomException(e ,sys)

        
        
    