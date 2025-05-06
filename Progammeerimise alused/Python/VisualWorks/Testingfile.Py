"""Here I wrote mathematical calculations part 1."""

import math


def sum_and_difference(num_a: int, num_b: int) -> tuple:
    """Return the sum and difference of given variables num_a and num_b."""
    # Write your code here
    summa = (num_a + num_b)
    difference = (num_a - num_b)
    return summa, difference


print(sum_and_difference(2, 2))


def float_division(num_a: int, num_b: int) -> float:
    """Divide given variables num_a and num_b and return the result."""
    # Write your code here
    division = (num_a / num_b)
    return division


print(float_division(3, 4))


def integer_division(num_a: int, num_b: int) -> int:
    """Divide given variables num_a and num_b and return the result rounded down."""
    # Write your code here
    division = num_a // num_b
    return division


print(integer_division(21, 6))


def powerful_operations(num_a: int, num_b: int) -> tuple:
    """Return the product of given variables, num_a to the power of num_b and the remainder of division of variables."""
    # Write your code here-
    multiply_numbers = num_a * num_b
    power = num_a ** num_b
    remainder = num_a % num_b
    return multiply_numbers, power, remainder


print(powerful_operations(10, 8))


def find_average(num_a: int, num_b: int) -> float:
    """Return the average of given variables."""
    # Write your code here
    average = (num_a + num_b) / 2.0
    return average


print(find_average(10, 8))


def area_of_a_circle(radius: float) -> float:
    """Calculate and return the area of a circle."""
    # Write your code here
    circle_area = round((math.pi * radius ** 2), 2)
    return circle_area


print(area_of_a_circle(10))


def area_of_an_equilateral_triangle(side_length: float) -> int:
    """Calculate and return the area of an equilateral triangle."""
    # Write your code here
    triangle_area = round(math.sqrt(3) / 4 * side_length ** 2)
    return triangle_area


print(area_of_an_equilateral_triangle(8.5))


def calculate_discriminant(a: int, b: int, c: int) -> int:
    """Calculate discriminant with given variables and return the result."""
    # Write your code here
    discriminant = (b ** 2 - 4 * a * c)
    return discriminant


print(calculate_discriminant(2, 2, 6))


def calculate_hypotenuse_length(a: int, b: int) -> float:
    """Return the length of hypotenuse when the lengths of the catheti are given."""
    # Write your code here
    c = math.sqrt(a ** 2 + b ** 2)
    return c


print(calculate_hypotenuse_length(5, 7))


def calculate_cathetus_length(a: int, c: int) -> float:
    """Return the length of cathetus when the lengths of the second cathetus and hypotenuse are given."""
    # Write your code here
    b = math.sqrt(c ** 2 - a ** 2)
    return b


print(calculate_cathetus_length(2.0, 5.6))

a = 15
if a // 3 == 5 or a % 5 == 3:
    print(a)
elif a % 3 == 3 or a // 5 == 5:
    print(-a)
else:
    print(a % 3)
