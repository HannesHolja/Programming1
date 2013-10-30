def main():
    dictionary = {'JTT': 'E26-27','DSR':'E24','OHI':'F221','TJS':'L22'}
    nametosearchfor = input("Anna kurssin nimi jonka haluat etsiä ")
    if nametosearchfor in dictionary:
        print(dictionary[nametosearchfor])
main()
