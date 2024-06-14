import pyperclip


class Clipboard:
    def __init__(self):
        pass

    def copy_to_clipboard(self, text):
        pyperclip.copy(text)
