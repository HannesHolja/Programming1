from functions import deckshuffled, addtocardvalue,declarewinner
import random


def main():
    flag = True
    while flag == True:
        randomdeck = deckshuffled()
        valueofcards = 0
        numberofplayers = int(input("How many players?"))
        playernumber = 1
        cardvalues = {}
        while playernumber <= numberofplayers:
            if len(randomdeck) < 10:
                print("Cards out, shuffling a new deck")
                randomdeck = {}
                randomdeck = deckshuffled()
            playerscard = random.choice(list(randomdeck.keys()))
            valueofcards += addtocardvalue(randomdeck,playerscard)
            del randomdeck[playerscard]
            print("-------------------------------------------------------------------------------")
            print("Player {0} hits a {1}, overall the player has {2}".format(playernumber,playerscard,valueofcards))
            print("-------------------------------------------------------------------------------\n\n")
            if valueofcards > 21:
                print("It's a bust! The player loses")
                valueofcards = 0
                playernumber += 1
                continue
            elif valueofcards == 21:
                print("Players hits a blackjack!")
                cardvalues['Player ' + str(playernumber)] = valueofcards
                valueofcards = 0
                playernumber += 1
                continue
            print("Press 1 to hit a new card")
            print("Press 2 to stand")
            choice = int(input("Input your choice"))
            if choice == 1:
                continue
            else:
                print("The player stands at {0}".format(valueofcards))
                cardvalues['Player '+ str(playernumber)] = valueofcards
                playernumber += 1
                valueofcards = 0
        if declarewinner(cardvalues) != None:
            print("And the winner is {0} with {1}".format(declarewinner(cardvalues),cardvalues[declarewinner(cardvalues)]))
        else:
            print("Everybody busted!")
        newgame = input("Press 1 to quit, else a new game will start")
        if newgame == 1:
            flag == False


main()
