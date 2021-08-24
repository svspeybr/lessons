#### Vigenère cipher:

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

def getKey():
    print('Enter the key:')
    return input()

def getTranslatedMessage(mode, message, key):

    if mode[0] == 'd':
        key = -key

    translated = ''
    keyIndex = 0 #Index om key te doorlopen
    for symbol in message:
        symbolKey = key[keyIndex]
        symbolIndex = SYMBOLS.find(symbol)
        keySymbolIndex = SYMBOLS.find(symbolKey)
        keyIndex = (keyIndex + 1) % len(key)

        if symbolIndex == -1:
            translated = translated + symbol
        else:
            symbolIndex = symbolIndex + keySymbolIndex
            if symbolIndex >= len(SYMBOLS):
                symbolIndex = symbolIndex - len(SYMBOLS)
            if symbolIndex < 0:
                symbolIndex = symbolIndex + len(SYMBOLS)
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
