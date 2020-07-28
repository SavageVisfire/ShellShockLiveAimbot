import cv2.cv2 as cv2
import numpy as np
import matplotlib.pyplot as plt
import GetCoordsOfEnemy
import GetCoordsOfPlayer
import FindShotPowerNeeded
def findTanks():
    img = cv2.imread('ScreenShot.png')
    #Find Enemy Tanks
    #ORANGE_MIN = np.array([155, 195, 0],np.uint8)
    #ORANGE_MAX = np.array([179, 255, 255],np.uint8)
    ORANGE_MIN = np.array([0, 222, 117],np.uint8)
    ORANGE_MAX = np.array([51, 255, 255],np.uint8)
    
    hsv_img = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    frame_threshed = cv2.inRange(hsv_img, ORANGE_MIN, ORANGE_MAX)
    frame_threshed = cv2.GaussianBlur(frame_threshed, (7, 7), 0)
    cv2.imwrite('EnemyTanks.png', frame_threshed)

    #Find Player Tank
    ORANGE_MIN = np.array([21, 222, 0],np.uint8)
    ORANGE_MAX = np.array([65, 255, 225],np.uint8)
    hsv_img = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    frame_threshed = cv2.inRange(hsv_img, ORANGE_MIN, ORANGE_MAX)
    frame_threshed = cv2.GaussianBlur(frame_threshed, (7, 7), 0)
    cv2.imwrite('PlayerTank.png', frame_threshed)
    #plt.imshow(img)
    #plt.show()
    #Enemy Tanks
    #h 155-180
    #s 255-255
    #v 0-255
    #Your Tank
    #h 21-65
    #s 222-255
    #v 0-225

    #Run Next
    PlayerCoords = GetCoordsOfPlayer.GetCoords()
    EnemyCoords = GetCoordsOfEnemy.GetCoords()
    if len(EnemyCoords) > 1:
        #cv2.imshow("Enemy Tanks Detected",cv2.imread("ImageWithEnemyCoords.png"))
        #cv2.waitKey(5000)
        #cv2.destroyAllWindows()
        EnemyNum = int(input("Type Which Enemy you would like (0-"+str(len(EnemyCoords) -1)+ "): "))
    elif len(EnemyCoords) == 1:
        EnemyNum = 0
    elif len(EnemyCoords) == 0:
        return "Error"
    if len(PlayerCoords) > 1:
        #cv2.imshow("Player Tanks Detected",cv2.imread("ImageWithPlayerCoords.png"))
        #cv2.waitKey(5000)
        #cv2.destroyAllWindows()
        PlayerNum = int(input("Type Which Player you would like (0-"+str(len(PlayerCoords) -1)+ "): "))
    elif len(PlayerCoords) == 1:
        PlayerNum = 0
    elif len(PlayerCoords) == 0:
        return "Error"
    x1,y1 = EnemyCoords[EnemyNum]
    x2,y2 = PlayerCoords[PlayerNum]
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
                #print("Power: "+str(power))
        except:
            print('nope')
        if angle > 90:
            break
    return "Success"