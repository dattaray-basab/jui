# set up the screen
import turtle

def win_mgt():
    wn = turtle.Screen()
    def fn_create_screen(color="green", title="Snake Game by Jui", width=600, height=600):

        wn.title(title)
        wn.bgcolor(color)
        wn.setup(width=width, height=height)
        wn.tracer(0)
        return wn

    fn_create_screen()

    return wn