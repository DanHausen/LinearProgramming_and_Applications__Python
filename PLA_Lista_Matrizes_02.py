# Dan Hausen

def questao1():
    print('Questao 1: calcule matrizA * matrizB')
    matrizA = [[2,1],[-3,4]]
    matrizB = [[0,-1],[2,5]]
    matrizResultante = [[0,0],[0,0]]

    #matrizResultante[0][0] = matrizA[0][0] * matrizB[0][0] + matrizA[0][1] * matrizB[1][0]
    #matrizResultante[0][1] = matrizA[0][0] * matrizB[0][1] + matrizA[0][1] * matrizB[1][1]
    #matrizResultante[1][0] = matrizA[1][0] * matrizB[0][0] + matrizA[1][1] * matrizB[1][0]
    #matrizResultante[1][1] = matrizA[1][0] * matrizB[0][1] + matrizA[1][1] * matrizB[1][1]

    for l in range(len(matrizA)): #Multiplicacao
        for c in range(len(matrizB[0])):
            for k in range(len(matrizB)):
                #print('- L: ', l)
                #print('-- C: ', c)
                #print('--- K: ', k)     
                matrizResultante[l][c] += matrizA[l][k] * matrizB[k][c]
    for r in matrizResultante:
        print(r)

def questao2():
    print('Questao 2: calcule (matrizA + matrizB) * matrizC')
    matrizA = [[2,1],[-3,4]]
    matrizB = [[0,-1],[2,5]]
    matrizC = [[3,0],[6,1]]
    matrizSoma = [[0,0],[0,0]]
    matrizResultante = [[0,0],[0,0]]

    for l in range(len(matrizA)): #Soma
        for c in range(len(matrizB)):
            matrizSoma[l][c] = matrizA[l][c] + matrizB[l][c]

    for l in range(len(matrizSoma)):
        for c in range(len(matrizC[0])):
            for k in range(len(matrizC)):
                matrizResultante[l][c] += matrizSoma[l][k] * matrizC[k][c]
    for r in matrizResultante:
        print(r)
    
def questao3():
    print('Questao 3: calcule [matrizA + (matrizB - matrizCT)] * In')
    matrizA = [[2,1],[-3,4]]
    matrizB = [[0,-1],[2,5]]
    matrizCT = [[3,6],[0,1]]
    matrizSub = [[0,0],[0,0]]
    matrizSoma = [[0,0],[0,0]]
    matrizIdent = [[1,0],[0,1]]
    matrizResultante = [[0,0],[0,0]]

    for l in range(len(matrizB)):
        for c in range(len(matrizCT)):
            matrizSub[l][c] = matrizB[l][c] - matrizCT[l][c]

    for l in range(len(matrizA)):
        for c in range(len(matrizCT)):
            matrizSoma[l][c] = matrizA[l][c] + matrizSub[l][c]

    for l in range(len(matrizSoma)):
        for c in range(len(matrizIdent[0])):
            for k in range(len(matrizIdent)):
                matrizResultante[l][c] += matrizSoma[l][k] * matrizIdent[k][c]

    for r in matrizResultante:
        print(r)

def questao4(): #falta essa
    print('Questao 4: calcule matrizA * matrizA-¹= In')
    matrizA = [[2,1],[-3,4]]
    matrizAi = [[0,0],[0,0]]
    matrizAi = [[4/11,-1/11],[3/11,2/11]]
    matrizResultante = [[0,0],[0,0]]
    
    determinante = matrizA[0][0] * matrizA[1][1] - matrizA[0][1] * matrizA[1][0]
    matrizAi[0][0] = matrizA[1][1]
    matrizAi[0][1] = matrizA[1][0]
    matrizAi[1][0] = matrizA[0][1]
    matrizAi[1][1] = matrizA[0][0]

    for l in range(len(matrizAi)):
        for c in range(len(matrizAi)):
            matrizAi[l][c] = matrizAi[l][c] / determinante

    for l in range(len(matrizA)):
        for c in range(len(matrizA[0])):
            for k in range(len(matrizA)):
                matrizResultante[l][c] += matrizA[l][k] * matrizAi[k][c]

    for n in matrizResultante:
        print(n)

selecao = 0
selecao = int(input("Selecione a questao:\n 1 - Questao 1 \n 2 - Questao 2 \n 3 - Questao 3 \n 4 - Questao 4 \n"))

if(selecao == 1):
    questao1()
elif(selecao == 2):
    questao2()
elif(selecao == 3):
    questao3()
elif(selecao == 4):
    questao4()