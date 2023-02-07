import turtle


def food_mgt(color = "red", shape = "circle", x = 0, y = 100):
    # Snake food
    food = turtle.Turtle()
    food.speed( 0 )
    food.shape( shape )
    food.color( color )
    food.penup()
    food.goto( x, y )

    return food

