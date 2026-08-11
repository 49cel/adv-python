### intro to numpy
- - -
- numpy, also known as numerical python is used for fast numerical computing, also dealing with multidimensional arrays
- it is actually written in C, so it is much faster than your typical python list management
- to check the time difference, you can either use the time library or the timeit function, the time library stores the current time universally for everyone which keeps incrementing every second, the duration is calculated by calculating the difference between the timestamp after execution and before execution

### arange function
- - -
- used to generate an ndarray of evenly spaced intervals 
- the interval is [start, stop), meaning the starting value is included and the ending value is excluded
- step sets the spacing bw two adjacent intervals
- dtype specifies the data type of output array

### linspace function
- - -
-