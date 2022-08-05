numeros = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if 0 <= num <= 20:
        break
    print('Tente novamente. ', end='')
print(f'Você digitou o número {numeros[num]}')

# print(len(numeros))

# for c in numeros:
    # print(f'Eu vou contar {c}')

# for pos, c in enumerate(numeros):
    # print(f'Eu vou contar {c} na posição {pos}')

# for cont in range(0, len(numeros)):
    # print(f'eu vou contar {numeros[cont]} na posição {cont}')

# print(sorted(numeros)) - Esse comando mostra a variável em ordem.

# a = (2, 5, 4)
# b = (5, 8, 1, 2)
# c = a + b = (2, 5, 4, 5, 8, 1, 2)
# print(len(c)) pra mostrar quantos elementos tem na variável C.
# print(c.count(5)) Pra mostrar quantas vezes o 5 aparece.
# print(c.index(8)) Pra descobrir em que posição ta o 8.
