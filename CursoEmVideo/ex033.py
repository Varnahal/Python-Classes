a = int(input('digite o valor do primeiro lado: '))
b = int(input('digite o valor do segundo lado: '))
c = int(input('digite o valor do terceiro lado: '))



if ((abs(b - c) < a) and (a < (b + c))) and ((abs(a - c) < b) and (b < (a + c))) and ((abs(a - b) < c) and (c < (a + b))):
    print('triangulo')
else:
    print('not triangulo')

