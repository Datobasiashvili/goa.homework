# 8) გაიმეორეთ გავლილი მასალა

from turtle import *


bgcolor("cyan") 

#drawing grass

speed(15)
width(7)
begin_fill()
color("Dark green")
forward(400)
left(180)
forward(800)  #width of grass, top left corner (-400, 0)
left(90)
forward(400)
left(90)
forward(800)
left(90)
forward(400)
end_fill()

#drawing a house
penup()
goto(-100, 0)   #bottom left corner of a house
pendown()
begin_fill()
color("tomato2")
forward(180)   #height of a house
right(90)
forward(250)   #width of a house
right(90)
forward(180)
end_fill()

#drawing a door
penup()
goto(0, 0)   #bottom left corner of a door
pendown()
begin_fill()
color("OrangeRed4")
left(180)
forward(80)  #height of a door
right(90)
forward(55)   #width of a door
right(90)
forward(80)
end_fill()

#drawing a door knob
width(1)
penup()
goto(40, 45)
pendown()
begin_fill()
color("black")
circle(3)
end_fill()

#drawing a roof
width(7)
penup()
goto(-100, 180)
pendown()
begin_fill()
color("blue4")
left(180)
right(60)
forward(145)
right(60)
forward(145)
end_fill()

#drawing first window
penup()
width(2)
goto(-70, 80)   #bottom left corner of a window
pendown()
begin_fill()
color("DarkGray")
left(120)
forward(70)    #height of a window
right(90)
forward(40)      #width of a window
right(90)
forward(65)
right(90)
forward(40)
end_fill()

width(4)
begin_fill()
color("black")
penup()
goto(-70, 115)
pendown()
right(180)
forward(40)

penup()
goto(-50, 150)
pendown()
right(90)
forward(69)

#drawing a second window
width(2)
penup()
goto(85, 80)
pendown()
left(180)
begin_fill()
color("DarkGray")
forward(70)   #height of a window
right(90)
forward(40)   #width of a window
right(90)
forward(70)
right(90)
forward(40)
end_fill()

width(4)
penup()
goto(85, 115)
pendown()
begin_fill()
color("black")
right(180)
forward(40)
end_fill()

penup()
goto(105, 150)
pendown()
begin_fill()
color("black")
right(90)
forward(70)

#little details
width(7)
penup()
goto(-400, 0)
pendown()
begin_fill()
color("Dark green")
left(90)
forward(800)

penup()
goto(-70, 80)
pendown()
begin_fill()
color("tomato2")
forward(41)
end_fill()

penup()
goto(-100, 180)
pendown()
begin_fill()
color("blue4")
forward(250)
end_fill()

#drawing sun
penup()
goto(-250, 200 )
pendown()
begin_fill()
color("Gold")
circle(30)
end_fill()

exitonclick()