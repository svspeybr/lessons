#### Caesar cipher:
### Volgende code beschrijft een programma waarbij de gebruiker een tekst ingeeft die geëncrypteerd
### of gedecodeerd wordt volgens de 'Caesarcijfer':
### Het porgramma vraagt of:
### 1) de tekst geëncrypteerd ('encrypt' of 'e') moet worden of gedecrypteerd ('decrypt' of 'd')
### 2) het Caesarcijfer (de sleutel)
### 3) de tekst die vertaald moet worden ('translatedtext'

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
MAX_KEY_SIZE = len(SYMBOLS)

## Schrijf een functie 'getMode' die de gebruiker vraagt of hij/zij een tekst wil encrypteren of decrypteren.
## Zorg dat:
# 1) de gebruiker een tekst ziet verschijnen met de vraag,
# 2) de gebruiker enkel als invoerwaarden 'encrypt' en 'decrypt' kan ingeven of de afkortingen 'e' en 'd',
# 2) (vervolg) Indien de gebruiker niet de correcte tekst ingeeft,
# 2) (vervolg) verwittigt het programma de gebruiker dat hij/zij enkel 'encrypt','e', 'decrypt', 'd' mag invoeren,
# 3) Daarna stelt het programma opnieuw de vraag uit 1)
# 4) De functie geeft het toegelaten antwoord van de gebruiker terug (via 'return')

def getMode():
    correctMode = False
    while not correctMode:
        print('Do you wish to encrypt, decrypt or hack a message?')
        mode = input().lower()
        if mode in ['encrypt', 'e', 'decrypt', 'd', 'hack', 'h']:
            correctMode = True
    return mode

#Schrijf een functie (getMessage) die de gebruiker vraagt een te vertalen bericht in te geven.
# (De functie geeft het bericht ongewijzigd terug (via return)

def getMessage():
    print('Enter your message:')
    return input()

# Schrijf een functie die gebruiker naar de 'key' (Caesarcijfer) vraagt:
# Indien een te groot of negatief cijfer wordt ingevoerd, wordt de vraag opnieuw gesteld.

def getKey():
    receivedKey = False
    while not receivedKey:
        print('Enter the key number (1-' + str(MAX_KEY_SIZE)+'):')
        key = int(input())
        if (key >= 1 and key <= MAX_KEY_SIZE):
            receivedKey = True
    return key

# Schrijf de functie getTranslatedMessage met invoerwaarden:
# mode ('encrypt' of 'decypt), message, key
# De functie vertaald het bericht (message) via de Caesar cipher methode:

def getTranslatedMessage(mode, message, key):
    #stap 2: wat als de mode 'decypt' was
    if mode[0] == 'd':
        key = -key

    #stap 1: schuif elke letter op op basis van de 'key'
    translated = ''
    for symbol in message:
        symbolIndex = SYMBOLS.find(symbol)
        #Stap 3: Wat als de tekst symbolen bevat die niet in Symbols voorkomen?
        if symbolIndex == -1:
            translated = translated + symbol
        else:
            symbolIndex = symbolIndex + key
            if symbolIndex >= len(SYMBOLS):
                symbolIndex = symbolIndex - len(SYMBOLS)
            if symbolIndex < 0:
                symbolIndex = symbolIndex + len(SYMBOLS)
            translated = translated + SYMBOLS[symbolIndex]

    return translated

def hackMessage(message):
    for key in range(MAX_KEY_SIZE):
        print(getTranslatedMessage('d', message, key + 1))

# Schrijf het programma 'main' (zonder invoerwaarden) die nu de vorige functies combineert:
# 1) de functie bevat de variabelen:  'mode', 'message' en 'key'.
# 2) de waarden van de variabelen worden gevormd door de functies getMode, getMessage en getKey op te roepen.
# 3) de functie getTranslatedMessage wordt opgeroepen en het vertaalde bericht wordt uitgeprint:

def main():
    mode = getMode()
    message = getMessage()
    # Wat als de optie 'hack' gekozen is? PAS AAN:
    if mode[0] != 'h':
        key = getKey()
    print('Your translated text is: ')
    # Wat als de optie 'hack' gekozen is? PAS AAN:
    if mode[0] != 'h':
        print(getTranslatedMessage(mode, message, key))
    else:
        hackMessage(message)
# start het programma:
main()
