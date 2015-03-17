# Utkarsh Garg. partners: Thomas Bridges & MingMing Hu
# 902904045
# utkarsh6@gatech.edu
# Collaboration Statement: We worked alone (we three partners) using only this semester's course materials
# Created in Python 2




from myro import *


# Since this was filmed from A-Bot's perspective we don't necessarily have a separate
# filming and acting code. So, this code is essentially those two codes combined. 


# takeOne function
# Assasin Bot(a.k.a. A-Bot) simply moves forward and scans the area, going forward
# and turning occassionaly to simulate looking around. AB then notices the
# other robot.

def takeOne():
    aList = []
    for i in range(20):
       forward(.5,.5)
       p = takePicture()
       aList.append(p)
    for i in range(4):
       turnRight(.5,.5)
       p = takePicture()
       aList.append(p)
    for i in range(8):
       turnLeft(.5,.5)
       p = takePicture()
       aList.append(p)
    for i in range(4):
       turnRight(.5,.5)
       p = takePicture()
       aList.append(p)

    for i in range(20):
       p = takePicture()
       forward(.5,1)
       aList.append(p)

    for i in range(4):
       turnRight(.5,.5)
       p = takePicture()
       aList.append(p)
    for i in range(8):
       turnLeft(.5,.5)
       p = takePicture()
       aList.append(p)
    for i in range(4):
       turnRight(.5,.5)
       p = takePicture()
       aList.append(p)
    for i in range(5):
       p = takePicture()
       forward(.5,1)
       aList.append(p)
    for i in range(3):
        p = takePicture()
        turnLeft(.5,.5)
        aList.append(p)
    for i in range(10):
        p = takePicture()
        forward(.5,.2)

    savePicture(aList,"scene1.gif")

# hide function
# This code is run after [takeOne()] AB notices its victim (a.k.a. V-Bot), then it goes
# into hiding to avoid being noticed.

def hide():
    hideList = []
    for i in range(7):
        backward(1,.8)
        p = takePicture()
        hideList.append(p)

    turnRight(1,.21)
    p = takePicture()
    hideList.append(p)

    turnRight(1,.21)
    p = takePicture()
    hideList.append(p)

    turnRight(1,.21)
    p = takePicture()
    hideList.append(p)

    
    forward(1,2.2)
    p = takePicture()
    hideList.append(p)
    savePicture(hideList, "Hiding.gif")

# leaveRoom V-BOT
# This function is run [in conjunction with A-Bot running filmBot()] after
# V-Bot noticed that he has been followed and looks around then leaves the room.

def leaveRoom(): #code by V-Bot
    turnRight(1,.73)
    turnLeft(1,.73)
    turnLeft(1,.73)
    turnRight(1,.73)
    forward(1,10)


# filmBot function
# This function is run [after hide(), while V-Bot runs leaveRoom()] A-Bot simply watches
# V-Bot look around and leave the area.

def filmBot():
    filmList = []
    while timeRemaining(13):
        p = takePicture()
        filmList.append(p)
    savePicture(filmList, "filmBot.gif")

# runAway funtion V-BOT
# This function is run after [leaveRoom(), while A-Bot runs chaseScene()] V-Bot
# leaves the room and continues to attempt to escape. 

def runAway(): #Code by V-Bot
    forward(1,20)
    turnRight(1,.6)
    forward(1,10)

# chaseScene funtion
# This function is run as [after flimBot(), change of scenery while V-Bot runs runAway()] A-Bot has found his way to where V-Bot has attempted
# to escape. A-Bot simply sits and watches as V-Bot tries to run away. 

def chaseScene():
    chaseList = []
    while timeRemaining(35):
        p = takePicture()
        chaseList.append(p)
        
        savePicture(chaseList, "chase.gif")

# capture function
# This code is run after A-Bot has seen V-Bot try to escape. A-Bot then follows
# V-Bot to the stairs which are a dead end. 


def capture():
    captureList=[]
    while timeRemaining(47):
        forward(1,.5)
        p = takePicture()
        captureList.append(p)
        savePicture(captureList, "capture.gif")


# move function
# This code is run immediately after [capture()]. A-Bot approaches V-Bot and
# sees that V-Bot is cornered.

def move():
    moveList=[]
    forward(1,.5)
    p = takePicture()
    moveList.append(p)
    
    forward(1,.5)
    p = takePicture()
    moveList.append(p)
    
    forward(1,.5)
    p = takePicture()
    moveList.append(p)
    
    forward(1,.5)
    p = takePicture()
    moveList.append(p)
    
    forward(1,.5)
    p = takePicture()
    moveList.append(p)

    forward(1,.5)
    p = takePicture()
    moveList.append(p)
    
    turnRight(1,.25)
    p = takePicture()
    moveList.append(p)

    turnRight(.8,.25)
    p = takePicture()
    moveList.append(p)

      
    while timeRemaining(8):
        forward(1,.5)
        p = takePicture()
        
        moveList.append(p)
        savePicture(moveList, "move.gif")

# moveMore function
# This function is run after [move()] A-Bot has found V-Bot to be cornered.
# A-Bot approaches V-Bot slowly as V-Bot panics to find a way out.

def moveMore():
    moveMoreList=[]
    while timeRemaining(18):
        forward(1,.5)
        p = takePicture()
        
        moveMoreList.append(p)
        savePicture(moveMoreList, "moveMore.gif")

# push function
# This function is run after [moveMore()] A-Bot just rushes forward to push
# V-Bot down the stairs to kill it.

def push():
    pushList=[]
    while timeRemaining(45):
        forward(1,.5)
        p = takePicture()
        
        pushList.append(p)
        savePicture(pushList, "push.gif")

# death function
# This function was run after [push()]. However this function required some
# "hands-on" camera work as it's nearly impossible to get a scribbler to traverse
# a flight of stairs without completely destroying it. So, we ran this function
# with the A-Bot in our hand and just took pictures moving down the stairs for
# A-Bot to see that his job was finished and V-Bot was finally dead. 

def death():
    deathList = []
    while timeRemaining(15):
        p = takePicture()
        deathList.append(p)
        beep(.3, 800)
        savePicture(deathList, "death.gif")
