primeiro = float(input('Primeiro número: '))
segundo = float(input('Segundo número: '))
if primeiro > segundo:
    print('O PRIMEIRO valor é maior')
elif segundo > primeiro:
    print('O SEGUNDO valor é maior')
elif primeiro == segundo:
    print('Os dois valores são IGUAIS')