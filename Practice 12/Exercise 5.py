from functions import readlinestolist,longestword,shortestword,userschars,numbers

def main():
    returnvalue = False
    while returnvalue == False:
        filename = input("Input the filename you wish to work with")
        returnvalue = readlinestolist(filename)
    loops = True
    while loops == True:
        print("How to use this program:")
        print("Press 1 to find the longest word")
        print("Press 2 to find the shortest word")
        print("Press 3 to input characters and see which word has the most of your inputted characters")
        print("Press 4 to find out which words are simply numbers")
        print("Press 5 to quit")
        choice = int(input("Input your choice:"))
        if choice == 1:
            longestone = longestword(returnvalue)
            print("The longest word in your file is: {0}".format(longestone))
        if choice == 2:
            shortestone = shortestword(returnvalue)
            print("The shortest word in your file is: {0}".format(shortestone))
        if choice == 3:
            chars = input("Input your characters:")
            print("The word which contains the most of your inputted characters is: {0}".format(userschars(chars, returnvalue)))
        if choice == 4:
            print("Found {0} numbers from your file. The numbers are {1}".format(len(numbers(returnvalue)),numbers(returnvalue)))
        if choice == 5:
            print("Stopping program.....")
            loops=False
main()
