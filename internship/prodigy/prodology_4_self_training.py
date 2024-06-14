import os
import time

import cv2
import numpy as np
import tensorflow as tf
from sklearn.model_selection import train_test_split
from tensorflow.keras import layers, models
from tqdm import tqdm


# Function to load images from directories
def load_images(root_dirs, target_size=(100, 100)):
    images = []
    labels = []
    dir_image_counts = {}
    total_images = 0
    for i, root_dir in enumerate(root_dirs):
        dir_name = os.path.basename(root_dir)
        image_count = 0
        for dirpath, _, filenames in os.walk(root_dir):
            for filename in filenames:
                if filename.endswith('.png'):
                    image_path = os.path.join(dirpath, filename)
                    label = i  # Assign label based on directory index
                    # Read and preprocess image
                    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
                    image = cv2.resize(image, target_size)
                    images.append(image)
                    labels.append(label)
                    image_count += 1  # Increment image count
                    total_images += 1
        dir_image_counts[dir_name] = image_count  # Update image count for directory
    return np.array(images), np.array(labels), total_images, dir_image_counts


# Define directories containing images
root_dir = "/home/harshit/Desktop/c and java and python programming/python/ai_ml practise/ml/internship/hand_guesture/leapGestRecog"
dir_names = ['01_palm', '02_l', '03_fist', '04_fist_moved', '05_thumb', '06_index', '07_ok', '08_palm_moved', '09_c',
             '10_down']
root_dirs = [os.path.join(root_dir, dir_name) for dir_name in dir_names]

# Load images and preprocess them
images, labels, total_images, dir_image_counts = load_images(root_dirs)
X_train, X_temp, y_train, y_temp = train_test_split(images, labels, test_size=0.2, random_state=42)
X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.5, random_state=42)

# Print total number of images and counts for each directory
print("Total number of images:", total_images)
sorted_dirs = sorted((key, value) for key, value in dir_image_counts.items() if key in dir_names)
for dir_name, count in sorted_dirs:
    print(f"{dir_name}: {count}")
print("\n")
print("Training set:", X_train.shape, y_train.shape)
print("Validation set:", X_val.shape, y_val.shape)
print("Testing set:", X_test.shape, y_test.shape)

# Preprocess images
X_train = X_train.reshape(-1, 100, 100, 1) / 255.0  # Normalize pixel values
X_val = X_val.reshape(-1, 100, 100, 1) / 255.0
X_test = X_test.reshape(-1, 100, 100, 1) / 255.0

# Define the CNN models architecture
model = models.Sequential([
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(100, 100, 1)),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.Flatten(),
    layers.Dense(64, activation='relu'),
    layers.Dense(10, activation='softmax')
])

# Compile the models
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Print models summary
model.summary()


# Define callback for tqdm progress bar during training
class TqdmCallback(tf.keras.callbacks.Callback):
    def __init__(self, total):
        super(TqdmCallback, self).__init__()  # Call superclass's __init__ method
        self.total = total
        self.pbar = None

    def on_train_begin(self, logs=None):
        self.epochs = self.params['epochs']

    def on_epoch_begin(self, epoch, logs=None):
        self.seen = 0
        if self.pbar is None:
            self.pbar = tqdm(total=self.total)
        self.log_values = []

    def on_batch_end(self, batch, logs=None):
        # No need to check for 'metrics' key in params
        self.seen += logs.get('size', 0)  # Use logs directly
        for k, v in logs.items():  # Iterate through all log items
            self.log_values.append((k, v))
        self.pbar.update(self.seen)

    def on_epoch_end(self, epoch, logs=None):
        if self.pbar is not None:
            self.pbar.close()
            self.pbar = None



# Record start time
start_time = time.time()

# Train the models with progress bar
tqdm_callback = TqdmCallback(total=len(X_train))
history = model.fit(X_train, y_train, epochs=10, batch_size=800, validation_data=(X_val, y_val), verbose=0,
                    callbacks=[tqdm_callback])

# Record end time
end_time = time.time()

# Calculate total time
total_time = end_time - start_time
print("Total time taken:", total_time, "seconds")

# Evaluate the models on the testing data
test_loss, test_accuracy = model.evaluate(X_test, y_test)
print("Test Loss:", test_loss)
print("Test Accuracy:", test_accuracy)

# Save the trained models to the specified location
model.save("/home/harshit/Desktop/hand_gesture_model.h5")
print("Model saved successfully at /home/harshit/Desktop/hand_gesture_model.h5")
