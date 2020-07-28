import pyautogui
import keyboard
import win32api
import time
import FindTanks
start = 0
end = 0
while True:
    try:
        if keyboard.is_pressed('|'):
            print('You Pressed A Key!')
            myScreenshot = pyautogui.screenshot()
            myScreenshot.save('ScreenShot.png')
            print(FindTanks.findTanks())
        if keyboard.is_pressed('['):
            break
        #if keyboard.is_pressed(']'):
        #    x, y = win32api.GetCursorPos()
        #    print(x,y)
        #if keyboard.is_pressed('space'):
        #    start = time.time()
        #    print(start)
        #if keyboard.is_pressed('/'):
        #    end = time.time()
        #    print(end - start)
    except:
        x = 1+1