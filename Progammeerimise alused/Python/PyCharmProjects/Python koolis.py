"""Koosta programm, mis küsib kasutajalt 10 korda arve ja väljastab seejärel nende arvude summa. Täienda seda programmi
nii, et kasutajalt küsitakse arve seni, kuni kasutaja enam uut arvu ei sisesta, vaid vajutab lihtsalt sisestusklahvi.
Proovige seda ülesannet lahendada nii while- kui for-tsükliga."""


def sum_ten_user_input_numbers():
    result = 0
    print("Summeerin kümme sinu sisestatud täisarvu")
    for i in range(10):
        input_text = input(f"Sisesta {i + 1} täisarv: ")
        input_number = int(input_text)
        print(f"{result}+{input_text}=", end="")
        result = result + input_number
        print(result)
    print("Sisestatud arvude summa on " + str(result))


if __name__ == "__main__":
    sum_ten_user_input_numbers()
