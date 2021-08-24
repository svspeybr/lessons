# Verwissel de letters bij een gegeven woord:
import random

woord = input("Voer een woord in: ")
lengte = len(woord)
iteraties = 0

while iteraties < lengte:
    # lengte -1 is de index van de laatste letter, randrange gaat van 0 TOT 'lengte -1'
    i = random.randrange(0, lengte - 1)
    j = random.randrange(i + 1, lengte)
    begin = woord[0 : i]
    midden = woord[i + 1: j]
    einde = woord[j + 1: lengte]
    woord = begin + woord[j] + midden + woord[i] + einde
    # volgende iteratie
    iteraties += 1

print(woord)