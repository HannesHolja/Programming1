import functions

def main():
    filename = input("Input filename we'll be working with: ")
    while True:
        try:
            choice = int(functions.golfgreeter())
            if choice == 0:
                break
            elif choice == 1:
                functions.addgolfer(functions.golfername(), functions.golferpoints(), filename)
            elif choice == 2:
                functions.erasegolfer(functions.golfername(), filename)
            elif choice == 3:
                functions.editgolfer(functions.golfername(), filename)
            elif choice == 4:
                list = functions.listalllines(filename)
                for i in list:
                    print(i, end='')
                print("\n")
        except ValueError:
            print("Your choice made no sense")

main()
