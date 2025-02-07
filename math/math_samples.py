import math

# Returns the ceiling of x, the smallest integer greater than or equal to x.
print(math.ceil(4.2))  # Output: 5
# Returns the floor of x, the largest integer less than or equal to x.
print(math.floor(4.8))  # Output: 4
# Returns the absolute value of x.
print(math.fabs(-5.5))  # Output: 5.5
# Returns the factorial of x.
print(math.factorial(5))  # Output: 120
# Returns the remainder when x is divided by y.
print(math.fmod(20, 3))  # Output: 2.0
# Returns the greatest common divisor of x and y.
print(math.gcd(48, 18))  # Output: 6
# Returns True if x is neither an infinity nor a NaN (Not a Number).
print(math.isfinite(10))  # Output: True
print(math.isfinite(math.inf))  # Output: False
# Returns True if x is a positive or negative infinity.
print(math.isinf(math.inf))  # Output: True
print(math.isinf(10))  # Output: False
# Returns True if x is a NaN (Not a Number).
print(math.isnan(math.nan))  # Output: True
print(math.isnan(10))  # Output: False
# Returns e raised to the power of x.
print(math.exp(2))  # Output: 7.3890560989306495
# Returns the logarithm of x to the given base. If the base is not specified, returns the natural logarithm (base e) of x.
print(math.log(10))  # Output: 2.302585092994046
print(math.log(100, 10))  # Output: 2.0
# Returns the base-10 logarithm of x.
print(math.log10(100))  # Output: 2.0
# Returns x raised to the power of y.
print(math.pow(2, 3))  # Output: 8.0
# Returns the square root of x.
print(math.sqrt(16))  # Output: 4.0
# Returns the sine of x (x is in radians).
print(math.sin(math.pi / 2))  # Output: 1.0
# Returns the cosine of x (x is in radians).
print(math.cos(math.pi))  # Output: -1.0
# Returns the tangent of x (x is in radians).
print(math.tan(math.pi / 4))  # Output: 1.0
# Converts angle x from radians to degrees.
print(math.degrees(math.pi))  # Output: 180.0
# Converts angle x from degrees to radians.
print(math.radians(180))  # Output: 3.141592653589793