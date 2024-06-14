import tkinter as tk
from tkinter import messagebox

import matplotlib.pyplot as plt

import bmi_calculation
import data_storage

# Global variables
root = None
weight_entry = None
height_entry = None
bmi_label = None
category_label = None


def calculate_bmi():
    try:
        global weight_entry, height_entry, bmi_label, category_label
        weight = float(weight_entry.get())
        height = float(height_entry.get())

        if weight <= 0 or height <= 0:
            raise ValueError("Weight and height must be greater than zero.")

        bmi = bmi_calculation.calculate_bmi(weight, height)
        category = bmi_calculation.classify_bmi(bmi)

        bmi_label.config(text=f"BMI: {bmi:.2f}")
        category_label.config(text=f"Category: {category}")

        data_storage.save_to_csv(weight, height, bmi)
        messagebox.showinfo("Success", "BMI calculation completed and data saved successfully.")
    except ValueError as ve:
        messagebox.showerror("Error", str(ve))


def view_historical_data():
    historical_data = data_storage.read_from_csv()
    if historical_data:
        show_historical_data(historical_data)
    else:
        messagebox.showinfo("Historical Data", "No historical data available.")


def show_historical_data(data):
    history_window = tk.Toplevel(root)
    history_window.title("Historical Data")

    # Create a frame to contain the historical data entries
    frame = tk.Frame(history_window)
    frame.pack(padx=10, pady=10)

    # Lists to store BMI values and corresponding timestamps
    timestamps = []
    bmis = []

    # Iterate through the data and create a label for each entry
    for idx, entry in enumerate(data):
        weight = float(entry['Weight (kg)'])
        height = float(entry['Height (m)'])
        bmi = float(entry['BMI'])  # Convert BMI value to float

        # Append BMI and timestamp to lists
        bmis.append(bmi)
        timestamps.append(entry['Timestamp'])

        # Create a label for the current entry
        entry_label = tk.Label(frame,
                               text=f"Entry {idx + 1}: Weight: {weight} kg, Height: {height} m, BMI: {bmi:.2f}, Timestamp: {entry['Timestamp']}")
        entry_label.pack(anchor='w', padx=10, pady=5)

    # Create a line chart to visualize BMI data over time
    plt.figure(figsize=(8, 6))
    plt.plot(timestamps, bmis, marker='o', linestyle='-')
    plt.title('Historical BMI Data')
    plt.xlabel('Timestamp')
    plt.ylabel('BMI')
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Display the line chart
    plt.show()


def create_input_fields(root):  # Modified to accept root argument
    weight_label = tk.Label(root, text="Weight (kg):")
    weight_label.grid(row=0, column=0, padx=10, pady=5)

    weight_entry = tk.Entry(root)
    weight_entry.grid(row=0, column=1, padx=10, pady=5)

    height_label = tk.Label(root, text="Height (m):")
    height_label.grid(row=1, column=0, padx=10, pady=5)

    height_entry = tk.Entry(root)
    height_entry.grid(row=1, column=1, padx=10, pady=5)

    return weight_entry, height_entry


def create_buttons(root):  # Modified to accept root argument
    calculate_button = tk.Button(root, text="Calculate BMI", command=calculate_bmi)
    calculate_button.grid(row=2, column=0, columnspan=2, pady=10)

    view_data_button = tk.Button(root, text="View Historical Data", command=view_historical_data)
    view_data_button.grid(row=3, column=0, columnspan=2, pady=10)


def create_display_section(root):  # Modified to accept root argument
    bmi_label = tk.Label(root, text="BMI: ")
    bmi_label.grid(row=4, column=0, columnspan=2, pady=10)

    category_label = tk.Label(root, text="Category: ")
    category_label.grid(row=5, column=0, columnspan=2, pady=10)

    return bmi_label, category_label


def main():
    global root, weight_entry, height_entry, bmi_label, category_label

    root = tk.Tk()
    root.title("BMI Calculator")

    weight_entry, height_entry = create_input_fields(root)
    bmi_label, category_label = create_display_section(root)
    create_buttons(root)

    root.mainloop()


if __name__ == "__main__":
    main()
