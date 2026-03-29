import turtle
import random
import time

screen = turtle.Screen()
screen.title("Turtle Racing Game")
screen.bgcolor("lightblue")

print("Hello! I am the turtle guessing game")

tutle = int(input("How many turtles: "))
guess = int(input(f"Which trtle will win: "))

colors = ["red", "blue", "green", "orange", "purple", "pink", "yellow", "black"]
turtles = []

start_y = -100
spacing = 200 / max(1, tutle - 1)

for i in range(tutle):
    t = turtle.Turtle()
    t.shape("turtle")
    t.color(colors[i % len(colors)])
    t.penup()
    t.goto(-300, start_y + i * spacing)
    turtles.append(t)

finish_x = 300

winner = None

while winner is None:
    for i, t in enumerate(turtles):
        move = random.randint(1, 10)
        t.forward(move)

        if t.xcor() >= finish_x:
            winner = i + 1
            break

    time.sleep(0.02)

print(f'Turtle' , winner , 'won the race!')

if guess == winner:
    print("You guessed it right, good boy")
else:
    print("try again")

screen.mainloop()