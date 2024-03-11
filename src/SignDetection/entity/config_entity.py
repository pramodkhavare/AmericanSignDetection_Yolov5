import os ,sys 
from src.SignDetection.constant import *
from datetime import datetime
from dataclasses import dataclass

@dataclass(frozen=True)
class DataIngestionConfig:
    data_ingestion_dir :str 
    feature_store_file_path :str 
    data_download_url :str