"""
Koosta vähemalt kümnest elemendist koosnev järjend arvudest. Koosta programm, mis küsib kasutajalt tegurit ja korrutab kõik algses järjendis olnud arvud sellega läbi ning väljastab tulemuse ekraanile.

Sisesta tegur: 3
45 * 3 = 135
7 * 3 = 21
...
267 * 3 = 801
"""


def multiply(multiplier):
    numbers = [2, 4, 55, 11, 23, 19, 0, -7, 6, 10]  # suvaline kümnarvuline jada numbreid
    for number in numbers:
        print(f"{number} * {multiplier} = {number * multiplier}")


if __name__ == "__main__":
    number = int(input("Enter a number: "))
    multiply(number)
