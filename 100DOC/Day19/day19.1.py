import turtle
import random


screen = turtle.Screen()


screen.setup(width = 500, height = 400)
user_bet = screen.textinput(title= "Make your bet ", prompt="Which turtle will win the race. Enter a color: ")
colors = ["red", "purple", "green", "orange", "pink", "black"]
all_turtles = []
for i in range(0, 6):

    turt = turtle.Turtle("turtle")
    turt.penup()
    turt.color(colors[i])
    all_turtles.append(turt)
    turt.goto(x=-230, y=-100 + 40*i)




if user_bet:
    is_race_on = True

while is_race_on:


    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"you have won. The winning color is: {winning_color}")
            else:
                print(f"you have lost . The winning color is: {winning_color}")
        random_distance = random.randint(0,10)
        turtle.forward(random_distance)





screen.exitonclick()