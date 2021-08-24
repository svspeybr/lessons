## Backtracking:
# Bepaal voor een gegeven labyrint (= matrix bestaande uit '*' en ' ') alle mogelijke uitgangen:
# gegeven een labyrint en positie [rij, kolom] bv.
# labyrint: ['* *******', '*     * *', '* ***** *', '* * *   *', '* * *** *', '*   *   *', '*** * * *', '*     * *', '******* *']
# positie: [4, 4] (4de rij en 4de kolom)
# geef alle mogelijke paden om beginnend vanaf een gegeven positie (4,4) het labyrint te verlaten.
# --De paden zijn gevormd door een opeenvolging van 'x' tekens.

# Gebruik de code uit queens.py (pp. 578-579)

### Vervolledig waar nodig:
# main functie:
def main():
    maze = ['* *******',
            '*     * *',
            '* ***** *',
            '* * *   *',
            '* * *** *',
            '*   *   *',
            '*** * * *',
            '*     * *',
            '******* *']
    start = [4, 4]
    solve(maze, start)

## Variabelen:
# aantal rijen en kolommen van een labyrint:
COLUMNS = 9
ROWS = 9

ACCEPT = 1
CONTINUE = 2
ABANDON = 3

## Schrijf een functie 'printMaze' die gegeven een labyrint deze rij per rij uitprint
# EN eindigt met een extra lijn lege ruimte
def printMaze(maze):
    for row in maze:
        print(row)
    print("\n")

## Print alle oplossingen om het labyrint te doorlopen die uitgebreid konden worden vanuit
## een gegeven deeloplossing (= partialSolution) en de laatste nog niet bewandelde positie:

def solve(partialSolution, lastPosition):
    exam = examine(partialSolution, lastPosition)
    if exam != ABANDON:
        newPartialSolution = update(partialSolution, lastPosition)
        if exam == ACCEPT:
            printMaze(newPartialSolution)
        else:
            for newPosition in extend(lastPosition):
                solve(newPartialSolution, newPosition)

##'Examine' onderzoekt eerts (= examines) of de positie leeg is (dus gelijk aan ' '):
# Indien niet --> dan bevinden we ons in de muur of een reeds bewandeld pad --> ABANDON
# Indien wel --> controleer of
# we aan de rand van het doolhof zijn:
# Indien wel --> ACCEPT
# Indien niet --> CONTINUE

def examine(partialSolution, lastPosition):
    rowPosition = lastPosition[0]
    columnPosition = lastPosition[1]
    if partialSolution[rowPosition - 1][columnPosition - 1] != ' ':
        return ABANDON
    elif borderCheck(rowPosition, columnPosition):
        return ACCEPT
    else:
        return CONTINUE

def borderCheck(rowPosition, columnPosition):
    return rowPosition == 1 or rowPosition == ROWS or columnPosition == 1 or columnPosition == COLUMNS


def update(partialSolution, lastPosition):
    newPartialSolution = list(partialSolution)
    rowPosition = lastPosition[0]
    columnPosition = lastPosition[1]
    row = partialSolution[rowPosition - 1]
    newPartialSolution[rowPosition - 1] = row[0:columnPosition - 1] + 'x' + row[columnPosition: COLUMNS]
    return newPartialSolution

def extend(lastPosition):
    rowPosition = lastPosition[0]
    columnPosition = lastPosition[1]
    return [[rowPosition - 1, columnPosition],
            [rowPosition + 1, columnPosition],
            [rowPosition, columnPosition - 1],
            [rowPosition, columnPosition + 1]]

#start program
main()