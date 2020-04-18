# Two formulas based on input
def sum_arithmetic_series(n, first, last):
    return n*(first + last)/2
    
def sum_arithmetic_series_diff(n, first, diff=1):
    return n * (2 * first + (n - 1)*diff)/2


# Tests
t1a = sum_arithmetic_series(4, 1, 4)
assert t1a == 10
print(t1a)

t1b = sum_arithmetic_series_diff(4, 1, 1)
assert t1b == 10
print(t1b)

t2a = sum_arithmetic_series(255, 1, 255)
assert t2a == 32640
print(t2a)

t2b = sum_arithmetic_series_diff(1000000, 255, 5)
assert t2b == 2500252500000
print(t2b)
