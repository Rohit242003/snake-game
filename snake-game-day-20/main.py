from turtle import Turtle,Screen
import  time

import scoreborard
import snake
import food

food = food.Food()
snake = snake.Snake()
scoreborard= scoreborard.Scoreboard()
screen = Screen()
screen.setup(height=600,width=600)
screen.bgcolor("black")
screen.title("welcome! to snake game")
screen.tracer(0)

screen.listen()
screen.onkey(key="Up",fun=snake.up)
screen.onkey(key="Down",fun=snake.down)
screen.onkey(key="Left",fun=snake.left)
screen.onkey(key="Right",fun=snake.right)


is_on = True
while is_on:
    screen.update()
    time.sleep(0.2)
    snake.move_snake()

    # detect collision with food
    if snake.turtles[0].distance(food) <15:
        scoreborard.increase_score()

        food.refresh()
        screen.tracer(0)
        snake.increase_size()
    # detect collision with wall

    if snake.turtles[0].xcor() > 280 or snake.turtles[0].xcor() < -280 or snake.turtles[0].ycor() > 280 or snake.turtles[0].ycor() < (-280):

        is_on = False
        scoreborard.game_over()
    for turtle in snake.turtles[1:]:

        if snake.turtles[0].distance(turtle) < 10 :
            is_on = False
            scoreborard.game_over()

screen.exitonclick()
