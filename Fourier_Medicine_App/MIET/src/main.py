import os

# Path to the dataset folder
dataset_folder = 'C:\\Users\\Denisa\\Desktop\\Diploma Project\\Diploma-Project\\Fourier_Medicine_App\\MIET\\resources'


# Traverse the dataset folder and its subfolders
for root, dirs, files in os.walk(dataset_folder):
    for file in files:
        # Check if the file is an image (jpg, png, jpeg)
        if file.lower().endswith(('.jpg', '.jpeg', '.png')):
            # Construct the full path to the image file
            image_file = os.path.join(root, file)

            # Process the image file as needed (Just to test: will print the path to each image file)
            print("Image File:", image_file)


