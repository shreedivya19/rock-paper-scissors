import random

print("===================")
print("Rock Paper Scissors")
print("===================\n")

print("1) ✊")
print("2) ✋")
print("3) ✌️")

player = int(input("Pick a number: "))

# Store emoji moves
moves = {1: "✊", 2: "✋", 3: "✌️"}

# Computer randomly picks 1, 2 or 3
cpu = random.randint(1, 3)

print(f"\nYou chose: {moves[player]}")
print(f"CPU chose: {moves[cpu]}")

# Decide winner using if-else
if player == cpu:
    print("It's a tie!")
elif (player == 1 and cpu == 3) or (player == 2 and cpu == 1) or (player == 3 and cpu == 2):
    print("The player won!")
else:
    print("CPU won!")
