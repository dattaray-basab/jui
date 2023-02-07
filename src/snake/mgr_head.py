import turtle


def head_mgt():
    # Snake head
    head = turtle.Turtle()
    head.speed( 0 )
    head.shape( "square" )
    head.color( "black" )
    head.penup()
    head.goto( 0, 0 )
    head.direction = "stop"

    def fn_stop_head():
        head.direction = "stop"
    # Functions
    def go_up():
        if head.direction != "down":
            head.direction = "up"

    def go_down():
        if head.direction != "up":
            head.direction = "down"

    def go_left():
        if head.direction != "right":
            head.direction = "left"

    def go_right():
        if head.direction != "left":
            head.direction = "right"

    def move():
        if head.direction == "up":
            y = head.ycor()
            head.sety( y + 20 )

        if head.direction == "down":
            y = head.ycor()
            head.sety( y - 20 )

        if head.direction == "left":
            x = head.xcor()
            head.setx( x - 20 )

        if head.direction == "right":
            x = head.xcor()
            head.setx( x + 20 )
            
    def fn_reset_head():
        head.goto(0, 0)

    def fn_does_head_collide_with_border():
        if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
            return True
        return False

    def fn_is_food_within_devourable_distance(food):
        if head.distance( food ) < 20:
            return True
        return False

    return head, \
        fn_stop_head, \
        fn_does_head_collide_with_border, \
        fn_is_food_within_devourable_distance, \
        fn_reset_head, \
        go_up, go_down, go_left, go_right, move
    
        