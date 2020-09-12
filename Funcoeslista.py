lista_compras = [10.00, 25.05, 55.30, 29.90, 0.5, 0.75, 5.95, 16.54, 78.00, 25,90, 4.55, 8.95]
#soma
print(sum(lista_compras))
total = sum(lista_compras)
print (total)

#menor
print(min(lista_compras))
menor = min(lista_compras)
print(menor)

#max
print(max(lista_compras))
maior = max(lista_compras)
print(maior)

#numero de elementos
print(len(lista_compras))
num_itens = len(lista_compras)
print(num_itens)

#média
media = sum(lista_compras)/ len(lista_compras)
print(media)

#adicionar itens
lista_compras.append(12.75)
lista_compras.append(5.60)
lista_compras.append(32.85)
print(lista_compras)

#inserir numa determinada posição
lista_compras.insert(2,2.75)
#                 posição, valor    
print(lista_compras)

#remover o ultimo valor e outro em determinada posição
lista_compras.pop()
lista_compras.pop(2) #posição
#se quiser salvar numa variável o valor removido
# nome = lista_compras.pop()
# nome2 = lista_compras.pop(2)
# print(f'{nome} \n {nome2}')

print(lista_compras)

#remover pelo valor
lista_compras.remove(90) #remove o primeiro que ele achar
print(lista_compras)

#ordenar do menor para maior  #sort só funciona com numero
lista_compras.sort()
print(lista_compras)

#ordenar do maior pelo menor
lista_compras.sort(reverse=True)
print(lista_compras)

#só inteverter a ordem
lista_compras.reverse()
print(lista_compras)






