# Snake Game by Mahesh Sawant

import turtle
import time
import random

from src.snake.mgr_food import food_mgt
from src.snake.mgr_head import head_mgt
from src.snake.mgr_pen import pen_mgt
from src.snake.mgr_wn import win_mgt

delay = 0.1

# Score
score=0
high_score=0

wn = win_mgt()

head, fn_stop_head, go_up, go_down, go_left, go_right, move = head_mgt()

food = food_mgt()

segments=[]

fn_write_score = pen_mgt()


# keyboard bindings
wn.listen()
wn.onkeypress(go_up,"Up")
wn.onkeypress(go_down,"Down")
wn.onkeypress(go_left,"Left")
wn.onkeypress(go_right,"Right")


def fn_create_new_segment():
    # Add a segment
    new_segment = turtle.Turtle()
    new_segment.speed( 0 )
    new_segment.shape( "square" )
    new_segment.color( "grey" )
    new_segment.penup()

    return new_segment





# Main game loop
while True:
    wn.update()

    # Check for a collision with the border
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        fn_stop_head()

        # Hide the segments
        for segment in segments:
            segment.goto(1000,1000)

        # Clear the segments list
        segments.clear()

        # Reset the score
        score=0

        # Reset the delay
        delay = 0.1

        fn_write_score(score, high_score)


    #Check for a collision with the food
    if head.distance(food)<20:
        # move the food to a random spot
        x=random.randint(-285,285)
        y=random.randint(-285,285)
        food.goto(x,y)

        new_segment = fn_create_new_segment()
        segments.append(new_segment)

        # Shorten the delay
        delay -= 0.001

        # Increase the score
        score+=10

        if score > high_score:
            high_score = score

        fn_write_score( score, high_score )

    # Move the end segment first in reverse order
    for index in range(len(segments)-1,0,-1):
        x=segments[index-1].xcor()
        y=segments[index-1].ycor()
        segments[index].goto(x,y)

    # Move segment 0 to where the head is
    if len(segments)>0:
        x=head.xcor()
        y=head.ycor()
        segments[0].goto(x,y)

    move()

    # Check for head collision with the body segments
    for segment in segments:
        if segment.distance(head)<20:
            time.sleep(1)
            head.goto(0,0)
            fn_stop_head()

            # Hide the segments
            for segment in segments:
                segment.goto(1000,1000)

            # Clear the segments list
            segments.clear()

            # Reset the score
            score = 0

            #Reset the delay
            delay = 0.1

            fn_write_score()

    time.sleep(delay)

wn.mainloop()
