from random import randint

print('Dies ist eine Zahlenratespiel')
print('Du hast drei Versuche die Nummer zu eraten')

versuche = 3
zufallsnum = randint(0, 10)

while True:
    if versuche == 0:
        print('Du hast Verloren.')
        break
    eingabe = input('Bitte Nummer raten (1-10): ')
    if int(eingabe) == zufallsnum:
        print('Du hast gewonnen!')
        break
    if int(eingabe) > zufallsnum:
        print(f'Die Nummer ist kleiner als {eingabe}')
        versuche = versuche - 1
    if int(eingabe) < zufallsnum:
        print(f'Die Nummer ist größer als {eingabe}')
        versuche = versuche - 1
    print()

print('Programm beendet')
    
