from functools import reduce

lista = [1,24,45,666,1,33,2]

print(reduce(lambda x, y: x+y,lista))