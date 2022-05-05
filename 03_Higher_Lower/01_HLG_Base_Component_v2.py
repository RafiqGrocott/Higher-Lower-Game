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
        response = input("How many rounds? : ")

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
rounds_drawn = 0

game_summary = []

choose_instruction = "Please choose rock (r), paper (p), or scissors (s), "

mode = "regular"

# Ask user got # of rounds, <enter> for infinite mode
rounds = check_rounds()

if rounds == "":
    mode = "infinite"
    rounds = 100

end_game = "no"
while end_game == "no":

# Start of Game Play Loop

    rounds_played += 1

    if mode == "infinite":
        rounds += 1

    # Rounds Heading
    print()
    if mode == "infinite":
        heading = "Continuous Mode: Round {}".format(rounds_played)

    else:
        heading = "Round {} of {}".format(rounds_played, rounds)

    print(heading)
    choose_instruction = "Please choose rock (r), paper (p), or scissors (s)"
    choose_error = "Please choose from rock/paper/scissors (or xxx to quit)"

    # Ask user for choice and check it's valid
    user_choice = choice_checker(choose_instruction, choose_error)

    if user_choice == "xxx":
        break



    # Start of Game Play Loop

    rounds_played += 1

    if mode == "infinite":
        rounds += 1

# Functions go here
def check_rounds():
    while True:

        response = input("How many rounds, or <enter> for infinite mode")

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
        
# Main routine goes here...

rounds_played = 0
choose_instructions = "Please choose 'higher' or 'lower'"

# Ask user for # of rounds, <enter> for infinite mode
rounds = check_rounds()

end_game = "no"
while end_game:

    # Rounds Heading
    print()
    if rounds == "":
        heading = "Continuous Mode: Round {}".format(rounds_played + 1)

    else:
        heading = "Round {} of {}".format(rounds_played + 1, rounds)

    print(heading)