import forca
import adivinhacao


def choose_game():
    print("*********************************")
    print("****** Choose your game! ******")
    print("*********************************")

    print("(1) Forca (2) Adivinhação")

    game = int(input("Which game? "))

    if game == 1:
        print("Playing forca")
        forca.play()
    elif game == 2:
        print("Playing adivinhacao")
        adivinhacao.play()


if __name__ == "__main__":
    choose_game()
