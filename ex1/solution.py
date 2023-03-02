from maior_menor import maiormenor
import random

x = int(input('Quantos números deseja testar?: '))
array = []

while x > 0:
    array.append(random.randint(-100,100))
    x = x-1

print(array)
print(maiormenor(array))


