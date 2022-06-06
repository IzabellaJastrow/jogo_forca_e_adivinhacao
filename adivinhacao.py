import random
import jogos

def imprime_mensagem_abertura():
    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")

def sorteio_numero():
    numero_secreto = random.randrange(1, 101)
    return numero_secreto

def escolha_nivel():
    print("Qual nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")
    nivel = int(input(("Defina o nível:")))


    if (nivel == 1):
        total_tentativas = 20
    elif (nivel == 2):
        total_tentativas = 10
    else:
        total_tentativas = 5
    return total_tentativas

def jogar_novamente():
    print("Você quer jogar novamente?")
    jogar_novamente = int(input("[1] Sim [2] Não"))

    if jogar_novamente == 1:
        jogos.selecao()
def jogar():
    imprime_mensagem_abertura()
    numero_secreto = sorteio_numero()
    total_tentativas = escolha_nivel()
    pontos = 1000

    for rodada in range(1, total_tentativas+1):
        print("Tentativa {} de {}".format(rodada,total_tentativas))
        chute_str = input("Digite um número entre 1 e 100:")
        chute_int = int(chute_str)
        print("Você digitou", chute_str)

        if(chute_int < 1 or chute_int > 100):
            print("Você deve digitar um número entre 1 e 100")
            continue

        acertou     = chute_int == numero_secreto
        chute_maior = chute_int > numero_secreto
        chute_menor = chute_int < numero_secreto

        if (acertou):
            print("Você acertou e fez {} pontos!".format(pontos))
            break
        else:
            if(chute_maior):
                print("Você errou! O seu chute foi maior que o número secreto")
            elif(chute_menor):
                print("Você errou! O seu chute foi menor que o número secreto")

            pontos_perdidos = abs(numero_secreto - chute_int)
            pontos -= pontos_perdidos


    print("Fim de jogo, o numero secreto era {}".format(numero_secreto))

    jogar_novamente()

if(__name__ == "__main__"):
    jogar()

