from random import randint
#
#
#
me = 0
you = 0
maxVal = 100

def run(me, you):

        print "Guess two, unique, random numbers between 1 and %d" %(maxVal)

        cardC = randint(0, maxVal - 1)
        cardA = int(raw_input("What is your first number?:"))

        if cardA > cardC:
                print "I think your first number is greater than your second number"
        else:
                print "I think your first number is less than your second number"

        correct = raw_input("Was I wright? (y/n):")

        if correct != "n":
                me += 1
        else:
                you += 1

        print ""

        print "I have %d point(s), and you have %d point(s)" % (me, you)

        print ""
                 
        replay = raw_input("Would you like to replay (y/n): ")
    
        if replay != "n":
                run(me, you)
        else:
                print "Good bye"
#
#
#
run(me, you)

    
    
