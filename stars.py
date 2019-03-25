from turtle import *
# turtle methods https://docs.python.org/3/library/turtle.html

color('red', 'brown')
shape("turtle")

# a function to do the annoying penup/pendown etc
# to move somewhere without drawing a line
def moveto(xpos, ypos):
  penup()
  setpos(xpos,ypos)
  pendown()

# a function for drawing stars, if you want to use it
def stars(points=5,turn=144,size=100):
  for x in range(points):
    forward(size)
    left(turn)

moveto(100,100)

begin_fill()

for x in range(5):
    forward(100)
    left(144)

end_fill()

moveto(-200,-200)

begin_fill()

for x in range(10):
    forward(200)
    left(108)

penup()

end_fill()
done()
