# Dan Hausen

#! Questao 1

def questao1():
    print('Questao 1, selecionada')
    name = str(input('Insira seu nome.. '))    
    print(name.upper() [::-1])

#! Questao 2
def questao2():
    print('Questao 2, selecionada')
    somaImpost(10,100)

def somaImpost(taxaImposto, custo):
    taxaImposto = taxaImposto / 100
    custo = custo + (custo*taxaImposto)
    print(custo)    

#! Questao 3

def questao3():
    print('Questao 3, selecionada')
    n = 0
    name = str(input('Insira o nome...'))
    for n in name:
        print(n)

#! Questao 4 - em progresso

def questao4():
    print('Questao 4, selecionada')
    cpf = str(input('Insira o CPF...'))
    tamanho_cpf = len(str(cpf))


#! Questao 5

def questao5():
    print('Questao 5, selecionada')


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