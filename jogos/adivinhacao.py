import random


def play():

    print("*********************************")
    print("************* Welcome! **********")
    print("*********************************")

    secret_number = random.randrange(1, 101)
    score = 1000

    print("Levels:")
    print("(1) Easy (2) Medium (3) Hard")

    level = int(input("Define the level: "))

    if level == 1:
        attempts = 20
    elif level == 2:
        attempts = 10
    else:
        attempts = 5

    for round_game in range(1, attempts + 1):
        print(f"Attempt {round_game} of {attempts}")

        guess = int(input("Enter a number between 1 and 100: "))

        if guess < 1 or guess > 100:
            print("You need to enter a number between 1 and 100!")
            continue

        if guess == secret_number:
            print(f"You are right and your score is {score}!")
            break
        else:
            if guess > secret_number:
                print("You are wrong! Your shot is greater than the secret number.")
            elif guess < secret_number:
                print("You are wrong! Your shot is lesser than the secret number.")
            score = score - abs(secret_number - guess)
    print(f"The Secret Number is {secret_number}.")


if __name__ == "__main__":
    play()
