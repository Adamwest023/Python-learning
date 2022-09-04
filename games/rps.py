import random
exit = False
user_points = 0
computer_points = 0

while exit == False:
    options = ["rock", "paper", "scissors"]
    user_input = input("Choose rock, paper, scissors or exit : ")
    computer_input = random.choice(options)

    if user_input == "exit":
        print("Game has ended")
        exit = True

    if user_input == "rock":
        if computer_input == "rock":
            print("You picked rock")
            print("Computer picked rock")
            print("It is a tie")
        elif computer_input == "paper":
            print("You picked rock")
            print("Computer picked paper")
            print("Computer wins the round")
            computer_points += 1
        elif computer_input == "scissors":
            print("You picked rock")
            print("Computer picked scissors")
            print("You win this round")
            user_points += 1

    elif user_input == "paper":
        if computer_input == "paper":
            print("You picked paper")
            print("Computer picked paper")
            print("It is a tie")
        if computer_input == "scissors":
            print("You picked paper")
            print("Computer picked scissors")
            print("Computer wins the round")
            computer_points += 1
        if computer_input == "rock":
            print("You picked paper")
            print("Computer picked rock")
            print("You win this round")
            user_points += 1

    elif user_input == "scissors":
        if computer_input == "scissors":
            print("You picked scissors")
            print("Computer picked scissors")
            print("It is a tie")
        if computer_input == "rock":
            print("You picked scissors")
            print("Computer picked rock")
            print("Computer wins the round")
            computer_points += 1
        if computer_input == "paper":
            print("You picked scissors")
            print("Computer picked paper")
            print("You win this round")
            user_points += 1
    elif user_input != "rock" or user_input != "paper" or user_input != "scissors":
        print("Invalid user input")
            
    print("Your score is " + str(user_points))
    print("Computer score is " + str(computer_points))