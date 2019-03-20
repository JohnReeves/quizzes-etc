# import libraries
from tkinter import * 
# the usual minimal tkinter graphics app
# practice the 5 essentials & key bindings
# the program is flawed and needs kids to fix it

import random

# invariants
c_height,c_width=350,350
ballx, bally=0, 0
balldx, balldy=5, 5
rndx=random.randint(0,5)
rndy=random.randint(0,5)
baty=0

def move_Up(event):
    # remember why we need 'global'
    global baty
    baty-=10
    if baty>0:
       canvas.move(bat,0,-10)

def move_Down(event):
    global baty
    baty+=10
    if bat<c_height-100:
       canvas.move(bat,0,10)

def move_oval():
    # 'global' needed to stop python making a new thing
    # with the same name as the things outside
    # other languages work other way.
    # try removing these lines to see what happens.
    global ballx,bally
    global balldx,balldy

    if ballx<10:
        balldx=(balldx+rndx)
    
    if ballx>c_width:
        balldx=-(balldx+rndx)

    if bally<10:
        balldy=(balldy+rndy)
     
    if bally>c_height:
        balldy=-(balldy+rndy)

    ballx+=balldx
    bally+=balldy
    canvas.move(ball,balldx,balldy)
    canvas.after(100, move_oval)

# create the top level Tk object
window=Tk()
window.title("a pong")

# create the canvas
canvas = Canvas(window, height=600, width=600)

# draw stuff on the canvas
#rect=canvas.create_rectangle(100,100,150,200,fill="brown")
bat=canvas.create_rectangle(50,0,50,100)
ball=canvas.create_oval(200,200,300,300,fill="brown")


move_oval()

window.bind("<Up>", move_Up)
window.bind("<Down>", move_Down)


# pack the canvas and run the Tk mainloop
canvas.pack()
window.mainloop()

