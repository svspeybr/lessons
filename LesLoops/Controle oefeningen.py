integer = 1
while integer < 51:
    if integer % 4 == 0 or integer % 5 == 0 and not(integer % 7 == 0):
        print(integer)
    integer += 1