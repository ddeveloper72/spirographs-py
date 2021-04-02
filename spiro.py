# spiro.py

# Description: drawing spirographs using math equations with python
# Tutorial from: Spirographs by Playground: Geeky Projects for the Curious
# Programmer

import turtle
import math
import numpy as np
from math import gcd
import sys
import random
import argparse
from PIL import Image
from datetime import datetime


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

    # set restart method for the drawing
    def restart(self):
        # set the flag
        self.drawingComplete = False

        # show the turtle
        self.t.showturtle()

        # go to the first point to begin plot
        self.t.up()
        R, k, l = self.R, self.k, self.l
        a = 0.0
        x = R*((1-k)*math.cos(a) + l*k*math.cos((1-k)*a/k))
        y = R*((1-k)*math.sin(a) - l*k*math.sin((1-k)*a/k))
        self.t.setpos(self.xc + x, self.yc + y)
        self.t.down()

    # Specify the draw method
    def draw(self):
        # draw the remaining points
        R, k, l, = self.R, self.k, self.l
        for i in range(0, 360*self.nRot + 1, self.step):
            a = math.radians(i)
            x = R*((1-k)*math.cos(a) + l*k*math.cos((1-k)*a/k))
            y = R*((1-k)*math.sin(a) - l*k*math.sin((1-k)*a/k))
            self.t.setpos(self.xc + x, self.yc + y)
        # drawing is done so hide the turtle cursor
        self.t.hideturtle()

    # update the drawing by one step crating animatin effect
    def update(self):
        # skip remaining steps if complete
        if self.drawingComplete:
            return

        # increment the angle
        self.a += self.step

        # draw a step
        R, k, l = self.R, self.k, self.l

        # set angle
        a = math.radians(self.a)
        x = self.R*((1-k)*math.cos(a) + l*k*math.cos((1-k)*a/k))
        y = self.R*((1-k)*math.sin(a) - l*k*math.sin((1-k)*a/k))
        self.t.setpos(self.xc + x, self.yc + y)

        # if drawing is complete, set the flag
        if self.a >= 360*self.nRot:
            self.drawingComplete = True

            # drawing is done, so hide turtle cursor
            self.t.hideturtle()

    # clear everything
    def clear(self):
        self.t.clear()


# class for animating the spirographs
class SpiroAnimator:
    # constructor
    def __init__(self, N):
        # set the timer value in millisecords
        self.deltaT = 10

        # get the window dimensions
        self.width = turtle.window_width()
        self.height = turtle.window_height()

        # crate spiro objects
        self.spiros = []
        for i in range(N):

            # generate random parameters
            rparams = self.genRandomParams()

            # set the spiro parameters
            spiro = Spiro(*rparams)
            self.spiros.append(spiro)

        # call timer
        turtle.ontimer(self.update, self.deltaT)

    # restart the spiro drawing
    def restart(self):
        for spiro in self.spiros:

            # clear
            spiro.clear()

            # generate random parameters
            rparams = self.genRandomParams()

            # set the spiro parameters
            spiro.setparams(*rparams)

            # restart drawing
            spiro.restart()

    # generate random parameters
    def genRandomParams(self):
        width, height = self.width, self.height
        R = random.randint(50, min(width, height)//2)
        r = random.randint(10, 9*R//10)
        l = random.uniform(0.1, 0.9)
        xc = random.randint(-width//2, width//2)
        yc = random.randint(-height//2, height//2)
        col = (random.random(),
               random.random(),
               random.random()
               )
        return(xc, yc, col, R, r, l)

    # update method
    def update(self):
        # Update all spiros
        numComplete = 0
        for spiro in self.spiros:

            # update
            spiro.update()

            # count completed spiros
            if spiro.drawingComplete:
                numComplete += 1

        # restart if all spiros are complete
        if numComplete == len(self.spiros):
            self.restart()

        # call the timer
        turtle.ontimer(self.update, self.deltaT)

    # toggle cursor
    def toggleTurtles(self):
        for spiro in self.spiros:
            if spiro.t.isvisible():
                spiro.t.hideturtle()
            else:
                spiro.t.showturtle()


# save drawings to PNG files
def saveDrawing():
    # hide the turtle cursor
    turtle.hideturtle()

    # generate unique filenames
    dateStr = (datetime.now()).strftime("%d%b%Y-%H%M%S")
    fileName = 'spiro-' + dateStr
    print('saving drawing to %s.esp/png' % fileName)

    # get the tkinter canvas
    canvas = turtle.getcanvas()

    # save the drawings as a post script image
    canvas.postscript(file=fileName + '.eps')

    # use the Pillow module to convert the postscript image file to PNG
    img = Image.open(fileName + '.eps')
    img.save(fileName + '.png', 'png')

    # show the turtle cursor
    turtle.showturtle()


# The main() function
def main():
    # use sys.argv if needed
    print('generating spirograph...')

    # create parser
    descStr = """This program draws Spirographs using the turtle module.
    When run with no arguments, this program draws random Spirographs.

    Terminology:

    R: radius of outer circle
    r: radius of inner circle
    i: ratio of hole distance to r
    """

    parser = argparse.ArgumentParser(description=descStr)

    # add expected arguments
    parser.add_argument('--sparams', nargs=3, dest='sparams', required=False,
                        help="The three arguments in sparms: R, r, l.")

    # parse args
    args = parser.parse_args()

    # set width of the spiro drawing window 60% of the screen width, height
    turtle.setup(width=0.6, height=0.6)

    # set shape of the turtle cursor
    turtle.shape('turtle')

    # set the title to the Spirographs!
    turtle.title("Spirographs")

    # add the key handler to save your drawings
    turtle.onkey(saveDrawing, "s")

    # start listening
    turtle.listen()

    # hide the main turtle cursor
    turtle.hideturtle()

    # check for any arguments sent to --sparams and draw the Spirograph
    if args.sparams:
        params = [float(x) for x in args.sparams]

        # draw the Spirograph with the given parameters
        col = (0.0, 0.0, 0.0)
        spiro = Spiro(0, 0, col, *params)
        spiro.draw()
    else:
        # create the animator object
        spiroAnim = SpiroAnimator(4)

        # add a keyhandler to toggle the turtle cursor
        turtle.onkey(spiroAnim.toggleTurtles, "t")

        # add a keyhandler to restart the animation
        turtle.onkey(spiroAnim.restart, "space")

    # start the turtle main loop
    turtle.mainloop()


# call main
if __name__ == '__main__':
    main()
