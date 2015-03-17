#Utkarsh garg
#utkarsh6@gatech.edu

from myro import*
init()


def SeeingRed():
    #Sets a red tint to a picture by setting the red value to 170 for every pixel.
    p = takePicture()
    r = copyPicture(p)
    show(p)
    for pix in (getPixels(r)):
        a = getRed(pix)
        pix = setRed(pix , 170)
    show(r)
    savePicture(r,"SeeingRed.gif")
SeeingRed()


def robotZoom():
    #Zooms in a number of times equal to n.
    aList=[]
    n = input("How many times do you want it to zoom ?")
    for x in range(int(n)):
        p = takePicture()
        aList.append(p)
        forward(1,0.7)
    for y in range(len(aList)):
        show(aList[y])
        wait(.7)
    savePicture(aList,"Robotzoom.gif")
robotZoom()

def dollyShot():
    #Similar to robotZoom, but the robot turns before and after taking the picture.
    aList=[]
    for x in range(6):
        turnLeft(1,0.7)
        p = takePicture()
        turnRight(1,0.7)
        aList.append(p)
        forward(1,1)
    for y in range(len(aList)):
        show(aList[y])
        wait(.7)
    savePicture(aList,"dollyShot.gif")
dollyShot()


def fadeOut():
   #Fades out a picture.
   x = input("How many layers do you want?")
   x = int(x)
   p = takePicture()
   show(p)
   for i in range(x):
    for pix in getPixels(p):
      r = getRed(pix)
      b = getBlue(pix)
      g = getGreen(pix)
      r1 = r-255/x
      b1 = b-255/x
      g1 = g-255/x
      if r1 > 0 and b1 > 0 and g1 > 0:
       setRed(pix , abs(r1))
       setBlue(pix, abs(b1))
       setGreen(pix , abs(g1))
      else:
        setRed(pix ,0)
        setBlue(pix,0)
        setGreen(pix,0)
    savePicture(p,"faded.jpg")
    show(p)
fadeOut()

def multipleExposure():
    #combines two pictures by averaging out their pixel rgb values.
    p = takePicture()
    forward(1,1)
    turnRight(1,0.5)
    p1 = takePicture()
    for x in range(getWidth(p)):
        for y in range(getHeight(p)):
            pix = getPixel(p,x,y)
            pixl = getPixel(p1,x,y)
            r1 = getRed(pix)
            g1 = getGreen(pix)
            b1 = getBlue(pix)
            r2 = getRed(pixl)
            g2 = getGreen(pixl)
            b2 = getBlue(pixl)
            r = (r1+r2)/2
            b = (b1+b2)/2
            g = (g1+g2)/2
            setRed(pix,r)
            setGreen(pix,g)
            setBlue(pix,b)
    show(p)
multipleExposure()

def seeingChristmas():
    p  = takePicture()
    #Tints half the picture red, and half the picture Green. Because this is slightly more complicated than the seeingRed function, we believe we should get 35 points for this original function.
    for pix in getPixels(p):
        r = getRed(pix)
        g = getGreen(pix)
        x = getX(pix)
        if x <= 127:
            setRed(pix, r+80)
        else:
            setGreen(pix,g+80)
    show(p)
seeingChristmas()

def tempoChange():
    #Drastically changes the tempo of a video.
    k = []
    p = [r1,r2,r3,r1,r2,r3,r1,r2,r3]
    r1 = takePicture()
    turnRight(.5,.5)
    r2 = takePicture()
    turnRight(.5,.5)
    r3 = takePicture()
    k = [r1,r1,r1,r1,r1,r1,r1,r1,r1,r2,r2,r2,r2,r2,r2,r2,r3,r3,r3,r3,r3,r3,r3,r3]
    p.append(l)
    savePicture(p , "motion.gif")
tempoChange()


def flashingLights():
    #Creates alternate red, green and blue tints for a picture. I expect to get about 35 points for this function.
    p = takePicture()
    p1 = copyPicture(p)
    p2 = copyPicture(p)
    show(p)
    for i in range(10):
     for pix in getPixels(p):
       r = getRed(pix)
       setRed(pix, 190)
     show(p)
     show(p1)
     for pix in getPixels(p1):
       g = getGreen(pix)
       setGreen(pix, 210)
     show(p1)
     show(p2)
     for pix in getPixels(p2):
       b = getBlue(pix)
       setBlue(pix, 200)
     show(p2)
     show(p)
flashingLights()


def view360():
    #Shows a panoramic 360 degree photo from several pictures.
    aList = []
    for i in range(9):
        p = takePicture()
        aList = aList + [p]
        turnRight(1,0.5)
    savePicture(aList , "360view.gif")
    around = makePicture("360view.gif")
    show(around)
view360()

def crossfade(p1, p2, s):
    
    p1 = makePicture(p1)
    p2 = makePicture(p2)
    aList1 = []
    
    for i in range(s+1):
        for pix in getPixels(p1):
            r = getRed(pix)
            b = getBlue(pix)
            g = getGreen(pix)
            
            x = getX(pix)
            y = getY(pix)

            p = getPixel(p2, x, y)
            r2 = getRed(p)
            b2 = getBlue(p)
            g2 = getGreen(p)

            setRed(pix, r + (r2 - r)*i / float(s))
            setBlue(pix, b + (b2 - b)*i / float(s))
            setGreen(pix, g + (g2 - g)*i / float(s))
            aList1.append(Pic1)
        show(p1)
        print "sss"

    for n in aList1[]:
        show(n)

    savePicture(aList1, crossfaderesult.gif)
crossfade()
    
