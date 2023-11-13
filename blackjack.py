#Klenn Jakek V. Borja
#CMSC 12 LAB T2-1L
#Blackjack Game

import random, time, os, sys, blackjack_highscore
#random for randomizing the cards, time for time.sleep() decoration, os for clearing the terminal (makes it look more clean)
#blackjack_highscore import for getting the highscores, and saving the user's score after the game

#leaderboards placeholder. this will be used by the functions in another file. will also be used to LOAD and SAVE the leaderboards, everytime
#the program was used
leaderboards = {}

#dictionary of the BLACKJACK CARDS. (contains the POINTING system of all 52 cards in the deck)
blackjack_cards = {
    #HEART CARDS
        "Ah": 1, 
        "2h": 2, 
        "3h": 3, 
        "4h": 4, 
        "5h": 5, 
        "6h": 6, 
        "7h": 7, 
        "8h": 8, 
        "9h": 9, 
        "10h": 10, 
        "Kh": 10,
        "Qh": 10,
        "Jh": 10,
    #DIAMOND CARDS
        "Ad": 1, 
        "2d": 2, 
        "3d": 3, 
        "4d": 4, 
        "5d": 5, 
        "6d": 6, 
        "7d": 7, 
        "8d": 8, 
        "9d": 9, 
        "10d": 10, 
        "Kd": 10,
        "Qd": 10,
        "Jd": 10,
    #SPADE CARDS
        "As": 1, 
        "2s": 2, 
        "3s": 3, 
        "4s": 4, 
        "5s": 5, 
        "6s": 6, 
        "7s": 7, 
        "8s": 8, 
        "9s": 9, 
        "10s": 10, 
        "Ks": 10,
        "Qs": 10,
        "Js": 10,
    #CLUB CARDS
        "Ac": 1, 
        "2c": 2, 
        "3c": 3, 
        "4c": 4, 
        "5c": 5, 
        "6c": 6, 
        "7c": 7, 
        "8c": 8, 
        "9c": 9, 
        "10c": 10, 
        "Kc": 10,
        "Qc": 10,
        "Jc": 10
}

#cardPicker function. the whole point of this function is to "GET" and "REMOVE" the card from the "LIST" containing the deck of cards,
#that will be used for the WHOLE GAME. 
def cardPicker(list_blackjack_cards):

    #list_blackjack_cards will be used in here (a.k.a the specific deck of cards)

    #used a random.choice() function, to randomly "GET" a card from a list
    picked_card = random.choice(list_blackjack_cards)
    #after getting a card in the list, will "REMOVE" the card from the list
    list_blackjack_cards.remove(picked_card)

    #used for debugging the no. of cards everytime it is used:
    # print(len(list_blackjack_cards))
    
    #will return the picked_card, and will designate this picked_card as cardN (card1, card2, card3...)
    return picked_card


#function for alignment (i think there is a more suitable code for this XD)
#widthEditor(text you want to place here), only sole purpose is for decorating the program
def widthEditor(dialogue):
    character_width = 120
    #example dialogue is "hello" = 5 characters
    character_width = character_width - len(dialogue)
    character_width = character_width//2
    if len(dialogue) % 2 == 1:
        print(character_width*"=" + dialogue + (character_width+1)*"=")
    else:
        print(character_width*"=" + dialogue + (character_width)*"=")

#word design function. design for a "popping-like" characters on the screen one-by-one. testing those matrix things
def designWords(words):
    for n in words:
        sys.stdout.flush()
        time.sleep(0.03)
        print(n, end="")
    print()

#IMPORTANT: THE WHOLE GAME REVOLVES AROUND THE IDEA OF STORING VALUES IN A DICTIONARY. THERE ARE OTHER WAYS ON HOW TO
#CODE THE GAME OTHER THAN A DICTIONARY. MY PURPOSE OF USING A DICTIONARY IS THAT I CAN QUICKLY BROWSE THROUGH THE VALUES 
#BEING GIVEN TO THE "USER" AND THE "DEALER"
gameInfo = {

    #USERINFO
    "userInfo":{
        #user info contains keys and values such as:
        #card1 : name of card1
        #card2 : name of card2
        #value1 : value of card1
        #value2 : value of card2 
        #total : value1 + value2 + valueN
        #cardN... : name of cardN...
        #valueN... : value of cardN...
        #P.S: THIS IS IMPORTANT. MY MAIN REGRET IS THAT INSTEAD OF ACTUALLY USING KEY:VALUE PAIRS "name of card1": "value of card 1", I SEPARATED cardN and valueN AS KEYS.
        #P.S2: I CAN CHANGE THIS IF I WANT TO, BUT i dunno.
    },
    "dealerInfo":{
        #dealer info basically mirrors all the info userInfo has. only difference is that there are no cardN and valueN,
        #as the dealer only has 2 cards at the start and end of the round.
    }


}

#game function. WHOLE LOGIC OF THE BLACKJACK
#logic (rules):
#1. USER AND DEALER IS GIVEN 2 CARDS FROM THE BEGINNING (TOTAL WILL BE CALCULATED IMMEDIATELY)
#2. USER CAN "HIT" AND "STAND" WHILE DEALER CANNOT
#3. TOTAL OF THE USER MUST NOT GO OVER "21" (BLACKJACK)
#3.1. HIT: USER IS GIVEN ANOTHER CARD.
#3.1.1 IF THE USER HITS BUT GOES OVER THE "21" MARK, USER LOSES
#3.1.2 IF THE USER HITS, AND TOTAL IS NOT EQUAL TO 21. USER IS GIVEN ANOTHER CHANCE TO HIT AND STAND.
#3.2 STAND: USER IS NOT GIVEN ANOTHER CARD AND WILL CHECK WHETHER THE USER IS:
#3.2.1 IF USER HAS A TOTAL LESS THAN THE DEALER, USER LOSES
#3.2.2 IF USER HAS A TOTAL GREATER THAN THE DEALER, USER WINS
#3.2.2 IF USER HAS A TOTAL EQUAL TO THE DEALER, NO ONE WINS

def game(score):
    #every game has a specific deck of cards that contains originally the original blackjack cards
    #using the list() function, all of the keys in the blackjack_cards dictionary will be converted to a list
    #that can be picked by the cardPicker(). see cardPicker() function
    list_blackjack_cards = list(blackjack_cards)

    #no. of rounds.
    a= 1
    while True:
        #CODE FOR CHANGING THE VALUES IN THE DICTIONARY:

        #THE TOTAL OF userInfo IS FIRST GIVEN a "0" (though I think, this is not necessary?)
        gameInfo["userInfo"]["total"] = 0
        #USER WILL BE GIVEN TWO CARDS, THAT WILL BE PICKED USING cardPicker() 
        gameInfo["userInfo"]["card1"] = cardPicker(list_blackjack_cards)
        gameInfo["userInfo"]["card2"] = cardPicker(list_blackjack_cards)

        #A SEPARATE LIST IS USED CONTAINING ALL OF THE CARDS THE USER HAS
        drawn_cards = [gameInfo["userInfo"]["card1"], gameInfo["userInfo"]["card2"]]

        #USING THE blackjack_cards DICTIONARY, WE WILL FIND THE VALUE ASSOCIATED WITH THE CARD THAT WAS GIVEN TO THE USER
        #e.g, card1 is 10s (ten of spades), its value is 10
        #AFTERWARDS, userInfo WILL HAVE KEYS value1, value2, IN THE userInfo key dictionary
        gameInfo["userInfo"]["value1"] = blackjack_cards[gameInfo["userInfo"]["card1"]]
        gameInfo["userInfo"]["value2"] = blackjack_cards[gameInfo["userInfo"]["card2"]]
        #value1 AND value2 ARE ADDED TO MAKE UP THE TOTAL
        gameInfo["userInfo"]["total"] = gameInfo["userInfo"]["value1"] + gameInfo["userInfo"]["value2"]

        #game_dealer function. SIMILAR TO THE CODE ABOVE WILL BE PERFORMED, BUT SOLELY FOR THE DEALER
        game_dealer(list_blackjack_cards)

        #function for checking if total is less than 21. i used a while loop so that, the 
        #user may hit or stand repeatedly until it goes over 21 or is equal to 21
        while gameInfo["userInfo"]["total"] < 21:
            #shows the user its information
            print(green("Your cards are: "), drawn_cards)
            print(green("Your total is: "), gameInfo["userInfo"]["total"])
            print(green("Your score is: "), score)
            #if the user's first two picked cards is an ace and a ten (or vice-versa), the user wins the round and goes to the next round
            if ("A" in gameInfo["userInfo"]["card1"] or "A" in gameInfo["userInfo"]["card2"]) and ("10" in gameInfo["userInfo"]["card1"] or "10" in gameInfo["userInfo"]["card2"]):
                print(green("You got a ten and an ace! BLACKJACK."))
                print(green("You won! (You won 21 points)"))
                score += 21
                break
            else:
                #i variable is the number of cards the user has. this will be used if ever the user hits, and is given a new card
                i = 2

                #the user is given the option to stand or hit
                print(red("CHOOSE YOUR OPTION: "))
                print(green("[1] STAND"))
                print(green("[2] HIT"))
                #gets the input of the user
                game_choice = input()
                
                #if the user stands and its total is below 21, this will check whether the user has a greater total than the dealer
                if game_choice == "1":
                    if gameInfo["userInfo"]["total"] > gameInfo["dealerInfo"]["total"]:
                        userGui(drawn_cards)
                        print(green("Congrats! You won. (You gain 10 points)"))
                        score += 10
                        break
                    #if the user and the dealer has the same points
                    elif gameInfo["userInfo"]["total"] == gameInfo["dealerInfo"]["total"]:
                        userGui(drawn_cards)
                        print("Nobody wins! You and the dealer have the same total. (You lost nothing)")
                        break
                    #if the user stands and the user has a total lesser than the dealer's, then the user loses
                    else:
                        userGui(drawn_cards)
                        print(red("Sorry! You lost. (You lost 10 points)"))
                        score -= 10
                        break

                #if the user hits, they will be given a new card
                elif game_choice == "2":
                    #i variable is the iteration of the number of cards the user have.
                    i += 1
                    gameInfo["userInfo"]["card"+ str(i)] = cardPicker(list_blackjack_cards)
                    #APPENDS THE NEWLY DRAWN CARD TO THE LIST
                    drawn_cards.append(gameInfo["userInfo"]["card"+ str(i)])
                    gameInfo["userInfo"]["value"+ str(i)] = blackjack_cards[gameInfo["userInfo"]["card"+ str(i)]]
                    gameInfo["userInfo"]["total"] = gameInfo["userInfo"]["total"] + gameInfo["userInfo"]["value"+ str(i)]
                #will print an invalid input if the user types a letter, or a number that is not within 1 or 2
                #will reprompt the user still.
                else:
                    print("INVALID INPUT!")

        #if the user has total that is not equal to 21 (if total is greater than 21 or equal to 21 when the user HITS), it will be passed into an else statement
        else:
            #if the user has a total that is equal to 21 (when the player hits), then it is a blackjack and the player wins
            if gameInfo["userInfo"]["total"] == 21:
                userGui(drawn_cards)
                print(green("Congrats! You hit a BLACKJACK. (You gain 21 points)"))
                score += 21
            else: 
                #if the user hits and its total goes over 21, then the user loses
                userGui(drawn_cards)
                print(red("Your total has exceeded over 21! You lost. (Game Over)"))
                return score

        #will detect whether the number of the game cards is less than 10. if so, will get new deck of cards. 
        if len(list_blackjack_cards) < 10:
            print("YOU DO NOT HAVE ENOUGH DECK OF CARDS! (<10 cards)")
            print("GETTING NEW DECK OF CARDS...")
            #used a list function that will make the original blackjack_cards to be used.
            list_blackjack_cards = list(blackjack_cards)
            for n in range(3):
                sys.stdout.flush()
                time.sleep(1)
                print(".")
            os.system('cls')
        a += 1
        print("STARTING NEXT ROUND")
        for n in range(3):
            print(".", end="")           
            sys.stdout.flush()
            time.sleep(1)
        os.system('cls')
        #take note that i used an f-string here. it is so that i can use the variable a (no. of rounds) as a paremeter inside a widthEditor() function
        widthEditor(red(f"ROUND {a}"))             

def userGui(drawn_cards):
    #always remember (note for myself) that lists, and dictionaries are mutable. that's why even if we did not pass a parameter, we can still access the lists and dictionaries
    print(green("Your cards are:"), drawn_cards)
    print(green("Your total is:"), gameInfo["userInfo"]["total"])
    print(red("Dealer's cards are: "), gameInfo["dealerInfo"]["card1"], gameInfo["dealerInfo"]["card2"])
    print(red("Dealer's total is:"), gameInfo["dealerInfo"]["total"])

#function for getting the cards for the game dealer. same as the code for the user
def game_dealer(list_blackjack_cards):

    gameInfo["dealerInfo"]["card1"] = cardPicker(list_blackjack_cards)
    gameInfo["dealerInfo"]["card2"] = cardPicker(list_blackjack_cards)
    gameInfo["dealerInfo"]["value1"] = blackjack_cards[gameInfo["dealerInfo"]["card1"]]
    gameInfo["dealerInfo"]["value2"] = blackjack_cards[gameInfo["dealerInfo"]["card2"]]
    gameInfo["dealerInfo"]["total"] = gameInfo["dealerInfo"]["value1"] + gameInfo["dealerInfo"]["value2"]
    
#function that will be ran when the user inputs a choice of "1" in the main menu
def blackJack():
    #os function for clearing the output terminal. makes it easier for the user to play the game.
    os.system('cls')
    designWords(red("HELLO AND WELCOME TO BLACKJACK!"))
    designWords(red("WHAT IS YOUR NAME?: "))
    #this will be used for recording the user's data
    name = input()
    #f-string so that i can put a variable inside a parameter inside a string
    designWords(red("LET'S GET STARTED, ") + green(name) + red("!"))
    #score is first assigned as zero
    score = 0
    #after the game ends, the score is returned
    user_score = game(score)
    print("Name:", name)
    print("Score:", user_score)
    #will ask the user whether they want to save their score or not
    while True:
        save_score = input("Do you wish to save your score? (y/n)")
    #put inside a while loop, so that if the user's choice is not y/n, then it will re-prompt
        if save_score.lower() == "y":
            blackjack_highscore.writeHighscore(name, user_score)
            print("Your score has been saved! Thanks for playing.")
            break
        elif save_score.lower() == "n":
            print("Your score will not be saved.")
            break
        else:
            print("INVALID INPUT.")

#function for viewing the leaderboards
def viewHighscores():
    while True:
        widthEditor("VIEW HIGHSCORES")
        print("NAME:")
        #leaderboards is replaced with the information in the scores.txt
        leaderboards = blackjack_highscore.readHighscore()
        #i used a sorted() function. normally the sorted() function ONLY sorts the keys in an ascending order inside a dictionary. so there are
        #different parameters used to sort the values in a descending order WHILE also maintaining its key-value pairs
        leaderboards = sorted(leaderboards.items(), key=lambda x:x[1], reverse=True)
        #sorted function returns a list, that's why i used a dict() function to turn the list into a dictionary
        leaderboards = dict(leaderboards)
        #used a for loop to print the keys and values of the leaderboards (also used an items() function)
        for k,v in leaderboards.items():
            print(k,v)
        print("")
        print("[0] EXIT")
        choice = input()
        if choice == "0":
            break
        else:
            print("INVALID INPUT.")

#to make sentences green
def green(sentence):
    sentence = "\u001b[32m" + sentence + "\u001b[0m"
    return sentence
#to make sentences red
def red(sentence):
    sentence = "\u001b[31m" + sentence + "\u001b[0m"
    return sentence

#start of the foreground code===========================================================================


#menu
#while loop for re-prompting the user to the menu until the user inputs an exit choice
while True:
    os.system('cls')
    widthEditor("HELLO AND WelCOME TO")
    for n in range(3):
        sys.stdout.flush()
        time.sleep(0.5)
        print(".", end="")
    sys.stdout.flush()
    time.sleep(0.5)
    os.system('cls')

    #escape codes for color green
    print(green("""
    ____  __    ___   ________ __    _____   ________ __
   / __ )/ /   /   | / ____/ //_/   / /   | / ____/ //_/
  / __  / /   / /| |/ /   / ,< __  / / /| |/ /   / ,<   
 / /_/ / /___/ ___ / /___/ /| / /_/ / ___ / /___/ /| |  
/_____/_____/_/  |_\____/_/ |_\____/_/  |_\____/_/ |_|  
                                                         
    """))
    widthEditor("MENU")
    print("\n"+"[1]" + green(" PLAY BLACKJACK"))
    print("[2]" + red(" VIEW HIGHSCORES"))

    print("[0] EXIT")
    choice = input("CHOOSE YOUR OPTION: ")
    if choice == "1":
        blackJack()
    elif choice == "2":
        viewHighscores()
    elif choice == "0":
        print("THANKS FOR PLAYING!")
        break
    else:
        print("INVALID INPUT!")

#COMPLETE!