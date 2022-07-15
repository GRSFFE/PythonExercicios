print('============ LOJAS GUANABARA ============')
preco = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão
Qual é a opção?''')
opcao = int(input('Sua opção: '))
if opcao == 1:
    d1 = preco - (preco * 10 / 100)
    print(f'Sua compra de R${preco:.2f} vai custar R${d1:.2f} no final.')
elif opcao == 2:
    d2 = preco - (preco * 5 / 100)
    print(f'Sua compra de R${preco:.2f} vai custar R${d2:.2f} no final.')
elif opcao == 3:
    d3 = preco / 2
    print(f'Sua compra de R${preco:.2f} parcelada em 2x SEM JUROS vai sair em R${d3:.2f} por mês.')
elif opcao == 4:
    juros = preco + (preco * 20 / 100)
    parc = int(input('Quantas parcelas? '))
    d4 = juros / parc
    print(f'Sua compra será parcelada em {parc}x de R${d4:.2f} COM JUROS')
    print(f'Sua compra de R${preco:.2f} vai custar R${juros:.2f} no final.')
else:
    print('OPÇÃO INVÁLIDA de pagamento. Tente novamente!')
