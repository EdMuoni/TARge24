"""
https://courses.cs.ut.ee/t/pythonkoolis/Main/TsykkelYl

Koosta programm, mis küsib kasutajalt nime ja tervitab teda nimeliselt 5 korda ja lisab ka tervituse järjekorranumber.

Palun sisesta oma nimi:
>> Siim
Ole tervitatud, Siim, 1. korda.
Ole tervitatud, Siim, 2. korda.
Ole tervitatud, Siim, 3. korda.
Ole tervitatud, Siim, 4. korda.
Ole tervitatud, Siim, 5. korda."""


def ask_for_name_and_greet_five_times():
    name = input("Mis on sinu nimi?: ")
    for i in range(5):
        print(f"Ole tervitatud, {name}, {i + 1}. korda")


if __name__ == "__main__":
    ask_for_name_and_greet_five_times()

