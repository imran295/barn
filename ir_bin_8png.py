# To convert IR bin files into 8-bit tiff or png files while scaling pixel values between 0 , 255


import os
import numpy as np
from PIL import Image

# Specify the folder containing the .bin files and output folder for png or tiff files
input_folder = 'C:/Users/Imrang/Desktop/ir'
output_folder = 'C:/Users/Imrang/Desktop/barn/ir'

# Specify the dimensions of the images
width, height = 640, 480  # dimensions

# Loop through all files in the input folder
for filename in os.listdir(input_folder):
    if filename.endswith('.bin'):
        # Load the binary data
        file_path = os.path.join(input_folder, filename)
        with open(file_path, 'rb') as f:    # rb means 'read .bin'
            data = np.fromfile(f, dtype=np.uint16)  # Adjust dtype as necessary --> here assuming 16-bit data in bin file.

        # Reshape the data according to image dimensions
        data = data.reshape((height, width))

        # Normalizing the data to 8-bit
        data_normalized = ((data - data.min()) * (255 / (data.max() - data.min()))).astype(np.uint8)
        # (data - data.min()) --> Subtracts the minimum value of 'data' array from the every element of the array. 
        # data.max() - data.min() --> gives the range of the original data.
        # 255 / (data.max() - data.min()) --> calculates the factor by which to scale the data so that the maximum value maps to 255.


        # Create the image
        img = Image.fromarray(data_normalized)

        # Generate the output file name
        # os.path.splitext(filename) splits the filename into two parts:The root name of the file and the file extension (including the dot).
        # [0] to access the first part of name (base or root name)
        output_filename = os.path.splitext(filename)[0] + '.tiff'
        output_path = os.path.join(output_folder, output_filename)

        # Save the image as PNG
        img.save(output_path)
        print(f'Converted {filename} to {output_filename}')

print('Conversion complete.')

# In png & tiff images, shades of gray correspond to different distances from the camera.