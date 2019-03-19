# import libraries
from Tkinter import * 

# create the top level Tk object
window=Tk()
window.title("a window")

# create the canvas
canvas = Canvas(window, height=600, width=600)

# draw stuff on the canvas
# first the pizza base
canvas.create_oval(200,200,300,300,fill="brown")

# draw some more stuff
# this might be the tomato sauce toppings
# now add your cheese and anything else, before we get to the pepperoni

# pack the canvas and run the Tk mainloop
canvas.pack()
window.mainloop()
