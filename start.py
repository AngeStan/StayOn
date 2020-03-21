import pyautogui
import time

print('Welcom to "StayOn" program.')

try:
    while True:
        pyautogui.moveTo(100, 0, duration=0.5)
        time.sleep(5)
        pyautogui.moveTo(100, 100, duration=0.5)
        time.sleep(5)
except KeyboardInterrupt:
    print('Interrupted')
