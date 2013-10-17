from usefulFunctions import wherethefilesat,readlinestolist,compare,wrongones

def main():
    rightanswers = ['B','D','A','A','C','A','B','A','C','D','B','C','D','A','D','C','C','B','D','A' ]
    youranswers =readlinestolist(wherethefilesat())
    right=compare(rightanswers,youranswers)
    print("You got {0} right".format(right))
    print("You answered wrong to questions {0}, You had {1} wrong answers.".format(wrongones(rightanswers,youranswers),len(wrongones(rightanswers,youranswers))))
    if right >= 15:
        print("You passed the test")
    else:
        print("You didn't pass the test")
main()
