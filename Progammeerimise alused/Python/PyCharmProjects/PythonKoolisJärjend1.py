"""
Koosta järjend vähemalt kümne Euroopa pealinnaga (suvalises järjekorras).

Väljasta linnad eraldi ridadena.
Järjesta need tähestikulisse järjekorda.
Lase kasutajal lisada kaks uut Euroopa pealinna ja järjesta uuesti.
Esita linnade nimed tähestikulises järjekorras, lisades iga nime ette ka järjekorra numbri.
Lisa väljundile kokkuvõttev lause "Meie järjendis on 12 Euroopa pealinna", kus linnade arv leitakse vastava funktsiooni abil.
"""


def print_on_separate_lines(lis_of_strings, with_line_numbers=False):
    line_number = 1
    for element in lis_of_strings:
        if with_line_numbers:
            print(f"{line_number}. ", end="")
            line_number += 1
        print(element)


def print_with_enumerate(lis_of_strings):
    for index, element in enumerate(lis_of_strings, start=1):
        print(f"{index}. {element}")


def capitals_list():
    capitals = ["Tallinn", "Rome", "Moscow",
                "London", "Helsingi", "Brüssel",
                "Dublin", "Berlin", "Paris", "Madrid"]
    print("Unsorted capitals:")
    print_on_separate_lines(capitals)
    sort_and_print(capitals)
    # while len(capitals) < 12:
    # user_input = input("Enter a new European capital: ")
    #     if user_input in capitals:
    #         print("The capital is already in the list.")
    #     else:
    #         capitals.append(user_input)
    # sort_and_print(capitals)
    # return capitals
    sort_and_print(capitals, True)  # Sulgudes on kutsuv protgramm kas ma tahan numerdatud pealinnad True või ei taha False
    print_with_enumerate(capitals)


def sort_and_print(capitals, with_lines_number=False):
    capitals.sort()
    print("\nSorted capitals:")
    print_on_separate_lines(capitals, with_lines_number)


if __name__ == "__main__":
    capitals_list()
