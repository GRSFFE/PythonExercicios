precotot = totmil = menor = cont = 0
barato = ' '
print('_' * 20)
print('LOJA SUPER BARATÃO')
print('_' * 20)
while True:
    produto = str(input('Nome do produto: '))
    preco = float(input('Preço: R$'))
    cont += 1
    precotot += preco
    if preco > 1000:
        totmil += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('---------- FIM DO PROGRAMA ----------')
print(f'O total da compra foi R${precotot:.2f}')
print(f'Temos {totmil} produto custando mais de R$1000')
print(f'O produto mais barato foi {barato} que custa R${menor:.2f}')
