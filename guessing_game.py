# This is an exercise in using random, while loops, if statements, and elif
# in Python to make a simple guessing game

import random
win = False

def player_guess(x, player_score):
    # this function takes a bound and an initial score
    random_number = random.randint(1, x)
    # the computer generates a random number for a player
    # to guess
    guess = 0
    # initialize the guess and set player equal to player_score
    # so that it can be returned later.  Each guess adds one to
    # player and uses a while loop to track whether guess and the random number
    # are the same
    player = player_score
    while guess != random:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess < random_number:
            print("Sorry, too low.  Guess again.")
            player = player + 1
        elif guess > random_number:
            print("Sorry, too high.  Guess again")
            player = player + 1
        elif guess == random_number:
            print(f"You guessed correctly, the number is {guess}")
            player = player + 1
            return player



def computer_guess(y, computer_score):
    # much like player_guess above, this function takes a range and starting score
    low = 1
    high = y
    feedback = ''
    computer = computer_score
    while feedback != 'j':
        guess = random.randint(low, high)
        # this time, fwe have a variable feedback is equal to the user input
        feedback = input(f'is {guess} too high(H) too low(L) or just right(J)?')
        # every time we get a new random int (guess), this function receives feedback
        # until feedback is j, the loop continues.
        if feedback == 'h':
            high = guess - 1
            computer = computer + 1
        elif feedback == 'l':
            low = guess + 1
            computer = computer + 1
        elif feedback == 'j':
            print(f"The computer has guessed your number {guess}")
            computer = computer + 1
            return computer



if __name__ == "__main__":
    # set the initial scores for both players
    computer_score = 0
    player_score = 0

    while win != True:
        # while loop continues until some condition is true
        # in this case if someone has won

        # here we set the value of computer to the value
        # returned by computer_guess, and its counterpart
        # player_guess does the same for player
        computer = computer_guess(10, computer_score)
        player = player_guess(10, player_score)

        # here computer and player are compared.  The
        # object of the game is to guess the other player's
        # number in as few tries as possible.  After checking
        # both the computer and the player's scores, one is
        # declared the winner, win is set to True, and the loop breaks
        if computer > player:
            print(f"You Win!  Your score was {player}, "
                  f"and the computer scored {computer}")
            win = True
        elif player > computer:
            print(f"The computer has won.  Your score was {player}, "
                  f"the computer scored {computer}")
            win = True
        elif computer == player:
            print("Tie!  No one wins this time.")
            win = True

        # This if elif statement executes after the while loop
        # and checks if the user wants to play again
        response = input("Thanks for playing.  Play again? (Y/N)")
        if response == 'y':
            win = False
        elif response == 'n':
            print("Have a good day >:)")
