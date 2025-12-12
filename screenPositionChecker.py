import pyautogui
import time
import sys

print("--- Mouse Coordinate Tracker ---")
print("Press Ctrl+C to stop.")

try:
    while True:
        x, y = pyautogui.position()

        sys.stdout.write(f"\rCurrent Position: X={x:<5} Y={y:<5}")
        sys.stdout.flush()

        time.sleep(0.1)

except KeyboardInterrupt:
    print("\n\nStopped.")
