import random
import turtle


screen=turtle.Screen()
game_over=False
score=0
FONT= ('Arial', 30 , 'normal')
screen.bgcolor("light grey")
screen.title("catch the turtle")

#turtle_list
turtle_list=[]

#score_turtle
score_turtle = turtle.Turtle()

#countdown_turtle
countdown_turtle = turtle.Turtle()

#make_turtles_properties
x_coordinates = [-20, -10, 0, 10, 20]
y_coordinates = [20, 10, 0, -10]
grid_size=5
def setup_score_turtle():

    score_turtle.hideturtle()
    score_turtle.color("blue")
    score_turtle.penup()

    top_height = screen.window_height() / 2
    y= top_height - top_height / 10
    score_turtle.setpos(0, y)
    score_turtle.write(arg="Score:0", move=False, align="center", font=FONT)

def make_turtle(x, y):
    t = turtle.Turtle()
    def handle_click(x, y):
         global score
         score += +1
         score_turtle.clear()
         score_turtle.write("Score: {}".format(score), move=False, align="center", font=FONT)
         print(x, y)

    t.onclick(handle_click)
    t.penup()
    t.shape("turtle")
    t.shapesize(2, 2)
    t.color("green")
    t.goto(x * grid_size, y * grid_size)
    t.pendown()
    turtle_list.append(t)


def setup_turtle():
    for x in x_coordinates:
        for y in y_coordinates:
            make_turtle(x,y)



def hide_turtles():
    for t in turtle_list:
        t.hideturtle()


def show_turtles_randomly():
    if not game_over:
        hide_turtles()
        random.choice(turtle_list).showturtle()
        screen.ontimer(show_turtles_randomly, 500)

def countdown(time):
    global game_over
    top_height = screen.window_height() / 2
    y = top_height - top_height /10
    countdown_turtle.hideturtle()
    countdown_turtle.penup()
    countdown_turtle.setpos(0, y-30)
    countdown_turtle.clear()

    if time > 0:
        countdown_turtle.clear()
        countdown_turtle.write("Time: {}".format(time), move=False, align="center", font=FONT)
        screen.ontimer(lambda : countdown(time - 1),1000)
    else:
        game_over=True
        countdown_turtle.clear()
        hide_turtles()
        countdown_turtle.write(arg="Game Over!", move=False ,align="center",font=FONT)

def start_game_up():
    global game_over
    game_over=False
    turtle.tracer(0)
    setup_score_turtle()
    setup_turtle()
    hide_turtles()
    show_turtles_randomly()
    turtle.tracer(1)
    screen.ontimer(lambda: countdown(10), 10)

start_game_up()
turtle.mainloop()