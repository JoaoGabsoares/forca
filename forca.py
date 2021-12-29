import random


def jogar():
    print('*'*50)
    print('***seja bem vindo ao jogo da forca***')
    print('*'*50)

    arquivo = open(
        "/home/joao/Área de trabalho/Curso/arquivos_programacao/projetos/forca/frutas.txt", "r")
    frutas = []

    for linha in arquivo:
        linha.strip()
        frutas.append(linha)

    arquivo.close()

    numeros = random.randrange(0, len(frutas))
    palavra_secreta = frutas[numeros].upper()

    letras_acertadas = ['_' for letra in palavra_secreta]

    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)

    while (not enforcou and not acertou):
        chute = input('digite a letra desejada: ')
        chute = chute.strip().upper()

        if (chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if (chute == letra):
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1

        enforcou = erros == 6

        acertou = '_' not in letras_acertadas
        print(letras_acertadas)

    if (acertou):
        print('você ganhou!!!!')
    else:
        print('você errou!')

    print('fim de jogo!')


if (__name__ == "__main__"):
    jogar()
