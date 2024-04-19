import os
from FourierAlgorithm import fourier_transform
import cv2


dataset_folder = 'C:\\Users\\Denisa\\Desktop\\Diploma Project\\Diploma-Project\\Fourier_Medicine_App\\MIET\\resources'

for disease_folder in os.listdir(dataset_folder):
    disease_path = os.path.join(dataset_folder, disease_folder)

    for image_file in os.listdir(disease_path):
        image_path = os.path.join(disease_path, image_file)

        image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

        if image is not None:
            disease_info = {'disease': disease_folder, 'image_path': image_path}

            f_transform = fourier_transform(image)

        else:
            print(f"Failed to load image: {image_path}")

