import tkinter as tk
from tkinter import messagebox

from clipboard_integration import Clipboard
from password_generator import PasswordGenerator


def show_error(title, message):
    messagebox.showerror(title, message)


def show_message(title, message):
    messagebox.showinfo(title, message)


class PasswordGeneratorGUI(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Password Generator")
        self.password_generator = PasswordGenerator()
        self.clipboard = Clipboard()
        self.create_widgets()

    def create_widgets(self):
        # Label and Entry for password length
        self.length_label = tk.Label(self.master, text="Password Length:")
        self.length_label.grid(row=0, column=0)
        self.length_entry = tk.Entry(self.master)
        self.length_entry.grid(row=0, column=1)
        self.length_entry.insert(0, "8")

        # Checkbuttons for character types
        self.use_letters_var = tk.BooleanVar(value=True)
        self.use_letters_check = tk.Checkbutton(self.master, text="Letters", variable=self.use_letters_var)
        self.use_letters_check.grid(row=1, column=0, sticky=tk.W)

        self.use_digits_var = tk.BooleanVar(value=True)
        self.use_digits_check = tk.Checkbutton(self.master, text="Digits", variable=self.use_digits_var)
        self.use_digits_check.grid(row=2, column=0, sticky=tk.W)

        self.use_symbols_var = tk.BooleanVar(value=True)
        self.use_symbols_check = tk.Checkbutton(self.master, text="Symbols", variable=self.use_symbols_var)
        self.use_symbols_check.grid(row=3, column=0, sticky=tk.W)

        # Generate button
        self.generate_button = tk.Button(self.master, text="Generate Password", command=self.generate_password)
        self.generate_button.grid(row=4, column=0, columnspan=2)

        # Generated password display
        self.password_label = tk.Label(self.master, text="Generated Password:")
        self.password_label.grid(row=5, column=0, columnspan=2)
        self.password_entry = tk.Entry(self.master, state="readonly")
        self.password_entry.grid(row=6, column=0, columnspan=2)

        # Copy button
        self.copy_button = tk.Button(self.master, text="Copy to Clipboard", command=self.copy_to_clipboard)
        self.copy_button.grid(row=7, column=0, columnspan=2)

    def generate_password(self):
        try:
            length_str = self.length_entry.get()
            if not length_str.isdigit():
                raise ValueError("Password length must be a positive integer.")

            length = int(length_str)
            if length <= 0:
                raise ValueError("Password length must be a positive integer.")

            use_letters = self.use_letters_var.get()
            use_digits = self.use_digits_var.get()
            use_symbols = self.use_symbols_var.get()

            password = self.password_generator.generate_custom_password(length, use_letters, use_digits, use_symbols)
            self.password_entry.configure(state="normal")
            self.password_entry.delete(0, tk.END)
            self.password_entry.insert(0, password)
            self.password_entry.configure(state="readonly")
        except ValueError as e:
            show_error("Invalid Input", str(e))
        except Exception as e:
            show_error("Error", "An unexpected error occurred: " + str(e))

    def copy_to_clipboard(self):
        password = self.password_entry.get()
        self.clipboard.copy_to_clipboard(password)
        show_message("Clipboard", "Password copied to clipboard successfully.")
