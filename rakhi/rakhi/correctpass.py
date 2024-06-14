import tkinter as tk
from tkinter import messagebox

class CorrectPassProgram:
    def __init__(self, root, main_program_function):
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

        self.run_main_program = main_program_function

    def verify_password(self):
        entered_password = self.password_entry.get()
        if entered_password == self.correct_password:
            self.root.destroy()  # Close the password verification window
            self.run_main_program()
        else:
            self.attempts_left -= 1
            if self.attempts_left > 0:
                remaining_attempts = self.attempts_left
                messagebox.showerror("Incorrect Password",
                                     f"Incorrect password entered. Attempts left: {remaining_attempts}")
            else:
                messagebox.showerror("Incorrect Password", "Maximum attempts reached. Exiting.")
                self.root.destroy()  # Close the password verification window
                self.root.quit()  # Exit the program

if __name__ == "__main__":
    root = tk.Tk()
    app = CorrectPassProgram(root, None)  # Pass None since main program function is not known yet
    root.mainloop()
