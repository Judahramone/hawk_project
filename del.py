import os
import random

# Paths to the hawk and non-hawk directories
hawk_dir = '/home/cygnus/workspace/dl/project/hawks'
non_hawk_dir = '/home/cygnus/workspace/dl/project/non_hawks'

# Get the list of image files in both directories
hawk_files = os.listdir(hawk_dir)
non_hawk_files = os.listdir(non_hawk_dir)

# Count the number of images in both directories
num_hawk_images = len(hawk_files)
num_non_hawk_images = len(non_hawk_files)

# Calculate the number of non-hawk images to delete to balance the dataset
num_to_delete = num_non_hawk_images - num_hawk_images

# Ensure we do not delete if non-hawk images are already equal or less
if num_to_delete > 0:
    # Randomly select non-hawk images to delete
    files_to_delete = random.sample(non_hawk_files, num_to_delete)

    # Delete the selected non-hawk images
    for file_name in files_to_delete:
        file_path = os.path.join(non_hawk_dir, file_name)
        os.remove(file_path)
    print(f"Deleted {num_to_delete} images from the non-hawk directory to balance the dataset.")
else:
    print("The non-hawk directory already has the same number or fewer images than the hawk directory. No files were deleted.")
