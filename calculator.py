"""

calculator

digits 0-9
ops add, subtract, multiply and divide
brackets and clear

use of eval to calculate expression

extend using
factorial, triangles, combinatorials
physical constants
roman, binary notation

"""

from Tkinter import * # include tkinter into namespace
from decimal import * # beware of naming convention

# special functions
def triangle(n):
    if n==0 or n==1:
        return 1
    else:
        return n+triangle(n-1)

def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)

def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

# key press / button function
#
def click(key):

    # constants display
    if key == constants_list[0]:
        display.insert(END, "3.141592654")
    elif key == constants_list[1]:
        display.insert(END, "300000000")
    elif key == constants_list[2]:
        display.insert(END, "330")
    elif key == constants_list[3]:
        display.insert(END, "149597887")

    # call the special functions
    elif key == specials_list[0]:
        n=int(display.get())
        display.delete(0,END)
        display.insert(END, str(triangle(n)))
    elif key == specials_list[1]:
        n=int(display.get())
        display.delete(0,END)
        display.insert(END, str(factorial(n)))
    elif key == specials_list[2]:
        n=int(display.get())
        display.delete(0,END)
        display.insert(END, str(fibonacci(n)))

    # numbers and operators make an expression
    # '=' calls eval to evaluate it
    elif key == "=":
        result=str(eval(display.get()))
        display.insert(END, "=" + result)
    elif key == "C":
        display.delete(0, END)
    else:
        display.insert(END, key)

# create the app layout
# main window with 3 Frames:
#     Frame 1 (N full width): top row for displaying results
#     Frame 2 (W half width): numeric keypad
#     Frame 3 (E half width): operator keypad
# extension
#     Frame 4 (W half width): constants area
#     Frame 5 (E half Width): special functions
#
# main window
window = Tk() # instantiate a tk window object
window.title("myCalculator")

# create top row frame
top_row=Frame(window)
top_row.grid(row=0, column=0, columnspan=2, sticky=N)

# create num_pad frame
num_pad=Frame(window)
num_pad.grid(row=1, column=0, sticky=W)

# create operator frame
operator = Frame(window)
operator.grid(row=1, column=1, sticky=E)

# create num_pad frame
constants=Frame(window)
constants.grid(row=2, column=0, sticky=W)

# create operator frame
specials = Frame(window)
specials.grid(row=2, column=1, sticky=E)



# make the window look like a calculator
# entry widget for display
display = Entry(top_row, width=45, bg="light pink")
display.grid()

# keypad and operator buttons
num_pad_list=[
    '1','2','3',
    '4','5','6',
    '7','8','9',
    '0','.','='
    ]

operator_list=[
    '*','/',
    '+','-',
    '(',')',
    'C'
    ]

constants_list=[
    'pi',
    'speed of light',
    'speed of sound',
    'av dist to the sun'
    ]

specials_list=[
    'triangle',
    'factorial',
    'fibonacci',
    '-> roman numerals'
    ]

# num_pad creation loop
r,c = 0, 0 # row, column number works in the Frame

for btn_text in num_pad_list:
    def cmd(x=btn_text):
        click(x)
    Button(num_pad, text=btn_text,width=5, command=cmd).grid(row=r,column=c)
    c+=1
    if c>2:
        c=0
        r+=1

# operator creation loop
r,c = 0, 0 # row, column number works in the Frame

for btn_text in operator_list:
    def cmd(x=btn_text):
        click(x)
    Button(operator, text=btn_text,width=5, command=cmd).grid(row=r,column=c)
    c+=1
    if c>1:
        c=0
        r+=1

# constants creation loop
r,c = 0, 0 # row, column number works in the Frame

for btn_text in constants_list:
    def cmd(x=btn_text):
        click(x)
    Button(constants, text=btn_text,width=22, command=cmd).grid(row=r,column=c)
    r+=1

# specials creation loop
r,c = 0, 0 # row, column number works in the Frame

for btn_text in specials_list:
    def cmd(x=btn_text):
        click(x)
    Button(specials, text=btn_text,width=13, command=cmd).grid(row=r,column=c)
    r+=1

# run mainloop
window.mainloop()
