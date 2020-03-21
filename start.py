import pyautogui, time

print('Welcome to "StayOn" program.')

while True:
    input('To start the mouse movement, press Enter\nYou can stop it anytime with Ctrl+C')
    try:
        while True:
            pyautogui.move(0, 200, duration=0.5)
            pyautogui.leftClick()
            pyautogui.move(0, -200, duration=0.5)
            pyautogui.leftClick()
            time.sleep(2)
    except KeyboardInterrupt:
        print('Interrupted')
