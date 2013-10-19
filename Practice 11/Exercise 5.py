from usefulFunctions import isinlist, readtolist

def main():
        print("How to use this program:")
        print("To input a girl name and check if it's in the list of most used finnish girl names press 1")
        print("To input a boy name and check if it's in the list of most used finnish boy names press 2")
        while True:
            try:
                choice = int(input("Input your choice: "))
                if choice == 1:
                    girlnames=readtolist('tytot.txt')
                    value = isinlist(input("Give a girl's name: "),girlnames)
                    if value == True:
                        print("The name was found from the girls list")
                    elif value == False:
                        print("The name was not found from the girls list")
                if choice == 2:
                    boynames=readtolist('pojat.txt')
                    value = isinlist(input("Give a boy's name: "),boynames)
                    if value == True:
                        print("The name was found from the boys list")
                    elif value == False:
                        print("The name was not found from the boys list")
            except ValueError:
                print("Your choice made no sense")
                continue


main()
