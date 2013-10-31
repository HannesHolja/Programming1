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
                            if character.isalpha():
                                tmplist.append(character)
                                continue
                        for i in tmplist:
                            newword += i
                        reallines.append(newword)
                        newword = ''
                        tmplist = []


    except IOError:
            print("Filename specified was not found")
    return reallines
