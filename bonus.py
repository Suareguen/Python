import random

secret_number = random.randint(1, 100)

attempts = 0

while True:
    guess = int(input("Guess a number between 1 and 100: "))
    attempts += 1
    if guess == secret_number:
        guessed = True
    elif guess < secret_number:
        print("The secret number is greater.")
    else:
        print("The secret number is less.")

print("Congratulations! You guessed the number in " + attempts + " attempts.")

