import turtle


class Brick(turtle.Turtle):
    def __init__(self, hardness=1):
        super().__init__()
        self.penup()
        self.speed(0)
        self.hardness = hardness
        self.shape('square')
        self.setheading(90)
        self.shapesize(4, 2, 0)
        self.set_color()

    def set_color(self):
        if self.hardness == 1:
            self.color('blue')
        elif self.hardness == 2:
            self.color('green')
        elif self.hardness == 3:
            self.color('red')

    def reduce_hardness(self):
        self.hardness -= 1
        if self.hardness == 0:
            self.hideturtle()
            turtle.turtles().remove(self)
        else:
            self.set_color()

