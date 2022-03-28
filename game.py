import random

attempts_list = []
def show_score():
    #Define score using if and else statements
    if len(attempts_list) <= 0:
        print("There is no max score yet, please accept it")
    else:
        ("The high score is {} attempts".format(min(attempt_list)))  

def start_game():
    
    random_number = int(random.randint(1, 10))
    print("Hello traveler! Welcome to the game of guesses!")
    player_name = input("What is your name? ")
    wanna_play = input("Hi, {}, would you like to play the guessing game? (Enter y/n) ".format(player_name))
    #Where the show_score function USED to be
    attempts = 0
    show_score()
    
    while wanna_play.lower() == "y":
        
        try:
            #Guess is between 1 - 20
            guess = input("Please guess a number between 1 and 10 ")
            if int(guess) == random_number:
                print("Nice! You got it!")
                attempts += 1
                attempts_list.append(attempts)
                print("It took you {} attempts".format(attempts))
                play_again = input("Would you like to play again? (Enter y/n) ")
                attempts = 0
                show_score()
                random_number = int(random.randint(1, 20))
                if play_again.lower() == "n":
                    print("That's cool, have a good one!")
                    break
            #Write elif statements for when the number is lower or higher with print statements, increment attempts
            elif  int(guess) < random_number:
                   print("You entered a lower number")
                   attempts +=1
            elif int(guess) > random_number:
               print("You entered a higher number")
               attempts +=1
        except ValueError as err:
            print("Oh no!, that is not a valid value. Try again...")
            print("({})".format(err))
    else:
        print("That's cool, have a good one!")
if __name__ == '__main__':
    start_game()
