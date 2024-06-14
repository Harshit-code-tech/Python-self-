import os

import cv2
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout

# Define the path to the dataset directory
dataset_dir = "/media/harshit/HG_DISK/ml project/hand_guesture"


# Data Exploration
for subject_folder in sorted(os.listdir(dataset_dir)):
    subject_path = os.path.join(dataset_dir, subject_folder)
    print("Subject:", subject_folder)

    for gesture_folder in sorted(os.listdir(subject_path)):
        gesture_path = os.path.join(subject_path, gesture_folder)
        print("\tGesture:", gesture_folder)

        num_images = len(os.listdir(gesture_path))
        print("\t\tNumber of Images:", num_images)
# Data Loading and Preprocessing
image_paths = []
labels = []

# Loop through each subject folder
for subject_folder in os.listdir(dataset_dir):
    subject_path = os.path.join(dataset_dir, subject_folder)

    # Loop through each gesture folder for the current subject
    for gesture_folder in os.listdir(subject_path):
        gesture_path = os.path.join(subject_path, gesture_folder)

        # Loop through each image file for the current gesture
        for img_name in os.listdir(gesture_path):
            # Append the image path and corresponding label to the lists
            image_paths.append(os.path.join(gesture_path, img_name))
            labels.append(gesture_folder)

# Convert labels to numerical values
label_to_index = {label: idx for idx, label in enumerate(np.unique(labels))}
labels = np.array([label_to_index[label] for label in labels])

from collections import defaultdict

# Count the number of samples for each subject and gesture
subject_gesture_count = defaultdict(int)
for subject_folder in os.listdir(dataset_dir):
    subject_path = os.path.join(dataset_dir, subject_folder)
    for gesture_folder in os.listdir(subject_path):
        gesture_path = os.path.join(subject_path, gesture_folder)
        subject_gesture_count[subject_folder] += len(os.listdir(gesture_path))

# Filter out subjects with insufficient samples
min_samples_per_gesture = 2
filtered_subjects = [subject for subject, count in subject_gesture_count.items() if count >= min_samples_per_gesture]

# Filter out corresponding image paths
filtered_image_paths = []
filtered_labels = []
for subject_folder in filtered_subjects:
    subject_path = os.path.join(dataset_dir, subject_folder)
    for gesture_folder in os.listdir(subject_path):
        gesture_path = os.path.join(subject_path, gesture_folder)
        for img_name in os.listdir(gesture_path):
            filtered_image_paths.append(os.path.join(gesture_path, img_name))
            filtered_labels.append(gesture_folder)

# Convert labels to numerical values
label_to_index = {label: idx for idx, label in enumerate(np.unique(filtered_labels))}
filtered_labels = np.array([label_to_index[label] for label in filtered_labels])

# Split the filtered dataset
train_images, test_images, train_labels, test_labels = train_test_split(
    filtered_image_paths, filtered_labels, test_size=0.2, random_state=42, stratify=None
)

# Further split the combined training and validation set into training and validation sets
train_images, val_images, train_labels, val_labels = train_test_split(
    train_images, train_labels, test_size=0.125, random_state=42, stratify=train_labels
)

# Print the sizes of the splits
print("Number of training images:", len(train_images))
print("Number of validation images:", len(val_images))
print("Number of test images:", len(test_images))



# Define Model Architecture
model = Sequential([
    Conv2D(32, (3, 3), activation='relu', input_shape=(img_width, img_height, 3)),
    MaxPooling2D((2, 2)),
    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D((2, 2)),
    Flatten(),
    Dense(128, activation='relu'),
    Dropout(0.5),
    Dense(10, activation='softmax')
])

# Compile the models
model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# Display the models summary
model.summary()

