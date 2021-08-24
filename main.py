
# Exercise P 3.28 - p146: Roman numbers - if statements

roman = ''
print('Voer een natuurlijk getal in strikt tussen 0 en 4000:')
italic = int(input())
multiple = 0

if italic >= 1000 :
    multiple = italic // 1000
    roman = roman + multiple * 'M'
    italic = italic - multiple * 1000

if italic >= 100 :
    multiple = italic // 100
    italic = italic - multiple * 100
    if multiple >= 9 :
        roman = roman + 'CM'
    elif multiple >= 5 :
        roman = roman + (multiple - 5) * 'C' + 'D'
    elif multiple == 4 :
        roman = roman + 'DC'
    else :
        roman = roman + multiple * 'C'

if italic >= 10:
    multiple = italic // 10
    italic = italic - multiple * 10
    if multiple >= 9:
        roman = roman + 'XC'
    elif multiple >= 5:
        roman = roman + (multiple - 5) * 'X' + 'L'
    elif multiple == 4:
        roman = roman + 'LX'
    else :
        roman = roman + multiple * 'X'

if italic > 0:
    multiple = italic // 1
    italic = italic - multiple * 1
    if multiple >= 9:
        roman = roman + 'IX'
    elif multiple >= 5:
        roman = roman + (multiple - 5) * 'I' + 'V'
    elif multiple == 4:
        roman = roman + 'VI'
    else :
        roman = roman + multiple * 'I'

print('Omgezet in Romeinse cijfers: ' + roman)