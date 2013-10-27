from functions import bigletters,smallletters,numbercases,spaces

def main():
    filename = input("Please input the filename you wish to get info from:")
    bigs = bigletters(filename)
    smalls = smallletters(filename)
    numbers = numbercases(filename)
    spacesamount = spaces(filename)
    print("The number of uppercase letters in the file specified is: {0}".format(bigs))
    print("The number of lowercase letters in the file specified is: {0}".format(smalls))
    print("The number of numbers in the file specified is: {0}".format(numbers))
    print("The number of spaces in the file specified is: {0}".format(spacesamount))
main()
