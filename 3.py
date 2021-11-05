import random

guessed_number=0
number=random.randint(1,100)

while guessed_number != number:
    guessed_number=int(input("Guess a number!"))
    if guessed_number < number:
        print("Choose something bigger")
    elif guessed_number > number:
        print("Choose something smaller")
print("You find it correctly")
