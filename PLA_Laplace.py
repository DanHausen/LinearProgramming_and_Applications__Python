# Dan Hausen
import math
def questao1(matriz):
    print('Questao 1... selecionada')  

    determinante = 0
    diagonalPrincipal = 1
    diagonalSecundaria = 1
    # x = 0
    # row = 0
    # col = 0

    matriz = []
    subList = []

    linhas = int(input('Insira o numero de linhas... '))
    colunas = int(input('Insira o numero de colunas... '))

    if(linhas != colunas or linhas <= 0 or colunas <= 0):   # ? Verificacao se é matriz quadrada
        print('Não é possivel calcular o determinanate, a matriz não é quadrada')
    else:                                                   # ? Criação dos elementos da matriz
        if(linhas == 1):
            determinante = int(input('Insira o valor da matriz 1 x 1... '))
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

            elif(linhas >= 3):         
                determinante = 0
                for i in range(linhas):
                    newMatrix = matriz[1:,:]
                    for n in range(linhas):
                        newMatrix = newMatrix.remove[n][i]
                    determinante = determinante + math.pow(-1, 1+i+1) * matriz[0,i] * (questao1(newMatrix))
                return determinante

                # while x < linhas:
                #     if(matriz[0][x] != 0):
                #         matrix = []
                #         i_aux = 0
                #         j_aux = 0
                #         while row < linhas:
                #             while col < linhas:
                #                 if(col != x):
                #                     matrix.append(matriz[row][col])
                #                     j_aux += 1
                #                 col += 1
                #             i_aux += 1
                #             j_aux = 0
                #             row += 1       
                #         factor = (x % 2 == 0) if matriz[0][x] else -matriz[0][x]
                #         determinante = determinante + factor * (linhas - 1)
                #     x += 1
        print('A determinante é: ', determinante) 