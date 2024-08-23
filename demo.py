from src.SignDetection.pipeline.training_pipeline import Pipeline
from src.SignDetection.config.configuration import ConfigurationManager
from src.SignDetection.exception import CustomException 
from src.SignDetection.logger import logging
import os ,sys 
from pathlib import Path
detect_file = Path("yolov5\detect.py")
weight_file = Path("best.pt")
img_path = Path("inputImage.jpg")
def main():
    try:
        
        pipeline = Pipeline(config=ConfigurationManager())
        pipeline.run()


    except Exception as e:
        logging.error(f"{e}")
  
def predict():
    try:
        os.system(f"python {detect_file} --weights {weight_file} --img 416 --conf 0.5 --source {img_path}") 
    except Exception as e:
        logging.error(f"{e}")
        
if __name__ == "__main__":
    main()