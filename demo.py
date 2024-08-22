from src.SignDetection.pipeline.training_pipeline import Pipeline
from src.SignDetection.config.configuration import ConfigurationManager
from src.SignDetection.exception import CustomException 
from src.SignDetection.logger import logging

def main():
    try:
        
        pipeline = Pipeline(config=ConfigurationManager())
        pipeline.run()


    except Exception as e:
        logging.error(f"{e}")

        

if __name__ == "__main__":
    main()