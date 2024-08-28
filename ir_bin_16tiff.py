# To convert IR bin files into 16-bit tiff or png files without scaling pixel values

import numpy as np

# Specify the dimensions of the image
width = 640 
height = 480

# Read the binary file
with open('C:/Users/Imrang/Desktop/ir/e45f01b9b401_20240620_191608_ir.bin', 'rb') as file: 
    data = np.fromfile(file, dtype=np.uint16)  # Read as 16-bit unsigned integers

# Reshape the data to match the image dimensions
data = data.reshape((height, width))

from PIL import Image

# Convert the NumPy array to a PIL Image
tiff_image = Image.fromarray(data)

# Save the image as a 16-bit TIFF without scaling
tiff_image.save('C:/Users/Imrang/Desktop/barn/ir/16_bit/1.tiff')
