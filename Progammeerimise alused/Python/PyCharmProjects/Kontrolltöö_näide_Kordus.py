"""
KORDUS
Küsi kasutajalt kordamööda paaris ja paarituid arve. Kontrolli ja kuva ekraanile, et sisetatakse õige arv.
Lõpeta programm, kui kasutaja on 5 korda eksinud.
"""


def ask_a_number(number_type: str, correct_remainder: int) -> int:
    user_input = int(input(f"Sisesta {number_type}arv: "))
    if user_input % 2 == correct_remainder:
        print(f"Tubli, sisestasid {number_type}arvu.")
        return 0
    else:
        print(f"Seekord eksisid. {user_input} ei ole {number_type}arv")
        return 1


mistakes = 0
ask_even = True
while mistakes < 5:
    if ask_even:
        mistakes += ask_a_number("paaris", 0)
    else:
        mistakes += ask_a_number("paaritu", 1)
    ask_even = not ask_even
