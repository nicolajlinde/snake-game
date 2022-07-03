from turtle import Screen, Turtle
from snake import Snake
from utility import Utility
import time

settings = Utility()
screen = Screen()
snake = Snake()

screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.05)

    snake.move()









screen.exitonclick()