# # 1) Crie uma função que receba 3 notas por parâmetro e 
# # retorne a média.
# def media (n1, n2, n3):
#     calculo = (n1 + n2 + n3)/3
#     return calculo

# print (media (6,5,7))
# #ou
# resultado = media(6,5,7)
# print(resultado)
# print()
# # 2) Crie uma função que receba uma lista de qualquer 
# # tamanho e retorne a média

# def media (lista):
#     calculo = sum(lista)/len(lista)
#     return calculo

# lista = [8,9,8,7,9,6]
# print(media(lista))

# print()

# 3) Crie 4 funções para as operações matemáticas (+, -, /, *)


from matematica import soma
from matematica import diminuicao
from matematica import divisao
from matematica import multiplicacao

# def soma (n1, n2):
#     total = n1 + n2
#     return total

# def diminuicao (n1, n2):
#     total = n1 - n2
#     return total

# def divisao (n1, n2):
#     total = n1 / n2
#     return total

# def multiplicacao (n1, n2):
#     total = n1 * n2
#     return total

# var1 = 5
# var2 = 10

# print(soma(var1,var2))
# print(diminuicao(var1,var2))
# print(divisao(var1,var2))
# print(multiplicacao(var1,var2))
# print()

# 4) Crie um programa que peça 2 números. 
# Depois crie um menu interativo que peça qual 
# operação matemática deseja realizar (+, -, /, *). 
# Utilize as funções criadas no exercício anterior e
# mostre o resultado da operação escolhida. 
var1 = int(input("Informe um valor: "))
var2 = int(input("Informe um outro valor: "))
op = int(input(''' Escolha uma operação
1 - Soma
2 - Diminuição
3 - Divisão
4 - Multiplicacao: '''))

if op==1:
    print(soma(var1,var2))
elif op==2:    
    print(diminuicao(var1,var2))
elif op==2:    
        print(divisao(var1,var2))
elif op==2:    
    print(multiplicacao(var1,var2))
else:
    print("Operação inválida")    

