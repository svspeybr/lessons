# Vraag drie getallen op (werk met variabelen a, b,c )
a = float(input("Geef een getal:"))
b = float(input("Geef een tweede getal:"))
c = float(input("Geef een derde getal:"))

# Werk met een 4de variabele 'maximum' die de grootste waarde bijhoudt
maximum = a
# Vergelijk nu b en c met maximum( =a) en pas maximum aan indien nodig.
if b > maximum:
    maximum = b
if c > maximum:
    maximum = c

# Toon het grootste getal aan de gebruiker.
print("Het grootste getal is", maximum)