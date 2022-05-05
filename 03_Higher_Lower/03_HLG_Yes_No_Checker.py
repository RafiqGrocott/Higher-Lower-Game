# Lists of valid responses
yes_no_list = ["yes", "no"]

played_before = choice_checker("Have you played this game before? Please enter yes or no.", yes_no_list, "Please enter yes / no")

if played_before == "no":
    instructions()