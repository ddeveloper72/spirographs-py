# Mini project, using python tool to create Spirographs

This mini-project is a replication of work done by [Electronut Labs](http://electronut.in/) that uses parametric equations to draw a circle.
I've personally not used any trig functions since high school back in the late '80 early 90's; I graduated Matric or St 10 class of '91.  So this mini-project is an interesting refresher!
I came across this work, in an eBook, called Python [Playground: Geeky Projects for the Curious Programmer](https://g.co/kgs/quxp9B)
I've done this for the simple pure enjoyment factor of working with Python

## Draw circle

Created a snapshot of the application output

The origin or centre point of the circle is 0, the pen travels 360deg around this origin at a distance of r, which begins at an (x,y) coordinate and eventually finishes back at this same coordinate.  The function calculates the new (x,y) coordinate for each degree or radian about the origin.

If we specify a an origin point of (x=0, y=0), then place the imaginary pen nib at (x+r, y) we create a dot on the radius of the un-drawn circle.  The function below then calculates the new (x,y) values, then creates a new dot that is 5 radians away from the last dot, then repeats.

The range below is similar to a css rotation animation, that starts and 0deg, finishes at 365deg and rotates in increments of 5 radians.

```` python

for i in range(0, 365, 5):
        a = math.radians(i)
        turtle.setpos(
            x + r*math.cos(a),
            y + r*math.sin(a)
        )

````

Image showing Draw Circle output:

![Image showing circle](https://github.com/ddeveloper72/spirographs-py/blob/main/images/drawcircle.png "Image showing Draw Circle output")
