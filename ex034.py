sal = float(input('Qual é o salário do funcionário? R$'))
if sal <= 1250:
    aumento = sal + (sal * 0.15)
else:
    aumento = sal + (sal * 0.10)
print('Quem ganhava R${:.2f} passa a receber R${:.2f} agora.'.format(sal, aumento))
