import keyboard
import win32api
import FindShotPowerNeeded
Target = (0,0)
Player = (0,0)
def getPower():
    x1,y1 = Target
    x2,y2 = Player
    print(x1,x2,y1,y2)
    distancex = abs(x1-x2)
    distancey = y1-y2
    angle = 0
    while True:
        angle = angle + 1
        try:
            power = FindShotPowerNeeded.getPower(distancex,distancey,angle)
            if power < 100:
                print("Angle: " +str(angle) + ", Power: " + str(power))
        except:
            print('N/A, over 100 power required')
        if angle > 90:
            break
    return "Success"
while True:
    try:
        if keyboard.is_pressed('['):
            break
        if keyboard.is_pressed('P'):
            x, y = win32api.GetCursorPos()
            Player = (x,y)
        if keyboard.is_pressed('T'):
            x, y = win32api.GetCursorPos()
            Target = (x,y)
        if keyboard.is_pressed('|'):
            print(getPower())
    except:
        x = 1+1