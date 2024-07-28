from turtle import *

# we want to paint a house

#step 1: draw a square
begin_fill()
speed(10)
width(7)
color("purple")

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

#step 2: draw a door

begin_fill()
forward(70)
color("yellow")
left(90)
forward(120)      
right(90)
forward(60)
right(90)
forward(120)
end_fill()

# end drawing door

#step 3: draw a roof

penup()
goto(200, 200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()
# end of drawing roof

# step 4: draw windows

#drawing first window
left(30)
left(90)
penup()
goto(20, 140)
pendown()
color("cyan")

begin_fill()
forward(30)
left(90)
forward(30)
left(90)
forward(30)
left(90)
forward(30)
left(90)
end_fill()
#end of drawing first window

#drawing second window
penup()
goto(150, 140)
pendown()
begin_fill()
forward(30)
left(90)
forward(30)
left(90)
forward(30)
left(90)
forward(30)
left(90)
end_fill()
#end of drawing second window

#end of drawing windows


#little details
penup()
goto(0, 0)
pendown()
color("purple")
forward(200)

#drawing a door knob
penup()
goto(120, 63)
pendown()
color("brown")
forward(2)
penup()

#end of drawing a house

exitonclick()