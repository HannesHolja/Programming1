import functions



def main():
    filename = functions.filenameasker()
    numberoflines = functions.simplelinecount(filename)
    if numberoflines > 5:
        functions.printxlines(filename, 5)
    else:
        functions.printxlines(filename, numberoflines)
main()
