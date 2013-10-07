import laskimet


def main():
    tunnit = float(input("Ilmoita työtuntisi "))
    tuntipalkka = float(input("Anna tuntipalkkasi "))
    if tunnit <= 40:
        peruspalkka = laskimet.Laske_peruspalkka(tunnit, tuntipalkka)
        print("Peruspalkkasi työviikolta on: {0:.2f} euroa\nEt tehnyt ylityötunteja joten et saa ylityökorvausta\nYhteensä palkkasi on siis: {0:.2f} euroa".format(peruspalkka))
    else:
        peruspalkka = laskimet.Laske_peruspalkka(tunnit, tuntipalkka)
        ylityokorvaus = laskimet.Laske_ylityokorvaus(tunnit, tuntipalkka)
        print("Peruspalkkasi työviikolta on: {0:.2f} euroa\nTeit ylityötunteja {1}, joista sait ylityökorvausta: {2}\nYhteensä palkkasi on siis: {3:.2f} euroa".format(peruspalkka,tunnit-40, ylityokorvaus, ylityokorvaus + peruspalkka))


main()
