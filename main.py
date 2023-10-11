import pyautogui
import time

def main():
    print("The Forest - Automatic Log Duplication")
    print("Open The Forest in 3 seconds...")

    time.sleep(3)

    pyautogui.PAUSE = 0.01

    while True:
        pyautogui.press('e')
        pyautogui.press('c')
        pyautogui.press('g')

if __name__ == "__main__":
    main()
