import random

attempts_list = []
def show_score():
    #Define score using if and else statements
def start_game():
    random_number = int(random.randint(1, 10))
    print("Hello traveler! Welcome to the game of guesses!")
    player_name = input("What is your name? ")
    wanna_play = input("Hi, {}, would you like to play the guessing game? (Enter Yes/No) ".format(player_name))
    // Where the show_score function USED to be
    attempts = 0
    show_score()
    while wanna_play.lower() == "yes":
        try:
            #Guess is between 1 - 20
            if int(guess) == random_number:
                print("Nice! You got it!")
                attempts += 1
                attempts_list.append(attempts)
                print("It took you {} attempts".format(attempts))
                play_again = input("Would you like to play again? (Enter Yes/No) ")
                attempts = 0
                show_score()
                random_number = int(random.randint(1, 20))
                if play_again.lower() == "no":
                    print("That's cool, have a good one!")
                    break
            #Write elif statements for when the number is lower or higher with print statements, increment attempts
        except ValueError as err:
            print("Oh no!, that is not a valid value. Try again...")
            print("({})".format(err))
    else:
        print("That's cool, have a good one!")
if __name__ == '__main__':
    start_game()
