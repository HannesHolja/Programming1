import laskimet


def main():
    paino = float(input("Anna painosi kiloina "))
    raha = laskimet.Laske_summa(paino)
    print("Painollasi ansaitset {0:.2f} euroa.".format(raha))
    valinta = input("Tahdotko ostaa rahalla maata (m) vai toffeeta(t)? ")
    if valinta == 'm' :
        print("T'ällä hinnalla saat {0:.2f} hehtaaria maata".format(laskimet.Laske_pinta_ala(raha)))
    else:
        print("Tällä hinnalla saat {0:.2f} kiloa toffeeta!".format(laskimet.Laske_toffee_kilot(raha)))
main()
