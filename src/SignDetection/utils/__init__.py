from src.SignDetection.logger import logging
from src.SignDetection.exception import CustomException
import os ,sys 
from pathlib import Path 
from ensure import ensure_annotations
from box import ConfigBox
import yaml as yaml
import base64

@ensure_annotations
def read_yaml(path_to_yaml :str):
    """Code will run yaml file 
    args ==1] path_to_yaml :-path where your yaml file stored 
    """
    try:
        with open(path_to_yaml ,'rb') as yaml_file:
            content = yaml.safe_load(yaml_file)
            return content 
    except Exception as e:
        logging.info(f"Unable to read yaml file{path_to_yaml}")
        raise CustomException(e ,sys)


def write_yaml_file(file_path :str ,content: object ,replace: bool =False)->None :
    try:
        if replace:
            if os.path.exists(file_path):
                os.remove(file_path)

        os.makedirs(os.path.dirname(file_path)  ,exist_ok=True)

        with open(file_path ,'wb') as file:
            yaml.dump(content ,file)
            logging.info('Succefully Created yaml file')
    except Exception as e:
        logging.info('Unablr to create logging file')
        raise CustomException(e ,sys)
    


# def decodeImage(imgstring, fileName):
#     print(123345)
#     imgdata = base64.b64decode(imgstring)
#     print('IMG')
#     with open("../data/" + fileName, 'wb') as f:
#         print(12334)
#         f.write(imgdata)
#         f.close()
import base64
import base64
import os

def decodeImage(imgstring, fileName):
    directory = "./data/"
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Decode the base64 string
    imgdata = base64.b64decode(imgstring)
    # Write the decoded data to a file
    filePath = os.path.join(directory, fileName)
    with open(filePath, 'wb') as f:
        f.write(imgdata)


def encodeImageIntoBase64(croppedImagePath):
    with open(croppedImagePath, "rb") as f:
        return base64.b64encode(f.read())

@ensure_annotations
def create_directory(path_to_directory:list ,verbose=True):
    """Code will help to create directory"""
    try:
        for path in path_to_directory:
            os.makedirs(path ,exist_ok=True)
            if verbose:
                logging.info(f"Creted directory at {path}")
        
    except Exception as e:
        logging.info(f"Unable to create new directory {path_to_directory}")
        raise CustomException(e ,sys)
    