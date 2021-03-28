# drawcircle.py

# Description: drawing spirographs using math equations with python
# Tutorial from: Spirographs by Playground: Geeky Projects for the Curious Programmer


import math
import turtle  # drawing application


# drawing circle
def drawCircleTurtle(x, y, r):

    # Imagine moving a pen to the centre of the circle
    # then seting it done to begin drawing
    turtle.up()
    turtle.setpos(x + r, y)
    turtle.down()

    # draw circle with these parameters:
    # start at, 0 the center of the circle
    # travel 365 degrees around the center
    # place the pen at r the distance out from the center
    for i in range(0, 365, 5):
        a = math.radians(i)
        turtle.setpos(
            x + r*math.cos(a),
            y + r*math.sin(a)
        )


drawCircleTurtle(100, 100, 150)
turtle.mainloop()
