import turtle as t
import random
screen = t.Screen()
race_on = False
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make a bet", prompt="Which turtle will win? Pick a Color: ")
colors = ["red", "blue", "green", "purple", "orange", "yellow"]
y_pos = [-70, -40, -10, 20, 50, 80]
all_turtles = []


for i in range(6):
    new_turtle = t.Turtle(shape='turtle')
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_pos[i])
    all_turtles.append(new_turtle)

    new_turtle.color(colors[i])

if user_bet:
    race_on = True
while race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 220:
            race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You have won! The color you chose is {winning_color}")
            else:
                print(f"You lose! Winning color is {winning_color}")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)
screen.exitonclick()
