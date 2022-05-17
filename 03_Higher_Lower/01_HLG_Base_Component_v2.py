import random

# Show instrustions
def instructions():
    print("*****Instrustions*****")
    print()
    print("Rules of the game...")
    print()
    print("Type in the number of rounds you would like to play OR,"
                "press <enter> to play infinite mode.")
    print()
    print("Next, you will guess your number (between your high number and low number). The computer will then tell you if your guess was too high, or too low")
    print()

# checks users choice based on a list
def choice_checker (question, valid_list, error):

    valid = False
    while not valid:

        # Ask user for choice (and put in lowercase)
        response = input(question).lower()

        # Iterates through list and if response us an item
        # In the list (or the first letter of an item), the
        # Full item name is returned
        for item in valid_list:
            if response == item[0] or response == item:
                return item
        
        # Output error if item not in list
        print("item is not in list")
        print(error)
        print()

# Functions go here
def check_rounds():
    while True:
        response = input("How many rounds? or <enter> for continuous mode: ")
        print()


        round_error = "Please type either <enter> or an integer " \
                        "that is more than 0\n"

        # If infinite mode not chosen, check response
        # Is an integer that is more than 0
        if response != "":
            try:
                response = int(response)

                # If response is too low, go back to
                # Start of loop
                if response < 1:
                    print(round_error)
                    continue
            # If response is not an integer go back to
            # Start of loop
            except ValueError:
                print(round_error)
                continue

        return response


# Lists of valid responses
yes_no_list = ["yes", "no"]

played_before = choice_checker("Have you played this game before? Please enter yes or no. ", yes_no_list, "Please enter yes / no")
print()

if played_before == "no":
    instructions()

# Ask user for # of rounds then loop...
rounds_played = 0
rounds_lost = 0

game_summary = []

choose_instruction = "Please choose a number in between your guidelines. "

mode = "regular"

# Number checking function goes here
def intcheck(question, low=None, high=None, exit_code = None):

    while True:

        #sets up error messages
        if low is not None and high is not None:
            error = "Please enter an integer between {} and {} (inclusive)".format(low, high)
        elif low is not None and high is None:
            error = "Please enter an integer that is more than or equal to {}".format(low)
        elif low is None and high is not None:
            error = "Please enter an integer that is less than or equal to {}".format(high)
        else:
            error = "Please enter an integer"

        try:
            response = input(question)

            #check to see if response is the exit code and return it
            if response == exit_code:
                return response

            #change the response into an integer
            else:
                response = int(response)

            #checks response is not too low, not use of 'is not' keywords
            if low is not None and response < low:
                print(error)
                continue
            #checks response is not too high
            if high is not None and response > high:
                print(error)
                continue

            return response

        #checks input is a integer
        except ValueError:
            print(error)
            continue
        

# ***** Main Routine *****

# checks that response is a integer
low_num = intcheck("Low Number: ")
print("You chose a low number of ", low_num)

#checks that resopnse is an integer more than the low number
high_num = intcheck("High Number: ", low_num)
print("You chose a high number of ", high_num)

# checks that the response is either the exit code
# or a number between low_num and high_num
guess = intcheck("Guess: ", low_num, high_num, "xxx")

# New code

print("You guessed {}".format(guess))
# Ask user for # of rounds, <enter> for infinite mode
rounds = check_rounds()

if rounds == "":
    mode = "infinite"
    rounds = 99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999

end_game = "no"
while end_game:

    # Rounds Heading
    print()
    if mode == "infinite":
        heading = "Continuous Mode: Round {}".format(rounds_played + 1)

    else:
        heading = "Round {} of {}".format(rounds_played + 1, rounds)

    print(heading)

    guess = input("Guess: ")
    if guess == "xxx":
        break

    rounds_played += 1

    # End game if requested # of rounds has been played
    if rounds_played >= rounds:
        break

