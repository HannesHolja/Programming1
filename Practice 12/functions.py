﻿import string

def consonant(sentence):
    listofconsonants = "bcdfghjklmnpqrstvwxz"
    many = compare(listofconsonants,sentence)
    return many


def vocal(sentence):
    listofvocals = "aeiouyäö"
    many = compare(listofvocals,sentence)
    return many

def bigletters(sentence):
    number = 0
    try:
        with open(sentence, 'r') as file:
            for line in file:
                for i in line:
                    if i.isupper():
                        number +=1
    except IOError:
        print("Filename specified was not found")
    return number

def smallletters(sentence):
        number = 0
        with open(sentence, 'r') as file:
            for line in file:
                for i in line:
                    if i.islower():
                        number +=1
        return number

def numbercases(sentence):
        number = 0
        with open(sentence, 'r') as file:
            for line in file:
                for i in line:
                    if i.isdigit():
                        number +=1
        return number

def spaces(sentence):
        number = 0
        with open(sentence, 'r') as file:
            for line in file:
                for i in line:
                    if i.isspace():
                        number +=1
        return number-1

def mostcommon(sentence):
    d = dict.fromkeys(string.ascii_lowercase,0) #Lets generate the english letters first
    d.update({'ä':0})   #Then we input the finnish letters manually
    d.update({'ö':0})
    for i in d:
        for x in sentence.lower():
            if x == i:
                d[i] += 1
    print("Here is a sorted interpretation of all letters in the sentence with corresponding values of letters found")
    for key in sorted(d, key=d.get, reverse=True): #Get the dictionary keys value and sort based on those.
        if d[key] != 0: #Don't want to print junk! Just the letters that are REALLY on that sentence
            print(key,d[key], end='  ')
def compare(finnishalphabet,sentence):
    howmany = 0
    for letter in finnishalphabet:
        for i in sentence.lower():
            if i == letter:
                howmany+=1
    return howmany

def sikalat(sentence):
    sentence = sentence.split()
    newword = ''
    for i in sentence:
        word = i
        firstchar = word[0]
        word = word[1:] #Exclude first character
        word = word + firstchar + 'AI'
        newword += ' ' + word
        newword = newword.lstrip().upper()
    return newword
def writesikalatfile(filename):
    try:
        with open(filename,'r') as file1:
            with open('salat.txt','w') as file2:
                for line in file1:
                    file2.write(sikalat(line))
    except IOError:
        print("The filename specified was not found")

def readlinestolist(filename):
    reallines = []
    try:
            with open(filename,'r') as file:
                for line in file: #Read the lines first
                    for word in line.split(): #Splits when it hits a space
                        reallines.append(word)
    except IOError:
            print("Filename specified was not found")
            return False
    return reallines
def longestword(list):
    lenght = 0
    for word in list:
        if len(word) > lenght:
            longest = word
            lenght = len(word)
    return longest
def shortestword(list):
    lenght = len(list[0])
    for word in list:
        if len(word) < lenght:
            longest = word
            lenght = len(word)
    return longest
def userschars(userchars, list):
    number = 0
    mostuserchars = 0
    for word in list:
        for i in userchars:
            for letter in word:
                if letter == i:
                    number+=1
                if mostuserchars < number:
                    mostcharsword = word
                    mostuserchars = number
        number = 0
    return mostcharsword
def numbers(sentence):
        number = 0
        numberlist = []
        for word in sentence:
                if word.isdigit():
                    numberlist.append(word)
        return numberlist




