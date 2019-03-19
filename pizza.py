# import libraries
from Tkinter import * 

# create the top level Tk object
window=Tk()
window.title("a window")

# create the canvas
canvas = Canvas(window, height=600, width=600)

# draw stuff on the canvas
# first the pizza base
canvas.create_oval(50,50,450,450,fill="brown")
# then the tomato topping
canvas.create_oval(65,65,435,435,fill="red")


# draw some more stuff
# this might be the tomato sauce toppings
# now add your cheese and anything else, before we get to the pepperoni

# pack the canvas and run the Tk mainloop
canvas.pack()
window.mainloop()
