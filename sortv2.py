import os
import csv

# Paths to the hawk and non-hawk directories
hawk_dir = '/home/cygnus/workspace/dl/project/hawks'
non_hawk_dir = '/home/cygnus/workspace/dl/project/non_hawks'

# CSV file path
csv_file_path = '/home/cygnus/workspace/dl/project/dataset_labels.csv'

# Open the CSV file in write mode
with open(csv_file_path, 'w', newline='') as file:
    writer = csv.writer(file)
    # Write the header
    writer.writerow(['image_name', 'label'])

    # Write the hawk images and label
    for image_name in os.listdir(hawk_dir):
        writer.writerow([image_name, 1])

    # Write the non-hawk images and label
    for image_name in os.listdir(non_hawk_dir):
        writer.writerow([image_name, 0])

print(f"CSV file has been created at {csv_file_path}")
