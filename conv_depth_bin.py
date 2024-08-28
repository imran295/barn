# To convert a depth bin file into .ply file. 

import numpy as np

# Parameters
width, height = 640, 480  # Replace with actual resolution
focal_length = 525.0  # Replace with the focal length of the depth sensor

# Load the depth data
depth_file_path = 'C:/Users/Imrang/Desktop/depth/e45f01b9e77a_20240620_193014_depth.bin'   
depth = np.fromfile(depth_file_path, dtype=np.uint16).reshape(height, width)

# Generate 3D points
points = []
for v in range(height):
    for u in range(width):
        z = depth[v, u] / 1000.0  # Assuming depth is in millimeters; convert to meters
        x = (u - width / 2) * z / focal_length
        y = (v - height / 2) * z / focal_length
        points.append([x, y, z])

# Save as PLY
ply_file_path = 'C:/Users/Imrang/Desktop/depth/e45f01b9e77a_20240620_193014_depth.ply'
with open(ply_file_path, 'w') as f:
    f.write('ply\n')
    f.write('format ascii 1.0\n')
    f.write(f'element vertex {len(points)}\n')
    f.write('property float x\n')
    f.write('property float y\n')
    f.write('property float z\n')
    f.write('end_header\n')
    for point in points:
        f.write(f'{point[0]} {point[1]} {point[2]}\n')





