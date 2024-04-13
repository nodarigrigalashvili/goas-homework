from turtle import *


#we want to paint a house

#step 1:  draw a square
shape("turtle")
#speed(30)
width(7)
color("blue")
begin_fill()
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
end_fill()
#end of square

#drawing a door
forward(70)
color("brown")
begin_fill()
left(90)

forward(80)
right(90)

forward(35)
right(90)

forward(80)
end_fill()

penup()
goto(200, 200)
pendown()

color("gray")
begin_fill()
right(150)

forward(200)
left(120)

forward(200)
end_fill()

penup()
goto(130, 30)
pendown()

color("brown")
left(120)

forward(25)
left(90)

forward(75)
left(90)

forward(25)
left(90)

forward(75)
left(90)

forward(50)
left(90)

forward(75)
left(90)

forward(25)
left(90)

forward(37)
left(90)

forward(25)
right(180)

forward(50)

penup()
goto(310, 0)
pendown()

color("green")
forward(650)






exitonclick()