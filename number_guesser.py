import random

name=input("type your name: ")
print(f"welcome, {name}")
print("Guess a number between 1-10")
number_to_guess = random.randint(1,10)

guess= int(input("enter your guess:"))

if guess == number_to_guess:
    print("you guessed the number! ")
elif guess > number_to_guess:
    print(f"Too high, the number was {number_to_guess}")
else:
    print(f"Too low,the number was {number_to_guess}")