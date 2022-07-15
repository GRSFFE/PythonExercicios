casa = float(input('Valor da casa? R$'))
sal = float(input('Salário do comprador? R$'))
anos = int(input('Quantos anos de financiamento? '))
prest = casa / (anos * 12)
minimo = sal * 30 / 100
print('Para pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f}'.format(casa, anos, prest))
if prest <= minimo:
    print('Empréstimo pode ser CONDEDIDO!')
else:
    print('Empréstimo NEGADO!')
