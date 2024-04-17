import turtle
import random


class Ball(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.speed(0.1)
        self.moving_speed = 25
        self.visible = False
        self.color('#ff6666')
        self.bound_top = turtle.window_height() // 2
        self.bound_right = turtle.window_width() // 2
        self.bound_bottom = self.bound_top * (-1)
        self.bound_left = self.bound_right * (-1)
        self.obstacle = None
        # self.random = random.randint(1, 90)
        # self.direction = random.choice([1, -1])
        self.setheading(240)

    def move_ball(self):
        self.forward(self.moving_speed)

    def bounce(self, bouncing_effect=0):
        bouncing_effect = bouncing_effect
        if self.obstacle == "left":
            self.setx(self.xcor() + 10)
            self.setheading((180 - self.heading()) % 360)
        if self.obstacle == "right":
            self.setx(self.xcor() - 10)
            self.setheading((180 - self.heading()) % 360)
        if self.obstacle == "top":
            self.sety(self.ycor() - 10)
            self.setheading((180 - self.heading() + 180) % 360)
        if self.obstacle == "bottom":
            # if bounced on bat, effect is given based on the speed of the bat. Angle is adjusted if too flat
            self.sety(self.ycor() + 10)
            self.setheading((180 - self.heading() + 180 + bouncing_effect) % 360)
            if -25 < self.heading() < 30:
                self.setheading(30)
            if 150 < self.heading() < 205:
                self.setheading(150)

    def reset_position(self):
        self.setpos(0, 0)
        new_heading = random.choice(range(200, 340, 5))
        self.setheading(new_heading)
