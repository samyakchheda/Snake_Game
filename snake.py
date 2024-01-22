from turtle import Turtle,Screen
from food import Food
from scoreboard import Scoreboard


class Snake:
    def __init__(self):
        self.tim=Turtle()
        self.tim.hideturtle()
        self.screen=Screen()
        self.food=Food()
        self.scoreboard=Scoreboard()
        self.create_snake()


    def create_snake(self):

        self.segments = []
        for i in range(3):
            self.addSegment()

    def addSegment(self):
        tim = Turtle(shape="square")
        tim.hideturtle()
        tim.color("white")
        tim.speed("fastest")
        tim.penup()
        self.segments.append(tim)

    def extendSegment(self):
        self.addSegment()


    def move(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            self.segments[seg].showturtle()
            newx = self.segments[seg - 1].xcor()
            newy = self.segments[seg - 1].ycor()
            self.segments[seg].goto(newx, newy)


        self.segments[0].forward(20)

    def Up(self):
        if self.segments[0].heading()!=270:
            self.segments[0].setheading(90)
    def Down(self):
        if self.segments[0].heading() != 90:
            self.segments[0].setheading(270)
    def Left(self):
        if self.segments[0].heading() != 0:
            self.segments[0].setheading(180)
    def Right(self):
        if self.segments[0].heading() != 180:
            self.segments[0].setheading(0)

    def foodCollision(self):
        if self.segments[0].distance(self.food)<18:
            self.food.refresh()
            self.scoreboard.increaseScore()
            self.extendSegment()

    def wallCollision(self):
        if self.segments[0].xcor()>325 or self.segments[0].xcor()<-325 or self.segments[0].ycor()>260 or self.segments[0].ycor()<-265:
            self.scoreboard.gameover()
            return True
        else:
            return False

    def tailCollision(self):
        self.scoreboard.gameover()

