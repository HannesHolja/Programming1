import random

def Laske_summa(paino):
    rahamaara = paino*40726
    return rahamaara

def Laske_pinta_ala(raha):
    pinta_ala = raha / 30000
    return pinta_ala

def Laske_toffee_kilot(raha):
    kiloina = raha / 5
    return kiloina

def Laske_peruspalkka(tunnit, tuntipalkka):
    raha = tunnit * tuntipalkka
    return raha

def Laske_ylityokorvaus(tunnit,tuntipalkka):
    ylityotunnit = tunnit -40
    raha = ylityotunnit*1.5*tuntipalkka
    return raha

def vertaaja(arvaus, luku):
    if arvaus < luku:
        print("Arvauksesi oli pienempi kuin koneen arpoma luku")
    else:
        print("Arvauksesi oli suurempi kuin koneen arpoma luku")
def saksetvaipaperi():
    koneenvalinta=random.randint(1,3)
    return koneenvalinta

def kayttajanvalinta():
    valinta = int(input("Valitse numero vÃ¤liltÃ¤ 1-3. 1 = kivi, 2 = sakset, 3 = paperi"))
    return valinta
