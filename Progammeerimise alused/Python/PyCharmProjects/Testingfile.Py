def get_hello(greet="Hey"):
    return greet


def get_greeting(where, whom="everyone"):
    return f"{get_hello()}, I am greeting {whom} in {where}!"


def main():
    print(get_greeting("the class", "all the students"))


if __name__ == '__main__':
    main()


def say_hello(jaan):
    print("hello", "jaan")


say_hello("mari")


def my_first_quiz(first_quiz: bool):
    if first_quiz:

        return "This is my first quiz in Python and I love it!"

    else:

        return "This is not my first quiz in Python."


if __name__ == '__main__':
    my_first_quiz(True)


def introduce_yourself():
    return "Hello, I am function! Nice to meet ya!"


if __name__ == '__main__':
    introduce_yourself()


def greet(name):
    print("Hello, " + name)


# Hello, Mari

a = 15
if a // 3 == 5 or a % 5 == 3:
    print(a)
elif a % 3 == 3 or a // 5 == 5:
    print(-a)
else:
    print(a % 3)

count = 0

while count < 4:
    print(count, end=" ")
    count += 1

for element in [0, 1, 2, 3]:
    print(element)

numbers = [1, 5, 6, 3, 7]

total = 0

for nr in numbers:
    total = total + nr  # you can use += example: total += nr

print(f"Total sum is {total}")

total = 0

for i in range(10):
    print(i)
    total += i

print(f"Total sum is {total}")  # Total sum is 45

names = ["Harry", "Hermione", "Ron"]

for i in range(len(names)):
    print(f"Element at index {i} is {names[i]}")

names = ["Frodo", "Merry", "Pippin", "Sam"]

for name in names:
    print(f"Analyzing name {name}")
    if name.startswith("M"):
        print(f"Found a name starting with M: {name}")
        break

numbers = [1, 2, 4, 5, 6, 9, 10]

for nr in numbers:
    if nr % 2 == 0:
        continue
    print(f"Odd number: {nr}")

text = "Hello world!"

for char in text:
    print(char, end=" ")
print()

words = ["orange", "pear", "apple", "banana", "ananas"]

result = ""
for word in words:
    if word.startswith("a"):
        result = word

if result == "":
    print("No word starting with a")
else:
    print(f"The last word starting with a: {result}")

for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i * j:4}", end="")
    print()
"""1   2   3   4   5   6   7   8   9  10  # i = 1 and j = [1---10]
   2   4   6   8  10  12  14  16  18  20  # i = 2 and j = [1---10]
   3   6   9  12  15  18  21  24  27  30
   4   8  12  16  20  24  28  32  36  40
   5  10  15  20  25  30  35  40  45  50
   6  12  18  24  30  36  42  48  54  60
   7  14  21  28  35  42  49  56  63  70
   8  16  24  32  40  48  56  64  72  80
   9  18  27  36  45  54  63  72  81  90
  10  20  30  40  50  60  70  80  90 100
"""

for num in range(5):
    print(num)

sum = 0

for x in range(1, 6):

    if x % 2 == 0:
        sum = sum + (x * 2)

print(sum)

for i in range(0, 10):

    if i % 2 == 0:
        print(i)

s = 0
for i in range(7, 13):
    if i % 3 != 0:
        s += i
    else:
        s -= i
print(s)

for num in range(2, -5, -1):
    print(num, end=", ")


a = 3
b = 0
for i in range(a):
    for j in range(a):
        b += j
print(b)

