# Exercicio 13
# 
# Crie um programa que peça o nome do cliente, idade, endereço, email e telefone.
# 
# Depois crie um menu interativo com as seguintes opções: Dados, Endereço, Contato.
# 
# Se o usuário selecionar "Dados" deve aparecer o nome do cliente e a idade
# 
# Se o usuário selecionar "Endereço" deve aparecer o nome do cliente e o endereço
# 
# Se o usuário selecionar "Contato" deve aparecer o nome do cliente, email e o telefone

nome = input('Informe nome do cliente: ')
idade = input('Informe idade do cliente: ')
endereco = input('Informe endereço do cliente: ')
email = input('Informe e-mail do cliente: ')
telefone = input('Informe telefone do cliente: ')
op = input('''
Selecione
1- Dados
2- Endereço
3- Contato:
''')

if op == "1":
    print(f'Nome: {nome}, idade: {idade}')
elif op == "2":
    print(f'Nome: {nome}, Endereço: {endereco}')
elif op == "3":
    print(f'Nome: {nome}, E-mail: {email}, Telefone: {telefone}')        



