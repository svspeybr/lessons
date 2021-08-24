import random
import time

def toonIntro():
    print("Je bevindt je in een land vol draken. Voor jou zie je twee grotten:\n In de ene grot, " +
          "is een vriendelijke draak die zijn schat met jou wil delen.\n In de andere grot is een " +
          "hebzuchtige en hongerige draak die je zal opeten.")

def kiesGrot():
    grot = ""
    while grot != 1 and grot != 2:
        grot = int(input("Welke grot ga je binnen? (1 of 2): "))
    return grot

def controleGrot(grot):
    print("Je nadert de grot...")
    time.sleep(2)
    print("Het is hier donker en akelig...")
    time.sleep(2)
    print("Een gigantische draak verschijnt voor jou! Hij opent zijn kaken en...")
    time.sleep(2)

    vriendelijkeGrot = random.randrange(1, 3)

    if vriendelijkeGrot == grot:
        print("Geeft jou haar schat!")
    else:
        print("Eet je op in één hap!")

def main():
    spelOpnieuw = "ja"
    while spelOpnieuw == "ja" or spelOpnieuw ==  "j":
        toonIntro()
        grot = kiesGrot()
        controleGrot(grot)

        spelOpnieuw = input("Wil je opnieuw spelen? (ja of nee) ")

main()