import turtle
from PIL import Image
import random
from bat import Bat
from ball import Ball
from brick import Brick

bg = Image.open('watercolour_night_sky_background_2607.gif')
bg.thumbnail((1080, 800))
bg.save('resized_bg.gif')

screen = turtle.Screen()
screen.setup(bg.width, bg.height, startx=None, starty=0)
screen.bgpic('resized_bg.gif')

bat = Bat()
ball = Ball()
brick_num = 0
lives = 5

brick_offset = screen.window_width() // 2 - 25

for x in range(5):
    brick = Brick(3)
    brick_num += 3
    brick.sety(270)
    brick.setx(screen.window_width() // 5 * x - brick_offset + screen.window_width() // 20)

for x in range(8):
    brick = Brick(2)
    brick_num += 2
    brick.sety(229)
    brick.setx(screen.window_width() // 8 * x - brick_offset + screen.window_width() // 24)

for x in range(10):
    brick = Brick(1)
    brick_num += 1
    brick.sety(188)
    brick.setx(screen.window_width() // 10 * x - brick_offset + screen.window_width() // 40)



old_bat_x = None


def start_game():
    mouse_x = screen.getcanvas().winfo_pointerx() - screen.window_width() // 2 - 250
    global old_bat_x
    old_bat_x = bat.xcor()
    bat.move_bat(mouse_x)
    if ball.move_ball():
        print('ball lost')
    if collision():
        ball.sety(ball.ycor() + ball.moving_speed)
        ball.bounce()
    if brick_num > 0 and lives > 0:
        screen.ontimer(start_game, 10)
    else:
        end_game()


def end_game():
    if lives > 0:
        bat.goto(0, 0)
        bat.write("You won", align="center", font=('Consolas', 50, 'normal'))
    else:
        ball.goto(0, 0)
        ball.write("Game Over", align="center", font=('Consolas', 50, 'normal'))
    ball.hideturtle()
    bat.hideturtle()


def bouncing_effect():
    x_diff = bat.xcor() - old_bat_x
    if x_diff < -25:
        return 25
    elif -25 <= x_diff <= 25:
        return x_diff * (-1)
    elif 25 < x_diff:
        return -25


def collision():
    # collision with bat
    if bat.xcor() - 40 < ball.xcor() < bat.xcor() + 40 and bat.ycor() < ball.ycor() < bat.ycor() + 40:
        ball.obstacle = "bottom"
        ball.bounce(bouncing_effect())

    # collision with walls
    if ball.xcor() < ball.bound_left + 10:
        ball.obstacle = "left"
        ball.bounce()
    elif ball.xcor() > ball.bound_right - 10:
        ball.obstacle = "right"
        ball.bounce()
    if ball.ycor() > ball.bound_top - 10:
        ball.obstacle = "top"
        ball.bounce()
    elif ball.ycor() < ball.bound_bottom + 10:
        ball.obstacle = "bottom"
        ball.bounce()
        ball.reset_position()
        global lives
        lives -= 1
        print(lives)

    # collision with bricks
    for brick in screen.turtles():
        if isinstance(brick, Brick):
            global brick_num
            if brick.xcor() + 45 < ball.xcor() < brick.xcor() + 70 and brick.ycor() - 15 < ball.ycor() < brick.ycor() + 15:
                print('brick left collision')
                ball.obstacle = "left"
                ball.bounce()
                brick.reduce_hardness()
                brick_num -= 1
                print(brick_num)
                break
            elif brick.xcor() - 70 < ball.xcor() < brick.xcor() - 45 and brick.ycor() - 15 < ball.ycor() < brick.ycor() + 15:
                print('birick right collision')
                ball.obstacle = "right"
                ball.bounce()
                brick.reduce_hardness()
                brick_num -= 1
                print(brick_num)
                break
            elif brick.xcor() - 50 < ball.xcor() < brick.xcor() + 50 and brick.ycor() - 40 < ball.ycor() < brick.ycor() - 15:
                print('brick top collision')
                ball.obstacle = "top"
                ball.bounce()
                brick.reduce_hardness()
                brick_num -= 1
                print(brick_num)
                break
            elif brick.xcor() - 50 < ball.xcor() < brick.xcor() + 50 and brick.ycor() + 15 < ball.ycor() < brick.ycor() + 40:
                print('brick bottom collision')
                ball.obstacle = "bottom"
                ball.bounce()
                brick.reduce_hardness()
                brick_num -= 1
                print(brick_num)
                break


start_game()
screen.mainloop()
