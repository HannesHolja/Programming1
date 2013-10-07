import laskimet

kivi = 1
paperi = 2
sakset = 3
koneenvoitot = 0
kayttajanvoitot = 0

nimet = {kivi: "Kivi", paperi: "Paperi", sakset: "Sakset"}
saannot  = {kivi: sakset, paperi: kivi, sakset: paperi} #Sanakirja jota käytetään sääntöjen muotoiluun

def main():
    global koneenvoitot, kayttajanvoitot, nimet
    while True:
        print("Käyttäjän voitot: {0}, Tietokoneen voitot {1}".format(kayttajanvoitot, koneenvoitot))
        kayttajan = laskimet.kayttajanvalinta()
        koneen = laskimet.saksetvaipaperi()
        print("Tietokone valitsi {0}".format(nimet[koneen]))
        if kayttajan == koneen:
            print("Se on muuten tasapeli!")
        elif saannot[kayttajan]==koneen:
            print("Voitit pelin!")
            kayttajanvoitot += 1
        else:
            print("Tietokone voitti!")
            koneenvoitot+=1
        if kayttajanvoitot == 3:
            print("Voitit koko pelin!")
            break
        elif koneenvoitot == 3:
            print("Tietokone voitti koko pelin!")
            break
main()

