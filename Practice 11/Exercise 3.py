from usefulFunctions import alphabetize,printall,userinput,deletenamefromlist,editnameinlist

def main():
    namelist = []
    print("This is a program that allows you to edit a list")
    print("To add a name to the list press 1\nTo delete a name from the list press 2")
    print("To change a name from the list press 3\nTo alphabetize the list press 4\nTo print out the list press 5")
    while True:
        choice = userinput()
        if choice == 1:
            namelist.append(input("Please input the name you wish to append to the list: "))
        elif choice ==2:
            deletenamefromlist(namelist,input("Please input the name you wish to delete from the list: "))
        elif choice == 3:
            nametoedit = editnameinlist(namelist,input("Please input the name you wish to edit in the list: "))
        elif choice == 4:
            namelist =alphabetize(namelist)
        elif choice == 5:
            printall(namelist)



main()

