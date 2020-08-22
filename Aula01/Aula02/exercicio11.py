
# Exercicio 11
# Faça um programa que peça o sexo do cliente. 
# 
# Se o cliente digitar 'F' deve aparecer a mensagem "Como você está bonita hoje!"
# 
# Se o cliente digitar 'M' deve aparecer a mensagem "Como você está forte? andou malhando?"
# 
# Se o cliente digitar qualquer outra coisa, deve aparecer a mensagem: "opção invalida!"
# 

sexo = input('''Informe o sexo
F: Feminino
M: Masculino''')

if sexo == "F":
    print('Como você está bonita hoje!')
elif sexo == "M":
    print ('Como você está forte? Andou malhando?')
else:
    print('Opção inválida')        
