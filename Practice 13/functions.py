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
