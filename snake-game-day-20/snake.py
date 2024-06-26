from turtle import Turtle


STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
class  Snake:
    def __init__(self):

        self.turtles = []
        self.create_snake()


    def create_snake(self):
        for positions in STARTING_POSITIONS:
           self.add_segment(positions)

    def move_snake(self):

        for turtle_index in range(len(self.turtles) - 1, 0, -1):
            new_x = self.turtles[turtle_index - 1].xcor()
            new_y = self.turtles[turtle_index - 1].ycor()
            self.turtles[turtle_index].goto(new_x, new_y)
        self.turtles[0].forward(20)
    def up(self):
        if self.turtles[0].heading() != DOWN:
            self.turtles[0].setheading(90)

    def down(self):
        if self.turtles[0].heading() != UP:
            self.turtles[0].setheading(270)

    def right(self):
        if self.turtles[0].heading() != LEFT:
            self.turtles[0].setheading(360)

    def left(self):
        if self.turtles[0].heading() != RIGHT:
            self.turtles[0].setheading(180)

    def add_segment(self,positions):
        tim = Turtle()
        tim.penup()
        tim.color("white")
        tim.shape("square")
        tim.goto(positions)
        self.turtles.append(tim)



    def increase_size(self):
        self.add_segment(self.turtles[-1].position())