import numpy as np

# syntax: linspace(start, stop, num=n, endpoint=True/False, retstep=True/False)

# default number of values is 50

print(np.linspace(1, 10))

# printing 7 values between 1 and 10 with equal step

print(np.linspace(1, 10, 7))

# if you want to exclude the endpoint while printing the result

print(np.linspace(1, 10, 7, endpoint=False))

# if you want to include the step value along with the result returned

print(np.linspace(1, 10, 7, retstep=True))