import os
import time
from multiprocessing import Pool

import cv2
import numpy as np
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from tqdm import tqdm


def load_image(image_path):
    image = cv2.imread(image_path)
    image = cv2.resize(image, (100, 100))
    return image.flatten()


def load_images_parallel(root_dir, label, num_processes=4):
    images = []
    labels = []
    image_paths = [os.path.join(root_dir, filename)
                   for filename in os.listdir(root_dir)
                   if filename.endswith('.jpg') or filename.endswith('.png')]

    with Pool(processes=num_processes) as pool:
        image_arrays = list(
            tqdm(pool.imap(load_image, image_paths), total=len(image_paths), desc=f"Loading {root_dir}"))

    for image_array in image_arrays:
        images.append(image_array)
        labels.append(label)

    return images, labels


def main():
    # Define directories containing images
    root_dir = "/home/harshit/Desktop/c and java and python programming/python/ai_ml practise/ml/internship/train"
    dog_dir = os.path.join(root_dir, "dog")
    cat_dir = os.path.join(root_dir, "cat")

    # Count and print the number of images in each directory
    dog_image_count = len(
        [filename for filename in os.listdir(dog_dir) if filename.endswith('.jpg') or filename.endswith('.png')])
    cat_image_count = len(
        [filename for filename in os.listdir(cat_dir) if filename.endswith('.jpg') or filename.endswith('.png')])
    print("Number of dog images:", dog_image_count)
    print("Number of cat images:", cat_image_count)
    print("Total number of images:", dog_image_count + cat_image_count)

    # Load dog images
    dog_images, dog_labels = load_images_parallel(dog_dir, 0)

    # Load cat images
    cat_images, cat_labels = load_images_parallel(cat_dir, 1)

    # Combine dog and cat images and labels
    X = np.concatenate((dog_images, cat_images), axis=0)
    y = np.concatenate((dog_labels, cat_labels), axis=0)

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Record start time
    start_time = time.time()

    # Train an SVM models
    svm_model = SVC(kernel='linear')  # Use a linear kernel
    svm_model.fit(X_train, y_train)

    # Record end time
    end_time = time.time()

    # Calculate total time
    total_time = end_time - start_time
    print("Total time taken:", total_time, "seconds")

    # Save the trained models
    model_path = "/home/harshit/Desktop/dog_cat_model.pkl"
    import joblib

    joblib.dump(svm_model, model_path)
    print("Model saved successfully at", model_path)

    # Predict labels for the test set
    y_pred = svm_model.predict(X_test)

    # Calculate accuracy
    accuracy = accuracy_score(y_test, y_pred)
    print("Accuracy:", accuracy)


if __name__ == "__main__":
    main()
