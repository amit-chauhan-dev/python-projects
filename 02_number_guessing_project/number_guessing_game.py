import random

print("🎮 Number Guessing Game")
print("Guess the number between 1 and 10")

# random number generate
secret_number = random.randint(1, 10)

guess = 0

while guess != secret_number:
    
    guess = int(input("Enter your guess: "))

    if guess > secret_number:
        print("Too High! Try again.")

    elif guess < secret_number:
        print("Too Low! Try again.")

    else:
        print(" Congratulations! You guessed the correct number! ")