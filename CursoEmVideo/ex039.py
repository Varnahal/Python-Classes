l1 = int(input('Digite o lado 1'))
l2 = int(input('Digite o lado 2'))
l3 = int(input('Digite o lado 3'))

if l1 == l2 and l2 == l3:
    print('equilatero')
elif (l1 == l2 and l2 != l3) or (l1 == l3 and l3 != l2) or (l3 == l2 and l2 != l1):
    print('isoceles')
elif l1 != l2 and l2 != l3:
    print('escaleno')
