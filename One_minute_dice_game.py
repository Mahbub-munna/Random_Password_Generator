import random
import time

print("Welcome to Munna's One Minute Dice Rolling Challenge")
print("You have 1 minute to roll the dice as many times as you can!")

start_time = time.time()
score = 0
rolls = 0
duration = 60  # game duration in seconds

while True:
    elapsed = time.time() - start_time
    remaining = int(duration - elapsed)

    if remaining <= 0:
        break

    input(f"\nPress Enter to roll the dice (Time left: {remaining}s)... ")
    roll = random.randint(1, 6)
    score += roll
    rolls += 1
    print(f"Roll {rolls}: You rolled {roll} (Current Score: {score})")

print("\nTime's up!")
print(f"You rolled {rolls} times in 1 minute.")
print(f"Your Final Score: {score}")

