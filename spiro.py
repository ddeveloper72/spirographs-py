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


# set the parameters
def setparams(self, xc, yc, col, R, r, l):
    # the Spirograph parameters
    self.xc = xc
    self.yc = yc
    self.R = int(R)
    self.r = int(r)
    self.l = l

    # reduce r/R to its smallest form by dividing with the GCD
    gcdVal = gcd(self.r, self.R)
    self.nRot = self.r//gcdVal

    # get ratio of radii
    self.k = r/float(R)

    # set color
    self.t.color(*col)

    # store the current angle
    self.a = 0
