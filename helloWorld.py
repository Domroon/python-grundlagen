import time
from random import randint

while True:
    print("Hello World!")
    nummer = randint(1, 42)
    print(f'Hier eine Zufallszahl: {nummer}')
    print()
    time.sleep(1)