from datetime import date
nasc = int(input('Ano de nascimento: '))
atual = date.today().year
idade = atual - nasc
print(f'O atleta tem {idade} anos.')
if idade <= 9:
    print('Classificação: Mirim')
elif idade >= 10 and idade <= 14:
    print('Classificação: Infantil')
elif idade >= 15 and idade <= 19:
    print('Classificação: Junior')
elif idade >= 20 and idade <= 25:
    print('Classificação: Sênior')
elif idade >= 26:
    print('Classificação: Master')
