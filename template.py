import os ,sys 
from pathlib import Path 
#Path help converting path according to OS system(terminal) 
#EX - cmd have \ where linux have / .Path will help to avoid configuration
import logging 

logging.basicConfig(level=logging.INFO , format= "[%(asctime)s]:%(message)s")

package_name = 'SignDetection'

list_of_files = [
    ".github/workflows/.gitkeep",
    "config/config.yaml" ,
    "config/schema.yaml" ,
    f"src/{package_name}/__init__.py",
    f"src/{package_name}/components/__init__.py",
    f"src/{package_name}/pipeline/__init__.py",
    f"src/{package_name}/utils/__init__.py",
    f"src/{package_name}/config/__init__.py",
    f"src/{package_name}/constant/__init__.py",
    f"src/{package_name}/entity/__init__.py",
    f"src/{package_name}/exception/__init__.py",
    f"src/{package_name}/logger/__init__.py",
    f"src/__init__.py" ,
    "requirements.txt",
    "setup.py",
    "research/trails.ipynb"
    
]

#cfg -configuration

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir ,filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir ,exist_ok=True)
        logging.info(f'Creating directory {filedir} for filename {filename}')
    

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath ,'w') as f:
            pass 
            logging.info(f"creating empty file : {filepath}") 
    else :
        logging.info(f'File is already present at : {filepath}')