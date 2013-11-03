import pickle,random


def stringtomorse(kirjainmerkitmorset,morsecodes):
        kirjainmerkit = {}
        i = 0
        for x in kirjainmerkitmorset:
                kirjainmerkit.update({x:morsecodes[i]})
                i+=1
        return kirjainmerkit
def morsetostring(kirjainmerkitmorset,morsecodes):
        morsemerkit = {}
        y = 0
        for z in morsecodes:
            morsemerkit.update({z:kirjainmerkitmorset[y]})
            y+=1
        return morsemerkit
def encrypt(name,kirjainmerkit):
    message = []
    for i in name:
        for x in kirjainmerkit:
            if i == x:
                message.append(kirjainmerkit[x])
                break
    return message
def decode(name,morsemerkit):
    name = name.rsplit(' ') #Recursivesplit splits the whole list with the splitter specified here, which is in my case is a space
    message = []
    for i in name:
        for x in morsemerkit:
            if i == x:
                message.append(morsemerkit[x])
                break
    return message

def readlinestolist(filename):
    reallines =[]
    tmplist = []
    newword = ''
    try:
            with open(filename,'r') as file:
                for line in file: #Read the lines first
                    for word in line.split(): #Splits when it hits a space or a punctuation mark
                        for character in word:
                            if character.isalpha(): #Iterate character-by-character to check if we are dealing with a symbol that is not from the alphabet
                                tmplist.append(character) #Lets append that alpha to tmplist, else continue to another char of that word
                                continue
                        for i in tmplist:
                            newword += i #Time to structurize back the word
                        reallines.append(newword.lower())   #Append the word as a lowercase to the list reallines
                        newword = ''
                        tmplist = []


    except IOError:
            print("Filename specified was not found")
    return reallines

def printlisttofile(list, filename):
        with open(filename,'w') as file:
                for i in list:
                    file.write("{0}\n".format(i))

def searchaddress(personname,osoitteet):
    if personname in osoitteet:
        email = osoitteet[personname]
        return email
    else:
        return False
def addaddress(personname,personmail,osoitteet):
    if personname in osoitteet:
        return False
    else:
        osoitteet[personname] = personmail
        return osoitteet
def changeaddress(personname,personnewmail,osoitteet):
        if personname in osoitteet:
            osoitteet[personname] = personnewmail
            return osoitteet
        else:
            return False

def flowcontrol(choice,osoitteet):
        if choice == 1:
            personname = input("Please input the persons name").lower()
            address = searchaddress(personname,osoitteet)
            if address == False:
                print("The person you were looking for was not found from the dictionary")
            else:
                print("Email address of {0} is {1}".format(personname,address))
        elif choice == 2:
            personname = input("Please input the persons name").lower()
            personmail = input("Please input the persons email address").lower()
            tmp = addaddress(personname,personmail,osoitteet)
            if tmp == False:
                print("Email address of {0} is already on the list".format(personname))
            else:
                osoitteet = tmp
                print("Email address of {0} was added to the list".format(personname))
                return osoitteet
        elif choice == 5:
            return False
        elif choice == 3:
            value =changeaddress(input("Please input the persons name").lower(),input("Please input the persons new email").lower(),osoitteet )
            if value != False:
                print("Persons email updated")
                return value
            else:
                print("Person was not found from the dictionary")
        elif choice == 4:
            value = removefromdict(input("Input the persons name you wish to delete from the dictionary "),osoitteet)
            if value != False:
                osoitteet = value
                return osoitteet
            else:
                print("The person name was not found from the dictionary")

def dumpdictionary(osoitteet,filename):
    with open(filename,'wb') as file:
        pickle.dump(osoitteet,file)

def loaddictionary():
    try:
        with open('osoitteet.dat','rb') as file:
            osoitteet =pickle.load(file)
            if osoitteet == None:
                return {}
            return osoitteet
    except IOError:
        return {}
    except EOFError:
        return {}

def removefromdict(name, osoitteet):
    if name in osoitteet:
        del osoitteet[name]
        return osoitteet
    else:
        return False

def deckshuffled():
    deck = {}
    for suit in ['Clubs', 'Diamonds', 'Hearts', 'Spades']:
        for num in range(2, 15):
            deck[suit+str(num)] = num
    return deck
def addtocardvalue(deck,playerscard):
        return deck[playerscard]
def declarewinner(cardvalues):
    try:
        return max(cardvalues, key=cardvalues.get)
    except ValueError:
        print("Everybody busted!")



