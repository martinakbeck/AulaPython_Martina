# lista = atribui
# lista [] fatia a lista

lista = ["Água", "Peixe", "Golfinho", "Tubarão", "Estrela", "Baleia", "Concha", "Alga", "Siri"]
#indice    0        1          2          3

#recuperação elementos da lista
print(lista[2]) 
#         posicao

#pegar último elemento da lista
print(lista[-1]) #negativo vai de trás para frente
#--------------------------------------------------------
#pegar um pedaço da lista
#lista[inicio : fim+1 : incremento]
#peixe até golfinho
print(lista[1:3])
#água até golfinho
print(lista[0:3])
#agua até tubarão
print(lista[1:])
#--------------------------------------------------------

#pegar de dois em dois
print(lista[::2])
#pegar de três em três
print(lista[::3])
#pegar do tubarão ate concha de dois em dois
print(lista[3::2])
#inverter lista
print(lista[::-1])
#inverter a lista de dois em dois
print (lista[::-2])

#percorrer a lista
qdd = len(lista)
for i in range(qdd):
    print(lista[i])

 