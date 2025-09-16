import random
number = random.randint(1, 100)
guesses = 0
record = 3  

print("Guess the Number Game!")
print("Try to guess the number between 1 and 100.")

while True:
    try:
        guess = int(input("Enter your guess: "))
        guesses += 1

        if guess < number:
            print("Guess Higher!")
        elif guess > number:
            print("Guess Lower!")
        else:
            print(f"Congratulations! You guessed the number {number} in {guesses} guesses.")

            if guesses < record:
                print("Amazing! You're the FINAL BOSS!")
            elif guesses == record:
                print("Great! You matched the current record!")
            else:
                print(f"You did it in {guesses} guesses. Try to beat the record of {record} next time!")
            break

    except ValueError:
        print("Please enter a valid integer.")
