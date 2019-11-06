import random


def play():

    print_opening()

    word = get_word("fruits.txt")

    letters = ["_" for letter in word]
    right = False
    attempts = 0

    print(*letters)

    while not right and (attempts < 7):
        guess = input("Which letter?").strip().upper()
        index = 0

        if guess in word:
            for letter in word:
                if letter == guess:
                    letters[index] = letter
                index += 1
        else:
            attempts += 1
            draw_body(attempts)

        right = "_" not in letters
        print("Word: ", *letters)

    print_final(right, word)


def print_opening():
    print("*********************************")
    print("************ Welcome! ***********")
    print("*********************************")
    print("HINT: is a fruit")
    print("")


def get_word(archive_name):
    archive = open(archive_name, "r")
    words = [line.split() for line in archive]
    return words[random.randrange(0, len(words))][0].upper()


def print_final(right, word):
    if right:
        print("Congratulations, You Win!")
        print("       ___________      ")
        print("      '._==_==_=_.'     ")
        print("      .-\\:      /-.    ")
        print("     | (|:.     |) |    ")
        print("      '-|:.     |-'     ")
        print("        \\::.    /      ")
        print("         '::. .'        ")
        print("           ) (          ")
        print("         _.' '._        ")
        print("        '-------'       ")
    else:
        print("You Lost!")
        print(f"The word is {word}")
        print("    _______________         ")
        print("   /               \       ")
        print("  /                 \      ")
        print("//                   \/\  ")
        print("\|   XXXX     XXXX   | /   ")
        print(" |   XXXX     XXXX   |/     ")
        print(" |   XXX       XXX   |      ")
        print(" |                   |      ")
        print(" \__      XXX      __/     ")
        print("   |\     XXX     /|       ")
        print("   | |           | |        ")
        print("   | I I I I I I I |        ")
        print("   |  I I I I I I  |        ")
        print("   \_             _/       ")
        print("     \_         _/         ")
        print("       \_______/           ")


def draw_body(errors):
    print("  _______     ")
    print(" |/      |    ")

    if errors == 1:
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")
    elif errors == 2:
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")
    elif errors == 3:
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")
    elif errors == 4:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")
    elif errors == 5:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")
    if errors == 6:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")
    if errors == 7:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")
    print(" |            ")
    print("_|___         ")
    print()


if __name__ == "__main__":
    play()
