import laskimet
import random

def main():
    lukumaara = 0
    luku = random.randint(1,100)
    while True:
        arvaus = int(input("Arvaa lukua väliltä 1-100 "))
        lukumaara += 1
        if arvaus == luku:
            print("Arvasit oikein {0}:llä arvauksella!".format(lukumaara))
            break
        else:
            laskimet.vertaaja(arvaus, luku)
            continue

main()
