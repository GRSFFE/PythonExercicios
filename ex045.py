from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Sua opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PÔ')
sleep(0.5)
print('-=' * 15)
print(f'O computador jogou {itens[computador]}')
print(f'O jogador jogou {itens[jogador]}')
print('-=' * 15)
if computador == 0: # Computador jogou PEDRA
    if jogador == 0:
        print('EMPATE!')
    elif jogador == 1:
        print('JOGADOR VENCE!')
    elif jogador == 2:
        print('COMPUTADOR VENCE!')
elif computador == 1: # Computador jogou PAPEL
    if jogador == 0:
        print('COMPUTADOR VENCE!')
    if jogador == 1:
        print('EMPATE!')
    if jogador == 0:
        print('JOGADOR VENCE!')
elif computador == 2: # Computador jogou TESOURA
    if jogador == 0:
        print('JOGADOR VENCE!')
    if jogador == 1:
        print('COMPUTADOR VENCE!')
    if jogador == 2:
        print('EMPATE!')
else:
    print('JOGADA INVÁLIDA!')