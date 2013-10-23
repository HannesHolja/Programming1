import string

def consonant(sentence):
    listofconsonants = "bcdfghjklmnpqrstvwxz"
    many = compare(listofconsonants,sentence)
    return many


def vocal(sentence):
    listofvocals = "aeiouyäö"
    many = compare(listofvocals,sentence)
    return many


def mostcommon(sentence):
    d = dict.fromkeys(string.ascii_lowercase,0) #Lets generate the english letters first
    d.update({'ä':0})   #Then we input the finnish letters manually
    d.update({'ö':0})
    for i in d:
        for x in sentence.lower():
            if x == i:
                d[i] += 1
    print("Here is a sorted interpretation of all letters in the sentence with corresponding values of letters found")
    for key in sorted(d, key=d.get, reverse=True): #Get the dictionary key value and sort based on those.
        if d[key] != 0: #Don't want to print junk! Just the letters that are REALLY on that sentence
            print(key,d[key], end='  ')
def compare(finnishalphabet,sentence):
    howmany = 0
    for letter in finnishalphabet:
        for i in sentence.lower():
            if i == letter:
                howmany+=1
    return howmany
