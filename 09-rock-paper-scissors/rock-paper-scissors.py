from random import choice

print("...rock...")
print("...paper...")
print("...scissors...")

# print("Enter player 1 choice")
player_1 = choice(["rock", "scissors", "paper"])

# print("NO CHEATING!!!!!!\n" * 30)

print("Enter choice")
player_2 = input()

print("SHOOT!")

if player_1 == player_2:
    print("DRAW!")
elif player_1 == "rock" and player_2 == "scissors":
    print("Player 1 wins!")
elif player_1 == "paper" and player_2 == "rock":
    print("Player 1 wins!")
elif player_1 == "scissors" and player_2 == "paper":
    print("Player 1 wins!")
else:
    print("Player 2 wins!")
