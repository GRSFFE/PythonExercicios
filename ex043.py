peso = float(input('Qual é seu peso? (kg) '))
altura = float(input('Qual a sua altura? (m) '))
imc = peso / (altura * altura)
print(f'O IMC dessa pessoa é de {imc:.1f}')
if imc < 18.5:
    print('Você está abaixo do peso!')
elif imc <= 25:
    print('Você está no peso ideal!')
elif imc <= 30:
    print('Você está com Sobrepeso!')
elif imc <= 40:
    print('Você está com Obesidade!')
else:
    print('CUIDADO! Você está com Obesidade Mórbida.')
