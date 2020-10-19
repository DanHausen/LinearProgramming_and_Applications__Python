# Dan Hausen

def questao1():
    print('Questao 1... selecionada')  

    determinante = 0
    subDeterminante = 0
    diagonalPrincipal = 1
    diagonalSecundaria = 1
    cofator = 1

    multD1 = 1
    multD2 = 1
    multD3 = 1
    multE1 = 1
    multE2 = 1
    multE3 = 1
    resultDiagPrincipal = 0
    resultDiagSecundaria = 0

    matriz = []
    subList = []

    linhas = int(input('Insira o numero de linhas... '))
    colunas = int(input('Insira o numero de colunas... '))

    if(linhas != colunas or linhas <= 0 or colunas <= 0):   # ! Verificacao se é matriz quadrada
        print('Não é possivel calcular o determinanate, a matriz não é quadrada')
    else:                                                   # ! Criação dos elementos da matriz
        if(linhas == 1):
            determinante = int(input('Insira o valor da matriz 1 x 1... '))
            cofator = determinante
        else:
            print('Insira os valores da matriz %s x %s' % (linhas, colunas))
            for n in range(linhas):
                for c in range(colunas):
                    elementos = int(input('Insira o valor do elemento %s x %s... ' % (n, c)))
                    subList.append(elementos)
                matriz.append(subList)
                #matriz.insert(len(matriz),subList)                     # ? Esta é uma outra forma de adicionar ao fim da lista
                for index, item in enumerate(matriz, start = 0):        # ? Serve para exibir a lista uma uma forma de tabela
                    print (item) 
                    if not index % 3:
                        print
                subList = []
                #subList.clear() # ? não funcionou adequadamente

            if(linhas == 2):        
                for n in range(linhas):
                    for c in range(colunas):
                        if(n == c):
                            diagonalPrincipal *= matriz[n][c]
                        else:
                            diagonalSecundaria *= matriz[n][c]
                determinante = diagonalPrincipal - diagonalSecundaria

            # ! Continuar a partir daqui

            elif(linhas >= 3):
                placeholder = linhas - 3
                n += placeholder
                c += placeholder
                for n in range(linhas):
                    for c in range(colunas):
                        if(n == c):
                            multD1 *= matriz[n][c]
                        elif(c == n+1 or c == n - 2):
                            multD2 *= matriz[n][c] 
                        elif(c == n+2 or c == n - 1):
                            multD3 *= matriz[n][c]

                        if(c + n == 2):
                            multE1 *= matriz[n][c]
                        elif(c + n ==  0 or c + n == 3):
                            multE2 *= matriz[n][c]
                        elif(c + n == 1 or c + n == 4):
                            multE3 *= matriz[n][c]

                    resultDiagPrincipal = multD1 + multD2 + multD3
                    resultDiagSecundaria = (multE1 + multE2 + multE3) *-1
                    determinante = resultDiagPrincipal + resultDiagSecundaria    
                subDeterminante += determinante
                placeholder -= 1
                while(placeholder >= 0):
                    for j in range(placeholder):
                        for i in range(placeholder):
                            if(i == placeholder):
                                elemento = (-1 ** (j+i)) * determinante
                                cofator += elemento
                    determinante = cofator
                    cofator = 0
                    placeholder -= 1
        print('A determinante é: ', determinante) 


def questao2():
    print('Voce selecionou a questao 2')

selecao = 0
selecao = int(input("Selecione a questao:\n 1 - Questao 1 \n 2 - Questao 2\n"))

if(selecao == 1):
    questao1()
elif(selecao == 2):
    questao2()