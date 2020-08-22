# nota 9 a 10 - aprovado com louvor
# nota 7 a 9 - aprovado
# nota 5.5 a 7 - recuperação
# nota menor que 5.5 - reprovado

nota = float(input('Informe nota do aluno: '))

if nota >= 9 and nota <= 10:
    print('Aprovado com louvor')
elif nota >= 7 and nota < 9:
    print('Aprovado')
elif nota >= 5.5 and nota < 7:
    print('Recuperação')
elif nota >= 0 and nota < 5.5:
    print('Reprovado')      
else:
    print('Valor inválido')      