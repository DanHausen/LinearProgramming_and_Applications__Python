def questao1():
    print('Questao 1')
    matriz = [[0,0],[0,0],[0,0]]

    for l in range(0,3):
        for c in range(0,2):
            matriz[l][c] = int(input("Digite um valor numerico para: [{},{}] ".format(l,c)))

    print('-=' * 30)
    for l in range(0,3):
        for c in range(0,2):
            if(l == c):
                matriz[l][c] = 1
            elif(l != c):
                matriz[l][c] = l * l                
            print('[{}]'.format(matriz[l][c]), end='')
        print()

def questao2():
    print('Questao 2')
    matriz = [[0,0,0,0],[0,0,0,0],[0,0,0,0]]

    for l in range(0,3):
        for c in range(0,4):
            matriz[l][c] = int(input("Digite um valor numerico para: [{},{}] ".format(l,c)))

    print('-=' * 30)
    for l in range(0,3):
        for c in range(0,4):
            if(l == c):
                matriz[l][c] = l+c
            elif(l != c):
                matriz[l][c] = 2*l-2*c                
            print('[{}]'.format(matriz[l][c]), end='')
        print()

print('A resposta é 0')

def questao3():
    print('Questao 3')
    matrizA = [[2,3],[4,-1],[0,2]]
    matrizB = [[-2,0],[7,-1],[8,5]]
    matrizResultante = [[0,0],[0,0],[0,0]]

    for l in range(0,3):
        for c in range(0,2):
            matrizResultante[l][c] = matrizA[l][c] + matrizB[l][c]
    print('O resultado: ', matrizResultante)


def questao4():
    print('Questao 4')
    matrizA = [[0,3],[2,-5]]
    matrizB = [[-2,4],[0,-1]]
    matrizC = [[4,2],[-6,0]]
    matrizResultanteA = [[0,0],[0,0]]
    matrizResultanteB = [[0,0],[0,0]]
    matrizResultanteC = [[0,0],[0,0]]


    for l in range(0,2):
        for c in range(0,2):
            matrizResultanteA[l][c] = matrizA[l][c] + matrizB[l][c]
            matrizResultanteB[l][c] = matrizA[l][c] + matrizC[l][c]
            matrizResultanteC[l][c] = matrizA[l][c] + matrizB[l][c] + matrizC[l][c]

    print('Questao A: ',matrizResultanteA)
    print('Questao B: ',matrizResultanteB)
    print('Questao C: ',matrizResultanteC)


def questao5():
    print('Questao 5')
    matrizA = [[1,-1,0],[2,3,4],[0,1,-2]]
    matrizAT = [[1,2,0],[-1,3,1],[0,4,-2]]
    matrizB = [[0,0,0],[0,0,0],[0,0,0]]

    for l in range(0,3):
        for c in range(0,3):
            matrizB[l][c] = matrizA[l][c] + matrizAT[l][c]

    print('O resultado: ', matrizB)



selecao = 0
selecao = int(input("Selecione a questao:\n 1 - Questao 1 \n 2 - Questao 2 \n 3 - Questao 3 \n 4 - Questao 4 \n 5 - Questao 5 \n"))

if(selecao == 1):
    questao1()
elif(selecao == 2):
    questao2()
elif(selecao == 3):
    questao3()
elif(selecao == 4):
    questao4()
elif(selecao == 5):
    questao5()