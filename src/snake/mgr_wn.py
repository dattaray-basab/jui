# set up the screen
import turtle

def win_mgt(go_up, go_down, go_left, go_right):
    wn = turtle.Screen()
    # keyboard bindings
    wn.listen()
    wn.onkeypress( go_up, "Up" )
    wn.onkeypress( go_down, "Down" )
    wn.onkeypress( go_left, "Left" )
    wn.onkeypress( go_right, "Right" )

    def fn_create_screen(color="green", title="Snake Game by Jui", width=600, height=600):

        wn.title(title)
        wn.bgcolor(color)
        wn.setup(width=width, height=height)
        wn.tracer(0)
        return wn

    fn_create_screen(title="Snake Game played by Anik")

    return wn