#Cria uma lista vazia antes do for
gatinhos = [] #vai armazenar os nomes
# Cirar um loop para receber os nomes dos gatos
# for i in range (5):
#     nome = input("Digite o nome do gatinho: ")
#     gatinhos.append(nome)
#     print(gatinhos)
#----------------------------------------------------------
#O nome em cada linha

# for i in ["Chico", "Naue", "Bolota", "Frida", "Amora"]:
#     print(i)
#----------------------------------------------------------
# lista_numeros = [1, 9, 5, 7, 8, 2, 4, 3, 6]

# for i in lista_numeros:
#     multi = i*3
#     print(multi)

#----------------------------------------------------------
lista_idade = [12, 15, 20, 18, 19, 23, 45, 11, 24, 26]

for i in lista_idade:
    if i >= 18:
        print (f'{i} anos - Maior de idade')
    else:
        print(f'{i} anos - Menor de idade')
            


