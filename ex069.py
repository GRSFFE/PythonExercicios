print('_' * 20)
print(f'CADASTRE UMA PESSOA')
print('_' * 20)
conta = 0
somahomem = 0
somamulher = 0
while 'N':
    idade = int(input('Idade: '))
    if idade >= 18:
        conta += idade
    sexo = str(input('Sexo [M/F]: '))
    cont = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if 'Nn':
        print(f'Total de pessoas com mais de 18 anos: {conta}')
        print('Ao todo temos {} homens cadastrados')
        print('E temos {} mulheres cadastradas')
