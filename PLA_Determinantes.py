# Dan Hausen

def questao1():
    print('Questao 1... selecionada')
    linhas = int(input('Insira o numero de linhas... '))
    colunas = int(input('Insira o numero de colunas... '))

    determinanate = 1
    diagonalPrincipal = 1
    diagonalSecundaria = 1

    multD1 = 1
    multD2 = 1
    multD3 = 1
    multE1 = 1
    multE2 = 1
    multE3 = 1

    resultDiagPrincipal = 0
    resultDiagSecundaria = 0
    matriz = [[],[]]
    matriz3 = [[0,0,0],[0,0,0],[0,0,0]]

    if(linhas != colunas):
        print('Nao e possivel calcular determinanate, a matriz nao e quadrada ')
    else:     
        if(linhas == 1):
            determinanate = int(input('Insira o valor da matriz 1x1'))

        elif(linhas == 2):
            print('Insira os valores da matriz %s x %s' % (linhas, colunas))
            for n in range(linhas):
                elementos = int(input('Insira o valor das linhas %s... ' % (n)))
                matriz[n].append(elementos)

            for c in range(colunas):
                elementos = int(input('Insira o valor das colunas %s... ' % (c)))
                matriz[c].append(elementos)

            for n in range(linhas):
                for c in range(colunas):
                    if(n == c):
                        diagonalPrincipal *= matriz[n][c]
                    else:
                        diagonalSecundaria *= matriz[n][c]
            determinanate = diagonalPrincipal - diagonalSecundaria
            print('Neste caso a determinanate é: ', determinanate)

        elif(linhas == 3):
            for n in range(linhas):          
                for c in range(colunas):
                    matriz3[n][c] = int(input('Insira o valor... '))

            for n in range(linhas):
                for c in range(colunas):
                    if(n == c):
                        multD1 *= matriz3[n][c]
                    elif(c == n+1 or c == n - 2):
                        multD2 *= matriz3[n][c] 
                    elif(c == n+2 or c == n - 1):
                        multD3 *= matriz3[n][c]

                    if(c + n == 2):
                        multE1 *= matriz3[n][c]
                    elif(c + n ==  0 or c + n == 3):
                        multE2 *= matriz3[n][c]
                    elif(c + n == 1 or c + n == 4):
                        multE3 *= matriz3[n][c]
        resultDiagPrincipal = multD1 + multD2 + multD3
        resultDiagSecundaria = (multE1 + multE2 + multE3) *-1
        determinanate = resultDiagPrincipal + resultDiagSecundaria
        print('A determinante é: ', determinanate)
        

def questao2():
    print('Questao 2... selecionada')
    determinanateA = 1

    multD1 = 1
    multD2 = 1
    multD3 = 1
    multE1 = 1
    multE2 = 1
    multE3 = 1

    matrizA = [[1,-1,0],[2,3,4],[0,1,-2]]
    matrizB = [[2,7,2],[8,-1,-3],[-1,9,5]]
    matrizAT = [[0,0,0],[0,0,0],[0,0,0]]
    matrizSoma = [[0,0,0],[0,0,0],[0,0,0]]
    matrizResultante = [[0,0,0],[0,0,0],[0,0,0]]


    for n in range(len(matrizA)):
                for c in range(len(matrizA)):
                    if(n == c):
                        multD1 *= matrizA[n][c]
                    elif(c == n+1 or c == n - 2):
                        multD2 *= matrizA[n][c] 
                    elif(c == n+2 or c == n - 1):
                        multD3 *= matrizA[n][c]

                    if(c + n == 2):
                        multE1 *= matrizA[n][c]
                    elif(c + n ==  0 or c + n == 3):
                        multE2 *= matrizA[n][c]
                    elif(c + n == 1 or c + n == 4):
                        multE3 *= matrizA[n][c]

    resultDiagPrincipal = multD1 + multD2 + multD3
    resultDiagSecundaria = (multE1 + multE2 + multE3) *-1
    determinanateA = resultDiagPrincipal + resultDiagSecundaria
    print('A determinante de A é: ', determinanateA)

    for l in range(len(matrizA)): #Soma
        for c in range(len(matrizB)):
            matrizAT[l][c] = matrizA[c][l]
            matrizSoma[l][c] = matrizB[l][c] + matrizAT[l][c]
            matrizResultante[l][c] = determinanateA * matrizSoma[l][c]
    for j in matrizAT:
        print(j)
    for r in matrizResultante:
        print(r)

selecao = 0
selecao = int(input("Selecione a questao:\n 1 - Questao 1 \n 2 - Questao 2\n"))

if(selecao == 1):
    questao1()
elif(selecao == 2):
    questao2()