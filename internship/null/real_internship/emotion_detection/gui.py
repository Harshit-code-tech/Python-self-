import tkinter as tk
from tkinter import filedialog, messagebox
import sounddevice as sd
import soundfile as sf
import numpy as np
import librosa
import pickle

# Load the trained emotion detection model
with open('emotion_audio.pkl', 'rb') as file:
    model = pickle.load(file)

# Emotion labels
emotion_labels = ['angry', 'calm', 'disgust', 'fear', 'happy', 'neutral', 'sad', 'surprise']

# Function to preprocess audio data
def preprocess_audio(file_path):
    audio, sr = librosa.load(file_path, sr=22050, duration=2.5)  # Load audio file
    mfccs = librosa.feature.mfcc(y=audio, sr=sr, n_mfcc=13)

    # Select the first MFCC feature
    mfccs = mfccs[0:1, :].T  # This selects the first MFCC and transposes the array

    # Padding or truncating to ensure the shape is (162, 1)
    if mfccs.shape[0] < 162:
        padded_mfccs = np.pad(mfccs, ((0, 162 - mfccs.shape[0]), (0, 0)), mode='constant')
    else:
        padded_mfccs = mfccs[:162, :]

    # No need to add a channel dimension since the expected shape is (162, 1)
    return padded_mfccs

# Function to predict emotion from audio
def predict_emotion(audio_file):
    features = preprocess_audio(audio_file)
    features = np.expand_dims(features, axis=0)  # Reshape for model input
    try:
        emotion_probabilities = model.predict(features)
        emotion = np.argmax(emotion_probabilities)
        return emotion_labels[emotion]
    except ValueError as e:
        print(f"Error: {e}")
        print(f"Expected input shape: {model.input_shape}")
        print(f"Actual input shape: {features.shape}")
        raise e

# Function to update status label
def update_status(message):
    status_label.config(text=message)
    window.update_idletasks()

# Function to handle audio recording
def record_audio():
    update_status("Recording...")
    fs = 22050  # Sample rate
    duration = 2.5  # seconds
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='float64')
    sd.wait()  # Wait until recording is finished
    sf.write('recorded_audio.wav', recording, fs)  # Save recorded audio to a file
    try:
        emotion = predict_emotion('recorded_audio.wav')  # Predict emotion
        messagebox.showinfo("Emotion Detection", f"Emotion detected (recorded audio): {emotion}")
        result_label.config(text=f"Detected Emotion: {emotion}")
    except ValueError:
        messagebox.showerror("Error", "Error in predicting emotion from recorded audio.")
    update_status("Ready")

# Function to handle file upload
def upload_audio():
    file_path = filedialog.askopenfilename(filetypes=[("Audio files", "*.wav")])
    if file_path:
        update_status("Processing...")
        try:
            emotion = predict_emotion(file_path)  # Predict emotion
            messagebox.showinfo("Emotion Detection", f"Emotion detected (uploaded audio): {emotion}")
            result_label.config(text=f"Detected Emotion: {emotion}")
        except ValueError:
            messagebox.showerror("Error", "Error in predicting emotion from uploaded audio.")
        update_status("Ready")

# Create GUI window
window = tk.Tk()
window.title("Emotion Detection")

# Create a frame for the buttons
button_frame = tk.Frame(window)
button_frame.pack(pady=20)

# Create a frame for the status and result labels
status_frame = tk.Frame(window)
status_frame.pack(pady=20)

# Status label
status_label = tk.Label(status_frame, text="Ready")
status_label.pack(pady=10)

# Result label
result_label = tk.Label(status_frame, text="", font=("Helvetica", 14))
result_label.pack(pady=10)

# Button to record audio
record_button = tk.Button(button_frame, text="Record Audio", command=record_audio)
record_button.grid(row=0, column=0, padx=10)

# Button to upload audio file
upload_button = tk.Button(button_frame, text="Upload Audio File", command=upload_audio)
upload_button.grid(row=0, column=1, padx=10)

# Run the GUI main loop
window.mainloop()
