from turtle import Turtle, Screen
import time
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)


snake = Snake()

game_is_on = True
while game_is_on:
    time.sleep(1)
    screen.update()
    snake.move_snake()

screen.exitonclick()