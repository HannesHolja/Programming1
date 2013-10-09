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
    with open(filename) as file:
        for line in file:
            if i < numberoflines:
                print(line)
                i += 1
            else:
                break
