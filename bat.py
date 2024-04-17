import turtle


class Bat(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.left(90)
        self.shapesize(4, 1, 1)
        self.penup()
        self.speed(0.1)
        self.visible = False
        self.color('#e6faff')
        self.y = - (turtle.window_height() // 2 - 30)
        self.bound_right = turtle.window_width() // 2
        self.bound_left = self.bound_right * (-1)
        self.setpos(0, self.y)

    def move_bat(self, x):
        if self.bound_left + 30 < x < self.bound_right - 50:
            self.setx(x)
        # if self.xcor() < self.bound_left + 50:
        #     self.setx(self.bound_left + 50)
        # if self.xcor() > self.bound_right - 50:
        #     self.setx(self.bound_right - 50)
