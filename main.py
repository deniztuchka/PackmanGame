import turtle
import random
import time

win = turtle.Screen()
win.bgcolor("black")
win.title("Pac-Man Game with Score and Timer")
win.setup(width=600, height=600)
win.tracer(0)

pacman = turtle.Turtle()
pacman.shape("circle")
pacman.color("yellow")
pacman.penup()
pacman.speed(0)

score = 0
score_display = turtle.Turtle()
score_display.speed(0)
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(-290, 260)
score_display.write(f"Score: {score}", align="left", font=("Arial", 16, "normal"))

start_time = time.time()
timer_display = turtle.Turtle()
timer_display.speed(0)
timer_display.color("white")
timer_display.penup()
timer_display.hideturtle()
timer_display.goto(200, 260)
timer_display.write("Time: 0s", align="left", font=("Arial", 16, "normal"))

walls = [
    (-250, 250), (-230, 250), (-210, 250), (-190, 250), (-170, 250), (-150, 250),
]

wall_turtles = []
for wall in walls:
    wall_turtle = turtle.Turtle()
    wall_turtle.shape("square")
    wall_turtle.color("blue")
    wall_turtle.penup()
    wall_turtle.goto(wall)
    wall_turtles.append(wall_turtle)

dots = []
for i in range(20):
    dot = turtle.Turtle()
    dot.shape("circle")
    dot.color("white")
    dot.penup()
    dot.goto(random.randint(-290, 290), random.randint(-290, 290))
    dots.append(dot)

pacman_direction = 'stop'
pacman_speed = 20

def go_up():
    global pacman_direction
    pacman_direction = 'up'

def go_down():
    global pacman_direction
    pacman_direction = 'down'

def go_left():
    global pacman_direction
    pacman_direction = 'left'

def go_right():
    global pacman_direction
    pacman_direction = 'right'

win.listen()
win.onkey(go_up, "w")
win.onkey(go_down, "s")
win.onkey(go_left, "a")
win.onkey(go_right, "d")

def move_pacman():
    if pacman_direction == 'up':
        pacman.sety(pacman.ycor() + pacman_speed)
    if pacman_direction == 'down':
        pacman.sety(pacman.ycor() - pacman_speed)
    if pacman_direction == 'left':
        pacman.setx(pacman.xcor() - pacman_speed)
    if pacman_direction == 'right':
        pacman.setx(pacman.xcor() + pacman_speed)

    if pacman.xcor() > 290 or pacman.xcor() < -290:
        pacman.goto(0, 0)
    if pacman.ycor() > 290 or pacman.ycor() < -290:
        pacman.goto(0, 0)

def check_collision():
    global score
    for dot in dots:
        if pacman.distance(dot) < 20:
            dot.goto(1000, 1000)
            dots.remove(dot)
            score += 1
            score_display.clear()
            score_display.write(f"Score: {score}", align="left", font=("Arial", 16, "normal"))

def update_timer():
    elapsed_time = int(time.time() - start_time)
    timer_display.clear()
    timer_display.write(f"Time: {elapsed_time}s", align="left", font=("Arial", 16, "normal"))

while True:
    win.update()
    move_pacman()
    check_collision()
    update_timer()
    time.sleep(0.1)

win.mainloop()
