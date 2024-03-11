#classess related with input data
import os ,sys 
from src.SignDetection.constant import *
from datetime import datetime
from dataclasses import dataclass

@dataclass(frozen=True)
class DataIngestionConfig:
    data_ingestion_dir :str 
    feature_store_file_path :str 
    data_download_url :str



@dataclass(frozen=True)
class DataValidationConfig:
    data_validation_dir_name :str 
    data_validation_status_file :str
    data_validation_file_required: list


@dataclass(frozen=True)
class ModelTrainingConfig:
    model_trainer_dir :str 
    weight_name :str 
    no_epochs :int 
    batch_size :int