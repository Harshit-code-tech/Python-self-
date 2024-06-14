import os
import time
import cv2
import numpy as np
import pandas as pd
from tqdm import tqdm
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import LinearSVC
import joblib

# Define the image size for resizing
image_size = (64, 64)


# Function to load images from a directory
def load_images(root_dir, label):
    images = []
    labels = []

    try:
        filenames = os.listdir(root_dir)
    except FileNotFoundError:
        print(f"Directory '{root_dir}' not found.")
        return images, labels

    for filename in filenames:
        if filename.endswith('.jpg') or filename.endswith('.png'):
            image_path = os.path.join(root_dir, filename)
            try:
                # Read the image
                image = cv2.imread(image_path)
                if image is not None:
                    # Resize the image
                    image = cv2.resize(image, image_size)
                    # Flatten the image array and append to the list of images
                    images.append(image.flatten())
                    labels.append(label)
                else:
                    print(f"Failed to load image: {image_path}")
            except Exception as e:
                print(f"Error loading image: {image_path}\n{e}")

    return images, labels


# Define the directories for dog and cat images
root_dir = "/home/harshit/Desktop/c and java and python programming/python/ai_ml practise/ml/internship/train"
dog_dir = os.path.join(root_dir, "dog")
cat_dir = os.path.join(root_dir, "cat")

# Load dog images
print("Fetching dog images")
dog_images, dog_labels = load_images(dog_dir, 0)
print("Number of dog images:", len(dog_images))

# Load cat images
print("Fetching cat images")
cat_images, cat_labels = load_images(cat_dir, 1)
print("Number of cat images:", len(cat_images))

# Concatenate dog and cat images and labels
X = np.concatenate((dog_images, cat_images), axis=0)
y = np.concatenate((dog_labels, cat_labels), axis=0)

# Display dataset information
print("Shape of X:", X.shape)
print("Shape of y:", y.shape)
print("Counts of each class in y:", np.bincount(y))

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize the features by scaling
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Initialize a Linear SVM models
svm_model = LinearSVC(dual=False, max_iter=10000)

# Training the SVM models
print("Training the SVM models...")
start_training_time = time.time()

# Set the batch size for training
batch_size = 2000
num_complete_batches = len(X_train_scaled) // batch_size
num_batches = num_complete_batches + 1 if len(X_train_scaled) % batch_size != 0 else num_complete_batches

print("Total number of batches:", num_batches)

# Initialize tqdm progress bar
with tqdm(total=num_complete_batches) as pbar:
    # Loop over complete batches
    for i in range(0, len(X_train_scaled) - batch_size, batch_size):
        print(f"Batch {i // batch_size + 1}/{num_complete_batches}")  # Print current batch number
        X_batch = X_train_scaled[i:i + batch_size]
        y_batch = y_train[i:i + batch_size]
        # Fit the models on the current batch
        svm_model.fit(X_batch, y_batch)
        # Update progress bar
        pbar.update(1)

    # Handle the last incomplete batch
    if len(X_train_scaled) % batch_size != 0:
        print(f"Batch {num_complete_batches + 1}/{num_batches}")  # Print current batch number
        X_batch = X_train_scaled[num_complete_batches * batch_size:]
        y_batch = y_train[num_complete_batches * batch_size:]
        # Fit the models on the last batch
        svm_model.fit(X_batch, y_batch)
        # Update progress bar
        pbar.update(1)

# Calculate total training time
end_training_time = time.time()
training_time = end_training_time - start_training_time

# Make predictions on the test set
y_pred = svm_model.predict(X_test_scaled)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)

# Display results
print("Accuracy:", accuracy)
print("Total number of images:", len(X))
print("Training set:", X_train.shape, y_train.shape)
print("Testing set:", X_test.shape, y_test.shape)
print("Model:", svm_model)
print("Total training time:", training_time, "seconds")

# Save the trained SVM models to a file
model_filename = '/home/harshit/Desktop/svm_model.pkl'
try:
    joblib.dump(svm_model, model_filename)
    print("SVM models saved to:", model_filename)
except Exception as e:
    print(f"Error saving models: {e}")

# Path to the test folder containing images of dogs and cats
test_folder = "/media/harshit/HG_DISK/ml project/dogs-vs-cats/test1/test1"

# Initialize lists to store image names and predictions
image_names = []
predictions = []

# Iterate over each image in the test folder
for filename in os.listdir(test_folder):
    if filename.endswith('.jpg') or filename.endswith('.png'):
        image_path = os.path.join(test_folder, filename)
        # Load and preprocess the image
        try:
            image = cv2.imread(image_path)
            if image is not None:
                image = cv2.resize(image, (64, 64))
                image = image.flatten()
                # Scale the image using the same scaler used for training
                scaled_image = scaler.transform([image])  # Assuming scaler is already defined
                # Make predictions using the trained SVM models
                prediction = svm_model.predict(scaled_image)
                image_names.append(filename)
                predictions.append(prediction[0])
            else:
                print(f"Failed to load image: {image_path}")
        except Exception as e:
            print(f"Error processing image: {image_path}\n{e}")

# Create a DataFrame to store image names and predictions
df = pd.DataFrame({'Image_Name': image_names, 'Prediction': predictions})

# Save the DataFrame to a CSV file
csv_filename = '/home/harshit/Desktop/predictions.csv'
df.to_csv(csv_filename, index=False)

print("Predictions saved to:", csv_filename)
