while True:
    t = int(input('Escolha um número para ver sua tabuada: '))
    print('_' * 30)
    if t < 0:
        break
    for c in range(1, 11):
        print(f'{t} x {c} = {t * c}')
    print('_' * 30)
print('Programa ENCERRADO! Volte sempre!')
