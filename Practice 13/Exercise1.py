import string
from functions import stringtomorse,morsetostring,encrypt,decode

def main():
        kirjainmerkit = {}
        morsemerkit = {}
        i,y = 0,0
        morsecodes = ['.-','-...','-.-.','-..','.','..-.','--.','....','..','.---','-.-','.-..','--','-.','---','.--.','--.-','.-.','...','-','..-','...-','.--','-..-','-.--','--..','']
        kirjainmerkitmorset = string.ascii_lowercase
        kirjainmerkitmorset += ' '
        kirjainmerkitmorset.split()
        kirjainmerkit = stringtomorse(kirjainmerkitmorset,morsecodes)
        morsemerkit = morsetostring(kirjainmerkitmorset,morsecodes)
        choice = int(input("Press 1 to encode a message, Press 2 to decrypt a message"))
        if choice == 1:
            name = input("Input the message you wish to encode: ")
            print("The encrypted message is: ")
            message = encrypt(name,kirjainmerkit)
            for i in message:
                print(i,end=' ')
        if choice == 2:
            name = input("Input the message you wish to decode: ")
            name.split()
            print("The decoded message is: ",end='')
            message = decode(name,morsemerkit)
            for i in message:
                print(i,end='')

main()
