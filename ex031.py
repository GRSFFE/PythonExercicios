d = float(input('Qual é a distância da sua viagem? '))
if d <= 200:
    passagem = 0.5 * d
else:
    passagem = 0.45 * d
print('Preço da passagem: R$ {:.2f}'.format(passagem))

