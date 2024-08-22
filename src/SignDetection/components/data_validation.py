from src.SignDetection.utils import * 
from src.SignDetection.logger import logging 
from src.SignDetection.exception import CustomException 
import os ,sys 
from src.SignDetection.config.configuration import ConfigurationManager
from src.SignDetection.utils import *
from src.SignDetection.entity.artifact_entity import DataValidationArtifacts ,DataIngestionArtifacts
import shutil 
from src.SignDetection.constant import *
from typing import List, Dict
import os
import json
class MissingReport:
    def __init__(self ,validation_status ,reason , available_files , required_files):
        self.validation_status = validation_status 
        self.reason = reason 
        self.available_files = available_files 
        self.required_files = required_files
    def __repr__(self):
        return (f"MissingReport(validation_status={self.validation_status}, "
                f"reason={self.reason}, available_files={self.available_files}, "
                f"required_files={self.required_files})")
    
    
class DataValidation:
    def __init__(self ,config :ConfigurationManager  ,
                 data_ingestion_artifacts :DataIngestionArtifacts,
                 ):
        try:
            self.data_validation_config = config
            self.data_ingestion_artifacts = data_ingestion_artifacts
            schema_file_path = SCHEMA_FILE_PATH
            self.schema_file_content = read_yaml(schema_file_path)
        except Exception as e:
            raise CustomException(e,sys)
        
    def validation_all_files_exist(self ,list_of_files :List)->bool :
        try:
            validation_status = None 
            all_available_files = os.listdir(
                self.data_ingestion_artifacts.feature_store_file_path
            )

            validation_status = all(element in list_of_files for element in all_available_files)
            return validation_status 

        except Exception as e:
            raise (CustomException (e ,sys))
        
    def get_report(self ,status ,reason ,required_files , available_files):
        try:

            missing_report  =MissingReport(
                validation_status= status ,
                reason= reason ,
                available_files= available_files,
                required_files= required_files
            ) 
            
            serializable_missing_report = {
                'report' : {
                     'validation_status' : status ,
                     'reason'  : reason ,
                     'available_files' : available_files,
                     'required_files'  : required_files
                }
            }

            logging.info(f"Missing report prepared: {missing_report}")
            report_file_dir = os.path.dirname(self.data_validation_config.data_validation_dir)
            os.makedirs(report_file_dir ,exist_ok=True)
            report_file_path = self.data_validation_config.data_validation_status_file
            
            with open(report_file_path, 'w') as json_file:
                json.dump(serializable_missing_report, json_file, indent=4)
            
            return serializable_missing_report
        except Exception as e:
            raise (CustomException (e ,sys))
        
    def check_file_exist(self ,filepath)->bool:
        try:
            logging.info('Checking file exist or not') 
            is_file_exist = False 
            is_file_exist = os.path.exists(filepath)
            file_path = filepath
            if not is_file_exist:
                logging.info("We Cant procees because file is not available")
                raise Exception(f"Training  File :[{file_path}] is not available")
            return is_file_exist
        except Exception as e:
            raise CustomException(e ,sys) from e 


    def initiate_data_validation(self )->ConfigurationManager:
        logging.info("Data Validation process started")
        try:
            accepted_data_dir = self.data_validation_config.accepted_data_dir 
            rejected_data_dir = self.data_validation_config.rejected_data_dir
            input_folder_path = self.data_ingestion_artifacts.feature_store_file_path 
            report_file_path = self.data_validation_config.data_validation_status_file
            
            
            check_file_exist = self.check_file_exist(filepath=input_folder_path)
            
            if check_file_exist:
                list_of_files = list(self.schema_file_content['list_of_files'])
                status = self.validation_all_files_exist(list_of_files= list_of_files)
                
                
                if status :
                    os.makedirs(accepted_data_dir ,exist_ok= True)
                    shutil.copytree(input_folder_path ,accepted_data_dir ,dirs_exist_ok=True)
                    self.get_report(status = status ,reason= "All Files Matched",
                                    required_files=list_of_files,
                                    available_files= os.listdir(
                                    self.data_ingestion_artifacts.feature_store_file_path))
                    
                else:
                    os.makedirs(rejected_data_dir ,exist_ok= True)
                    shutil.copytree(input_folder_path ,rejected_data_dir ,dirs_exist_ok=True)
                    self.get_report(status= status ,reason= "Files MisMatched",
                                    required_files=list_of_files,
                                    available_files= os.listdir(
                                    self.data_ingestion_artifacts.feature_store_file_path))
            else:
                logging.info('We cant Procees As Input Folder is Not Available') 
            
            
            logging.info(f"Validation status is {status}")

            data_validation_artifacts = DataValidationArtifacts(
                data_validation_status = status ,
                accepted_folder_path = accepted_data_dir ,
                rejected_folder_path= rejected_data_dir ,
                report_file_path= report_file_path
            )
            

            return data_validation_artifacts

        except Exception as e:
            raise CustomException(e ,sys)

        
        
    