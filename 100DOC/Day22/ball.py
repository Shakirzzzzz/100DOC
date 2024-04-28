from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.goto(0,0)
        self.color("white")
        self.shape("circle")
        self.penup()

        self.x = 10
        self.y = 10

    def move_ball(self):

        new_x = self.xcor() + self.x
        new_y = self.ycor() + self.y
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y *= -1
    def bounce_x(self):
        self.x *= -1




