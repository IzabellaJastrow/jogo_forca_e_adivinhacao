import jogos
import random



def jogar():
    imprime_mensagem_abertura()
    palavra_secreta = escolher_palavra()
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    print(letras_acertadas)
    enforcou = False
    acertou = False
    erros = 0

    while(not enforcou and not acertou):
        chute = pede_chute()
        if (chute in palavra_secreta):
            marca_chute_correto(chute, letras_acertadas, palavra_secreta)
        else:
            erros += 1
            desenha_forca(erros)

        print(letras_acertadas)
        enforcou = erros == 7 #Se erro chegar a 7 enforcou vai ser True
        acertou = "_" not in letras_acertadas #checa se os caracteres todos foram alterados


        if (acertou):
            imprime_mensagem_vencedor()

        if(enforcou):
            imprime_mensagem_perdedor(palavra_secreta)

    jogar_novamente()

def imprime_mensagem_abertura():
    print("*********************************")
    print("***Bem vindo ao jogo de Forca!***")
    print("*********************************")
def escolher_palavra():
    arquivo = open("palavra.txt", "r")
    lista_palavra_secreta = []
    for linha in arquivo:
        linha = linha.strip()
        lista_palavra_secreta.append(linha)

    arquivo.close()

    palavra_secreta = random.choice(lista_palavra_secreta)
    palavra_secreta = palavra_secreta.upper()
    return  palavra_secreta
def inicializa_letras_acertadas(palavra):
    return ["_" for letra in palavra]

def pede_chute():
    chute = input("Qual letra?")
    chute = chute.strip().upper()  # tira espaço que usuario possa ter digitado e deixa em maiusculo
    return chute


def marca_chute_correto(chute,letras_acertadas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if (chute == letra.upper()):
            letras_acertadas[index] = letra

        index += 1

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

def imprime_mensagem_vencedor():
        print("Parabéns, você ganhou!")
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


def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
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


def jogar_novamente():
    print("Você quer jogar novamente?")
    jogar_novamente = int(input("[1] Sim [2] Não"))

    if jogar_novamente == 1:
        jogos.selecao()
if (__name__ == "__main__"):
    jogar()
