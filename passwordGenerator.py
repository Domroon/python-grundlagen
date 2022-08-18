import string
from random import randint


def generiere_zufallszeichen(alle_zeichen):
    pos = randint(0, len(alle_zeichen))
    return alle_zeichen[pos]
        

def main():
    buchstaben = string.ascii_letters
    sonderzeichen = string.punctuation
    alle_zeichen = buchstaben + sonderzeichen
    länge = input('Bitte Passwortlänge eingeben: ')

    passwort = ""
    for _ in range(0, int(länge)):
        zeichen = generiere_zufallszeichen(alle_zeichen)
        passwort = passwort + zeichen
    
    print(f'Generiertes Passwort: {passwort}')
        


if __name__ == '__main__':
    main()