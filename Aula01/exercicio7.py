# Solicite ao usuário o nome do aluno
# as 4 notas e mostre a média junto com o 
# nome do aluno usando o f-string

nome = input("Informe nome: ")
nota1 = float(input("Informe Nota 1: "))
nota2 = float(input("Informe Nota 2: "))
nota3 = float(input("Informe Nota 3: "))
nota4 = float(input("Informe Nota 4: "))
total = (nota1+nota2+nota3+nota4)
print (f"""
Aluno:  {nome}
Nota 1: {nota1}
Nota 2: {nota2}
Nota 3: {nota3}
Nota 4: {nota4}
Média é: {total/4:.2f}

""")