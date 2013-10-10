def simplelinecount(filename):
    lines = 0
    with open(filename) as file:
        for line in file:
            lines += 1
    return lines

def filenameasker():
    filename = input("Give me a file name: ")
    return filename

def printxlines(filename, numberoflines):
    i = 0
    with open(filename) as file:    #With-lause osaa sulkea tiedostokahvan automaattisesti
        for line in file:   #Sitten voidaan kÃ¤yttÃ¤Ã¤ line-operaatiota-> Koodi helpottuu
            if i < numberoflines:
                print(line)
                i += 1
            else:
                break

def listalllines(filename):
    numberlist = []
    try:
        with open(filename) as file:
                for line in file:
                    numberlist.append(line)
    except IOError:
            print("Filename specified was not found")
    except ValueError:
            print("Filename specified does not contain numerical data")
    return numberlist

def arithmeticmean(numberlist):
    mean = 0
    howmanynumbers = 0
    for i in numberlist:
        mean += int(i)
        howmanynumbers += 1
    return mean/howmanynumbers
