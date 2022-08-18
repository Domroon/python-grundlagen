import time


def führe_strategie_durch():
    print("Du werkelst den ganzen Tag...")
    print("Deine Strategie ist super. Du kannst die Prinzessin retten!")


def ergreife_entführer():
    print("Das war unüberlegt...")
    print("Mit einem kräftigen Schlag erledigt dich der Entführer.")
    print("Du bist Tod.")


def main():
    print('Hier wird eine Geschichte erzählt')
    print()
    print('Oh nein! Die Prinzessin wird gerade entführt')
    eingabe = input('1 - Ich renne sofort hinterher\n2 - Ich denke erstmal nach\n')
    while True:
        if int(eingabe) == 1:
            print("Du schaffst es den Entführer zu packen.")
            time.sleep(1)
            ergreife_entführer()
            break
        elif int(eingabe) == 2:
            print("Du entwickelst eine ausgeklügelte Strategie.")
            time.sleep(1)
            führe_strategie_durch()
            break
        else:
            print("Falsch Eingabe. Versuhe es nochmal.")
            eingabe = input('1 - Ich renne sofort hinterher\n2 - Ich denke erstmal nach\n')

if __name__ == '__main__':
    main()