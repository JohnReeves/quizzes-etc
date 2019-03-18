from Tkinter import *

c_height, c_width, c_colour=400, 600, "black"
p1_x, p1_y, line_length, line_width, line_colour = c_height/2, c_width/2, 5, 5,"purple"

def p1_move_N(event):
    global p1_y
    canvas.create_line (p1_x, p1_y, p1_x, p1_y-line_length, width=line_width, fill=line_colour)
    p1_y = p1_y - line_length

def p1_move_S(event):
    global p1_y
    canvas.create_line (p1_x, p1_y, p1_x, p1_y+line_length, width=line_width, fill=line_colour)
    p1_y = p1_y + line_length

def p1_move_E(event):
    global p1_x
    canvas.create_line (p1_x, p1_y, p1_x+line_length, p1_y, width=line_width, fill=line_colour)
    p1_x = p1_x + line_length

def p1_move_W(event):
    global p1_x
    canvas.create_line (p1_x, p1_y, p1_x-line_length, p1_y, width=line_width, fill=line_colour)
    p1_x = p1_x - line_length


def p1_move_NE(event):
    global p1_y, p1_x
    canvas.create_line (p1_x, p1_y, (p1_x + line_length), (p1_y-line_length), width=line_width, fill=line_colour)
    p1_y, p1_x = (p1_y - line_length), (p1_x + line_length)

def p1_move_SE(event):
    global p1_y, p1_x
    canvas.create_line (p1_x, p1_y, (p1_x+line_length), (p1_y+line_length), width=line_width, fill=line_colour)
    p1_y, p1_x = (p1_y + line_length), (p1_x + line_length)

def p1_move_NW(event):
    global p1_x, p1_y
    canvas.create_line (p1_x, p1_y, (p1_x-line_length), (p1_y-line_length), width=line_width, fill=line_colour)
    p1_y, p1_x = (p1_y -line_length), (p1_x - line_length)

def p1_move_SW(event):
    global p1_x,p1_y
    canvas.create_line (p1_x, p1_y, (p1_x-line_length), (p1_y+line_length), width=line_width, fill=line_colour)
    p1_y, p1_x = (p1_y + line_length), (p1_x - line_length)

def erase_all (event):
    canvas.delete(ALL)


root=Tk()
root.title("Etch-A-Sketch")

canvas=Canvas(width=c_width,height=c_height,bg=c_colour)
#canvas.create_line(p1_x,p1_y,(p1_x-line_length),(p1_y-line_width),fill=line_colour)
canvas.pack()

root.bind ("w", p1_move_N)
root.bind ("s", p1_move_S)
root.bind ("d", p1_move_E)
root.bind ("a", p1_move_W)

root.bind ("q", p1_move_NE)
root.bind ("e", p1_move_NW)
root.bind ("z", p1_move_SW)
root.bind ("x", p1_move_SE)

root.bind ("p", erase_all)

root.mainloop()
