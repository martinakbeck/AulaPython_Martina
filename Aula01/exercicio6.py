# Crie um programa que solicite ao cliente
# o nome do produto
# o preço do produto
# a quantidade
# e mostre usando o f-string

nome = input("Informe nome do produto: ")
preco = float(input("Informe preço do produto: "))
qtda = int(input("Informe quantidade do produto: "))

print(f'''Nome do produto: {nome}
Preço do produto: R${preco} 
Quantidade: {qtda}
Preço total: R${preco*qtda:.2f}''')
# :.2f significa 2 casa depois da virgula e o f significa float
