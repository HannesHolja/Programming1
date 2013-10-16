import random
import time

def simplelinecount(filename):
    lines = 0
    with open(filename) as file:
        for line in file:
            lines += 1
    return lines

def filenameasker():
    filename = input("Give me a file name: ")
    return filename

def printxlines(filename, numberoflines):
    i = 0
    with open(filename) as file:
        for line in file:
            if i < numberoflines:
                print(line)
                i += 1
            else:
                break

def listalllines(filename):
    numberlist = []
    try:
        with open(filename) as file:
                for line in file:
                    numberlist.append(line)
    except IOError:
            print("Filename specified was not found")
    except ValueError:
            print("Filename specified does not contain numerical data")
    return numberlist

def arithmeticmean(numberlist):
    mean = 0
    howmanynumbers = 0
    for i in numberlist:
        mean += int(i)
        howmanynumbers += 1
    return mean/howmanynumbers
def amountofnumbers():
    numbers = int(input("How many numbers do you wish to generate? "))
    return numbers

def randomgenerator(amountofnumbers):
    listofrandomints = random.sample(range(1,101),amountofnumbers)
    return listofrandomints

def printlisttofile(list, filename):
        with open(filename,'w') as file:
                for i in list:
                    file.write("{0}\n".format(i))
def greeter():
    print("1 = Add random values to file (Sequence 1-100)")
    print("2 = Read all the values from a file")
    choice = int(input("Give me a value "))
    return choice

def golfgreeter():
    print("1 = Add player and points to a file")
    time.sleep(1)
    print("2 = Delete player and points from a file")
    time.sleep(1)
    print("3 = Edit player and points")
    time.sleep(1)
    print("4 = Read  and print all the values from a file")
    time.sleep(1)
    print("Press 0 to end program")
    time.sleep(1)
    choice = input("Input your choice")
    return choice

def golfername():
    name = input("Input golfers name in format First Name Last Name ")
    return name
def golferpoints():
    while True:
        points = input("Input golfers points ")
        try:
            int(points)
            break
        except:
            print("You didn't input numbers!")
    return points
def addgolfer(name, points, filename):
    with open(filename, 'a+') as file:
        file.write("{0} {1}\n".format(name,points))
    alphabetize(filename)

def alphabetize(filename):
    with open(filename, 'r') as file:
        list = file.readlines()
        list.sort(key=str.lower) #Sortataan luettu lista
    with open(filename, 'w') as file:
        for i in list:
            file.write("{0}".format(i))
def erasegolfer(name, filename):
    with open(filename) as file:
        lines = file.readlines()
    with open(filename, 'w') as file:
        for line in lines:
            if not name in line:
                file.write(line)
def editgolfer(name, filename):
    newpoints = int(input("Give new points for player {0} :".format(name)))
    with open(filename) as file:
        lines = file.readlines()
    with open(filename, 'w') as file:
        for line in lines:
            if not name in line:
                file.write(line)
            else:
                file.write("{0} {1}".format(name, newpoints))
                print("Points edited")
