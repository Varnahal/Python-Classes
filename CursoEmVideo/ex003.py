

def num1(s):
    n1 = input(f'digite o {s} numero: ')
    if n1.isnumeric():
        return n1
    else:
        print('o valor precisa ser um numero')
        return num1(s)



n1 = int(num1('primeiro'))
n2 = int(num1('segundo'))

print(n1+n2)