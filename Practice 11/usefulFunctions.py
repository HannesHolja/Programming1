import time
import random

def greetingsjokeri():
    print("This program gives you a pseudo-random line for Veikkaus-game Jokeri\nHere it goes!")

def randomnumberlist():
    numberlist = []
    for i in range(1,8):
        numberlist.append(random.randint(1,9))
    return numberlist

def nameofnumber(i):
    numbername = ['first','second','third','fourth','fifth','sixth','seventh']
    return numbername[i-1]

def GreeterWeather():
    print("This program allows you to input values of this year for rain in millimeters")


def nameofmonth():
    nameofmonth = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November',  'December']
    rainlist = []
    x = 0
    while True:
        try:
                rainlist.append(int(input("Input rain value in millimeters for month {0}".format(nameofmonth[x]))))
                if x <len(nameofmonth)-1:
                    x += 1
                    continue
                else:
                    break
        except ValueError:
            print("You didn't input a proper value")
            continue
    return rainlist
def greatest(rainlist):
    greatest = max(rainlist)
    return greatest
def smallest(rainlist):
    minimum = min(rainlist)
    return minimum

def sum(rainlist):
    overall = 0
    for i in rainlist:
        overall += i
    return overall

def median(rainlist):
    lenght = len(rainlist)
    median = sum(rainlist)/lenght
    return median
def findindex(rainlist,whattosearch):
    index = rainlist.index(whattosearch)
    return index
def nameforfunctions(index):
    nameofmonth = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November',  'December']
    name = nameofmonth[index]
    return name

def alphabetize(namelist):
    equalize, greater, lesser = [], [], []
    if len(namelist) > 1:   #Just checking if the namelist is already divided to only 1 entity
        pivot = namelist[0]
        for i in namelist:
            if i < pivot:
                lesser.append(i)
            elif i >pivot:
                greater.append(i)
            else:
                equalize.append(i)
        return alphabetize(lesser)+alphabetize(equalize)+alphabetize(greater) ##Lets call these new lists recursively with the same function to sort them
    else:
        return namelist                 #Since the lenght is now 1 list is already sorted, lets return through the recursion loops

def printall(namelist):
    for i in namelist:
        print(i)
    print('\n')
def userinput():
    while True:
        try:
            choice = int(input("Make your choice "))
            break
        except ValueError:
            print("Your choice made no sense")
            continue
    return choice
def deletenamefromlist(namelist,name):
    try:
         namelist.remove(name)
    except:
        print("Name not found")
def editnameinlist(namelist, name):
    try:
        index = namelist.index(name)
    except:
        print("Name not found")
    deletenamefromlist(namelist,name)
    namelist.insert(index,input("Input the name you would wish to add to the old ones place: "))

def wherethefilesat():
    thefiles = input("Input the filename your answers are at: ")
    return thefiles

def readlinestolist(filename):
    reallines = []
    with open(filename,'r') as file:
        for line in file:
            reallines.append(line.rstrip('\n'))
    return reallines
def compare(rightanswers,youranswers):
    right = 0
    i = 0
    for x in youranswers:
        if x == rightanswers[i]:
            right+=1
            i+=1
        else:
            i+=1
    return right
def wrongones(rightanswers,youranswers):
    wronglist = []
    i = 0
    iterator = 1
    for x in youranswers:
        if x != rightanswers[i]:
           wronglist.append(iterator)
           i+=1
           iterator += 1
        else:
            i+=1
            iterator += 1
    return wronglist
