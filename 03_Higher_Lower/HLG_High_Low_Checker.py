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

# Ask user for # of rounds..
rounds = intcheck("How many rounds <enter> for infinite: ", 1, exit_code = "")

if rounds == "":
    print("you chose infinite mode")
else:
    print("you asked for {} rounds".format(rounds))

# checks that response is a integer
low_num = intcheck("Low Number: ")
print("You chose a low number of ", low_num)

#checks that resopnse is an integer more than the low number
high_num = intcheck("High Number: ", low_num)
print("You chose a high number of ", high_num)

# loop four times for easy testing
for item in range(0, 4):

    # checks that the response is either the exit code
    # or a number between low_num and high_num
    guess = intcheck("Guess: ", low_num, high_num, "xxx")
    print("You guessed {}".format(guess))