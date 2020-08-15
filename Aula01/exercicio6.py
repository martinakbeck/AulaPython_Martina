# Crie um programa que solicite ao cliente
# o nome do produto
# o preço do produto
# a quantidade
# e mostre usando o f-string

nome = input("Informe nome do produto")
preco = int(input("Informe preço do produto"))
qtda = int(input("Informe quantidade do produto"))

print(f"Nome do produto {nome}, preço do produto R${preco} e quantidade é {qtda}")