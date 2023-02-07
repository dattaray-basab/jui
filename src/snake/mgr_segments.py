import turtle


def segments_mgr(head):
    segments = []


    def fn_add_new_segment():
        new_segment = turtle.Turtle()
        new_segment.speed( 0 )
        new_segment.shape( "square" )
        new_segment.color( "grey" )
        new_segment.penup()
        segments.append(new_segment)

    def fn_expand_segment():
        # Move the end segment first in reverse order
        for index in range( len( segments ) - 1, 0, -1 ):
            x = segments[index - 1].xcor()
            y = segments[index - 1].ycor()
            segments[index].goto( x, y )

        # Move segment 0 to where the head is
        if len( segments ) > 0:
            x = head.xcor()
            y = head.ycor()
            segments[0].goto( x, y )

    def fn_reset_segments():
        # Hide the segments
        for segment in segments:
            segment.goto(1000,1000)

        # Clear the segments list
        segments.clear()

    def fn_get_segments():
        return segments


    return fn_add_new_segment, fn_expand_segment, fn_reset_segments, fn_get_segments