import math
def getPower(distancex1,distancey1,angle):
    distancex = distancex1
    distancey = distancey1
    thetat = angle
    g = -379.106 * 0.71145833333
    q = 0.0518718
    power = -2/(g * q)
    power = power * math.sqrt((-1*g*distancex * distancex)/(2 * math.cos(math.radians(thetat))* math.cos(math.radians(thetat)) *(math.tan(math.radians(thetat))*distancex -distancey )))
    return power