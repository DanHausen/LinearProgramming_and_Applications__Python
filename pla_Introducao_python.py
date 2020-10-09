# Daniel Nordhausen de Faria

""" 1
Saulo Pescador, comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 6,00 por quilo excedente. Saulo precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que Saulo deverá pagar. Exiba os dados do programa com as mensagens adequadas.
"""
def questao1():
    limite_de_peso = 50
    print("Questao 1 selecionada.")
    pesoDoPeixe = float(input("Insira o peso em Kg do peixe... "))
    if(pesoDoPeixe > limite_de_peso):
        peso_Em_Excesso = pesoDoPeixe - limite_de_peso
        multa = peso_Em_Excesso * 6
        print("LIMITE DE PESO EXCEDIDO")
        print("KGs Excedidos: " , peso_Em_Excesso)
        print('Deve pagar uma multa de: ' , multa)
    else:
        print('Peso dentro do limite permitido: ' , pesoDoPeixe)

""" 2 
Faça um programa que deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros (108m²), que custam R$ 80,00 ou em galões de 3,6 litros (21,6m²), que custam R$ 25,00. Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
• comprar apenas latas de 18 litros;
• comprar apenas galões de 3,6 litros;
• misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.
"""

def questao2():
    print('Questao 2 selecionada.')
    galao = 21.6
    lata = 108
    tamanhoDaAreaASerPintada = float(input("Insira o tamanho da area em m² a ser pintada... "))

    galaoArredondado = (tamanhoDaAreaASerPintada//galao) + (tamanhoDaAreaASerPintada % galao > 0)
    lataArredondada = (tamanhoDaAreaASerPintada//lata) + (tamanhoDaAreaASerPintada % lata > 0)

    print('Pode comprar em latas de 18L: ', lataArredondada)
    print('Pode comprar em galões de 3,6L: ', galaoArredondado)

    if(tamanhoDaAreaASerPintada / lata >= 1):
        lataInt = tamanhoDaAreaASerPintada // lata
        sobraLata = ((tamanhoDaAreaASerPintada / lata) - lataInt) * lata
        print('Pode comprar: ', lataInt, " lata. E ", (sobraLata // galao) + (sobraLata % galao > 0), " galao")
    elif(tamanhoDaAreaASerPintada / lata < 1):
        print('Pode comprar: ', galaoArredondado, ' galao')

""" 3
As empresas Mineiro & Cia resolveram dar um aumento de salário aos seus colaboradores e te contrataram para desenvolver o programa que calculará os reajustes. Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério:
• salários até R$ 1.280,00 (incluindo): aumento de 20%
• salários entre R$ 1.280,00 e R$ 1.700,00: aumento de 15%
• salários entre R$ 1.700,00 e R$ 11.500,00: aumento de 10%
"""

def questao3():
    print('Questao 3, selecionada')
    salarioFinal = 0
    salarioAtual = float(input("Insira o salário atual do funcionário... "))
    if(salarioAtual > 0 and salarioAtual <= 1280):
        salarioFinal = salarioAtual + (salarioAtual * 0.2)
    elif(salarioAtual > 2180 and salarioAtual <= 1700):
        salarioFinal = salarioAtual + (salarioAtual * 0.15)
    elif(salarioAtual > 1700 and salarioAtual <= 11500):
        salarioFinal = salarioAtual + (salarioAtual * 0.1)
    else:
        print("Sem aumento, lamento!!")

""" 4
Uma cientista, lhe contratou para desenvolver um programa que lê um conjunto indeterminado de temperaturas, e informe ao final a menor e a maior temperaturas informadas, bem como a média das temperaturas.
"""

def questao4():
    print('Questao 4, selecionada')
    list = []
    sizeOfList = int(input('Insira a quantidade de numeros... '))
    for n in range(sizeOfList):
        numeros = int(input('Insira o numero... '))
        list.append(numeros)

    print('\nO maior número é: ', max(list), '\nO menor número é: ', min(list))

""" 5
Faça um programa em que carregue um dicionário com os modelos de cinco carros e o consumo desses carros, isto é, quantos quilômetros cada um desses carros faz com um litro de combustível. Calcule e mostre:
• O modelo do carro mais econômico;
• Quantos litros de combustível cada um dos carros cadastrados consome para percorrer uma distância de 1.000 quilômetros e quanto isto custará, considerando um que a gasolina custe R$ 4,25 o litro.
"""

def questao5():
    print('Questao 5, selecionada')
    dicioCarros = {
        "Tesla" : 15,
        "Ford" : 9,
        "Chevrolet" : 11,
        "Honda" : 8,
        "Volkswagen" : 12
    }    
    print("O carro que mais rende é: ", max(dicioCarros, key=dicioCarros.get))
    for key in dicioCarros:
        print(key, " consome: ", round(1000/dicioCarros[key]), "litros. \nIsso irá custar: R$", round((1000/dicioCarros[key]) * 4.25))


""" 6
Construa uma função que receba uma data no formato DD/MM/AAAA e devolva uma string no formato de mesPorExtenso de AAAA. E, também, valide a data e retorne NULL caso a data seja inválida.
"""

import datetime
def questao6():
    print('Questao 6, selecionada')
    dia = int(input('Insira um dia... '))
    mes = int(input('Insira um mes... '))
    ano = int(input('Insira um ano... '))
    if(dia < 0 or dia > 31):
        print('NULL. Invalid DAY')
    elif(mes < 0 or mes > 12):
        print('NULL. Invalid MONTH')
    else:
        data = datetime.datetime(ano, mes, dia)
        data.strftime('%d-%m-%Y')
        print('O mes inserido foi: ', data.strftime('%B'), '\nNo ano: ', data.strftime('%Y'))

""" 7
Faça um programa que converta da notação de 24 horas para a notação de 12 horas. Por exemplo, o programa deve converter 14:25 em 2:25 P.M. A entrada é dada em dois inteiros. Deve haver pelo menos duas funções: uma para fazer a conversão e uma para a saída. Registre a informação A.M./P.M. como um valor ‘A’ para A.M. e ‘P’ para P.M. Assim, a função para efetuar as conversões terá um parâmetro formal para registrar se é A.M. ou P.M. Inclua um loop que permita que o usuário repita esse cálculo para novos valores de entrada todas as vezes que desejar.
"""

def questao7():
    print('Questao 7, selecionada')
    i = 0
    limite = int(input('Insira o numero de repetições... '))
    while i < limite:
        horas = int(input('Insira as horas, de 0 a 24... '))
        minutos = int(input('Insira os minutos, de 0 a 60... '))

        if(horas > 13 and horas <= 24):
            horas - 12
            print(horas, ':', minutos, 'P.M.')
        elif(horas >= 0 and horas <= 12):
            print(horas, ':', minutos, 'A.M.')
        i += 1


""" 8
Faça um programa que permita ao usuário digitar o seu nome e em seguida mostre o nome do usuário de trás para frente utilizando somente letras maiúsculas. Dica: lembre−se que ao informar o nome o usuário pode digitar letras maiúsculas ou minúsculas.
"""

def questao8():
    print('Questao 8, selecionada')
    name = str(input('Insira seu nome.. '))    
    print(name.upper() [::-1])


""" 9
Uma empresa de 500 funcionários, está tendo problemas de espaço em disco no seu servidor de arquivos. Para tentar resolver este problema, o Administrador de Rede precisa saber qual o espaço ocupado pelos usuários, e identificar os usuários com maior espaço ocupado. Através de um programa, baixado da Internet, ele conseguiu gerar o seguinte arquivo, chamado "usuarios.txt":
alexandre 456123789, anderson 1245698456, antonio 123456456, carlos 91257581, cesar 987458 e rosemary 789456125

Neste arquivo, o nome do usuário possui 15 caracteres. A partir deste arquivo, você deve criar um programa que gere um relatório, chamado "relatório.txt", no seguinte formato:
Uso do espaço em disco pelos usuários
---------------------------------------------------------------------------------------
Nr. Usuário Espaço utilizado % do uso
1 alexandre 434,99 MB 16,85%
2 anderson 1187,99 MB 46,02%
3 antonio 117,73 MB 4,56%
4 carlos 87,03 MB 3,37%
5 cesar 0,94 MB 0,04%
6 rosemary 752,88 MB 29,16%
Espaço total ocupado: 2581,57 MB
Espaço médio ocupado: 430,26 MB
O arquivo de entrada deve ser lido uma única vez, e os dados armazenados em memória, caso sejam necessários, de forma a agilizar a execução do programa. A conversão do espaço ocupado em disco, de bytes para megabytes deverá ser feita através de uma função separada, que será chamada pelo programa principal. O cálculo do percentual de uso também deverá ser feito através de uma função, que será chamada pelo programa principal.
"""

import random
def questao9():
    print('Questao 9, selecionada')
    qtdeFuncionarios = 1
    funcionarios = ['Alexandre', 'Anderson', 'Antonio', 'Carlos', 'Cesar', 'Rosemary']
    espacoTotal = int(input('Insira o tamanho do armazenamento em MB... '))
    espacoRestante = espacoTotal
    for qtdeFuncionarios in funcionarios:
        n = random.randint(0, espacoRestante)
        espacoRestante -= n
        print(qtdeFuncionarios, n, 'MB', (n/espacoTotal) * 100, '%')
        
selecao = 0
selecao = int(input("Selecione a questao:\n 1 - Questao 1 \n 2 - Questao 2 \n 3 - Questao 3 \n 4 - Questao 4 \n 5 - Questao 5 \n 6 - Questao 6 \n 7 - Questao 7 \n 8 - Questao 8 \n 9 - Questao 9 \n"))

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
elif(selecao == 6):
    questao6()
elif(selecao == 7):
    questao7()
elif(selecao == 8):
    questao8()
elif(selecao == 9):
    questao9()
