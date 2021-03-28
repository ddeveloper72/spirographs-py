# spiro.py

# Description: drawing spirographs using math equations with python
# Tutorial from: Spirographs by Playground: Geeky Projects for the Curious
# Programmer

import turtle


# Class for drawing a Spirograph
class Spiro:
    # the constructor
    def __init__(self, xc, yc, col, R, r, l):

        # crate the turtle object
        self.t = turtle.Turtle()

        # set the cursor shape
        self.t.shape('turtle')

        # set the drawings steps/increments in degrees
        self.step = 5

        # set the drawing complete flag
        # see https://docs.python.org/3.3/library/turtle.html 
        self.drawingComplete = False

        # set the paramaters from the functions below
        self.setparams(xc, yc, col, R, r, l)

        # initialize the drawing
        self.restart()
