import random

ram = random.randint(1,4)

n1 = input("Nome do primeiro aluno:")
n2 = input("Nome do segundo aluno:")
n3 = input("Nome do terceiro aluno:")
n4 = input("Nome do quarto aluno:")


match ram:
    case 1:
        print(n1)
    case 2:
        print(n2)
    case 3:
        print(n3)
    case 4:
        print(n4)