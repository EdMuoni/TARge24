"""
Leia kolmest arvust suurim
"""

arv1 = int(input("Sisesta esimene täisarv:"))
arv2 = int(input("Sisesta teine täisarv:"))
arv3 = int(input("Sisesta kolmas täisarv:"))

if arv1 > arv2:
    if arv1 > arv3:
        print(str(arv1) + " on suurim")
    else:
        print(str(arv3) + " on suurim")
else:
    if arv3 > arv2:
        print(str(arv3) + " on suurim")
    else:
        print(str(arv2) + " on suurim")
