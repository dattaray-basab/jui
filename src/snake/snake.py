# Snake Game by Mahesh Sawant

import turtle
import time
import random

from src.snake.mgr_food import food_mgt
from src.snake.mgr_head import head_mgt
from src.snake.mgr_pen import pen_mgt
from src.snake.mgr_segments import segments_mgr
from src.snake.mgr_wn import win_mgt

delay = 0.1

# Score
score=0
high_score=0



head, fn_stop_head, fn_does_head_collide_with_border, fn_is_food_within_devourable_distance,\
    go_up, go_down, go_left, go_right, move = head_mgt()

wn = win_mgt(go_up, go_down, go_left, go_right,)

food = food_mgt()

# segments=[]
fn_add_new_segment, fn_expand_segment, fn_reset_segments, fn_get_segments = segments_mgr(head)

fn_write_score = pen_mgt()


# Main game loop
while True:
    wn.update()

    # Check for a collision with the border
    if fn_does_head_collide_with_border():
        time.sleep(1)
        head.goto(0,0)
        fn_stop_head()

        fn_reset_segments()

        # Reset the score
        score=0

        # Reset the delay
        delay = 0.1

        fn_write_score(score, high_score)


    #Check for a collision with the food
    if fn_is_food_within_devourable_distance(food):
        # move the food to a random spot
        x=random.randint(-285,285)
        y=random.randint(-285,285)
        food.goto(x,y)

        fn_add_new_segment()

        # Shorten the delay
        delay -= 0.001

        # Increase the score
        score+=10

        if score > high_score:
            high_score = score

        fn_write_score( score, high_score )

        fn_expand_segment()

    move()

    # Check for head collision with the body segments
    segments = fn_get_segments()
    for segment in segments:
        if fn_is_food_within_devourable_distance(food):
            time.sleep(1)
            head.goto(0,0)
            fn_stop_head()

            fn_reset_segments()

            # Reset the score
            score = 0

            #Reset the delay
            delay = 0.1

            fn_write_score( score, high_score)

    time.sleep(delay)

wn.mainloop()
