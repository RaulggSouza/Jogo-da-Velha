#Programa de Jogo da Velha em Python
from random import randrange #Importa o módulo 
from time import sleep

original = ((1,2,3),(4,5,6),(7,8,9)) #Tabuleiro original
tabuleiro = [[1,2,3],[4,5,6],[7,8,9]] #Tabuleiro mutável

def desenho(): #Desenha o tabuleiro
    for i in range (len(tabuleiro)):
        a= tabuleiro[i][0]
        b= tabuleiro[i][1]
        c= tabuleiro[i][2]
        print("+-------+-------+-------+")
        print("|       |       |       |")
        print("|  ",a,"  |  ",b,"  |  ",c,"  |")
        print("|       |       |       |")
    print("+-------+-------+-------+")

def jogar_comp():
    #Sorteia o lugar onde o computador vai jogar
    linha_comp = randrange(3)
    coluna_comp = randrange(3)
    if testa_jogada(tabuleiro[linha_comp][coluna_comp]): #Testa se a jogada é válida    
        print("Vez do Computador:")
        tabuleiro[linha_comp][coluna_comp] = "X" #Substitui a coordenada da tabela referente a jogada do computador por "X"
        desenho()
    else:
        jogar_comp() #Se a jogada for inválida executa o código de novo

def testa_jogada(jogada):
  #Testa se a jogada do computador é em lugar válido
  if jogada == "X" or jogada == "O":
      return False
  if jogada > 0 and jogada < 10: #Testa se o usuário digitou um número válido
        for i in range (len(original)):
            for j in range (len(original[i])):
                #Testa se a jogada do usuário já está ocupada
                if tabuleiro[i][j] == "X" and original[i][j] == jogada:
                    print("\nValor já escolhido pelo computador")
                    return False
                elif tabuleiro[i][j] == "O" and original[i][j] == jogada:
                    print("\nValor já escolhido pelo usuário")
                    return False
        return True #Se tudo der certo segue normalmente
  else:
    return False

def jogar_jogador():
    print("Vez do Jogador:")
    while True:
        try:
            jogada = int(input("Escolha um lugar disponível para jogar digitando o número do quadrado: "))
            break
        except ValueError:
            print("Lugar indisponível")
            continue
    if testa_jogada(jogada):
        for i in range(len(tabuleiro)):
            for j in range(len(tabuleiro[i])):
                if tabuleiro[i][j] == jogada:
                    tabuleiro[i][j] = "O"
    else:
        print("\nInsira outro valor")
        jogar_jogador()

def jogar():
    s = 1
    desenho()
    while True:
        sleep(s)
        if jogo_acabou() == False:
            jogar_comp()
            sleep(s)
        else: break
        if jogo_acabou() == False:
            jogar_jogador()
            desenho()
            sleep(s)
        else: break
    print(resultado)

def jogo_acabou():
    diagonalP_comp = 0
    diagonalP_jogador = 0
    diagonalI_comp = 0
    diagonalI_jogador = 0
    for i in range(len(tabuleiro)):
        contador_comp = 0
        contador_jogador = 0
        if testar_grade("X",contador_comp):
            fim(1)
            return True
        if testar_grade("O",contador_jogador):
            fim(2)
            return True
        contador_comp, contador_jogador = 0, 0
        if diagonal(diagonalP_comp, diagonalI_comp, "X"):
            fim(1)
            return True
        if diagonal(diagonalP_jogador, diagonalI_jogador, "O"):
            fim(2)
            return True
    if empate("X", "O"):
        fim(3)
        return True
    return False

def testar_grade(letra, var):
    for linha in range(len(tabuleiro)):
        var = 0
        #Testa se vitória horizonal
        for coluna in range(len(tabuleiro[linha])):
            if tabuleiro[linha][coluna] == letra:
                var += 1
                if var == 3:
                    return True
        var = 0
        #Testa se vitória vertical
        for coluna in range(len(tabuleiro[linha])):
            if tabuleiro[coluna][linha] == letra:
                var += 1
                if var == 3:
                    return True
            
def diagonal(var, varI, letra):
    var = 0
    varI = 0
    for i in range(len(tabuleiro)):
        #Testa se vitória na diagonal principal
        if tabuleiro[i][i] == letra:
            var += 1
            if var == 3:
                return True
        #Testa se vitória na diagonal inversa
        if tabuleiro[i][-(i+1)] == letra:
            varI +=1
            if varI == 3:
                return True

def empate(letraC, letraJ):
    empatar = 0
    for linha in range(len(tabuleiro)):
        for coluna in range(len(tabuleiro[linha])):
            #Testa se toda a grade está preenchida
            if tabuleiro[coluna][linha] == letraC or tabuleiro[coluna][linha] == letraJ:
                empatar += 1
                if empatar == 9:
                    return True

def fim(valor):
    global resultado
    resultado = ""
    if valor == 1:
        resultado = "Computador Ganhou"
    elif valor == 2:
        resultado = "Jogador Ganhou"
    elif valor == 3:
        resultado = "Empate"
print("Boas vindas ao Jogo da Velha! Você é 'O'")
jogar()