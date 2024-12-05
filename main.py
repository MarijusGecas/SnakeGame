from turtle import Screen
from snake import Snake
import time
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=800, height=800)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()
score = 0

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")



game_is_on= True
while game_is_on:
    screen.update()
    time.sleep(0.05)
    snake.move()

    #Food collision
    if snake.head.distance(food) < 15:
        food.refresh()
        score+=1
        snake.extend()
    scoreboard.display_score(score)

    # Border collision
    if snake.head.xcor() > 380 or snake.head.xcor() < -380 or snake.head.ycor() > 380 or snake.head.ycor() < -380:
        game_is_on= False
        scoreboard.game_over()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) <10:
            game_is_on = False
            scoreboard.game_over()














screen.exitonclick()