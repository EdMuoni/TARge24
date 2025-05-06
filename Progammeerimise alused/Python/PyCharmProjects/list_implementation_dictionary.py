"""
Lihtsa sõnaraamatu jaoks koosta neli järjendit (arv, eesti, inglise, itaalia)
sisuga: arv - 1, 2, 3, 4
eesti - üks, kaks, kolm, neli inglise - one, two, three, four itaalia - uno, due, tre, quattro

Väljasta kõik elemendid tabelina ekraanile: 1 - üks - one - uno 2 - kaks - two - due ...

Lisa arvude ja eesti järjendile veel kaks elementi.
Kontrolli, kas itaalia sõnade järjendis eksiteerib element 'tre'
Väljasta kõigi nelja järjendi elemendid tähestikulises järjekorras kasvavalt.
"""

arv = ["1", "2", "3", "4"]
eesti = ["üks", "kaks", "kolm", "neli"]
inglise = ["one", "two", "three", "four"]
itaalia = ["uno", "due", "tre", "quattro"]

print("arv - eesti - inglise - itaalia")
for i in range(min(len(arv), len(eesti), len(inglise), len(itaalia))):
    print(f"{arv[i]:>3} - {eesti[i]:<5} - {inglise[i]:<7} - {itaalia[i]}")

arv.append("5")
arv += ["6"]
eesti += ["viis", "kuus"]

if "tre" in itaalia:
    print(f"'tre' on itaalia järjends postitsioonil {itaalia.index('tre')}")
else:
    print(f"'tre' pole itaalia järjendis")

sorted_list = sorted(arv + eesti + inglise + itaalia)
for value in sorted_list:
    print(value)
