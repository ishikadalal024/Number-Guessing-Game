import random

# Generate random number
number = random.randint(1, 100)

print("Welcome to Number Guessing Game!")
print("Guess a number between 1 and 100")

attempts = 0

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess < number:
        print("Too Low! Try Again.")
    
    elif guess > number:
        print("Too High! Try Again.")
    
    else:
        print("Congratulations! You guessed the number correctly.")
        print("Total Attempts:", attempts)
        break
