import random
import jogos

def imprime_mensagem_abertura():
    print("*********************************")
    print("Bem vindo ao jogo de Pedra, papel e tesoura!")
    print("*********************************")

def sorteio_computador():
    opcoes = ('pedra','papel', 'tesoura')
    chute_computador = random.choice(opcoes)
    return chute_computador

def jogar_novamente():
    print("Você quer jogar novamente?")
    jogar_novamente = int(input("[1] Sim [2] Não"))

    if jogar_novamente == 1:
        jogos.selecao()

def escolha_jogador():
    chute_jogador = input("Qual o sua escolha: Pedra, papel ou tesoura?")
    chute_jogador = chute_jogador.lower()
    return chute_jogador

def mensagem_vencedor():
    print('Parabens, você derrotou o computador!')
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

def mensagem_derrota():
    print('Que pena, você perdeu :(')

def mensagem_empate():
    print("Vocês apostaram iguais, empatou!")

def jogar():
    print("\n" * 130) #para limpar terminal antes de inicializar o jogo
    imprime_mensagem_abertura()
    chute_computador = sorteio_computador()
    chute_jogador = escolha_jogador()

    jogador_venceu = False
    if (chute_jogador == 'pedra' and chute_computador == 'tesoura'):
        jogador_venceu = True
    elif (chute_jogador == 'tesoura' and chute_computador == 'papel'):
        jogador_venceu = True
    elif (chute_jogador == 'papel' and chute_computador == 'pedra'):
        jogador_venceu = True

    jogador_perdeu = False
    if (chute_computador == 'pedra' and chute_jogador == 'tesoura'):
        jogador_perdeu = True
    elif (chute_computador == 'tesoura' and chute_jogador == 'papel'):
        jogador_perdeu = True
    elif (chute_computador == 'papel' and chute_jogador == 'pedra'):
        jogador_perdeu= True
    
    empate = False
    if (chute_computador == chute_jogador):
        empate = True
        
    print("Você apostou em {} e o computador apostou em {}".format(chute_jogador, chute_computador))

    if (jogador_venceu == True):
        mensagem_vencedor()
    elif (jogador_perdeu == True):
        mensagem_derrota()
    elif (empate == True):
        mensagem_empate()

    jogar_novamente()


if (__name__ == "__main__"):
    jogar()