import random

print('Welcome to the game of rock, paper scissors! May the best person win(: \n')

playerPoints = 0
computerPoints = 0

while playerPoints !=3 and computerPoints != 3:
    your_choice = input("Enter a choice (rock, paper, scissors): ")
    collection = ["rock", "paper", "scissors"]
    cpu_selection = random.choice(collection)
    
    print(f"User selection: {your_choice}, Opponent chose {cpu_selection}.")

    if your_choice == cpu_selection:
        print("A draw? How boring.. try again, this time with PASSION!")
    elif your_choice == "rock":
        if cpu_selection == "scissors":
            print("Rock SMASH! You win!")
            playerPoints += 1
        else: 
            print("Paper beats rock, Better luck next time!")
            computerPoints += 1
    elif your_choice == "paper":
        if cpu_selection == "rock":
            print("Paper destroys rock all day! You win!")
            playerPoints += 1
        else: 
            print("Scissors slices right through your puny paper. \n Try again!")
            computerPoints += 1
    elif your_choice == "scissors":
        if cpu_selection == "paper":
            print("Scissors slices right through that paper. YOU WIN!")
            playerPoints += 1
        else: 
            print("Rock SMASH! You lose!!!")
            computerPoints += 1

if playerPoints > computerPoints:
    print("You win! game over.")
else: 
    playerPoints < computerPoints
    print("You lose!")