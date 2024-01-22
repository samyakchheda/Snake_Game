from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.score=0
        self.color("white")
        self.penup()

        self.goto(0, 265)
        self.write(arg=f"Score = {self.score}",align="center", font=("Courier",15,"bold"))

    def increaseScore(self):
        self.score+=1
        self.clear()
        self.write(arg=f"Score = {self.score}", align="center", font=("Courier", 15, "bold"))

    def gameover(self):
        self.goto(0,0)
        self.color("yellow")
        self.write(arg=f"GAME OVER", align="center", font=("Courier", 25, "bold"))

