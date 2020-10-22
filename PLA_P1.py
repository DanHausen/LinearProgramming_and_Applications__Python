def MatrizTransposta():
    matriz = []
    linhas = int(input("Insira o número de linhas da matriz: "))
    colunas = int(input("Insira o número de colunas da matriz: "))

    for l in range(linhas):
        linha = []
        for c in range(colunas):
            elemento = int(input(f"Informe o dado do elemento [{l}][{c}]: "))
            linha.append(elemento)
        matriz.append(linha)
    mT = []    
    linhas = len(matriz[0])
    colunas = len(matriz)

    for l in range(linhas):
        linha = []
        for c in range(colunas):
            linha.append(matriz[c][l])
        mT.append(linha)
    print(f"Matriz T\n")
    for l in mT:
        print("{}".format(l))
    print("\n")

MatrizTransposta()
