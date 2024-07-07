#6) უნდა დახაზოთ სასახლე turtle ის გამოყენებით და თქვენი გემოვნებით გააფორმოთ
from turtle import *

#drawing first tower
shape('circle')
speed(30)
width(7)
begin_fill()
color("Peru")
forward(400)
left(90)
forward(200) #first tower height
left(90)
forward(100) #first tower width
left(90)
forward(200)
end_fill()


#drawing second tower
penup()
goto(0, 0)
pendown()
begin_fill()
color("Peru")
right(180)
forward(200) #second tower height
right(90)
forward(100) #second tower width
right(90)
forward(200)
end_fill()

#drawing the center tower
penup()
goto(100, 100)
pendown()
begin_fill()
color("Peru")
left(90)
forward(200)
right(90)
forward(100)
right(90)
forward(200)
right(90)
forward(100)
end_fill()

#drawing a roof for the first tower
penup()
goto(300, 200)
pendown()
begin_fill()
color("firebrick")
right(30)
forward(100)
right(120)
forward(100)
end_fill()

#drawing a roof for the second tower
penup()
goto(0, 200)
pendown()
begin_fill()
color("firebrick")
left(120)
forward(100)
right(120)
forward(100)
end_fill()

begin_fill()
color("peru")
right(120)
forward(100)
end_fill()
penup()
goto(300,200)
pendown()
right(180)
forward(100)

#drawing a roof for the center tower
penup()
goto(100, 100)
pendown()
begin_fill()
color("firebrick")
left(30)
forward(115)
right(60)
forward(115)
end_fill()

begin_fill()
color("Peru")
right(150)
forward(200)

#drawing first window
penup()
goto(30, 70)
pendown()
begin_fill()
color("cyan")
right(90)
forward(80) #height of a window
right(90)
forward(40) #width of a window
right(90) 
forward(80)
right(90)
forward(40)
right(180)
end_fill()

#drawing second window
penup()
goto(330, 70)
pendown()
begin_fill()
color("cyan")
left(90)
forward(80) #height of a window
right(90)
forward(40) #width of a window
right(90)
forward(80)
right(90)
forward(40)
end_fill()

#drawing a door
penup()
goto(150, 0)
pendown()
begin_fill()
color("red4")
right(90)
forward(70) #height of a door
right(90)
forward(100) #width of a door
right(90)
forward(70)
right(90)
forward(100)
end_fill()

#drawing a door knob
penup()
goto(230, 35)
pendown()
begin_fill()
color("Black")
forward(1)
penup()
end_fill()

exitonclick()

