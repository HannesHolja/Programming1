from functions import flowcontrol,dumpdictionary,loaddictionary

def main():
    osoitteet = {}
    osoitteet = loaddictionary()
    flag = True
    while flag == True:
        print("Names currently in the dict: {0}".format([i for i in osoitteet.keys()])) #For demonstration purposes only, delete if this gets too big
        print("How to use this program:")
        print("Press 1 to search for an email address")
        print("Press 2 to add a new email address")
        print("Press 3 to change an email address")
        print("Press 4 to delete an email address")
        print("Press 5 to quit")
        choice = int(input("Input your choice:"))
        tmp = flowcontrol(choice,osoitteet)
        if tmp == False:
            dumpdictionary(osoitteet,'osoitteet.dat')
            flag = False
        elif tmp != None:
            osoitteet = tmp



main()
