import os
import time
import joblib
import cv2
import numpy as np
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from tqdm import tqdm


# Function to load and preprocess images in batches with data augmentation
def load_images(root_dir, label, batch_size=100):
    images = []
    labels = []
    unique_images = set()  # Track unique images to avoid counting duplicates

    filenames = os.listdir(root_dir)
    num_batches = len(filenames) // batch_size
    for i in tqdm(range(num_batches), desc=f"Loading {label} images"):
        batch_filenames = filenames[i * batch_size: (i + 1) * batch_size]
        for filename in batch_filenames:
            if filename.endswith('.jpg') or filename.endswith('.png'):
                image_path = os.path.join(root_dir, filename)
                if image_path not in unique_images:  # Check if image already processed
                    unique_images.add(image_path)  # Add to unique set
                    image = cv2.imread(image_path)
                    image = cv2.resize(image, (100, 100))  # Resize image to a fixed size
                    images.append(image.flatten())  # Flatten the image array
                    labels.append(label)

                    # Data augmentation: horizontal flip (optional)
                    # flipped_image = cv2.flip(image, 1)
                    # images.append(flipped_image.flatten())
                    # labels.append(label)

    return images, labels


# Define directories containing images
root_dir = "/home/harshit/Desktop/c and java and python programming/python/ai_ml practise/ml/internship/train"
dog_dir = os.path.join(root_dir, "dog")
cat_dir = os.path.join(root_dir, "cat")

# Load dog images in batches with data augmentation
start_time = time.time()
dog_images, dog_labels = load_images(dog_dir, 0)
print("Number of dog images:", len(dog_images))

# Load cat images in batches with data augmentation
cat_images, cat_labels = load_images(cat_dir, 1)
print("Number of cat images:", len(cat_images))
end_time = time.time()
# Combine dog and cat images and labels
X = np.concatenate((dog_images, cat_images), axis=0)
y = np.concatenate((dog_labels, cat_labels), axis=0)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Feature scaling
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Hyperparameter tuning
param_grid = {'C': [0.1, 1, 10], 'kernel': ['linear', 'rbf', 'poly']}
svm_model = SVC()
grid_search = GridSearchCV(svm_model, param_grid, cv=5, verbose=2)
grid_search.fit(X_train_scaled, y_train)
best_params = grid_search.best_params_

# Train an SVM models with the best hyperparameters
start_training_time = time.time()
print("Training the SVM models...")

# Replace the placeholder loop with actual models fitting
for i, (features, target) in tqdm(enumerate(zip(X_train_scaled, y_train)), total=len(X_train_scaled)):
    svm_model.fit(features.reshape(1, -1), np.array([target]))  # Reshape features for single sample training
    # Adjust sleep time for desired progress bar speed (optional)
    time.sleep(0.001)  # Uncomment for visual progress bar effect

end_training_time = time.time()

# Predict labels for the test set
y_pred = svm_model.predict(X_test_scaled)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
print("Best hyperparameters:", best_params)
print("Accuracy:", accuracy)

# Print total time taken
print("Total number of images:", len(X))
print("Training set:", X_train.shape, y_train.shape)
print("Testing set:", X_test.shape, y_test.shape)
print("Model:", svm_model)

print("Total time for loading images:", end_time - start_time, "seconds")
print("Total time for training:", end_training_time - start_training_time, "seconds")
# Save the trained SVM models to a file
model_filename = '/home/harshit/Desktop/svm_model.pkl'
joblib.dump(svm_model, model_filename)

print("SVM models saved to:", model_filename)
