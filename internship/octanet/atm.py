import tkinter as tk
from tkinter import messagebox
import json
import os
from cryptography.fernet import Fernet

class ATM1:
    def __init__(self):
        self.data_file = 'atm_users_encrypted.json'
        self.key_file = 'key.key'
        self.key = self.load_key()
        self.cipher_suite = Fernet(self.key)
        self.users = self.load_user_data()
        self.current_user = None

    def load_key(self):
        if os.path.exists(self.key_file):
            with open(self.key_file, 'rb') as file:
                return file.read()
        else:
            key = Fernet.generate_key()
            with open(self.key_file, 'wb') as file:
                file.write(key)
            return key

    def load_user_data(self):
        if os.path.exists(self.data_file):
            with open(self.data_file, 'rb') as file:
                encrypted_data = file.read()
                decrypted_data = self.cipher_suite.decrypt(encrypted_data)
                return json.loads(decrypted_data)
        else:
            return {}

    def save_user_data(self):
        data = json.dumps(self.users).encode()
        encrypted_data = self.cipher_suite.encrypt(data)
        with open(self.data_file, 'wb') as file:
            file.write(encrypted_data)

    def start(self):
        self.open_pin_entry()

    def open_pin_entry(self):
        self.root = tk.Tk()
        self.root.resizable(False, False)
        self.root.geometry("300x420")
        self.root.title("Enter PIN")

        label = tk.Label(self.root, text="Enter your User ID:", font=("Roboto", 12))
        label.pack(pady=10)

        self.user_id_entry = tk.Entry(self.root, font=("Roboto", 12))
        self.user_id_entry.pack(pady=5)

        label = tk.Label(self.root, text="Enter your PIN:", font=("Roboto", 12))
        label.pack(pady=10)

        self.pin_entry = tk.Entry(self.root, show="*", font=("Roboto", 12))
        self.pin_entry.pack(pady=5)

        show_pin_var = tk.BooleanVar()
        show_pin_checkbox = tk.Checkbutton(self.root, text="Show PIN", variable=show_pin_var, command=self.toggle_show_pin)
        show_pin_checkbox.pack()

        self.status_label = tk.Label(self.root, text="", font=("Roboto", 10))
        self.status_label.pack()

        submit_button = tk.Button(self.root, text="Submit", width=15, command=self.verify_user, font=("Roboto", 14), bg="green", fg="white")
        submit_button.pack(pady=10)

        register_button = tk.Button(self.root, text="Register", width=15, command=self.register_user, font=("Roboto", 14), bg="blue", fg="white")
        register_button.pack(pady=10)

        self.root.mainloop()

    def toggle_show_pin(self):
        if self.pin_entry.cget('show') == '*':
            self.pin_entry.config(show="")
        else:
            self.pin_entry.config(show="*")

    def verify_user(self):
        user_id = self.user_id_entry.get()
        pin = self.pin_entry.get()

        if user_id in self.users and self.users[user_id]['pin'] == pin:
            self.current_user = user_id
            self.root.destroy()
            self.open_atm_gui()
        else:
            self.pin_entry.delete(0, tk.END)
            self.status_label.config(text="Invalid User ID or PIN", fg="red")

    def register_user(self):
        user_id = self.user_id_entry.get()
        pin = self.pin_entry.get()

        if user_id in self.users:
            self.status_label.config(text="User ID already exists", fg="red")
        else:
            self.users[user_id] = {"pin": pin, "balance": 0, "history": []}
            self.save_user_data()
            self.status_label.config(text="User registered successfully", fg="green")

    def open_atm_gui(self):
        self.root = tk.Tk()
        self.root.resizable(False, False)
        self.root.geometry("390x800")
        self.root.title("ATM Interface")
        self.root.configure(bg="green")

        label_1 = tk.Label(self.root, text="Welcome to the ATM", font='Roboto 18 bold', bg="coral")
        label_3 = tk.Label(self.root, text="Enter the amount: ", font='Helvetica 15 bold', bg="violet")

        button_1 = tk.Button(self.root, text="Withdraw Money", bg="yellow", fg="black", font="8", command=self.withdraw)
        button_2 = tk.Button(self.root, text="Deposit Money", bg="orange", fg="black", font="8", command=self.deposit)
        button_3 = tk.Button(self.root, text="Check Balance", bg="pink", fg="black", font="8", command=self.check_balance)
        button_4 = tk.Button(self.root, text="Exit", bg="red", fg="black", font="8", width=12, command=self.exit_program)
        history_button = tk.Button(self.root, text="History", bg="cyan", fg="black", font="8", width=12, command=self.show_transaction_history)

        self.text_box = tk.Text(self.root, width=40, height=5, bd=4, font='Roboto 12 bold')
        self.entry_box = tk.Entry(self.root, width=18, font="12", bd=6)

        label_1.place(x=60, y=20)
        button_1.place(x=20, y=120)
        button_2.place(x=250, y=120)
        button_3.place(x=20, y=180)
        button_4.place(x=140, y=640)
        history_button.place(x=255, y=180)
        label_3.place(x=20, y=390)
        self.text_box.place(x=10, y=250)
        self.entry_box.place(x=200, y=390)

        self.entry_box.insert(tk.END, "0")

        keyboard_layout = [
            ["1", "2", "3"],
            ["4", "5", "6"],
            ["7", "8", "9"],
            ["C", "0", "OK"]
        ]

        for i in range(4):
            for j in range(3):
                if keyboard_layout[i][j] != "":
                    button = tk.Button(self.root, text=keyboard_layout[i][j], bg="lightgray", fg="black", width=5, font=38,
                                       command=lambda key=keyboard_layout[i][j]: self.button_click_amount(key))
                    button.place(x=80 + j * 80, y=440 + i * 50)

        self.root.mainloop()

    def button_click_amount(self, key):
        if key == "C":
            self.entry_box.delete(0, tk.END)
        elif key == "OK":
            pass  # You can define the behavior for OK button here
        else:
            self.entry_box.insert(tk.END, key)

    def print_statement(self, statement):
        self.text_box.delete("1.0", tk.END)
        self.text_box.insert(tk.END, statement)

    def withdraw(self):
        try:
            amount = int(self.entry_box.get())
            if amount <= self.users[self.current_user]['balance']:
                self.users[self.current_user]['balance'] -= amount
                self.users[self.current_user]['history'].append(f"Withdrawn: {amount}")
                self.print_statement(f"Successfully withdrawn {amount}.")
            else:
                self.print_statement("Insufficient balance.")
        except ValueError:
            self.print_statement("Invalid amount.")
        self.save_user_data()

    def deposit(self):
        try:
            amount = int(self.entry_box.get())
            self.users[self.current_user]['balance'] += amount
            self.users[self.current_user]['history'].append(f"Deposited: {amount}")
            self.print_statement(f"Successfully deposited {amount}.")
        except ValueError:
            self.print_statement("Invalid amount.")
        self.save_user_data()

    def check_balance(self):
        self.print_statement(f"Your balance is {self.users[self.current_user]['balance']}.")

    def show_transaction_history(self):
        self.text_box.delete("1.0", tk.END)
        for transaction in self.users[self.current_user]['history']:
            self.text_box.insert(tk.END, transaction + "\n")

    def exit_program(self):
        messagebox.showinfo("Thank You", "Best of Luck!")
        self.root.destroy()

if __name__ == "__main__":
    atm = ATM1()
    atm.start()
