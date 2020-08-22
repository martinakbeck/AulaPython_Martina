# Exercicio 12
# 
# Crie um programa que peça 2 números.
# 
# Depois mostre um menu interativo contendo 5 operações matemáticas do python
# (adição, subtração, multiplicação, divisão e expoente)
# 
# Peça para o usuário escolher uma destas opções e mostre o resultado da operação escolhida.
menu = '''
Escolha a operação:
1- Soma
2- Subtração
3- Divisão
4- Multiplicação
5- Expoente
6- Sair: '''

while True:
    op = input(menu)

    num1 = int(input('Informe um valor: '))
    num2 = int(input('Informe outro valor: '))
    if op == '1':
        print(f'Soma: {num1+num2}')
    elif op == '2':
        print(f'Subtração = {num1-num2}')
    elif op == '3':
        if num2 == '0':
            print('Divisão não pode ser feita')
        else:
            print(f'Divisão = {num1/num2}')
    elif op == '4':
        print(f'Multiplicação = {num1*num2}')
    elif op == '5':
        print(f'Expoente = {num1**num2}')
    elif op == '6':
        print('Fim do programa')
        break
   









