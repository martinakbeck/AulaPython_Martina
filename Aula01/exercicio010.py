# Escreva um programa que peça para 
# o usuário o valor de a, b e c
# calcule o delta

# delta = b² - 4ac
# 

valor_a = int(input("Informe o valor de A: "))
valor_b = int(input("Informe o valor de B: "))
valor_c = int(input("Informe o valor de C: "))

print(f"O valor de delta é {(valor_b**2)-(4*valor_a*valor_c)}")
