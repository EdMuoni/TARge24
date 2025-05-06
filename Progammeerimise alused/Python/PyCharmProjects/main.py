# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print("Hi, " + str(name))
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def greet_with_given_name():
    print("Hello, I am your program!")
    name = input("What is your name: ")
    print(f"Hello {name}!")


if __name__ == '__main__':
    print_hi('PyCharm')
    greet_with_given_name()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
