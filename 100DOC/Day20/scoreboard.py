from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        with open("data.txt") as file:
            score =  int(file.read())
        self.score = 0
        self.color('white')
        self.high_score = score
        self.hideturtle()
        self.penup()
        self.goto(0, 259)
        self.write(f'Score = {self.score}', align= 'center', font= ('Arial', 24, 'normal'))
    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
    def update_scoreboard(self):
        self.clear()
        self.write(f'Score = {self.score}, high score = {self.high_score}', align='center', font=('Arial', 24, 'normal'))


    def refresh(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as file:
                file.write(str(self.high_score))


        self.score = 0
        self.update_scoreboard()


























