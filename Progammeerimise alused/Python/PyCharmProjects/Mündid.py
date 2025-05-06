"""Euromüntide seerias on kuus erineva nimiväärtusega senti: 1 sent, 2 senti, 5 senti, 10 senti, 20 senti, 50 senti. Sendid väärtustega 1, 2 ja 5 on pronksikarva (vasega kaetud teras), sendid väärtustega 10, 20 ja 50 on kullakarva (vasesulam, mis sisaldab alumiiniumi, tsinki ja tina, nn Nordic Gold).
Peres on kombeks, et pronksikarva mündid panna hoiupõrsasse.
Müntide andmed on failis kirjas nii, et iga mündi väärtus on eraldi real. Näiteks failis mündid.txt nii:
1
20
20
5
50
2
2
1
Esmalt koostada funktsioon pronksikarva_summa, mis
•	võtab argumendiks täisarvude järjendi ja
•	tagastab selles järjendis olevate arvude 1, 2 ja 5 summa.
Näide funktsiooni tööst
# >>> pronksikarva_summa([2, 1, 10, 5, 50, 20, 20])
8
Teiseks koostada programm, mis
1.	küsib kasutajalt selle faili nime, milles asuvad sentide väärtused;
2.	moodustab täisarvujärjendi vastavast failist loetud väärtustest;
3.	rakendab funktsiooni pronksikarva_summa, andes argumendiks koostatud täisarvujärjendi;
4.	väljastab ekraanile tulemuseks saadud kõikide pronksikarva sentide summa.
"""


def bronxe_sum(coins):
    """Add together coins with value of 1, 2 or 5 and return the sum."""
    result = 0
    for coin in coins:
        if coin in [1, 2, 5]:
            result += coin  # result = result + coin
    return result


if __name__ == '__main__':
    print(bronxe_sum([2, 1, 10, 5, 50, 20, 20]))


def bronxe_sum(coins):
    """Add together coins with value of 1, 2 or 5 and return the sum."""
    result = []
    for coin in coins:
        if coin in [1, 2, 5]:
            result += [coin]  # result = result + coin
    return result


if __name__ == '__main__':
    print(bronxe_sum([2, 1, 10, 5, 50, 20, 20]))


def bronxe_sum(coins):
    """Add together coins with value of 1, 2 or 5 and return the sum."""
    result = []
    for coin in coins:
        if coin in [1, 2, 5]:
            result += [coin]  # result = result + coin
    return result


if __name__ == '__main__':
    print(sum(bronxe_sum([2, 1, 10, 5, 50, 20, 20])))


def bronxe_sum(coins):
    """Add together coins with value of 1, 2 or 5 and return the sum."""
    result = []
    for coin in coins:
        if coin == 1 or coin == 2 or coin == 5:
            result += [coin]  # result = result + coin
    return result


if __name__ == '__main__':
    print(bronxe_sum([2, 1, 10, 5, 50, 20, 20]))
