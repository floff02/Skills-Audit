# Import numpy and matplotlib.pyplot
import numpy 
import matplotlib.pyplot as plot

# Define a function y(x) that returns the value of the expression "e^(-x) * sin(2x + pi/3)"
def y(x):
    return numpy.exp(-x) * numpy.sin(2 * x + numpy.pi / 3)

# Create an array of 1000 equally spaced values between -2*pi and 2*pi and assigns it to the variable "x"
x = numpy.linspace(-2 * numpy.pi, 2 * numpy.pi, 1000)

# calls the function "y(x)" and assigns the output to the variable "y"
y = y(x)

# Plot the values of x and y using the "plot.plot(x, y)" command from the matplotlib library
plot.plot(x, y)

# Give the x-axis the label "x"
plot.xlabel('x')
# Give the y-axis the label "y"
plot.ylabel('y')
# Give the graph a title "y = e^(-x) * sin(2x + pi/3), -2pi ≤ x ≤ 2pi"
plot.title('y = e^(-x) * sin(2x + pi/3), -2pi ≤ x ≤ 2pi')

# Show the graph using the "plot.show()" command
plot.show()
