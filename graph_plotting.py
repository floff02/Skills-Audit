
import numpy 
import matplotlib.pyplot as plot


def y(x):
    return numpy.exp(-x) * numpy.sin(2 * x + numpy.pi / 3)


x = numpy.linspace(-2 * numpy.pi, 2 * numpy.pi, 1000)


y = y(x)


plot.plot(x, y)


plot.xlabel('x')

plot.ylabel('y')

plot.title('y = e^(-x) * sin(2x + pi/3), -2pi ≤ x ≤ 2pi')


plot.show()
