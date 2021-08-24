# Constante variabelen (= worden niet gewijzigd als de code wordt uitgevoerd!)
PERC = 0.1
PERC_EX = 0.25
SINGLE_LIM = 32000.0
GEHUWD_LIM = 64000.0

# Vraagt de gebruiker naar inkomen en burgelijke staat:
bs = input("Vul 's' in voor single, 'g' voor gehuwd: ")
inkomen = int(input("Vul uw inkomen in: "))

#Bereken belastingen
belas = 0.0
belas_ex = 0.0

if bs == "s":
    if inkomen <= SINGLE_LIM:
        belas = inkomen * PERC
    else:
        belas = SINGLE_LIM * PERC
        belas_ex = (inkomen -SINGLE_LIM) * PERC_EX
else:
    if inkomen <= GEHUWD_LIM:
        belas = inkomen * PERC
    else:
        belas = GEHUWD_LIM * PERC
        belas_ex = (inkomen - GEHUWD_LIM) * PERC_EX

totaal_belas = belas + belas_ex
print("U moet", totaal_belas, "aan de staat.")