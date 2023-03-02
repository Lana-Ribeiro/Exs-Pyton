import ordem
import random

x = int(input('Quantos números deseja testar?: '))
array = []

while x > 0:
    array.append(random.randint(-100,1000))
    x = x-1
print(array)
print(ordem.ordena_numeros(array))