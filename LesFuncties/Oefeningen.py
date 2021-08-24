# module voor het getal pi te verkrijgen (en functies als sin(), cos()...)
import math

def cilinderVol(r, h):
    return math.pi * (r ** 2) * h


def cilinderOpp(r, h):
    mantelOpp = 2 * math.pi * r * h
    grondvlakOpp = math.pi * (r ** 2)
    return mantelOpp + 2 * grondvlakOpp
# abs

def telWoorden(string):
    stringLijst = list(string)
    aantal = 1
    for teken in stringLijst:
        if teken == " ":
            aantal += 1
    return aantal

print(telWoorden("Marie heeft een goudvis"))
### EXTRA 1: De functie telWoorden is niet ideaal:
# vind voorbeelden van strings waarvoor telWoorden meer woorden aangeeft dan er zijn.

### (***) We kunnen telWoorden() als volgt verbeteren:
# gebruik een variabele 'eindeWoord' (einde van een woord == gebied na het woord met enkel spaties) zodat...
# - als eindeWoord == True:
#       'aantal' woorden ENKEL toeneemt van zodra een niet-spatie teken gevonden wordt (dus een nieuw woord)
# - als eindeWoord == False: (een woord wordt doorlopen)
#        zet eindeWoord = True van zodra een spatie gevonden is op het einde van het woord.

def telWoorden2(string):
    stringLijst = list(string)
    aantal = 0
    eindeWoord = True
    for teken in stringLijst:
        if eindeWoord:
            if teken != " ": # eerste letter van nieuw woord gevonden
                aantal += 1
                eindeWoord = False # Zet op False: nieuw woord gevonden
        elif teken == " ": #einde van het woord gevonden
            eindeWoord = True
    return aantal

print(telWoorden2("  Marie heeft  een enorme inktvis  "))

#### EXTRA 2: Maak een tabel met...
### - in de eerste kolom de waarde van 'teken',
### - in de tweede kolom de waarde van 'eindeWoord' (True of False),
### - in de derde kolom de waarde van 'aantal',
### bij het doorlopen van de for -lus in telWoorden2() voor de string:
### "  Marie heeft  een inktvis " (Let op de spaties!)

#Test for changes
def commit(woord):
    for letter in woord:
        print(letter)