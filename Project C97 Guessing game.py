import random
print("NUMBER gUESSING GAME")
number = random.randint(1,9)

chances = 0

print("Enter a random number between 1 and 9")
while chances < 5:
    guess = int(input("Enter your guess"))
    if guess == number:
        print("Congratulation YOU WON!!!")
        break
    elif chances < 5:
        print("You Lose!!! The number is", number)
    else:
        print("Your guess was too high: Guess another number",guess)
    chances += 1
if not chances <5:
    print("YOU LOSE !!! The number is", number)
