import pyautogui as pg
import time

try:
    print("Starting in 5 seconds...")
    time.sleep(5)

    for i in range(100):
        pg.write("jyotika = alien")
        pg.press("enter")
        time.sleep(0.1)  # You may need to adjust the sleep time for your system

except Exception as e:
    print(f"An error occurred: {e}")
