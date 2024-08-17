import os , sys 
import cv2 
import time 
import uuid 

IMPORT_PATH = "Collected-images"

labels = ['Hello' ,'Yes' ,'No' ,'Thanks' ,"I love you" ,'Please']

no_of_images = 5         #Images for each label 


for label in labels:
    image_path = os.path.join(IMPORT_PATH ,label) 
    
    os.makedirs(image_path ,exist_ok= True)
    
    #open camera 
    capture =  cv2.VideoCapture(0)   #0 for default camera 
    
    print(f'Collecting images for {label}')
    time.sleep(3) 
    
    for imgnum in range(no_of_images):
        ret , frame = capture.read() 
        imagename = os.path.join(image_path , label + f'.{uuid.uuid1()}.jpg')
        
        cv2.imwrite(imagename ,frame)
        
        cv2.imshow('frame' ,frame)
        time.sleep(2)
        
        # Wait for 1 ms and check if the user pressed 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("Stopping the camera...")
            break 
    
    capture.release() 
    

import os
import shutil


##CODE TO COPY ALL IMAGES FROM SUBFOLDER INTO ANOTHER FOLDER :-

# # Define the source folder containing the subfolders
# source_folder = 'path_to_source_folder'

# # Define the destination folder where images will be copied
# destination_folder = 'path_to_destination_folder'

# # Ensure the destination folder exists
# os.makedirs(destination_folder, exist_ok=True)

# # Iterate through each subfolder in the source folder
# for subfolder in os.listdir(source_folder):
#     subfolder_path = os.path.join(source_folder, subfolder)
    
#     # Check if it's a directory
#     if os.path.isdir(subfolder_path):
#         # Iterate through each file in the subfolder
#         for file_name in os.listdir(subfolder_path):
#             file_path = os.path.join(subfolder_path, file_name)
            
#             # Check if the file is an image (optional, based on file extension)
#             if file_name.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
#                 # Copy the image to the destination folder
#                 shutil.copy(file_path, destination_folder)
#                 print(f"Copied {file_name} to {destination_folder}")

# print("All images have been copied.")
