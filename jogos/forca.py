import random


def play():
    print("*********************************")
    print("************ Welcome! ***********")
    print("*********************************")

    archive = open("fruits.txt", "r")
    words = [line.split() for line in archive]
    word = words[random.randrange(0, len(words))][0].upper()
    letters = ["_" for letter in word]
    right = False
    attempts = 5

    print("HINT: is a fruit")
    print(*letters)

    while not right and attempts:
        guess = input("Which letter?").strip().upper()
        index = 0

        if guess in word:
            for letter in word:
                if letter == guess:
                    letters[index] = letter
                index += 1
        else:
            attempts = attempts - 1

        right = "_" not in letters
        print("Word: ", *letters)

    if right:
        print("You win");
    else:
        print("The Word is %s" % word)
        print("You lost")


if __name__ == "__main__":
    play()
