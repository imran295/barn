# # To convert a depth bin file into .ply file. 

# import numpy as np

# # Parameters
# width, height = 640, 480  # Replace with actual resolution
# focal_length = 525.0  # Replace with the focal length of the depth sensor

# # Load the depth data
# depth_file_path = 'C:/Users/Imrang/Desktop/depth/e45f01b9e77a_20240620_193014_depth.bin'   
# depth = np.fromfile(depth_file_path, dtype=np.uint16).reshape(height, width)

# # Generate 3D points
# points = []
# for v in range(height):
#     for u in range(width):
#         z = depth[v, u] / 1000.0  # Assuming depth is in millimeters; convert to meters
#         x = (u - width / 2) * z / focal_length
#         y = (v - height / 2) * z / focal_length
#         points.append([x, y, z])

# # Save as PLY
# ply_file_path = 'C:/Users/Imrang/Desktop/depth/e45f01b9e77a_20240620_193014_depth.ply'
# with open(ply_file_path, 'w') as f:
#     f.write('ply\n')
#     f.write('format ascii 1.0\n')
#     f.write(f'element vertex {len(points)}\n')
#     f.write('property float x\n')
#     f.write('property float y\n')
#     f.write('property float z\n')
#     f.write('end_header\n')
#     for point in points:
#         f.write(f'{point[0]} {point[1]} {point[2]}\n')

############################################################
# To covert bin file into 2D grayscale depth map

import numpy as np

# Replace with the actual width and height of the ToF sensor
width = 640
height = 480

# Load the binary data into a NumPy array
depth_data = np.fromfile('C:/Users/Imrang/Desktop/depth/e45f01b9e3c0_20240620_192621_depth.bin', dtype=np.uint16)  # Adjust dtype based on your data
depth_data = depth_data.reshape((height, width))
# e45f01b99049_20240620_191716_depth
# e45f01b9e728_20240620_052445_depth
# e45f01b9e3c0_20240620_192621_depth

# Normalize the depth data to the range [0, 255]
depth_min = np.min(depth_data)
depth_max = np.max(depth_data)

normalized_depth = 255 * (depth_data - depth_min) / (depth_max - depth_min)
normalized_depth = normalized_depth.astype(np.uint16)

from PIL import Image

depth_image = Image.fromarray(normalized_depth)
depth_image.save('C:/Users/Imrang/Desktop/depth/e45f01b9e3c0_20240620_192621_depth.png')


# print(depth_data[:100]) 
depth_min = np.min(depth_data)
depth_max = np.max(depth_data)
print(f'Min Depth: {depth_min}, Max Depth: {depth_max}')

import matplotlib.pyplot as plt

plt.hist(depth_data.flatten(), bins=256, range=(0, 65535), color='gray')
plt.title('Histogram of Depth Values')
plt.xlabel('Depth Value')
plt.ylabel('Frequency')
plt.show()
