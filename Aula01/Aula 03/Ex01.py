import circulo

pi = 3.14
raio = float(input("Informe o raio: "))
opcao = int(input("""Informe a opção
1 - Circuferencia
2 - Area
"""))

if opcao == 1:
    print(f"{circulo.circ(pi, raio)}")
elif opcao == 2:
    print(f"{circulo.area(pi,raio)}")    








