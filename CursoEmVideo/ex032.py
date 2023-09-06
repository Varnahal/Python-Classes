#n = int(input('digite um numero'))

n1 = 3
n2 = 2
n3 = 7

if n1> n2 and n1> n3:
    print(f'o maior numero é {n1}')
elif n2> n1 and n2> n3:
    print(f'o maior numero é {n2}')
elif n3> n1 and n3> n2:
    print(f'o maior numero é {n3}')

if n1< n2 and n1< n3:
    print(f'o menor numero é {n1}')
elif n2< n1 and n2< n3:
    print(f'o menor numero é {n2}')
elif n3< n1 and n3< n2:
    print(f'o menor numero é {n3}')