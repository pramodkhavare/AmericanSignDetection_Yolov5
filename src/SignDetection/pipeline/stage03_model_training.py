from src.SignDetection.components.data_validation import DataValidation 
from src.SignDetection.components.data_ingestion import DataIngestion
from src.SignDetection.components.model_trainer import ModelTrainer
from src.SignDetection.logger import logging
from src.SignDetection.exception import CustomException
from src.SignDetection.config.configuration import ConfigurationManager

config = ConfigurationManager()
get_data_ingestion = config.get_data_ingestion_config()

data_ingestion = DataIngestion(get_data_ingestion)
data_ingestion_artifacts = data_ingestion.initiate_data_ingestion()

get_data_validation = config.get_data_validation_config()

data_validation = DataValidation(config=get_data_validation , 
                                data_ingestion_artifacts = data_ingestion_artifacts)
data_validation_artifacts = data_validation.initiate_data_validation()

get_model_trainer = config.get_model_training_config()

model_trainer = ModelTrainer(config=get_model_trainer)
model_trainer.initiate_model_trainer()