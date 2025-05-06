"""Esitan funktsioonid."""


def func():
    """Func väljakutsumisel kirjutab I´m inside the function."""
    print("I´m inside the function")  # I am inside the function


def my_name_is(name):
    """My name is ..."""
    print(f"My name is {name}")  # My name is Mari


def sum_six(num):
    """Funktsiooon peab tagastama(return) number 6 ja funktsiooni sisendi summa."""
    num = int(num)
    return num + 6  # --> 12


def sum_numbers(a, b):
    """Funktsioon peab tagastama(return) sisendite summa."""
    a = int(a)
    b = int(b)
    return a + b  # -->10

    print(sum_numbers(5, 5))  # -->10


def usd_to_eur(amount_usd):
    """Funktsioon töötab nii, et kui sisendiks on rahasumma dollarites, tagastab funktsioon summa eurodes."""
    exchange_rate = 0.80
    amount_eur = amount_usd * exchange_rate
    return amount_eur  # --> 80
