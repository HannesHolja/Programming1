from functions import readlinestolist,printlisttofile
from time import sleep

def main():
    firstfile = input("Input filename for the first file")
    secondfile = input("Input filename for the second file")
    firstset = set(readlinestolist(firstfile))
    secondset = set(readlinestolist(secondfile))
    thirdset = firstset.intersection(secondset)
    print("These are all the words that are in both files: ")
    sleep(3)
    printlisttofile(firstset,'tmp.txt')
    for i in thirdset:
        if i == '':
            continue
        print(i,end=' ')
    print('\n\n')
    print("These are the words that only appear in the first file")
    sleep(3)
    thirdset = firstset.difference(secondset)
    for i in thirdset:
        if i == '':
            continue
        print(i,end=' ')

    print('\n\n')
    print("These are the words that only appear in one of the files, not both at the same time")
    sleep(3)
    thirdset = firstset.symmetric_difference(secondset)
    for i in thirdset:
        if i == '':
            continue
        print(i,end=' ')

main()
