import tkinter as tk

from gui import PasswordGeneratorGUI


def main():
    root = tk.Tk()
    root.title('Password Generator')
    app = PasswordGeneratorGUI(master=root)
    app.mainloop()


if __name__ == "__main__":
    main()
