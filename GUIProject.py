import tkinter as tk
from tkinter import Canvas
from tkinter import Button
from tkinter import messagebox
from tkinter import PhotoImage
import random
import time
import winsound

wn = tk.Tk()
wn.title("Pizza Roll Quest")
wn.geometry('640x480')
icon = tk.PhotoImage(file='Sprites/pizzarollicon.png')
wn.iconphoto(False, icon)
canvas = Canvas(wn, width=640, height=480)
canvas.pack(expand=1, fill="both")
bgimg = PhotoImage(file='Sprites/bricks.png')  # background brick image
logo = PhotoImage(file='Sprites/logosprite.png')
canvas.create_image(320, 240, image=bgimg, anchor='center')
startText = canvas.create_text(320, 450, text="Click anywhere to start!",
                               fill="yellow", font=("Fixedsys", 20), tags=("menuitem", "startText"))
textToggle = False  # text will flash on and off using this bool
# Animations
Frames1 = [PhotoImage(file='Sprites/000.png'),
           PhotoImage(file='Sprites/001.png'),
           PhotoImage(file='Sprites/002.png'),
           PhotoImage(file='Sprites/003.png'),
           PhotoImage(file='Sprites/004.png'),
           PhotoImage(file='Sprites/005.png'),
           PhotoImage(file='Sprites/006.png')]  # Pizza Roll Frames; the cornerstone of the program
Frames2 = [PhotoImage(file='Sprites/007.png'),
           PhotoImage(file='Sprites/008.png'),
           PhotoImage(file='Sprites/009.png'),
           PhotoImage(file='Sprites/008.png'),
           PhotoImage(file='Sprites/007.png'),
           PhotoImage(file='Sprites/008.png'),
           PhotoImage(file='Sprites/009.png')]  # Title Frames
Frames3 = [PhotoImage(file='Sprites/arms/001.png'),
           PhotoImage(file='Sprites/arms/002.png'),
           PhotoImage(file='Sprites/arms/003.png'),
           PhotoImage(file='Sprites/arms/004.png'),
           PhotoImage(file='Sprites/arms/005.png')]  # Arms Collect
Frames4 = [PhotoImage(file='Sprites/arms/006.png'),
           PhotoImage(file='Sprites/arms/007.png'),
           PhotoImage(file='Sprites/arms/008.png'),
           PhotoImage(file='Sprites/arms/009.png'),
           PhotoImage(file='Sprites/arms/010.png')]  # Arms Attack
Frames5 = [PhotoImage(file='Sprites/goblin/000.png'),
           PhotoImage(file='Sprites/goblin/001.png'),
           PhotoImage(file='Sprites/goblin/002.png'),
           PhotoImage(file='Sprites/goblin/003.png'),
           PhotoImage(file='Sprites/goblin/004.png'),
           PhotoImage(file='Sprites/goblin/005.png')]  # Goblin Idle
Frames6 = [PhotoImage(file='Sprites/goblin/006.png'),
           PhotoImage(file='Sprites/goblin/007.png'),
           PhotoImage(file='Sprites/goblin/008.png'),
           PhotoImage(file='Sprites/goblin/009.png')]  # Goblin Attack
Frames7 = [PhotoImage(file='Sprites/goblin/010.png'),
           PhotoImage(file='Sprites/goblin/011.png')]  # Goblin Damage
Frames8 = [PhotoImage(file='Sprites/goblin/010.png'),
           PhotoImage(file='Sprites/goblin/011.png'),
           PhotoImage(file='Sprites/goblin/012.png'),
           PhotoImage(file='Sprites/goblin/013.png'),
           PhotoImage(file='Sprites/goblin/014.png'),
           PhotoImage(file='Sprites/goblin/015.png'),
           PhotoImage(file='Sprites/goblin/016.png'),
           PhotoImage(file='Sprites/goblin/017.png')]  # Goblin Death
Frames9 = [PhotoImage(file='Sprites/hologram/000.png'),
           PhotoImage(file='Sprites/hologram/001.png'),
           PhotoImage(file='Sprites/hologram/002.png'),
           PhotoImage(file='Sprites/hologram/003.png'),
           PhotoImage(file='Sprites/hologram/004.png'),
           PhotoImage(file='Sprites/hologram/005.png'),
           PhotoImage(file='Sprites/hologram/006.png'),
           PhotoImage(file='Sprites/hologram/007.png'),
           PhotoImage(file='Sprites/hologram/008.png'),
           PhotoImage(file='Sprites/hologram/009.png'),
           PhotoImage(file='Sprites/hologram/010.png'),
           PhotoImage(file='Sprites/hologram/011.png'),
           PhotoImage(file='Sprites/hologram/012.png')]  # Hologram Frames
Frames10 = [PhotoImage(file='Sprites/death/000.png'),
            PhotoImage(file='Sprites/death/001.png'),
            PhotoImage(file='Sprites/death/002.png'),
            PhotoImage(file='Sprites/death/003.png'),
            PhotoImage(file='Sprites/death/004.png'),
            PhotoImage(file='Sprites/death/005.png'),
            PhotoImage(file='Sprites/death/006.png'),
            PhotoImage(file='Sprites/death/007.png'),
            PhotoImage(file='Sprites/death/008.png'),
            PhotoImage(file='Sprites/death/009.png'),
            PhotoImage(file='Sprites/death/010.png'),
            PhotoImage(file='Sprites/death/011.png')]  # Death Frames
myImage1 = canvas.create_image(320, 330, image=Frames1[0], anchor='center', tags="menuitem")  # Menu Pizza Roll
myImage2 = canvas.create_image(320, 120, image=Frames2[0], anchor='center', tags="menuitem")  # Menu Title
arms = PhotoImage(file='Sprites/arms/000.png')  # players arms
gameFrame = PhotoImage(file='Sprites/frame.png')
textFrame = PhotoImage(file='Sprites/frame2.png')
loop = True  # bool that controls program's main while loop
menuloop = True
gameloop = False
Screens = [PhotoImage(file='Sprites/dungeon/4way/000.png'),
           PhotoImage(file='Sprites/dungeon/3wayright/000.png'),
           PhotoImage(file='Sprites/dungeon/3wayleft/000.png'),
           PhotoImage(file='Sprites/dungeon/fork/000.png'),
           PhotoImage(file='Sprites/dungeon/deadend/000.png')]  # sprites for each possible corridor type
Corridor = ["FOURWAY", "THREEWAYRIGHT", "THREEWAYLEFT", "THREEWAYFORK", "DEADEND"]  # corridor types
currentscreen = ""  # current corridor type displayed
transition = False  # toggles transition animations between corridor screens
transitionIndex = 0  # used to increment over the frames of transition animations
pathIndex = 0  # index of whichever corridor screen is being used
anim = []  # empty PhotoImage array to later be filled with a relevant corridor transition animation
btnForward = Button  # game buttons
btnBackward = Button
btnLeft = Button
btnRight = Button
btnAttack = Button
btnCollect = Button  # button to grab pizza roll
collectButtonOnScreen = False
attack = False  # true if player is attacking with sword
rollOnScreen = False  # true if a pizza roll is on screen
goblinOnScreen = False  # true if a goblin is on screen
goblinAttack = False  # true if a goblin is attacking
goblinPain = False  # true if a goblin is in pain
goblinDeath = False  # true is a goblin is dead
goblinLives = 5  # amount of hits it takes to kill a goblin
playerDead = False  # true is player has died
hologramOnScreen = False  # true if a hologram Ted head is on screen
score = 0  # number of pizza rolls collected
scoretext = ""  # on screen score text
tiptext = ""  # text for tip box
fallbacktext = ""  # default tip that will display


def DisableButtons():  # disables game buttons, usually to prepare for a transition between corridor screens
    global rollOnScreen
    global hologramOnScreen
    global goblinOnScreen
    global collectButtonOnScreen
    btnForward["state"] = "disable"
    btnBackward["state"] = "disable"
    btnLeft["state"] = "disable"
    btnRight["state"] = "disable"
    btnForward.configure(background="gray")
    btnBackward.configure(background="gray")
    btnRight.configure(background="gray")
    btnLeft.configure(background="gray")
    btnAttack["state"] = "disable"
    btnAttack.configure(background="gray")
    canvas.delete("pizzaroll")
    canvas.delete("goblin")
    canvas.delete("hologram")
    if collectButtonOnScreen:
        btnCollect.destroy()
        collectButtonOnScreen = False
    hologramOnScreen = False
    rollOnScreen = False
    goblinOnScreen = False


def MoveForward():
    DisableButtons()  # don't want someone clicking these when in the middle of transitioning
    global currentscreen
    global anim
    global transition
    if currentscreen == "FOURWAY":
        anim = [PhotoImage(file='Sprites/dungeon/4way/005.png'),
                PhotoImage(file='Sprites/dungeon/4way/006.png'),
                PhotoImage(file='Sprites/dungeon/4way/007.png'),
                PhotoImage(file='Sprites/dungeon/4way/008.png')]
    elif currentscreen == "THREEWAYRIGHT":
        anim = [PhotoImage(file='Sprites/dungeon/3wayright/005.png'),
                PhotoImage(file='Sprites/dungeon/3wayright/006.png'),
                PhotoImage(file='Sprites/dungeon/3wayright/007.png'),
                PhotoImage(file='Sprites/dungeon/3wayright/008.png')]
    elif currentscreen == "THREEWAYLEFT":
        anim = [PhotoImage(file='Sprites/dungeon/3wayleft/005.png'),
                PhotoImage(file='Sprites/dungeon/3wayleft/006.png'),
                PhotoImage(file='Sprites/dungeon/3wayleft/007.png'),
                PhotoImage(file='Sprites/dungeon/3wayleft/008.png')]
    currentscreen = NewLocation()
    transition = True


def MoveLeft():
    DisableButtons()
    global currentscreen
    global anim
    global transition
    if currentscreen == "FOURWAY":
        anim = [PhotoImage(file='Sprites/dungeon/4way/001.png'),
                PhotoImage(file='Sprites/dungeon/4way/002.png'),
                PhotoImage(file='Sprites/dungeon/4way/003.png'),
                PhotoImage(file='Sprites/dungeon/4way/004.png')]
    elif currentscreen == "THREEWAYLEFT":
        anim = [PhotoImage(file='Sprites/dungeon/3wayleft/001.png'),
                PhotoImage(file='Sprites/dungeon/3wayleft/002.png'),
                PhotoImage(file='Sprites/dungeon/3wayleft/003.png'),
                PhotoImage(file='Sprites/dungeon/3wayleft/004.png')]
    elif currentscreen == "THREEWAYFORK":
        anim = [PhotoImage(file='Sprites/dungeon/fork/001.png'),
                PhotoImage(file='Sprites/dungeon/fork/002.png'),
                PhotoImage(file='Sprites/dungeon/fork/003.png'),
                PhotoImage(file='Sprites/dungeon/fork/004.png')]
    currentscreen = NewLocation()
    transition = True


def MoveRight():
    DisableButtons()
    global currentscreen
    global anim
    global transition
    if currentscreen == "FOURWAY":
        anim = [PhotoImage(file='Sprites/dungeon/4way/013.png'),
                PhotoImage(file='Sprites/dungeon/4way/014.png'),
                PhotoImage(file='Sprites/dungeon/4way/015.png'),
                PhotoImage(file='Sprites/dungeon/4way/016.png')]
    elif currentscreen == "THREEWAYRIGHT":
        anim = [PhotoImage(file='Sprites/dungeon/3wayright/001.png'),
                PhotoImage(file='Sprites/dungeon/3wayright/002.png'),
                PhotoImage(file='Sprites/dungeon/3wayright/003.png'),
                PhotoImage(file='Sprites/dungeon/3wayright/004.png')]
    elif currentscreen == "THREEWAYFORK":
        anim = [PhotoImage(file='Sprites/dungeon/fork/009.png'),
                PhotoImage(file='Sprites/dungeon/fork/010.png'),
                PhotoImage(file='Sprites/dungeon/fork/011.png'),
                PhotoImage(file='Sprites/dungeon/fork/012.png')]
    currentscreen = NewLocation()
    transition = True


def MoveBackward():
    DisableButtons()
    global currentscreen
    global anim
    global transition
    if currentscreen == "FOURWAY":
        anim = [PhotoImage(file='Sprites/dungeon/4way/009.png'),
                PhotoImage(file='Sprites/dungeon/4way/010.png'),
                PhotoImage(file='Sprites/dungeon/4way/011.png'),
                PhotoImage(file='Sprites/dungeon/4way/012.png')]
    elif currentscreen == "THREEWAYRIGHT":
        anim = [PhotoImage(file='Sprites/dungeon/3wayright/009.png'),
                PhotoImage(file='Sprites/dungeon/3wayright/010.png'),
                PhotoImage(file='Sprites/dungeon/3wayright/011.png'),
                PhotoImage(file='Sprites/dungeon/3wayright/012.png')]
    elif currentscreen == "THREEWAYLEFT":
        anim = [PhotoImage(file='Sprites/dungeon/3wayleft/009.png'),
                PhotoImage(file='Sprites/dungeon/3wayleft/010.png'),
                PhotoImage(file='Sprites/dungeon/3wayleft/011.png'),
                PhotoImage(file='Sprites/dungeon/3wayleft/012.png')]
    elif currentscreen == "THREEWAYFORK":
        anim = [PhotoImage(file='Sprites/dungeon/fork/005.png'),
                PhotoImage(file='Sprites/dungeon/fork/006.png'),
                PhotoImage(file='Sprites/dungeon/fork/007.png'),
                PhotoImage(file='Sprites/dungeon/fork/008.png')]
    elif currentscreen == "DEADEND":
        anim = [PhotoImage(file='Sprites/dungeon/fork/001.png'),
                PhotoImage(file='Sprites/dungeon/fork/002.png'),
                PhotoImage(file='Sprites/dungeon/fork/003.png'),
                PhotoImage(file='Sprites/dungeon/fork/004.png')]
    currentscreen = NewLocation()
    transition = True


attackIndex = 0  # increments to animate attack animation


def Attack():
    global attack
    global attackIndex
    global goblinLives
    global goblinPain
    global goblinDeath
    if attackIndex < 5:  # if animation isnt finished, disable button and increment frames
        btnAttack["state"] = "disabled"
        btnAttack.configure(background="gray")
        attack = True
        canvas.itemconfig(myarms, image=Frames4[attackIndex], anchor='center')
        attackIndex += 1
        if attackIndex == 4:
            if goblinOnScreen:
                goblinLives -= 1
                if goblinLives <= 0:  # if goblin ran out of lives, goblin dies.
                    goblinDeath = True
                    goblinLives = 5
                else:
                    goblinPain = True  # otherwise goblin is in pain
                    winsound.PlaySound("SFX/goblinpain.wav", 1)
            if hologramOnScreen:
                winsound.PlaySound("SFX/hit.wav", 1)
                randnum = random.randint(0, 4)
                if randnum == 0:
                    canvas.itemconfig(tiptext, text='Ted says: "Ouch." ')  # change tip
                elif randnum == 1:
                    canvas.itemconfig(tiptext, text='Ted says:\n"Watch where you swing\nthat thing!" ')  # change tip
                elif randnum == 2:
                    canvas.itemconfig(tiptext, text='Ted says: "You get an F." ')  # change tip
                else:
                    canvas.itemconfig(tiptext, text='Ted says:\n"Goodbye cruel world!" ')  # change tip
    else:
        canvas.itemconfig(myarms, image=arms, anchor='center')
        attackIndex = 0  # reset index
        btnAttack["state"] = "active"  # reactivate button
        btnAttack.configure(background="white")
        attack = False


def chooseButtons():  # decides what buttons to enable depending on the corridor configuration
    if currentscreen == "FOURWAY":
        btnForward["state"] = "active"
        btnBackward["state"] = "active"
        btnRight["state"] = "active"
        btnLeft["state"] = "active"
        btnForward.configure(background="white")
        btnBackward.configure(background="white")
        btnRight.configure(background="white")
        btnLeft.configure(background="white")
    elif currentscreen == "THREEWAYLEFT":
        btnForward["state"] = "active"
        btnBackward["state"] = "active"
        btnRight["state"] = "disabled"
        btnLeft["state"] = "active"
        btnForward.configure(background="white")
        btnBackward.configure(background="white")
        btnRight.configure(background="gray")
        btnLeft.configure(background="white")
    elif currentscreen == "THREEWAYRIGHT":
        btnForward["state"] = "active"
        btnBackward["state"] = "active"
        btnRight["state"] = "active"
        btnLeft["state"] = "disabled"
        btnForward.configure(background="white")
        btnBackward.configure(background="white")
        btnRight.configure(background="white")
        btnLeft.configure(background="gray")
    elif currentscreen == "THREEWAYFORK":
        btnForward["state"] = "disabled"
        btnBackward["state"] = "active"
        btnRight["state"] = "active"
        btnLeft["state"] = "active"
        btnForward.configure(background="gray")
        btnBackward.configure(background="white")
        btnRight.configure(background="white")
        btnLeft.configure(background="white")
    elif currentscreen == "DEADEND":
        btnForward["state"] = "disabled"
        btnBackward["state"] = "active"
        btnRight["state"] = "disabled"
        btnLeft["state"] = "disabled"
        btnForward.configure(background="gray")
        btnBackward.configure(background="white")
        btnRight.configure(background="gray")
        btnLeft.configure(background="gray")
    btnAttack["state"] = "active"
    btnAttack.configure(background="white")


buttonx = 90  # location of the button pad
buttony = 260
buttonbuffer = 50  # places buttons around center of pad
swordicon = PhotoImage(file='Sprites/swordicon.png')  # picture for sword button


def initButtons():  # creates game buttons
    global btnForward
    global btnRight
    global btnLeft
    global btnBackward
    global btnAttack
    global buttonx
    global buttony
    global buttonbuffer
    btnForward = Button(wn, text="⇧", width=3, height=1, command=MoveForward, anchor="center", font=("Fixedsys", 15))
    btnBackward = Button(wn, text="⇩", width=3, height=1, command=MoveBackward, anchor="center", font=("Fixedsys", 15))
    btnLeft = Button(wn, text="⇦", width=3, height=1, command=MoveLeft, anchor="center", font=("Fixedsys", 15))
    btnRight = Button(wn, text="⇨", width=3, height=1, command=MoveRight, anchor="center", font=("Fixedsys", 15))
    btnAttack = Button(wn, text="Attack", width=35, height=35, command=Attack, anchor="center", image=swordicon)
    btnForward.place(x=buttonx, y=buttony - buttonbuffer)
    btnBackward.place(x=buttonx, y=buttony + buttonbuffer)
    btnRight.place(x=buttonx + buttonbuffer, y=buttony)
    btnLeft.place(x=buttonx - buttonbuffer, y=buttony)
    btnAttack.place(x=buttonx, y=buttony - 3)
    btnForward["state"] = "disabled"
    btnBackward["state"] = "disabled"
    btnRight["state"] = "disabled"
    btnLeft["state"] = "disabled"
    chooseButtons()


def NewLocation():  # randomly chooses a corridor screen
    global pathIndex
    pathIndex = random.randint(0, 4)
    newpath = Corridor[pathIndex]
    return newpath


currentscreen = NewLocation()  # the corridor screen currently active
gameimg = Screens[Corridor.index(currentscreen)]  # image where corridor images are put
myarms = 0  # id for arms image to be set in StartGame()
myframe = 0  # ornate frame around game image
checkIndex = 0  # used to check if screen you're going to exists


def StartGame(event=None):
    global gameimg
    global menuloop
    global gameloop
    global scoretext
    global myarms
    global myframe
    global tiptext
    menuloop = False
    gameloop = True
    canvas.delete("menuitem")  # remove menu
    gameimg = canvas.create_image(420, 240, image=gameimg, anchor='center')  # initialize arms and game setting
    myarms = canvas.create_image(420, 240, image=arms, anchor='center')
    canvas.unbind("<Button-1>")  # removes click to start
    scoretext = canvas.create_text(80, 25, text="SCORE:0", fill="yellow", font=("Fixedsys", 15))
    canvas.create_image(25, 25, image=icon, anchor='center')
    myframe = canvas.create_image(420, 240, image=gameFrame, anchor='center')  # frame around game
    canvas.create_image(105, 120, image=textFrame, anchor='center')  # tip box
    canvas.create_image(108, 410, image=logo, anchor='center')  # logo
    tiptext = canvas.create_text(105, 120, text="Welcome to Pizza Roll\nQuest" + "! I'm your helpful tip\nbox. To move "
                                                                                 "around, click\nthe buttons below.")
    initButtons()


canvas.bind("<Button-1>", StartGame)  # allows click to start on menu

randomFeature = 0  # number to be randomized
pizzaroll = 0  # id for pizzaroll image to be set below
goblin = 0  # '' goblin ''
hologram = 0  # '' hologram Ted head ''

grabIndex = 0  # increments grab animation
grabRoll = False  # true if grabbing pizza rill
wonGame = False


def CollectRoll():  # grabs pizza roll, plays animation, and increments score.
    # Called over and over until animation is done
    global rollOnScreen
    global score
    global grabIndex
    global arms
    global grabRoll
    global fallbacktext
    global wonGame
    global collectButtonOnScreen
    btnCollect.destroy()
    collectButtonOnScreen = False
    if grabIndex < 5:
        grabRoll = True
        canvas.itemconfig(myarms, image=Frames3[grabIndex], anchor='center')
        grabIndex += 1
    else:
        canvas.itemconfig(myarms, image=arms, anchor='center')
        grabIndex = 0
        if rollOnScreen:
            score += 1
            canvas.itemconfig(scoretext, text="SCORE:" + str(score))
        rollOnScreen = False
        grabRoll = False
        winsound.PlaySound("SFX/collect.wav", 1)
        canvas.delete("pizzaroll")
    if score >= 3:  # supply hint that goblins can now spawn
        randnum = random.randint(0, 3)
        if randnum == 0:
            fallbacktext = "You smell strongly of pizza\nsauce and cheese..."
        elif randnum == 1:
            fallbacktext = "...Is someone following\nyou?"
        else:
            fallbacktext = "Careful! Those rolls might\nattract some unwanted\nattention"
    if score >= 10 and not wonGame:
        winsound.PlaySound("SFX/success.wav", 1)
        messagebox.askokcancel("CONGRATS!", "You have collected 10 pizza rolls!\nYou win!")
        wonGame = True


firstEncounter = True  # First time meeting a goblin needs this to prompt a message box
imageIndex = 0  # this is what updateFrame() uses to index looping animations


def placeFeature():  # This function places special stuff on screen like pizza rolls, goblins, and hologram Ted heads
    global randomFeature
    global rollOnScreen
    global goblinOnScreen
    global hologramOnScreen
    global pizzaroll
    global goblin
    global hologram
    global btnCollect
    global myarms
    global myframe
    global goblinAttack
    global goblinPain
    global goblinDeath
    global firstEncounter
    global imageIndex
    global collectButtonOnScreen
    if currentscreen == "DEADEND":  # items are randomly spawned, slightly higher chance on dead ends.
        randomFeature = random.randint(0, 2)
    else:
        randomFeature = random.randint(0, 6)
    if randomFeature == 0:  # spawn pizza roll
        imageIndex = 0  # reset animation index
        pizzaroll = canvas.create_image(420, 240, image=Frames1[0], anchor='center', tags="pizzaroll")
        rollOnScreen = True
        goblinOnScreen = False
        hologramOnScreen = False
        canvas.delete(myarms)
        canvas.delete(myframe)
        myarms = canvas.create_image(420, 240, image=arms, anchor='center')
        myframe = canvas.create_image(420, 240, image=gameFrame, anchor='center')
        btnCollect = tk.Button(wn, text="Collect", command=CollectRoll)
        btnCollect.place(x=buttonx + 5, y=125)
        collectButtonOnScreen = True
        print("created button")
        canvas.itemconfig(tiptext, text="You've found a scrumptious\n\npizza roll!")  # change tip
        print("spawned pizza roll")
    elif randomFeature == 1 and score >= 3:  # goblins are only spawned if player has 3+ pizza rolls
        imageIndex = 0  # reset animation index
        winsound.PlaySound("SFX/ominous.wav", 1)
        DisableButtons()
        btnAttack["state"] = "active"
        btnAttack.configure(background="white")
        goblinAttack = False
        goblinPain = False
        goblinDeath = False
        goblinOnScreen = True
        rollOnScreen = False
        hologramOnScreen = False
        goblin = canvas.create_image(420, 240, image=Frames6[0], anchor='center', tags="goblin")
        canvas.delete(myarms)
        canvas.delete(myframe)
        myarms = canvas.create_image(420, 240, image=arms, anchor='center')
        myframe = canvas.create_image(420, 240, image=gameFrame, anchor='center')
        canvas.itemconfig(tiptext, text="A nefarious goblin blocks\nthe path!")  # change tip
        print("spawned goblin")
        if firstEncounter:
            messagebox.askokcancel("LOOK OUT!", "You have run into a hungry goblin. "
                                                "He'll steal your pizza rolls if you don't act quick. "
                                                "Click the attack button to fight him off. Fair warning, "
                                                "if he manages to devour all of your pizza rolls, he'll eat you next!")
            firstEncounter = False
    elif random.randint(0, 20) == 15:  # rare 5% chance of getting a Ted head easter egg
        imageIndex = 0  # reset animation index
        rollOnScreen = False
        goblinOnScreen = False
        hologramOnScreen = True
        hologram = canvas.create_image(420, 240, image=Frames9[0], anchor='center', tags="goblin")
        canvas.delete(myarms)
        canvas.delete(myframe)
        myarms = canvas.create_image(420, 240, image=arms, anchor='center')
        myframe = canvas.create_image(420, 240, image=gameFrame, anchor='center')
        canvas.itemconfig(tiptext, text="Holy easter egg batman!\nIt's a hologram Ted head!")  # change tip
        print("spawned hologram")
        winsound.PlaySound("SFX/discovery.wav", 1)
    else:
        canvas.itemconfig(tiptext, text=fallbacktext)  # set to fallback text


btnRestart = Button
deathIndex = 0  # increments death animation
deathimg = 0
deathanim = False


def Restart():
    global gameimg
    global btnRestart
    global playerDead
    global currentscreen
    global deathIndex
    global score
    global deathimg
    global deathanim
    deathIndex = 0
    canvas.delete("all")  # clean slate
    btnRestart.destroy()
    canvas.create_image(320, 240, image=bgimg, anchor='center')  # add background again
    currentscreen = NewLocation()  # the corridor screen currently active
    gameimg = Screens[Corridor.index(currentscreen)]  # image where corridor images are put
    score = 0
    deathimg = 0
    deathanim = False
    StartGame()


def Death():
    global myframe
    global gameloop
    global deathIndex
    global deathimg
    global deathanim
    global playerDead
    global btnRestart
    gameloop = False
    playerDead = True
    if not deathanim:
        time.sleep(3)
        deathanim = True
        deathimg = canvas.create_image(420, 240, image=Frames10[deathIndex], anchor='center')
        canvas.delete(myframe)
        myframe = canvas.create_image(420, 240, image=gameFrame, anchor='center')
        winsound.PlaySound("SFX/death.wav", 1)
        winsound.PlaySound("SFX/death.wav", 1)
    if deathIndex < 11:
        canvas.itemconfig(deathimg, image=Frames10[deathIndex])
        deathIndex += 1
    if deathIndex == 11:
        canvas.itemconfig(deathimg, image=Frames10[deathIndex])
        wn.update()
        time.sleep(3)
        btnRestart = Button(wn, text="Play Again?", width=8, height=2, command=Restart, anchor="center")
        btnRestart.place(x=400, y=360)
        playerDead = False


goblindex = 0  # increments goblin animations
lostsomerolls = False


def goblinAction():  # controls goblin animations, actions
    global goblindex
    global goblin
    global goblinOnScreen
    global goblinAttack
    global goblinPain
    global goblinDeath
    global score
    global fallbacktext
    global lostsomerolls
    if goblinPain and goblindex <= 1:
        canvas.itemconfig(goblin, image=Frames7[goblindex])
        if goblindex == 1:
            goblindex = 0
            goblinPain = False
        else:
            goblindex += 1
    elif goblinDeath and goblindex <= 7:  # goblin has died!
        canvas.itemconfig(goblin, image=Frames8[goblindex])
        if goblindex == 0:
            winsound.PlaySound("SFX/goblindie.wav", 1)
        if goblindex == 7:
            if lostsomerolls:
                canvas.itemconfig(tiptext, text="You've slain the fowl\ncreature! But at the cost\nof some of "
                                                "your\npizza rolls :(")  # change tip
                lostsomerolls = False
            else:
                canvas.itemconfig(tiptext, text="You've slain the fowl\ncreature!")  # change tip
            goblindex = 0
            goblinOnScreen = False
            goblinDeath = False
            goblinAttack = False
            goblinPain = False
            chooseButtons()
        else:
            goblindex += 1
    elif goblinAttack and goblindex <= 3:
        canvas.itemconfig(goblin, image=Frames6[goblindex])
        if goblindex == 0:
            winsound.PlaySound("SFX/growl.wav", 1)
        if goblindex == 3:
            goblindex = 0
            goblinAttack = False
        else:
            if goblindex == 2:  # if goblin hits you, lose a pizza roll
                score -= 1
                lostsomerolls = True
                if score < 3:
                    fallbacktext = ""
                if score < 0:  # if you don't have any more pizza rolls to lose, you die.
                    print("You died")
                    goblinOnScreen = False
                    goblinDeath = False
                    goblinAttack = False
                    goblinPain = False
                    Death()
                else:
                    canvas.itemconfig(scoretext, text="SCORE: " + str(score))
            goblindex += 1


def animateTransition():  # animates corridor transitions
    global transition
    global transitionIndex
    global gameimg
    if len(anim) == 4:
        if transitionIndex < 4:
            canvas.itemconfig(gameimg, image=anim[transitionIndex], anchor='center')
            transitionIndex += 1
        else:
            canvas.itemconfig(gameimg, image=Screens[Corridor.index(currentscreen)], anchor='center')
            transitionIndex = 0
            transition = False
            chooseButtons()
            placeFeature()


def updateFrame(image, frames, increment, length):  # used to animate various looping animations
    global imageIndex
    if imageIndex == length - 1:
        imageIndex = 0
    elif increment:
        imageIndex += 1
    if imageIndex < length:
        canvas.itemconfig(image, image=frames[imageIndex])


def Close():  # closes off program loop when window is closed
    global loop
    global menuloop
    global gameloop
    loop = False
    menuloop = False
    gameloop = False


# https://stackoverflow.com/questions/111155/how-do-i-handle-the-window-close-event-in-tkinter

wn.protocol("WM_DELETE_WINDOW", Close)

animationSpeed = 100  # amount of time an animation will wait before it displays the next frame

while loop:  # main loop of the program
    if menuloop:
        wn.after(animationSpeed, updateFrame(image=myImage1, frames=Frames1, increment=True, length=7))
        wn.after(animationSpeed, updateFrame(image=myImage2, frames=Frames2, increment=False, length=7))
        if textToggle:
            canvas.delete("startText")  # flashing text after every 200 ms
        else:
            startText = canvas.create_text(320, 450, text="Click anywhere to start!",
                                           fill="yellow", font=("Fixedsys", 20), tags=("menuitem", "startText"))
        textToggle = not textToggle
    if gameloop:
        if transition:  # animate corridor transition animation
            wn.after(animationSpeed, animateTransition())
        if rollOnScreen:  # animate pizza roll
            wn.after(animationSpeed, updateFrame(image=pizzaroll, frames=Frames1, increment=True, length=7))
            if grabRoll:  # no need to use wn.after because it's already waited above
                CollectRoll()
            if attack:
                Attack()
        if goblinOnScreen:  # animate goblin
            if goblinAttack or goblinPain or goblinDeath:
                wn.after(animationSpeed, goblinAction())
            else:
                if imageIndex == 5 and random.randint(0, 2) == 1:
                    goblinAttack = True
                wn.after(animationSpeed, updateFrame(image=goblin, frames=Frames5, increment=True, length=6))
            if attack:
                Attack()
        if hologramOnScreen:  # animate hologram Ted Head
            wn.after(animationSpeed, updateFrame(image=hologram, frames=Frames9, increment=True, length=12))
            if attack:
                Attack()
        if not rollOnScreen and not goblinOnScreen and not hologramOnScreen:
            if grabRoll:  # now we need to call wn.after to get the right timing
                wn.after(animationSpeed, CollectRoll())
            if attack:
                wn.after(animationSpeed, Attack())
    if playerDead:
        wn.after(animationSpeed, Death())

    wn.update()  # refresh window
