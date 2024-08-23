from dataclasses import dataclass
@dataclass(frozen=True)
class DataIngestionArtifacts:
    zip_file_path :str 
    feature_store_file_path :str 

@dataclass(frozen=True)
class DataValidationArtifacts:
    data_validation_status :bool
    accepted_folder_path : str 
    rejected_folder_path :str 
    report_file_path :str 


@dataclass
class ModelTrainerArtifact:
    trained_model_file_path: str 
    
@dataclass(frozen=True)
class ModelPusherArtifacts:
    bucket_name : str 
    s3_model_path :str