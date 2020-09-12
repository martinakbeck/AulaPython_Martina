#Soma

def soma(num1, num2):
    soma_funcao = num1+num2
    return soma_funcao

resultado = soma(3, 5)
print(resultado)  

def media(lista):
    media_funcao = sum(lista)/len(lista)
    return media_funcao

lista = [8.5, 9.5, 7.5, 6.6]
resultado_media = media(lista)

print(resultado_media)