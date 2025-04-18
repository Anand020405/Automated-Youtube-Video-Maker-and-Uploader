import pyautogui
import time

print("Move your mouse to the desired location. Press Ctrl+C to stop.")

try:
    while True:
        x, y = pyautogui.position()
        print(f"X: {x}, Y: {y}", end='\r')  # \r keeps it on the same line
        time.sleep(0.1)
except KeyboardInterrupt:
    print("\nStopped.")
