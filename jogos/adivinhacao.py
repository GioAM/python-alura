import random


def play():

    print("*********************************")
    print("************* Welcome! **********")
    print("*********************************")

    numero_secreto = random.randrange(1,101)
    attempts = 0
    score = 1000

    print("Qual nível de dificuldade?")
    print("(1) Easy (2) Medium (3) Hard")

    level = int(input("Defina o nível: "))

    if level == 1:
        attempts = 20
    elif level == 2:
        attempts = 10
    else:
        attempts = 5

    for rodada in range(1, attempts + 1):
        print("Tentativa {} de {}".format(rodada, attempts))

        chute_str = input("Digite um número entre 1 e 100: ")
        print("Você digitou " , chute_str)
        chute = int(chute_str)

        if chute < 1 or chute > 100:
            print("Você deve digitar um número entre 1 e 100!")
            continue

        if chute == numero_secreto:
            print("Você acertou e fez {} pontos!".format(score))
            break
        else:
            if chute > numero_secreto:
                print("Você errou! O seu chute foi maior do que o número secreto.")
            elif chute < numero_secreto:
                print("Você errou! O seu chute foi menor do que o número secreto.")
            score = score - abs(numero_secreto - chute)

    print("End")


if __name__ == "__main__":
    play()
