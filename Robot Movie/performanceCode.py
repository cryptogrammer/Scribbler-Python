# Utkarsh Garg. partners: Thomas Bridges & MingMing Hu
# 902904045
# utkarsh6@gatech.edu
# Collaboration Statement: We worked alone (we three partners) using only this semester's course materials
# Created in Python 2


# perfomance code
from myro import*
def performancecode():
    aList = []
    p0 = makePicture("starring.gif")
    aList.append(p0)
    p = makePicture("Scene 1 Final.gif")
    aList.append(p)
    p1 = makePicture("Hiding.gif")
    aList.append(p1)
    p11 = makePicture("fade1.gif")
    p12 = makePicture("fade-2.gif")
    p13 = makePicture("fade3.gif")
    p14 = makePicture("fade4.gif")
    p15 = makePicture("fade5.gif")
    p16 = makePicture("fade6.gif")
    p2 = makePicture("Chase Final.gif")
    aList.append(p2)
    p3 = makePicture("Capture Final.gif")
    aList.append(p3)
    p4 = makePicture("Move Final.gif")
    aList.append(p4)
    p5 = makePicture("Move More Final.gif")
    aList.append(p5)
    p6 = makePicture("Push Final.gif")
    aList.append(p6)
    p7 = makePicture("Death Final.gif")
    aList.append(p7)
    p8 = makePicture("Seeing Red.gif")
    aList.append(p8)
    savePicture(aList,"EntireMovie.gif")
