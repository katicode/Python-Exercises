# Simple calculator (in Finnish)

import math

luku1 = input("Anna ensimmäinen luku: ")
luku2 = input("Anna toinen luku: ")
luku1 = int(luku1)
luku2 = int(luku2)

while True:
        print("(1) + \n(2) - \n(3) * \n(4) /\n(5)sin(luku1/luku2)\n(6)cos(luku1/luku2)\n(7)Vaihda luvut\n(8)Lopeta")
        print("Valitut luvut: ",luku1,luku2)

        valinta = input("Tee valinta (1-8): ")

        if valinta == "1":
                print("Tulos on: ",luku1+luku2)
        elif valinta == "2":
                print("Tulos on: ",luku1-luku2)
        elif valinta == "3":
                print("Tulos on: ",luku1*luku2)
        elif valinta == "4":
                print("Tulos on: ",luku1/luku2)
        elif valinta == "5":
                print("Tulos on: ",math.sin(luku1/luku2))
        elif valinta == "6":
                print("Tulos on: ",math.cos(luku1/luku2))
        elif valinta == "7":
                luku1 = input("Anna uusi ensimmäinen luku: ")
                luku2 = input("Anna uusi toinen luku: ")
                luku1 = int(luku1)
                luku2 = int(luku2)
        elif valinta == "8":
                break
        else:
                print("Valintaa ei tunnistettu.")
