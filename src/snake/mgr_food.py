import turtle


def food_mgt():
    # Snake food
    food = turtle.Turtle()
    food.speed( 0 )
    food.shape( "circle" )
    food.color( "red" )
    food.penup()
    food.goto( 0, 100 )

    return food

