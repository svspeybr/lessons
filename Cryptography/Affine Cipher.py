#### Affine cipher:

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
MAX_KEY_SIZE = len(SYMBOLS)

def getMode():
    correctMode = False
    while not correctMode:
        print('Do you wish to encrypt or decrypt a message?')
        mode = input().lower()
        if mode in ['encrypt', 'e', 'decrypt', 'd']:
            correctMode = True
    return mode

def getMessage():
    print('Enter your message:')
    return input()

# testIfPrime? --> Voorgaande oefening
def communDivisor(a, b):
    if b == 0:
        return a
    else:
        rest = a % b
        return communDivisor(b, rest)


def testIfPrime(number):
    if number > 1:
        for divider in range(2, number):
            if number % divider == 0:
                return False
        return True
    return False

def getKey():
    receivedKey = False
    while not receivedKey:
        print('Enter the first key primenumber (1-' + str(MAX_KEY_SIZE)+'):')
        firstkey = int(input())
        if (firstkey >= 1 and firstkey <= MAX_KEY_SIZE and communDivisor(firstkey, len(SYMBOLS)) == 1):
            print('Enter the second key (1-' + str(MAX_KEY_SIZE) + '):')
            secondkey = int(input())
            if (firstkey >= 1 and firstkey <= MAX_KEY_SIZE):
                receivedKey = True
    return [firstkey, secondkey]

def getTranslatedMessage(mode, message, key):

    if mode[0] == 'd':
        key = -key

    translated = ''
    for symbol in message:
        symbolIndex = SYMBOLS.find(symbol)
        if symbolIndex == -1:
            translated = translated + symbol
        else:
            symbolIndex = (key[0] * symbolIndex + key[1]) % len(SYMBOLS)
            translated = translated + SYMBOLS[symbolIndex]
    return translated


def main():
    mode = getMode()
    message = getMessage()
    key = getKey()
    print('Your translated text is: ')
    print(getTranslatedMessage(mode, message, key))

# start het programma:
main()

