# atm_gui.py
import tkinter as tk
from tkinter import messagebox
from atm_core import ATM


class ATMGUI:
    def __init__(self, atm):
        self.atm = atm
        self.root = None
        self.user_id_entry = None
        self.pin_entry = None
        self.status_label = None
        self.text_box = None
        self.entry_box = None

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
        user_id = self.user_id_entry.get().strip()
        pin = self.pin_entry.get().strip()
        if user_id and pin:
            if self.atm.verify_user(user_id, pin):
                self.root.destroy()
                self.open_atm_gui()
            else:
                self.pin_entry.delete(0, tk.END)
                self.status_label.config(text="Invalid User ID or PIN", fg="red")
        else:
            self.status_label.config(text="User ID and PIN are required", fg="red")

    def register_user(self):
        user_id = self.user_id_entry.get().strip()
        pin = self.pin_entry.get().strip()
        if user_id and pin:
            if self.atm.register_user(user_id, pin):
                self.status_label.config(text="User registered successfully", fg="green")
            else:
                self.status_label.config(text="User ID already exists", fg="red")
        else:
            self.status_label.config(text="User ID and PIN are required", fg="red")

    def open_atm_gui(self):
        self.root = tk.Tk()
        self.root.resizable(False, False)
        self.root.geometry("600x900")
        self.root.title("ATM Interface")
        self.root.configure(bg="lightgrey")

        label_1 = tk.Label(self.root, text="Welcome to the ATM", font='Roboto 18 bold', bg="coral")
        label_1.pack(pady=20)

        buttons_frame = tk.Frame(self.root)
        buttons_frame.pack(pady=20)

        button_texts = [
            ("Withdraw Money", self.withdraw, "yellow"),
            ("Deposit Money", self.deposit, "orange"),
            ("Check Balance", self.check_balance, "pink"),
            ("History", self.show_transaction_history, "cyan"),
            ("Transfer", self.transfer_money, "lightblue"),
            ("Exit", self.exit_program, "red")
        ]

        for i, (text, command, color) in enumerate(button_texts):
            button = tk.Button(buttons_frame, text=text, bg=color, fg="black", font="8", width=20, command=command)
            button.grid(row=i // 2, column=i % 2, padx=10, pady=10)

        label_3 = tk.Label(self.root, text="Enter the amount: ", font='Helvetica 15 bold', bg="violet")
        label_3.pack(pady=10)

        self.entry_box = tk.Entry(self.root, width=18, font="12", bd=6)
        self.entry_box.pack(pady=5)
        self.entry_box.insert(tk.END, "0")

        self.text_box = tk.Text(self.root, width=50, height=5, bd=4, font='Roboto 12 bold')
        self.text_box.pack(pady=10)

        keyboard_frame = tk.Frame(self.root)
        keyboard_frame.pack(pady=10)

        keyboard_layout = [
            ["1", "2", "3"],
            ["4", "5", "6"],
            ["7", "8", "9"],
            ["C", "0", "OK"]
        ]

        for i, row in enumerate(keyboard_layout):
            for j, key in enumerate(row):
                button = tk.Button(keyboard_frame, text=key, bg="lightgray", fg="black", width=5, font="38",
                                   command=lambda k=key: self.button_click_amount(k))
                button.grid(row=i, column=j, padx=5, pady=5)

        self.root.mainloop()

    def button_click_amount(self, key):
        if key == "C":
            self.entry_box.delete(0, tk.END)
        elif key == "OK":
            amount = self.entry_box.get().strip()
            if amount:
                if amount.startswith("-"):
                    self.withdraw()
                else:
                    self.deposit()
        else:
            self.entry_box.insert(tk.END, key)

    def print_statement(self, statement):
        self.text_box.delete("1.0", tk.END)
        self.text_box.insert(tk.END, statement)

    def withdraw(self):
        amount = self.entry_box.get().strip()
        result = self.atm.withdraw(amount)
        self.print_statement(result)
        self.entry_box.delete(0, tk.END)

    def deposit(self):
        amount = self.entry_box.get().strip()
        result = self.atm.deposit(amount)
        self.print_statement(result)
        self.entry_box.delete(0, tk.END)

    def check_balance(self):
        self.print_statement(self.atm.check_balance())

    def show_transaction_history(self):
        self.print_statement(self.atm.show_transaction_history())

    def transfer_money(self):
        transfer_window = tk.Toplevel(self.root)
        transfer_window.geometry("300x250")
        transfer_window.title("Transfer Money")

        label_1 = tk.Label(transfer_window, text="Recipient User ID:", font=("Roboto", 12))
        label_1.pack(pady=10)
        recipient_entry = tk.Entry(transfer_window, font=("Roboto", 12))
        recipient_entry.pack(pady=5)

        label_2 = tk.Label(transfer_window, text="Amount:", font=("Roboto", 12))
        label_2.pack(pady=10)
        amount_entry = tk.Entry(transfer_window, font=("Roboto", 12))
        amount_entry.pack(pady=5)

        def submit_transfer():
            recipient_id = recipient_entry.get().strip()
            amount = amount_entry.get().strip()
            result = self.atm.transfer_money(recipient_id, amount)
            messagebox.showinfo("Transfer Money", result)
            transfer_window.destroy()

        submit_button = tk.Button(transfer_window, text="Submit", font=("Roboto", 12), command=submit_transfer)
        submit_button.pack(pady=20)

    def exit_program(self):
        if messagebox.askyesno("Exit", "Do you really want to exit?"):
            messagebox.showinfo("Thank You", "Best of Luck!")
            self.root.destroy()


if __name__ == "__main__":
    atm = ATM()
    atm_gui = ATMGUI(atm)
    atm_gui.start()
