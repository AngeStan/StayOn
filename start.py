import pyautogui, time

print('Welcome to "StayOn" program.\n')

while True:
    input('\nTo start the mouse movement, press Enter\nYou can stop it anytime with Ctrl+C')
    try:
        while True:
            pyautogui.move(0, 200, duration=0.5)
            pyautogui.leftClick()
            pyautogui.move(0, -200, duration=0.5)
            pyautogui.leftClick()
            time.sleep(60)
    except KeyboardInterrupt:
        print('\nInterrupted')
