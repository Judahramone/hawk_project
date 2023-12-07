import os
import shutil

# List of directories corresponding to hawk images
hawk_dirs = ['0299', '0357', '0358', '0359', '0360', '0361', '0495', '0496', '0497', '0545', '0656', '0657', '0658', '0659', '0660', '0699', '0700']

# Base directory where all the image directories are located
base_dir = '/home/cygnus/workspace/dl/project/nabirds/images'

# Directories where you want to store hawk and non-hawk images
hawk_dest_dir = '/home/cygnus/workspace/dl/project/hawks'
non_hawk_dest_dir = '/home/cygnus/workspace/dl/project/non_hawks'

# Create destination directories if they don't exist
os.makedirs(hawk_dest_dir, exist_ok=True)
os.makedirs(non_hawk_dest_dir, exist_ok=True)

# Iterate through all directories in the base directory
for dir_name in os.listdir(base_dir):
    current_dir_path = os.path.join(base_dir, dir_name)
    
    # Check if the current directory is a hawk directory
    if dir_name in hawk_dirs:
        dest_dir = hawk_dest_dir
    else:
        dest_dir = non_hawk_dest_dir
    
    # Move or copy the images to the respective destination directory
    for image_name in os.listdir(current_dir_path):
        source_image_path = os.path.join(current_dir_path, image_name)
        dest_image_path = os.path.join(dest_dir, image_name)
        
        # Use shutil.move for moving or shutil.copy for copying
        shutil.copy(source_image_path, dest_image_path)

# Now you have all hawk images in 'hawk_dest_dir' and all non-hawk images in 'non_hawk_dest_dir'
