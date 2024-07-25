# 2) გადახედეთ https://www.w3schools.com/python/ref_random_choice.asp

import random

print("Welcome to the Guess the Number Game!")
print("I have selected a number between 1 and 100. Try to guess it!")

correct_number = random.randint(1, 100)
print(correct_number)
guess = int(input("Enter your guess: "))
attempts = 0


min_value = correct_number - 5
max_value = correct_number + 5


while guess != correct_number:
    if guess > correct_number and guess > max_value:
        print("Too high, try again!")
    elif guess <= max_value and guess > correct_number:
        print("Too high, but you are close!")
    elif guess >= min_value and guess < correct_number: 
        print("Too low, but you are close!")
    elif guess < min_value:
        print("Too low, try again!")
    elif guess < 0 or guess > 100:
        print("Invalid answer.")
    guess = int(input("Enter your guess: "))
    attempts += 1


if guess == correct_number:
    attempts = attempts + 1
    print("Congratulations! You guessed the number in", attempts, "attempts.")
