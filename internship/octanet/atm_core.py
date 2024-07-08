#atm_core.py
import json
import os

from cryptography.fernet import Fernet


class ATM:
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

    def validate_amount(self, amount):
        try:
            amount = int(amount)
            if amount <= 0:
                raise ValueError("Amount must be positive")
            return amount
        except ValueError:
            return None

    def verify_user(self, user_id, pin):
        if user_id in self.users and self.users[user_id]['pin'] == pin:
            self.current_user = user_id
            return True
        return False

    def register_user(self, user_id, pin):
        if user_id in self.users:
            return False
        self.users[user_id] = {"pin": pin, "balance": 0, "history": []}
        self.save_user_data()
        return True

    def withdraw(self, amount):
        amount = self.validate_amount(amount)
        if amount is None:
            return "Invalid amount"
        if amount <= self.users[self.current_user]['balance']:
            self.users[self.current_user]['balance'] -= amount
            self.users[self.current_user]['history'].append(f"Withdrawn: {amount}")
            self.save_user_data()
            return f"Successfully withdrawn {amount}"
        return "Insufficient balance"

    def deposit(self, amount):
        amount = self.validate_amount(amount)
        if amount is None:
            return "Invalid amount"
        self.users[self.current_user]['balance'] += amount
        self.users[self.current_user]['history'].append(f"Deposited: {amount}")
        self.save_user_data()
        return f"Successfully deposited {amount}"

    def check_balance(self):
        return f"Your balance is {self.users[self.current_user]['balance']}"

    def show_transaction_history(self):
        return "\n".join(self.users[self.current_user]['history'][-5:])

    def transfer_money(self, recipient_id, amount):
        amount = self.validate_amount(amount)
        if amount is None:
            return "Invalid amount"
        if recipient_id not in self.users:
            return "Recipient User ID not found"
        if amount > self.users[self.current_user]['balance']:
            return "Insufficient balance"
        self.users[self.current_user]['balance'] -= amount
        self.users[self.current_user]['history'].append(f"Transferred {amount} to {recipient_id}")
        self.users[recipient_id]['balance'] += amount
        self.users[recipient_id]['history'].append(f"Received {amount} from {self.current_user}")
        self.save_user_data()
        return f"Successfully transferred {amount} to {recipient_id}"
