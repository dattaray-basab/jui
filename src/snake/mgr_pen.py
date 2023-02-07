import turtle


def pen_mgt():
    # Pen
    # Pen
    pen = turtle.Turtle()
    pen.speed( 0 )
    pen.shape( "square" )
    pen.color( "white" )
    pen.penup()
    pen.hideturtle()
    pen.goto( 0, 260 )
    pen.write( "Score: 0 High Score: 0", align="center", font=("Courier", 24, "normal") )

    def fn_write_score(score, high_score):
        pen.clear()
        pen.write( "Score: {}  High Score: {}".format( score, high_score ), align="center",
                   font=("Courier", 24, "normal") )

    return fn_write_score
