expressao = str(input('Digite a expressão: '))
paberto = 0
pfechado = 0
for l in expressao:
    if l  == '(':
        paberto+=1
    elif l  == ')':
        pfechado+=1

if paberto == pfechado:
    print('Expressão válida')
else:
    print('Expressão inválida')