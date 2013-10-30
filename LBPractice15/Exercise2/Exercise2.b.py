def main():
    dictionary = {'JTT':'Opetusaika: Kello 8:00','DSR':'12:00','OHI':'10:00','TJS':'14:00'}
    nametosearchfor = input("Anna kurssin nimi jonka haluat etsiÃ¤ ")
    if nametosearchfor in dictionary:
        print("Sinun täytyy mennÃ¤ kouluun kello:")
        print(dictionary[nametosearchfor])
main()
