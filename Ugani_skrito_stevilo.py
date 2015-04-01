from random import randint

sec = randint(1,60)
print("Dobrodosli!")

g = 0
while g != sec:
    g = int(raw_input("Ugani pravilno stevilko: "))

    if g == sec:
        print("Zmagal/a si! ")
    elif g > sec:
        print("Previsoka stevilka.")
    else:
        print("Premajhna stevilka")

print("Cestitam za pravilno uganjeno stevilko! ")
print("Konec igre!")


