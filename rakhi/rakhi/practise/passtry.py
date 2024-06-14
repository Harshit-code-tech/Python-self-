import tkinter as tk
from tkinter import messagebox


class CorrectPassProgram:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Verification")

        self.attempts_left = 5
        self.correct_password = "rakhi2023"  # Replace with the actual correct password

        self.label = tk.Label(root, text="Enter the correct password:")
        self.label.pack(pady=10)

        self.password_entry = tk.Entry(root, show="*")
        self.password_entry.pack(pady=5)

        self.submit_button = tk.Button(root, text="Submit", command=self.verify_password)
        self.submit_button.pack(pady=10)

    def verify_password(self):
        entered_password = self.password_entry.get()
        if entered_password == self.correct_password:
            self.root.destroy()  # Close the password verification window
        else:
            self.attempts_left -= 1
            if self.attempts_left == 0:
                messagebox.showerror("Incorrect Password", "Maximum attempts reached. Exiting.")
                self.root.destroy()  # Close the password verification window

                # Additional code to exit the entire program if the password is incorrect
                # (optional, depending on your use case)


if __name__ == "__main__":
    root = tk.Tk()
    app = CorrectPassProgram(root)
    root.mainloop()
