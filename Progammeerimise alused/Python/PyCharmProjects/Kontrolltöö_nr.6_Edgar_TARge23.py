"""
1.     v Kasutajalt küsitakse sõna.
2.     v Kasutajalt küsitakse numbrit.
3.       Konsool prindib antud sõna välja sisestatud number * 2 korda (kordus).
4.       Juhul kui sisestatud number on suurem kui 10, tagastatakse „Viga“.
"""


def ask_for_word():
    word = input("Sisesta sõna: ")
    return word


def ask_for_number():
    number = input("Sisesta number: ")
    return number
    number = int(number)


def repeated_word(word: int, number: int):
    result = word * (number * 2)
    return result


if __name__ == "__main__":
    word = ask_for_word()
    number = ask_for_number()

    if number > 10:
        print("Viga!")
    else:
        print(repeated_word(word, number))
