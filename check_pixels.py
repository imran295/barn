# To check the pixel values for the image, Minimum , Maximum, Central Value

from PIL import Image

# Load the image
image_path = 'C:/Users/Imrang/Desktop/barn/ir/16_bit/1.tiff'
image = Image.open(image_path).convert('L')

# Get pixel value at a specific coordinate (e.g., center of the image)
width, height = image.size
center_pixel_value = image.getpixel((width // 2, height // 2))

# Get the minimum and maximum pixel values
pixel_values = list(image.getdata())
min_pixel_value = min(pixel_values)
max_pixel_value = max(pixel_values)

print(center_pixel_value, min_pixel_value, max_pixel_value)


# Opencv (cv2) did not work here.