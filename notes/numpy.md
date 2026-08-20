### intro to numpy
- - -
- numpy, also known as numerical python is used for fast numerical computing, also dealing with multidimensional arrays
- it is actually written in C, so it is much faster than your typical python list management
- to check the time difference, you can either use the time library or the timeit function, the time library stores the current time universally for everyone which keeps incrementing every second, the duration is calculated by calculating the difference between the timestamp after execution and before execution

### arange() function
- - -
- used to generate an ndarray of evenly spaced intervals 
- the interval is [start, stop), meaning the starting value is included and the ending value is excluded
- step sets the spacing bw two adjacent intervals
- dtype specifies the data type of output array
- arange works in an unexpected way when you specify dtype to be int, but then use a floating point value as step, since this is internally a c-level array it needs to allocate memory first, so it calculates how many elements are in the array and then converts them to int, which truncates or rounds off the fractional part, this causes unexpected behaviour (for example: when using 0.5 as the step value, it defaults to the step value being 1, and 2.5 gets rounded off to 3) this is a well known bug in the numpy documentation and should be avoided (i don't fully understand this yet so take it with a grain of salt)


### linspace() function
- - -
- syntax: `linspace(start, stop, num=n, endpoint'True/False, retstep=True/False)`
- it returns an ndarray consisting of equally spaced samples, the samples can lie within a closed interval or open interval depending on what you set the endpoint to be (True/False)
- the parameters used are - start, stop, num=50, endpoint and retstep
    1. **start** - specifies the starting value
    2. **stop** - specifies the ending value (may or may not be included)
    3. **endpoint** - specifies if endpoint should be included or not (last value), you can toggle it to be True or False
    4. **retstep** - returns the step value used
- whats different from arange is that, arange generates a number of values with the specified step between a starting and ending point, but in linspace you specify the number of elements to be generated and generates those elements with a step required to generate those many number of values
- there are two different formulae that get used whenever you toggle the endpoint to true or false
  1. formula for endpoint=True -> 
  
  $$ 
  \text{step} = \frac{\text{stop} - \text{start}}{\text{num} - 1}
  $$
  
  2. formula for endpoint=False ->
  
  $$
  \text{step} = \frac{\text{stop} - \text{start}}{\text{num}} 
  $$