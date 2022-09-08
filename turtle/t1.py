import turtle

def square(t,x,y,w,color,sidelen):
  """
  Parameters:
  t- a turtle
  x,y- location
  w- width of side
  color- color of drawing
  sidelen- length of each side
  Returns:
  nothing
  """
   # set the location, color, width of square
  t.penup()
  t.goto(x,y)
  t.width(w)
  t.color(color)
  t.pendown()
    # draw a square
  for i in range(4):
      t.forward(sidelen)
      t.right(90)

def triangle(t, x, y, w, color, sidelen):
   # set the location, color, width of triangle
  t.penup()
  t.goto(x,y)
  t.width(w)
  t.color(color)
  t.pendown()
   #draw a triangle
  for i in range(3):
    t.forward(sidelen)
    t.right(120)

def ngon(t, numsides, x, y, w, color, sidelen):
   # set the location, color, width of ngon
  t.penup()
  t.goto(x,y)
  t.width(w)
  t.color(color)
  t.pendown()
   #draw an ngon
  for i in range(numsides):
    t.forward(sidelen)
    t.right(45)
wn = turtle.Screen()

crush = turtle.Turtle()

square(crush,0,0,1,"green",50)

squirt = turtle.Turtle()
square(squirt,100,100,5,"red",80)
square(crush,-50,30,3,"yellow",100)
triangle(crush, 105, 105, 4, "green", 40)
ngon(squirt, 8, 130, 145,3, "yellow", 70)
wn.exitonclick()
wn.mainloop()