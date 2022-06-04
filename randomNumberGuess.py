import random

print("Guess the number I am thinking of 1-9...")
randomNum = random.randint(1, 9)
userNum = int(input())

while userNum != randomNum:
    if userNum < randomNum:
        print("Higher...")
    elif userNum > randomNum:
        print("Lower...")

    userNum = int(input())

print("Correct!")
