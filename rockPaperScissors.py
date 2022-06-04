player1 = ""
player2 = ""
menuSelection = "yes"

while menuSelection == "yes":
    print("Player 1 chooses:")
    player1 = input()
    print("Player 2 chooses:")
    player2 = input()

    if ((player1 == "rock" and player2 == "scissors") or
            (player1 == "scissors" and player2 == "paper") or
            (player1 == "paper" and player2 == "rock")):
        print("Player 1 Wins")
    elif player1 == player2:
        print("Tie")
    else:
        print("Player 2 Wins")

    print("Play Again?")
    menuSelection = input()

