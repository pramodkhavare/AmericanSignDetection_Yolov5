from src.SignDetection.components.data_validation import DataValidation 
from src.SignDetection.components.data_ingestion import DataIngestion
from src.SignDetection.logger import logging
from src.SignDetection.exception import CustomException
from src.SignDetection.config.configuration import ConfigurationManager

config = ConfigurationManager()
get_data_ingestion = config.get_data_ingestion_config()

data_ingestion = DataIngestion(get_data_ingestion)
data_ingestion_artifacts = data_ingestion.initiate_data_ingestion()

get_data_validation = config.get_data_validation_config()
data_validation = DataValidation(config=get_data_validation , 
                                data_ingestion_artifacts=data_ingestion_artifacts)
data_validation.initiate_data_validation()
