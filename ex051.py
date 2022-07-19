print('=' * 30)
print('     10 TERMOS DE UMA PA     ')
print('=' * 30)
n1 = int(input('Primeiro termo: '))
r1 = int(input('Razão: '))
d1 = n1 + (10 - 1) * r1
for c in range(n1, d1 + r1, r1):
    print(c, end=' -> ')
print('Acabou')
