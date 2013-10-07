######Okay, lets give the same idea a go with some lists######
import os


def isit(name, amount, file):
    found = False
    index, y = 0,0
    OldFile = open(file, 'r')
    values = []
    values = OldFile.readlines()
    filecloser(OldFile)
    for i in values:
        i = i.rstrip('\n')
        if i == name:
            values[y+1] = str(amount) + '\n'
            found = True
        y+=1
    if found:
        index = 0
        OldFile = open(file, 'w')
        for x in values:
            OldFile.write(values[index])
            index+=1
        print("The file was altered in a way you specified")
    else:
        print("The instance was not found")
    filecloser(OldFile)

def filecloser(fileobject):
    fileobject.close
isit('cacao', 16, 'file.txt')