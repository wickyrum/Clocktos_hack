import pyautogui
import time
import csv

# Coordinates for the password field
PASSWORD_FIELD_X, PASSWORD_FIELD_Y = 1256, 774

# Path to the CSV file with passwords
CSV_FILE = '4digit.csv'

# Region of the screen to check for changes (adjust as needed)
SCREEN_REGION = (100, 200, 300, 400)  # Example coordinates: (x, y, width, height)

def screen_has_changed(before, after):
    """Compares two screenshots and returns True if they are different."""
    return before != after

def enter_passwords():
    with open(CSV_FILE, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for index, row in enumerate(reader):
            if row:  # Skip empty rows
                password = row[0].strip()

                # Take a screenshot of the region before entering the password
                screenshot_before = pyautogui.screenshot(region=SCREEN_REGION)

                # Step 1: Touch the password field
                pyautogui.click(PASSWORD_FIELD_X, PASSWORD_FIELD_Y)
                time.sleep(0.1)  # Brief pause

                # Step 2: Enter the password
                pyautogui.typewrite(password)
                time.sleep(2)  # Increased pause to wait for app buffering
                print(f"Entered password: {password}")

                # Check if this is not the first entry, then use backspace
                if index > 0:
                    pyautogui.click(PASSWORD_FIELD_X, PASSWORD_FIELD_Y)
                    pyautogui.press('backspace', presses=len(password))
                    time.sleep(0.1)  # Brief pause

                # Enter the password again
                pyautogui.typewrite(password)
                time.sleep(2)  # Increased pause to wait for app buffering
                print(f"Entered password: {password}")

                # Take a screenshot after entering the password
                screenshot_after = pyautogui.screenshot(region=SCREEN_REGION)

                # Check if the screen has changed
                if screen_has_changed(screenshot_before, screenshot_after):
                    print("Correct password entered. Exiting...")
                    break

                # Output "100 passwords reached" after every 100 passwords
                if (index + 1) % 100 == 0:
                    print(f"\n\n100 passwords reached!\n\n")

if __name__ == "__main__":
    enter_passwords()

