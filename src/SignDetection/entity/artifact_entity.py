from dataclasses import dataclass
@dataclass(frozen=True)
class DataIngestionArtifacts:
    zip_file_path :str 
    feature_store_file_path :str 

@dataclass(frozen=True)
class DataValidationArtifacts:
    data_validation_status :bool


@dataclass
class ModelTrainerArtifact:
    trained_model_file_path: str