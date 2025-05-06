"""Basic function exercises."""
import math


def print_hello():
    """Print "hello"."""
    # code here
    print("Hello")


def get_hello() -> str:
    """Return "hello"."""
    # code here
    return "Hello"


def ask_name_and_greet_user():
    """
    Ask name and greet user.

    The user has to enter his/her name. The function prints the greeting.

    Regular greeting: Hi, [name]. Would you like to have a Hamburger?
    [name] is capitalized, meaning first letter is capital, the rest is lower.

    If the name is Thanos (case insensitive, so thanos and THANOS also count):
    Get out of here, Thanos! Nobody wants to play with you!
    """
    # code here
    name = input("What is your name: ")
    name_2 = "Thanos"
    if name.lower() == name_2.lower():
        print(f"Get out of here, {name.capitalize()}! Nobody wants to play with you!")
    else:
        print(f"Hi, {name.capitalize()}. Would you like to have a Hamburger?")


def calculate_hypotenuse_length(a: float, b: float) -> float:
    """Return hypotenuse value."""
    # code here
    cathetus_a = int(a)
    cathetus_b = int(b)
    hypotenuse_length = math.sqrt(cathetus_a ** 2 + cathetus_b ** 2)
    return hypotenuse_length


def calculate_cathetus_length(a: float, c: float) -> float:
    """Return cathetus value."""
    # code here
    cathetus_a = float(a)
    hypotenuse_c = float(c)
    cathetus_length = math.sqrt(hypotenuse_c ** 2 - cathetus_a ** 2)
    return cathetus_length


if __name__ == '__main__':
    print_hello()  # should print "Hello"
    hello = get_hello()  # should return "Hello"
    print(hello)  # let's check the value of hello variable
    ask_name_and_greet_user()  # should ask name and greet
    print(calculate_hypotenuse_length(3, 4))  # should print 5.0
    print(calculate_cathetus_length(3, 5))  # should print 4.0
