n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1 + n2) / 2
print(f'Com essas notas, a média do aluno é {media:.1f}')
if media >= 5 and media < 7:
    print('O aluno está em RECUPERAÇÃO!')
elif media < 5:
    print('O aluno está REPROVADO!')
elif media >= 7:
    print('O aluno está APROVADO!')
