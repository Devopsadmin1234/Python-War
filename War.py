#1. Card Names XX
#2. Flip Outputs XX
#3. Declare XX
#4. Place Function XX
#5. Directions XX
#6. Settings
#7. Card Quantities
#8. Play Human

#Imports
import random
import time

#Settings
placeEnabled = True

#Card Counts
oneCount = 4
twoCount = 4
threeCount = 4
fourCount = 4
fiveCount = 4
sixCount = 4
sevenCount = 4
eightCount = 4
nineCount = 4
tenCount = 4
jackCount = 4
queenCount = 4
kingCount = 4
jokerCount = 2

#Declare Vars
pOneDeclareScore = 0
pTwoDeclareScore = 0

#Card Count
playerCards = 26
placed = 0

  #Selections
pOneSelect = ""
pTwoSelect = ""
helpSelect = ""
place = 0
settingsSelect = ""
delayTime = 0.5

#DC Vals
drawnCardOne = ""
drawnCardTwo = ""
declare = 0

#Score Vals
pOneScore = 0
pTwoScore = 0
roundWinner = ""
finalWinner = ""

#DC Name Vals
drawnCardName = ""
drawnCardNameTwo = ""

#Naming Function
def naming():
    global pOneDeclareScore, pTwoDeclareScore, playerCards, pOneSelect, pTwoSelect, drawnCardOne, drawnCardTwo, declare, pOneScore, pTwoScore, roundWinner, drawnCardName, drawnCardNameTwo, oneCount, twoCount, threeCount, fourCount, fiveCount, sixCount, sevenCount, eightCount, nineCount, tenCount, jackCount, queenCount, kingCount, jokerCount

    if drawnCardOne == 1:
        drawnCardName = " a 1"
    elif drawnCardOne == 2:
        drawnCardName = " a 2"
    elif drawnCardOne == 3:
        drawnCardName = " a 3"
    elif drawnCardOne == 4:
        drawnCardName = " a 4"
    elif drawnCardOne == 5:
        drawnCardName = " a 5"
    elif drawnCardOne == 6:
        drawnCardName = " a 6"
    elif drawnCardOne == 7:
        drawnCardName = " a 7"
    elif drawnCardOne == 8:
        drawnCardName = " an 8"
    elif drawnCardOne == 9:
        drawnCardName = " a 9"
    elif drawnCardOne == 10:
        drawnCardName = " a 10"
    elif drawnCardOne == 11:
        drawnCardName = " a Jack"
    elif drawnCardOne == 12:
        drawnCardName = " a Queen"
    elif drawnCardOne == 13:
        drawnCardName = " a King"
    elif drawnCardOne == 14:
        drawnCardName = " a Joker"
    else:
        print("Fatal Error: Please Contact Developer. (Error Code: 1)")

    # DC2 Names
    if drawnCardTwo == 1:
        drawnCardNameTwo = " a 1"
    elif drawnCardTwo == 2:
        drawnCardNameTwo = " a 2"
    elif drawnCardTwo == 3:
        drawnCardNameTwo = " a 3"
    elif drawnCardTwo == 4:
        drawnCardNameTwo = " a 4"
    elif drawnCardTwo == 5:
        drawnCardNameTwo = " a 5"
    elif drawnCardTwo == 6:
        drawnCardNameTwo = " a 6"
    elif drawnCardTwo == 7:
        drawnCardNameTwo = " a 7"
    elif drawnCardTwo == 8:
        drawnCardNameTwo = " an 8"
    elif drawnCardTwo == 9:
        drawnCardNameTwo = " a 9"
    elif drawnCardTwo == 10:
        drawnCardNameTwo = " a 10"
    elif drawnCardTwo == 11:
        drawnCardNameTwo = " a Jack"
    elif drawnCardTwo == 12:
        drawnCardNameTwo = " a Queen"
    elif drawnCardTwo == 13:
        drawnCardNameTwo = " a King"
    elif drawnCardTwo == 14:
        drawnCardNameTwo = " a Joker"
    else:
        print("Fatal Error: Please Contact Developer. (Error Code: 1)")

def declareFunc():

    global pOneDeclareScore, pTwoDeclareScore, playerCards, pOneSelect, pTwoSelect, drawnCardOne, drawnCardTwo, declare, pOneScore, pTwoScore, roundWinner, drawnCardName, drawnCardNameTwo, oneCount, twoCount, threeCount, fourCount, fiveCount, sixCount, sevenCount, eightCount, nineCount, tenCount, jackCount, queenCount, kingCount, jokerCount

    drawnCardOne = random.randrange(1, 14, 1)
    pOneDeclareScore = pOneDeclareScore + drawnCardOne
    drawnCardTwo = random.randrange(1, 14, 1)
    pTwoDeclareScore = pTwoDeclareScore + drawnCardTwo

    naming()

    print("Player drew" + drawnCardName)
    print("Computer drew" + drawnCardNameTwo)
    playerCards = playerCards - 1

    time.sleep(0.5)

def countCheck():

    global pOneDeclareScore, pTwoDeclareScore, playerCards, pOneSelect, pTwoSelect, drawnCardOne, drawnCardTwo, declare, pOneScore, pTwoScore, roundWinner, drawnCardName, drawnCardNameTwo, oneCount, twoCount, threeCount, fourCount, fiveCount, sixCount, sevenCount, eightCount, nineCount, tenCount, jackCount, queenCount, kingCount, jokerCount

    if drawnCardOne == 1:
        if oneCount == 0:
            drawnCardOne = random.randrange(1, 14, 1)
            countCheck()
        else:
            oneCount = oneCount - 1

    if drawnCardOne == 2:
        if twoCount == 0:
            drawnCardOne = random.randrange(1, 14, 1)
            countCheck()

    if drawnCardOne == 3:
        if threeCount == 0:
            drawnCardOne = random.randrange(1, 14, 1)
            countCheck()

    if drawnCardOne == 4:
        if fourCount == 0:
            drawnCardOne = random.randrange(1, 14, 1)
            countCheck()

    if drawnCardOne == 5:
        if fiveCount == 0:
            drawnCardOne = random.randrange(1, 14, 1)
            countCheck()

    if drawnCardOne == 6:
        if sixCount == 0:
            drawnCardOne = random.randrange(1, 14, 1)
            countCheck()

    if drawnCardOne == 7:
        if sevenCount == 0:
            drawnCardOne = random.randrange(1, 14, 1)
            countCheck()

    if drawnCardOne == 8:
        if eightCount == 0:
            drawnCardOne = random.randrange(1, 14, 1)
            countCheck()

    if drawnCardOne == 9:
        if nineCount == 0:
            drawnCardOne = random.randrange(1, 14, 1)
            countCheck()

    if drawnCardOne == 10:
        if tenCount == 0:
            drawnCardOne = random.randrange(1, 14, 1)
            countCheck()

    if drawnCardOne == 11:
        if jackCount == 0:
            drawnCardOne = random.randrange(1, 14, 1)
            countCheck()

    if drawnCardOne == 12:
        if queenCount == 0:
            drawnCardOne = random.randrange(1, 14, 1)
            countCheck()

    if drawnCardOne == 13:
        if kingCount == 0:
            drawnCardOne = random.randrange(1, 14, 1)
            countCheck()

    if drawnCardOne == 14:
        if jokerCount == 0:
            drawnCardOne = random.randrange(1, 14, 1)
            countCheck()

    if drawnCardTwo == 1:
        if oneCount == 0:
            drawnCardOne = random.randrange(1, 14, 1)
            countCheck()

    if drawnCardTwo == 2:
        if twoCount == 0:
            drawnCardOne = random.randrange(1, 14, 1)
            countCheck()

    if drawnCardTwo == 3:
        if threeCount == 0:
            drawnCardOne = random.randrange(1, 14, 1)
            countCheck()

    if drawnCardTwo == 4:
        if fourCount == 0:
            drawnCardOne = random.randrange(1, 14, 1)
            countCheck()

    if drawnCardTwo == 5:
        if fiveCount == 0:
            drawnCardOne = random.randrange(1, 14, 1)
            countCheck()

    if drawnCardTwo == 6:
        if sixCount == 0:
            drawnCardOne = random.randrange(1, 14, 1)
            countCheck()

    if drawnCardTwo == 7:
        if sevenCount == 0:
            drawnCardOne = random.randrange(1, 14, 1)
            countCheck()

    if drawnCardTwo == 8:
        if eightCount == 0:
            drawnCardOne = random.randrange(1, 14, 1)
            countCheck()

    if drawnCardTwo == 9:
        if nineCount == 0:
            drawnCardOne = random.randrange(1, 14, 1)
            countCheck()

    if drawnCardTwo == 10:
        if tenCount == 0:
            drawnCardOne = random.randrange(1, 14, 1)
            countCheck()

    if drawnCardTwo == 11:
        if jackCount == 0:
            drawnCardOne = random.randrange(1, 14, 1)
            countCheck()

    if drawnCardTwo == 12:
        if queenCount == 0:
            drawnCardOne = random.randrange(1, 14, 1)
            countCheck()

    if drawnCardTwo == 13:
        if kingCount == 0:
            drawnCardOne = random.randrange(1, 14, 1)
            countCheck()

    if drawnCardTwo == 14:
        if jokerCount == 0:
            drawnCardOne = random.randrange(1, 14, 1)
            countCheck()

#Play Against Computer
def playComputer():

    global pOneDeclareScore, pTwoDeclareScore, playerCards, pOneSelect, pTwoSelect, drawnCardOne, drawnCardTwo, declare, pOneScore, pTwoScore, roundWinner, drawnCardName, drawnCardNameTwo, oneCount, twoCount, threeCount, fourCount, fiveCount, sixCount, sevenCount, eightCount, nineCount, tenCount, jackCount, queenCount, kingCount, jokerCount

    while playerCards >= 1:

        global settingsSelect, placeEnabled, placed, delayTime

        if placeEnabled:

            pOneSelect = input(bColors.YELLOW + "What would you like to do? \nEnter P to draw the next card, \nF to flip a placed card \nS to edit settings \nH to learn how to play the game:" + bColors.ENDC)
        else:
            pOneSelect = input(bColors.YELLOW + "What would you like to do? \nEnter F to proceed to the next turn \nS to edit settings \nH to learn how to play the game:" + bColors.ENDC)

        #Settings
        if pOneSelect == "S" or pOneSelect == "s":

          print(bColors.RED + "Settings:" + bColors.ENDC)
          print("Enter P to disable place for this current game session. (Current selection: ", placeEnabled,") \nEnter D to edit the delay time between turns. (Current Selection: ", delayTime," seconds)\nEnter Any Other Key to exit this menu.")
          settingsSelect = input(bColors.YELLOW + "Selection: " + bColors.ENDC)
          if settingsSelect == "P" or settingsSelect == "p":
            placeEnabled = False
            print("Place successfully disabled for this game. Now you only have to enter F to proceed to the next turn.")
          if settingsSelect == "D" or settingsSelect == "d":
            delayTime = float(input("Enter an amount of time (in seconds) or enter 0 for no delay: "))


        #Flip
        if pOneSelect == "H" or pOneSelect == "h":
            print("------------------------------------------------------------------------------------------------------")
            print("The game of war is played with a standard deck of 54 playing cards (with jokers). \nEach player gets half of the stack face-down. \nBoth players take the first card on the top of their pile and places it to the side face down. \nOnce both players have a card placed aside, they both flip their cards at the same time. \nThe player with the higher value card wins the round and gets 1 point. \nBoth cards are discarded in a separate pile, or with the winner player for point-counting.")
            print("------------------------------------------------------------------------------------------------------")

        if placeEnabled:
            if pOneSelect == "P" or pOneSelect == "p":
                placed = 1
                print("Player placed their card.")
                print("Computer placed their card.")
                print("Ready to Flip!")
        else:
            placed = 1


        if pOneSelect == "F" or pOneSelect == "f":

            #global placed

            if placed == 1:

                #Randomizers
                drawnCardOne = random.randrange(1, 14, 1)
                drawnCardTwo = random.randrange(1, 14, 1)

                countCheck()

                naming()

                playerCards = playerCards - 1

                #Points
                if drawnCardOne > drawnCardTwo:
                    pOneScore = pOneScore + 1
                    roundWinner = "Player "
                elif drawnCardTwo > drawnCardOne:
                    pTwoScore = pTwoScore + 1
                    roundWinner = "Computer "
                elif drawnCardOne == drawnCardTwo and playerCards < 5:
                    drawnCardOne = random.randrange(1, 14, 1)
                    drawnCardTwo = random.randrange(1, 14, 1)
                else:
                    declare = 1

                #Prints
                if declare == 0:
                    time.sleep(0.5)
                    print("---------------------------------")
                    print("Player drew" + drawnCardName)
                    print("Computer drew" + drawnCardNameTwo)
                    print(roundWinner + "wins the round!")
                    print("Player Score: ", pOneScore)
                    print("Computer Score: ", pTwoScore)
                    print(playerCards, "cards remain in your hand.")
                    print("---------------------------------")
                elif declare == 1:
                    print("Player drew" + drawnCardName)
                    print("Computer drew" + drawnCardNameTwo)
                    print("Both players drew the same card!")

                    print('"I"')
                    declareFunc()


                    print('"DE-"')
                    declareFunc()

                    print('"-CLARE"')
                    declareFunc()

                    print('"WAR!!"')
                    declareFunc()

                    #ADD IN DECLARE SCORES + WINNER PRINTS (4 POINTS TO WINNER)

                    if pOneDeclareScore > pTwoDeclareScore:
                        pOneScore = pOneScore + 5
                        print("Player Wins the Battle (+5 Points)")
                        print("---------------------------------")
                        print("Player Score:", pOneScore)
                        print("Computer Score:", pTwoScore)
                    elif pTwoDeclareScore > pOneDeclareScore:
                        pTwoScore = pTwoScore + 5
                        print("Computer Wins the Battle (+5 Points)")
                        print("---------------------------------")
                        print("Player Score:", pOneScore)
                        print("Computer Score:", pTwoScore)
                    elif pOneDeclareScore == pTwoDeclareScore:
                        pOneScore = pOneScore + 3
                        pTwoScore = pTwoScore + 3
                        print("Battle Was a TIE! (+3 Points Each)")
                        print("---------------------------------")
                        print("Player Score:" + pOneScore)
                        print("Computer Score:" + pTwoScore)
                    else:
                        print("Fatal Error. Please Contact Developer. (Error Code: 3, Zone 1)")
                placed = 0

            else:
                print("You haven't placed your card yet! (Use the command PLACE before using FLIP or disable flipping in Settings.)")

            declare = 0
        pOneSelect = ""

        while playerCards == 0:
            print(bColors.BLUE + "Out of Cards!" + bColors.ENDC)
            print("Final Scores:")
            print("Player's final score is: ", pOneScore)
            print("Computer's final score is:", pTwoScore)
            if pOneScore > pTwoScore:
                print(bColors.GREEN + "Player Wins the Match!" + bColors.ENDC)
            elif pTwoScore > pOneScore:
                print(bColors.RED + "Computer Wins the Match!" + bColors.ENDC)
            elif pOneScore == pTwoScore:
                print(bColors.YELLOW + "It's a Tie!" + bColors.ENDC)
            playerCards = -5

class bColors:
    RED = "\033[1;31;31m"
    YELLOW = '\33[33m'
    ENDC = '\033[0m'
    GREEN = '\033[32m'
    BLUE = '\033[34m'
print(bColors.RED + "This program is made by Zain Abuhatab, all rights reserved." + bColors.ENDC)
print("Welcome to the Game of War in Python.")

playComputer()
