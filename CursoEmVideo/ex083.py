alunos = []
aluno = []


while True:
    aluno.append(str(input('Nome: ')))
    aluno.append(float(input('Nota1: ')))
    aluno.append(float(input('Nota2: ')))

    alunos.append(aluno[:])

    aluno.clear()
    
    sair = str(input('deseja sair? ')).upper()
    if sair == 'S':
        break
print(f'{"No.":<5}{"Nome.":<20}{"Média.":<5}')
for i,p in enumerate(alunos):
    print(f'{i:<3} {p[0]:<20} {(p[1]+p[2])/2:<5}')

while True:
    n = int(input('de quem deseja a nota? para sair digite 999 '))
    if n == 999:
        break
    print(f'As notas de {alunos[n][0]} são {alunos[n][1:]}')