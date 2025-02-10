import pyautogui
import time
import csv


PASSWORD_FIELD_X, PASSWORD_FIELD_Y = 1256, 774

CSV_FILE = '4digit.csv'

SCREEN_REGION = (100, 200, 300, 400)  

def screen_has_changed(before, after):
    """Compares two screenshots and returns True if they are different."""
    return before != after

def enter_passwords():
    with open(CSV_FILE, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for index, row in enumerate(reader):
            if row:  
                password = row[0].strip()

                screenshot_before = pyautogui.screenshot(region=SCREEN_REGION)

                pyautogui.click(PASSWORD_FIELD_X, PASSWORD_FIELD_Y)
                time.sleep(0.1)  

                pyautogui.typewrite(password)
                time.sleep(2)  
                print(f"Entered password: {password}")

                if index > 0:
                    pyautogui.click(PASSWORD_FIELD_X, PASSWORD_FIELD_Y)
                    pyautogui.press('backspace', presses=len(password))
                    time.sleep(0.1)  

                pyautogui.typewrite(password)
                time.sleep(2)  
                print(f"Entered password: {password}")

                screenshot_after = pyautogui.screenshot(region=SCREEN_REGION)

                if screen_has_changed(screenshot_before, screenshot_after):
                    print("Correct password entered. Exiting...")
                    break

                if (index + 1) % 100 == 0:
                    print(f"\n\n100 passwords reached!\n\n")

if __name__ == "__main__":
    enter_passwords()

