from random import randint
#
#
#
maxVal = int(raw_input("Max random number: "))
while maxVal <=2:
        print "The max random number must be above 2"
        print ""
        maxVal = int(raw_input("Max random number: "))
runAmmount = int(raw_input("Ammount of simulation repeats: "))
repeatInfo = raw_input("Show information for each repeat (y/n): ")
keepSettings = "y"
#
#
#
def getCardA(maxVal):
        return randint(0, maxVal - 1)
#
#
#
def getCardB(maxVal):
        return randint(0, maxVal - 1)
#
#
#
def getCardC(maxVal):
        return randint(0, maxVal - 1)
#
#
#
def guess(guess, cardA, cardB):
        correct = 0
        incorrect = 0
        if guess == "A>B":
                if cardA > cardB:
                        correct = 1
                else:
                        incorrect = 1
        elif guess == "A<B":
                if cardA < cardB:
                        correct = 1
                else:
                        incorrect = 1
        return correct, incorrect
#
#
#
def run(maxVal, runAmmount, repeatInfo, keepSettings):
    
        if keepSettings != "y":
                maxVal = int(raw_input("Max random number: "))
                while maxVal <=2:
                        print "The max random number must be above 2"
                        print ""
                        maxVal = int(raw_input("Max random number: "))
                runAmmount = int(raw_input("Ammount of simulation repeats: "))
                repeatInfo = raw_input("Show information for each repeat (y/n): ")
    
        correctAmmount = 0
        incorrectAmmount = 0

        print ""
    
        for turn in range(runAmmount):
                cardA = getCardA(maxVal)
                cardB = getCardB(maxVal)
                cardC = getCardC(maxVal)

                while cardA == cardB:
                        cardB = getCardB(maxVal)

                if repeatInfo == "y":
                        print "Card A=%d, Card B=%d, and Card C=%d" % (cardA, cardB, cardC)

                if cardA > cardC:
                        answer = guess("A>B", cardA, cardB)
                        if repeatInfo == "y":
                                print "I think card A > card B"
                else:
                        answer = guess("A<B", cardA, cardB)
                        if repeatInfo == "y":
                                print "I think card A < card B"
        
                if answer[0] == 1 and repeatInfo == "y":
                        print "I was correct"
                elif repeatInfo == "y": 
                        print "I was incorrect"
        
                correctAmmount += answer[0]
                incorrectAmmount += answer[1]
        
                if repeatInfo == "y":
                        print ""
        
        print "correct %d time(s), incorrect %d time(s)." % (correctAmmount, incorrectAmmount)
    
        if incorrectAmmount != 0:
                print 'I was correct {:.2%} of the time'.format(float(correctAmmount) / runAmmount)

        print ""

        replay = raw_input("Would you like to replay (y/n): ")
    
        if replay == "y":
                keepSettings = raw_input("Would you like to keep previous settings (y/n): ")
                if keepSettings != "y":
                        print ""
                run(maxVal, runAmmount, repeatInfo, keepSettings)
        else:
                print "Good bye"
#
#
#
run(maxVal, runAmmount, repeatInfo, keepSettings)

    
    
