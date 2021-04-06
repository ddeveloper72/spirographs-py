# Mini project, using python tool to create Spirographs

This mini-project is a replication of work done by [Electronut Labs](http://electronut.in/) that uses parametric equations to draw a circle.
I've personally not used any trig functions since high school back in the late '80 early 90's; I graduated Matric or St 10 class of '91.  So this mini-project is an interesting refresher!
I came across this work, in an eBook, called Python [Playground: Geeky Projects for the Curious Programmer](https://g.co/kgs/quxp9B)
I've done this for the simple pure enjoyment factor of working with Python

## Draw circle

Created a snapshot of the application output

The origin or centre point of the circle is 0, the pen travels 360deg around this origin at a distance of r, which begins at an (x,y) coordinate and eventually finishes back at this same coordinate.  The function calculates the new (x,y) coordinate for each degree or radian about the origin.

If we specify a an origin point of (x=0, y=0), then place the imaginary pen nib at (x+r, y) we create a dot on the radius of the un-drawn circle.  The function below then calculates the new (x,y) values, then creates a new dot that is 5 radians away from the last dot, then repeats.

The range below is similar to a css rotation animation, that starts at 0deg, finishes at 360deg and rotates in increments of 5 radians, 365 times.

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

## Draw Spirographs

<img src="https://github.com/ddeveloper72/spirographs-py/raw/main/images/spiro-sample.png" alt="Image showing spirograph" title="Image showing Spirograph" style="max-width:40%;">

Spirographs can be drawn by considering the equation for a circle with a radius of *r*, then calculating the (x,y) coordinates for the plot line around the origin.


Consider the following:
An X Y axis has an angle of 90deg between them.  Its a perfect right angle.

But now somewhere between, the X and Y axis, we place a dot.  Then rule a line from the origin of the X Y axis, to our dot.  Call the origin 0.

Now if we measure the angle between our line and the X axis, we call this angle Theta, or use the Greek symbol, &#920; its units are in degrees or some may call it radians.

The formula for a circle is:


![Function of a circle](https://latex.codecogs.com/png.latex?\dpi{400}x^2+y^2=r^2 "Function of a circle")

This formula can be refactored below, to solve for x and y, which is our real interest- because we want to know where to place our pen; the dot, the (x,y) coordinate to begin drawing.

![Solve for x](https://latex.codecogs.com/png.latex?\dpi{400}y=rcos(\theta)) 

![Solve for y](https://latex.codecogs.com/png.latex?\dpi{400}x=rsin(\theta))



Ok, so we have a dot.  But how does one draw a a circle, comprised of multiple dots, all 5 radians apart? So... what if the 1st dot is on the X-axis.  That means Y is 0 and the angle, &#920; is also 0 degrees and x is some value bigger than 0  so pick 5, then the coordinate is (5,0).  This is handy, because 5 is the number of r, the radius as well.
The next coordinate depends on two constants.  The new value for &#920; and the constant for *r*.  With these two knowns, we can solve for the unknown, x and y.  See the pattern?  When we use python to do the math, it uses a tool called Turtle to act as the pen on paper.  In Turn, as the math is done from within the structure of a function, Turtle animates the drawing process- like a stop motion animation. Calculate dot, draw dot, calculate next dot, draw dot.  You and I see the magic of a beautiful curve, the result of loads and loads of mathematical computations to determine the values of (x,y).

So now we know how to draw a circle.  But this isn't a spirograph right.  A spirograph is a circle within a circle, where the inside circle rotates like a wheel, inside the larger circle.  
What? Hey?
The smaller circle roles around the inside for the bigger circle.  So as it roles, its outside edge follows the path of the inside edge of the larger circle.  Again we can calculate the (x,y) dots of the smaller circle, as they rotate their way around the the circumference of the larger circle.

So ok, what is it that is important we know?
For a start, the smaller circle as to have a centre.  Then the radius *r* from the centre of the smaller circle, can't extend beyond the radius *R* of the bigger circle.  If it did, it's not going to appear like the little circle rolling around the inside of the bigger circle, when we begin to animate all our dots together right.  

mmm.. so what we are doing is calculating the centre of the smaller circle, but we don't plot a dot at this point.  Instead, this (x,y) coordinate is the centre of the smaller circle, from were we can calculate another (x,y) coordinate where we can actually plot a dot.  The ratio between the radii of the two circles can be expressed as *k*

This is:

![Finding k](https://latex.codecogs.com/png.latex?\dpi{400}k=\frac{r}{R} "Function of a circle")


This new (x,y) coordinate has its own origin and there has its own angle &#920; that rotates 360 degrees.  We can call the origin of the smaller circle C.   The next step in our design, is to find the spot were we can place the pend tip within the radius of the smaller circle.  Call tis location P.  Here we use another function to determine the distance the pen tip from P.  the distance is called l.  In the code we use L, because l looks too much like 1 and can result in unexpected outcomes.

![Finding l](https://latex.codecogs.com/png.latex?\dpi{400}l=\frac{PC}{r})


When these variables are combined, the motion of P can be calculated to solve for (x,y)


![Solving for x](https://latex.codecogs.com/png.latex?\dpi{400}x=R((1-k)\cos(\theta)+Lk\cos(\frac{1-k}{k}\theta))) 

![Solving for y](https://latex.codecogs.com/png.latex?\dpi{400}y=R((1-k)\cos(\theta)+Lk\sin(\frac{1-k}{k}\theta)))

This is how we draw a circle within a circle.  So when we plot the next dot, showing the rotation of the smaller circle within the larger one, we start by incrementing the ϴ by 5deg in both circles, which means we get a new centre for the smaller circle which itself has rotated another ϴ.  We repeat the process of calculating the new (x,y) coordinates each time, and turtle animates the data to create beautiful curves representing this data in a more meaningfully way.


Using python, &#920; is represent by a for angle or radii

```` python

for i in range(0, 360*self.nRot + 1, self.step):
            a = math.radians(i)
            x = R*((1-k)*math.cos(a) + l*k*math.cos$((1-k)*a/k))
            y = R*((1-k)*math.sin(a) - l*k*math.sin((1-k)*a/k))

````

Image showing the Spirograph output:

![Image showing Spirographs](https://github.com/ddeveloper72/spirographs-py/blob/main/images/spiro-28Mar2021-234220.png "Image showing Turtle Spirographs")
