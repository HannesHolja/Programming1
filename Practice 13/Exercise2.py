from functions import readlinestolist


def main():
    filetrueflag = False
    filename = input("Input the filename: ")
    listofwords = set(readlinestolist(filename))
    for i in listofwords:
        print(i,end=' ')
main()

