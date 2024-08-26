import pyautogui
import time
try:
    while True:
        print(pyautogui.position())
        time.sleep(0.4)
except KeyboardInterrupt:
    print("\nDone.")

