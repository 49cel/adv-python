import numpy as np

# syntax: arange([start, stop), step, dtype = None])

a = np.arange(1, 10)
print(a)

x = np.arange(10.4) # default step is taken as 1, prints floating point values from 1 to 10
print(x)

y = np.arange(0.5, 10, 0.5) # prints values from 0.5 to 10 (not including 10), with a step of 0.5
print(y)

z = np.arange(0.5, 10, 0.5, int) # same thing but only prints the integral part, drops fractional part
print(z)