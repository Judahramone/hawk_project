import os
import csv
from keras.preprocessing.image import ImageDataGenerator, img_to_array, load_img, array_to_img
import pandas as pd

# Define the data generator with your specified augmentations
dataGen = ImageDataGenerator(
    rotation_range=15,
    width_shift_range=0.05,
    height_shift_range=0.05,
    shear_range=0.1,
    zoom_range=0.1,
    horizontal_flip=True,
    fill_mode='nearest',
    brightness_range=[0.75, 1.25]
)

# Assuming you have a dataframe 'df' with image names and labels
df = pd.read_csv('/home/cygnus/workspace/dl/project/dataset_labels.csv')

# Directories for hawk and non-hawk images
hawk_dir = '/home/cygnus/workspace/dl/project/hawks'
non_hawk_dir = '/home/cygnus/workspace/dl/project/non_hawks'

# Function to append data to CSV
def append_to_csv(csv_file_path, image_name, label):
    with open(csv_file_path, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([image_name, label])

# Function to augment and save images

def augment_and_save(image_path, save_dir, label, num_new_images=5):
    img = load_img(image_path)
    img_array = img_to_array(img)
    img_array = img_array.reshape((1,) + img_array.shape)

    i = 0
    for batch in dataGen.flow(img_array, batch_size=1):
        # Construct the new image name
        new_image_name = f"aug_{i}_{os.path.basename(image_path)}"
        # Save the image manually
        array_to_img(batch[0]).save(os.path.join(save_dir, new_image_name))
        # Append the new image name and label to the CSV
        append_to_csv('/home/cygnus/workspace/dl/project/augmented_images.csv', new_image_name, label)
        i += 1
        if i >= num_new_images:
            break  # Stop the loop after generating num_new_images


# Loop over the dataframe and augment images
for index, row in df.iterrows():
    file_name = row['image_name']
    label = row['label']
    # Set the directory based on the label
    directory = hawk_dir if label == 1 else non_hawk_dir
    image_path = os.path.join(directory, file_name)
    augment_and_save(image_path, directory, label)
