'''Harjoitus HA 16, tehtävä 5
Moduuli korttipakka '''

def main():
    kortit = luo_pakka()
    print(kortit)
    for kortti in kortit:
        print(kortit[kortti], end = ' ')


def luo_pakka():
    pakka = { 'Pata ässä' : 1, 'Pata 2' : 2, 'Pata 3' : 3, 'Pata 4': 4, 'Pata 5' : 5, 'Pata 6' : 6, 'Pata 7' : 7, 'Pata 8' : 8, \
              'Pata 9' : 9, 'Pata 10' : 10, 'Pata jätkä' : 11, 'Pata rouva' : 12, 'Pata kurko' : 13 , \
              'Hertta ässä' : 1, 'Hertta 2' : 2, 'Hertta 3' : 3, 'Hertta 4': 4, 'Hertta 5' : 5, 'Hertta 6' : 6, 'Hertta 7' : 7, 'Hertta 8' : 8, \
              'Hertta 9' : 9, 'Hertta 10' : 10, 'Hertta jätkä' : 11, 'Hertta rouva' : 12, 'Hertta kurko' : 13 , \
              'Risti ässä' : 1, 'Risti 2' : 2, 'Risti 3' : 3, 'Risti 4': 4, 'Risti 5' : 5, 'Risti 6' : 6, 'Risti 7' : 7, 'Risti 8' : 8, \
              'Risti 9' : 9, 'Risti 10' : 10, 'Risti jätkä' : 11, 'Risti rouva' : 12, 'Risti kurko' : 13 , \
              'Ruutu ässä' : 1, 'Ruutu 2' : 2, 'Ruutu 3' : 3, 'Ruutu 4': 4, 'Ruutu 5' : 5, 'Ruutu 6' : 6, 'Ruutu 7' : 7, 'Ruutu 8' : 8, \
              'Ruutu 9' : 9, 'Ruutu 10' : 10, 'Ruutu jätkä' : 11, 'Ruutu rouva' : 12, 'Ruutu kurko' : 13 }
    return pakka

        
    
main()
