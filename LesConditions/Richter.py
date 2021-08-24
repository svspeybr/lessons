##Programma dat voor een gegeven magnitude op de schaal van Richter,
# uitleg geeft over de schade bij een aardbeving van dergelijke magnitude.
# Versie 1:

richter = float(input("Voer een magnitude in op de schaal van Richter: "))

if richter >= 8:
    print("Merendeel van gebouwen stort in.")
else:
    if richter >= 7:
        print("Vele gebouwen zijn vernietigd.")
    else:
        if richter >= 6:
            print("vele gebouwen met enorme schade, enkele instoringen")
        else:
            if richter >= 4.5:
                print("schade aan slecht gefundeerde gebouwen")
            else:
                print("geen schade aan gebouwen")

# versie 2

richter = float(input("Voer een magnitude in: "))

if richter >= 8:
    print("Merendeel van gebouwen stort in.")
elif richter >= 7:
    print("Vele gebouwen zijn vernietigd.")
elif richter >= 6:
    print("vele gebouwen met enorme schade, enkele instoringen")
elif richter >= 4.5:
    print("schade aan slecht gefundeerde gebouwen")
else:
    print("geen schade aan gebouwen")