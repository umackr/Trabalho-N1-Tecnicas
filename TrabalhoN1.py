import random

def fazerEscolha(sala):
    opcao = 1 , 2

    print("Você esta na sala ", sala)
    print("escolha seu caminho")
    print("[1] Caminho Vermelho")
    print("[2] Caminho Preto\n")

    escolha = int(input())
    escolha -= 1

    while escolha < 0 or escolha > 1:
        print("O valor inserido é invalido, porfavor digite 1 ou 2")
        print("[1] Caminho Vermelho")
        print("[2] Caminho Preto\n")

        escolha = int(input())
        escolha -= 1

    return sala + opcao[escolha]

def sala6(sala):
    print("Você esta na sala ", sala)
    print("O caminho vermelho esta bloqueado\nSua unica opção é o caminho preto")
    print("[x] Caminho Preto\n")
    input("Pressione ENTER para continuar")

    sala = 8
    return sala

def sala8(sala):
    print("Você esta na sala ", sala)
    print("Um portal estranho te atrai\nVocê e sua equipe entram no portal")
    print("O portal te levou a um lugar familiar...\n")
    input("Pressione ENTER para continuar")
    
    sala = random.randint(1,5)
    return sala

def sala9():
    print("\nVocê esta na sala 9")
    print("Sua equipe encontra a saida da dungeon")
    print("Vocês vão em direção a saida\n")
    input("Pressione ENTER para continuar")

def final (contador):
    if contador < 7:
        sala9()       
        print("\nVocê chegou ao fim da dungeon com {} jogadas".format(contador))
        print("Parabens você ganhou!\n")
    elif contador == 10:
        print("\nVocês foram capturados pela Horda!")
        print("Se fudeu\n")
        
    else:
        sala9()       
        print("\nVocê chegou ao fim da dungeon com {} jogadas".format(contador))
        print("Você usou 7 ou mais jogadas, infelizmente você perdeu!\n")

def main():
    sala = 1
    contador = 0

    while sala != 9 and contador < 10:
        contador += 1
        print ("\nJOGADA ", contador)
        if sala != 6 and sala != 8:
            sala = fazerEscolha(sala)
        elif sala == 6:
            sala = sala6(sala)
        else:
            sala = sala8(sala) 
    final (contador)    

if __name__ == "__main__":
    main()