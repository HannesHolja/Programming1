import functions

def main():
    numberlist = functions.listalllines(functions.filenameasker())
    print("Numbers found in the file: ")
    for i in numberlist:
        print(int(i), end=' ')
    print("\nArithmetic mean for the numbers found in the file is {0}".format(functions.arithmeticmean(numberlist)))
main()
