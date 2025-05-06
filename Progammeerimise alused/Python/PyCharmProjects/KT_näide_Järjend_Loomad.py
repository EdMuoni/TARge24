"""
JÄRJEND

v Koosta järjend loomad
v Küsi kasutajalt looma nimesid
v Kui seda nime pole järjendis, siis lisa see
kui järjendis on loom, mis algab sama tähega kui sisestatud nimi lõppes, siis kirjuta see ekraanile,
ja küsi uus loom, kui ei ole, siis küsi kasutajalt uus loom, mis algab tähega, millega ellmine lõppese.

KORDUS
Küsi kasutajalt kordamööda paaris ja paarituid arve. Kontrolli ja kuva ekraanile, et sisetatakse õige arv.
Lõpeta programm, kui kasutaja on 5 korda eksinud.
"""

animal_list = []


def get_animal(first_char):
    for animal in animal_list:
        if animal.startswith(first_char):
            return animal


print("Koostame loomade jada, kus iga järgmine algab eelmise lõputähega")
while True:
    user_input = input("Siesta looma nimi: ").lower()
    if user_input not in animal_list:
        animal_list.append(user_input)
    else:
        print("Selle looma oled juba sisestanud. \nNägemist!")
        break
    matching_animal = get_animal(user_input[-1])
    if matching_animal is None:
        print(f"Sisesta loom, mis algab '{user_input[-1]}'-tähega")
    else:
        print(f"Me leidsime looma, mis algab sinu sisestatud looma lõpptähega : {matching_animal}")

print("Koostatud loomade nimekiri: ", ",".join(animal_list))
