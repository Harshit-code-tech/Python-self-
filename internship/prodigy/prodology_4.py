import cv2
import numpy as np
from keras.models import load_model

# Load the models
model = load_model("/home/harshit/Desktop/c and java and python programming/python/ai_ml practise/ml/internship/keras_model.h5", compile=False)

# Load the labels
class_names = open("/home/harshit/Desktop/c and java and python programming/python/ai_ml practise/ml/internship/labels.txt", "r").readlines()

# CAMERA can be 0 or 1 based on the default camera of your computer
camera = cv2.VideoCapture(0)

# Background Subtractor
bg_subtractor = cv2.createBackgroundSubtractorMOG2()

while True:
    # Grab the webcam's image.
    ret, frame = camera.read()

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Apply background subtraction
    fg_mask = bg_subtractor.apply(gray)

    # Apply thresholding to obtain binary image
    _, thresh = cv2.threshold(fg_mask, 127, 255, cv2.THRESH_BINARY)

    # Find contours
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Iterate through contours
    for contour in contours:
        # Get bounding box
        x, y, w, h = cv2.boundingRect(contour)

        # Draw bounding box
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Extract hand region and resize to (224, 224)
        hand_region = cv2.resize(gray[y:y + h, x:x + w], (224, 224))
        # Convert grayscale image to 3-channel format
        hand_region = cv2.cvtColor(hand_region, cv2.COLOR_GRAY2RGB)

        # Expand dimensions to match models input shape
        hand_region = np.expand_dims(hand_region, axis=0)
        hand_region = np.expand_dims(hand_region, axis=-1)

        # Normalize the hand region
        hand_region = (hand_region / 127.5) - 1

        # Predict the gesture
        prediction = model.predict(hand_region)
        index = np.argmax(prediction)
        class_name = class_names[index]
        confidence_score = prediction[0][index]

        # Print prediction and confidence score
        print("Class:", class_name[2:], end="")
        print("Confidence Score:", str(np.round(confidence_score * 100))[:-2], "%")

    # Show the webcam feed
    cv2.imshow("Webcam Feed", frame)

    # Listen to the keyboard for presses.
    keyboard_input = cv2.waitKey(1)

    # 27 is the ASCII for the esc key on your keyboard.
    if keyboard_input == 27:
        break

camera.release()
cv2.destroyAllWindows()
