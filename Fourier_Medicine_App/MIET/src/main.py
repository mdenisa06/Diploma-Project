import cv2
import numpy as np
import matplotlib.pyplot as plt
import os
import pydicom

# Path to the dataset folder
dataset_folder = 'C:\Users\Denisa\Desktop\manifest-1709566948192'

# Traverse the dataset folder and its subfolders
for root, dirs, files in os.walk(dataset_folder):
    for file in files:
        # Check if the file is a DICOM file
        if file.endswith('.dcm'):
            # Construct the full path to the DICOM file
            dcm_file = os.path.join(root, file)

            # Load and read the DICOM file
            ds = pydicom.dcmread(dcm_file)

            # Process DICOM metadata and pixel data as needed
            # Example: print patient ID and study description
            # print("Patient ID:", ds.PatientID)
            # print("Study Description:", ds.StudyDescription)

            # Example: access pixel data (assuming it's an image)
            #image_data = ds.pixel_array

            # Perform further processing or visualization with the pixel data
