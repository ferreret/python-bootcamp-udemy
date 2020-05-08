from random import choice

print("...rock...")
print("...paper...")
print("...scissors...")

# print("Enter player 1 choice")
computer = choice(["rock", "scissors", "paper"])

# print("NO CHEATING!!!!!!\n" * 30)

print("Enter choice")
player = input().lower()

print("SHOOT!")

print("Computer: ", computer)

if computer == player:
    print("DRAW!")
elif computer == "rock" and player == "scissors":
    print("Computer wins!")
elif computer == "paper" and player == "rock":
    print("Computer wins!")
elif computer == "scissors" and player == "paper":
    print("Computer wins!")
else:
    print("Player wins!")
