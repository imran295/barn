# still need to understand this code

import numpy as np
from PIL import Image

file_path = 'C:/Users/Imrang/Desktop/ir/e45f01b9b401_20240620_191608_ir.bin'
# Read the entire content of the binary file
with open(file_path, "rb") as file:
    data = file.read()

# Convert the binary data to a numpy array of 16-bit integers (assuming little-endian format)
values = np.frombuffer(data, dtype=np.uint16)

# Determine the closest square dimensions for the image
side_length = int(np.sqrt(len(values)))

# Reshape the data to a 2D array (image)
image_data = values[:side_length * side_length].reshape((side_length, side_length))

# Normalize the values to fit within the 8-bit range (0-255)
normalized_image_data = ((image_data - image_data.min()) / (image_data.max() - image_data.min()) * 255).astype(np.uint8)

# Create a grayscale image from the normalized data
image = Image.fromarray(normalized_image_data, mode='L')

# Save the image as a PNG file
output_image_path = "C:/Users/Imrang/Desktop/barn/1.tiff"
image.save(output_image_path)

output_image_path
