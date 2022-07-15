n1 = float(input('Primeiro segmento: '))
n2 = float(input('Segundo segmento: '))
n3 = float(input('Terceiro segmento: '))
if n1 == n2 == n3:
    print('Os segmentos acima podem formar um triângulo EQUILÁTERO!')
elif n1 != n2 != n3 != n1:
    print('Os segmentos acima podem formar um triângulo ESCALENO!')
else:
    print('Os segmentos acima podem formar um triângulo ISÓSCELES')