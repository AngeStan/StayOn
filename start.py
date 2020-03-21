import pyautogui, time

print('Welcome to "StayOn" program.\n')

while True:
    input('\nTo start the mouse movement, press Enter\nYou can stop it anytime with Ctrl+C')
    try:
        print('\nStarted...')
        while True:
            time.sleep(10)
            pyautogui.move(0, 200, duration=0.5)
            pyautogui.leftClick()
            pyautogui.move(0, -200, duration=0.5)
            pyautogui.leftClick()
            time.sleep(50)
    except KeyboardInterrupt:
        print('\nInterrupted')
