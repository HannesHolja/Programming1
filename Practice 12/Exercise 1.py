from functions import consonant, vocal,mostcommon
import time

def main():
    sentence = input("Please input your sentence:")
    print("Amount of consonants in your sentence: {0}".format(consonant(sentence)))
    print("Amount of vocals in your sentence: {0}".format(vocal(sentence)))
    time.sleep(5)
    mostcommon(sentence)
main()