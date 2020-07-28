import numpy as np 
import cv2.cv2 as cv2
  
def GetCoords():
    COORDSTOSEND = []
    # Reading image 
    font = cv2.FONT_HERSHEY_COMPLEX 
    img2 = cv2.imread('PlayerTank.png', cv2.IMREAD_COLOR)
    # Reading same image in another  
    # variable and converting to gray scale. 
    img = cv2.imread('PlayerTank.png', cv2.IMREAD_GRAYSCALE)
    # Converting image to a binary image 
    # ( black and white only image). 
    _, threshold = cv2.threshold(img, 110, 255, cv2.THRESH_BINARY) 
    # Detecting contours in image. 
    contours, _= cv2.findContours(threshold, cv2.RETR_TREE, 
                                cv2.CHAIN_APPROX_SIMPLE)
    tankNum = 0 
    # Going through every contours found in the image. 
    for cnt in contours : 
        data = []
        approx = cv2.approxPolyDP(cnt, 0.009 * cv2.arcLength(cnt, True), True) 
    
        # draws boundary of contours. 
        #cv2.drawContours(img2, [approx], 0, (0, 0, 255), 5)    
        # Used to flatted the array containing 
        # the co-ordinates of the vertices. 
        n = approx.ravel()  
        i = 0
    
        for j in n : 
            #delete x=j if it causes issues.
            x=j
            if(i % 2 == 0): 
                x = n[i] 
                y = n[i + 1] 
                data.append((x,y))
                string = str(x) + " " + str(y)
            i = i + 1
        #print(data)
        x,y = np.mean(data, axis=0)
        string = str(x)+" "+str(y)
        if y<650:
            print(string)
            COORDSTOSEND.append((x,y))
            cv2.putText(img2, str(tankNum), (int(x), int(y)),  font, 4, (0, 255, 0))
            tankNum = tankNum + 1
            cv2.drawContours(img2, [approx], 0, (0, 0, 255), 5)
    # Showing the final image. 
    #cv2.imshow('image2', img2)  
    cv2.imwrite('ImageWithPlayerCoords.png', img2)
    # Exiting the window if 'q' is pressed on the keyboard. 
    if cv2.waitKey(0) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
    return COORDSTOSEND