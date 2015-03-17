# Utkarsh Garg. partners: Thomas Bridges & MingMing Hu
# 902904045
# utkarsh6@gatech.edu
# Collaboration Statement: We worked alone (we three partners) using only this semester's course materials
# Created in Python 2
from myro import*
init()

def seeingRed():
    #Sets a red tint to a picture by setting the red value to 200 for every pixel.
    p = takePicture()
    r = copyPicture(p)
    show(p)
    for pix in (getPixels(r)):
        a = getRed(pix)
        pix = setRed(pix , 200)
    show(r)
    savePicture(r,"SeeingRed.gif")

def overlay(): 
    p = takePicture()
    win = GraphWin()
    
    image = Image(Point(getWidth(p)/2, getHeight(p)/2), makePixmap(p))
    image.draw(win)
    win["width"] = getWidth(p)
    win["height"] = getHeight(p) 
    image.refresh(win)
    point=Point(getWidth(p)/2, getHeight(p)/2) 
    message = Text(point, "Starring: A-Bot & V-Bot") 
    message.draw(win)
    wait(5)
    win.close()
    
def fadeOut():
   #Fades out a picture to black.
   p = takePicture()
   show(p)
   
   for i in range(5):
    for pix in getPixels(p):
      r = getRed(pix)
      b = getBlue(pix)
      g = getGreen(pix)
      r1 = r-51
      b1 = b-51
      g1 = g-51
      if r1 > 0 and b1 > 0 and g1 > 0:
       setRed(pix , abs(r1))
       setBlue(pix, abs(b1))
       setGreen(pix , abs(g1))
      else:
        setRed(pix ,0)
        setBlue(pix,0)
        setGreen(pix,0)
    wait(5)
    show(p)  



