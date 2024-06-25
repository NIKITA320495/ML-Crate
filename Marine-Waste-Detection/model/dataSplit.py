import os
import random
import shutil

def split_dataset(src_dir, train_dir, val_dir, split_ratio=0.8):
    # Create train and val directories if they don't exist
    os.makedirs(train_dir, exist_ok=True)
    os.makedirs(val_dir, exist_ok=True)

    # Get list of images from the source directory
    images = os.listdir(os.path.join(src_dir, 'Images'))

    # Shuffle the images to ensure randomness
    random.shuffle(images)

    # Determine split index based on split ratio
    split_index = int(len(images) * split_ratio)

    # Split images into train and val sets@Nikita
    train_images = images[:split_index]
    val_images = images[split_index:]

    # Copy images and annotations to train and val folders
    for image in train_images:
        src_image_path = os.path.join(src_dir, 'Images', image)
        dst_image_path = os.path.join(train_dir, 'images', image)
        shutil.copy(src_image_path, dst_image_path)

        annotation = image.replace('.png', '.txt')
        src_annotation_path = os.path.join(src_dir, 'yolo_annotations1', annotation)
        dst_annotation_path = os.path.join(train_dir, 'labels', annotation)
        shutil.copy(src_annotation_path, dst_annotation_path)

    for image in val_images:
        src_image_path = os.path.join(src_dir, 'Images', image)
        dst_image_path = os.path.join(val_dir, 'images', image)
        shutil.copy(src_image_path, dst_image_path)

        annotation = image.replace('.png', '.txt')
        src_annotation_path = os.path.join(src_dir, 'yolo_annotations1', annotation)
        dst_annotation_path = os.path.join(val_dir, 'labels', annotation)
        shutil.copy(src_annotation_path, dst_annotation_path)

# Define paths
src_dir = 'E:\marine'
train_dir = 'train'
val_dir = 'val'

# Split dataset
split_dataset(src_dir, train_dir, val_dir, split_ratio=0.8)
