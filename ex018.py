import math
an = float(input('Digite o ângulo que você deseja: '))
seno = math.sin(math.radians(an))
cosseno = math.cos(math.radians(an))
tangente = math.tan(math.radians(an))
print('O ângulo de {} tem o seno de {:.2f}'.format(an, seno))
print('O ângulo de {} tem o cosseno de {:.2f}'.format(an, cosseno))
print('O ângulo de {} tem a tangente de {:.2f}'.format(an, tangente))

