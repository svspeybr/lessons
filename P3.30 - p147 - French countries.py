#Constantes
EXCEPTIONS = ["Belize"," Cambodga", "Mexique", "Mozambique", "Zaïre", "Zimbabwe"]
PLURALS = ["PLURALS", "Pays-Bas"]
VOWELS = ["A", "E", "I", "O", "U"]

# Vraag naar de Franse naam van het land:
country = input("Insert french country name:")

# Wat als het land een uitzondering is:
if country in EXCEPTIONS:
    country = 'le ' + country
# Wat als het land in het meervoud staat:
elif country in PLURALS:
    country = 'les ' + country
# Wat als het land begint met een klinker:
elif country[0] in VOWELS:
    country = 'l\'' + country
# Wat als de naam van het land vrouwelijk is:
elif country[len(country)-1] == 'e':
    country = 'la ' + country
# Wat als de naam van het land mannelijk is:
else :
    country = 'le '+ country

print(country)