import functions
def main():
    choice = functions.greeter()
    if choice == 1:
        randomints = functions.randomgenerator(functions.amountofnumbers())
        functions.printlisttofile(randomints,functions.filenameasker())
    elif choice == 2:
        numberlist = functions.listalllines(functions.filenameasker())
        for i in numberlist:
            print(int(i), end=' ')
    else:
        print("You made a choice that made no sense")
main()
