import random
import string


class PasswordGenerator:
    def __init__(self):
        # For those characters which look same or can be confusing
        self.similar_characters = {
            'l': '1',
            '1': 'l',
            'I': 'l',
            'o': '0',
            'O': '0',
            '0': 'o',
            's': '5',
            'S': '5',
            'z': '2',
            'Z': '2',
            'B': '8',
            '8': 'B',
            'g': '9',
            'q': '9',
            '9': 'gq',
            'c': '(',
            '(': 'c',
            ')': '(',
            '[': '{',
            '{': '[',
            ']': '}',
            '}': ']',
            'I': '|',
            '|': 'I',
            '\\': '/',
            '/': '\\',
            '`': "'",
            "'": "`"
        }

    def generate_custom_password(self, length, use_letters=True, use_digits=True, use_symbols=True):
        characters = ''
        if use_letters:
            characters += string.ascii_letters
        if use_digits:
            characters += string.digits
        if use_symbols:
            characters += string.punctuation

        if length < 8:
            raise ValueError("Password length must be at least 8 characters.")

        if not (use_letters and use_digits and use_symbols):
            raise ValueError(
                "Password must include at least one character from each category: letters, digits, symbols.")

        password = ''.join(random.choice(characters) for _ in range(length))
        password = self.remove_similar_characters(password)

        return password

    def remove_similar_characters(self, password):
        for char in password:
            if char in self.similar_characters:
                password = password.replace(char, self.similar_characters[char])
        return password
