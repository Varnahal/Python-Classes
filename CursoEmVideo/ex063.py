from random import randint


vitorias = 0
while True:
    ai = randint(1,10)
    j = int(input('escolha um numero de 1 a 10: '))
    print('-----------------------------------------')
    parimpar = str(input('você escolhe par ou impar? [P/I]')).upper()
    print('-----------------------------------------')
    soma = ai+j

    if (soma % 2 == 0 and parimpar == 'P') or (soma % 2 != 0 and parimpar == 'I') :
        if(soma % 2 == 0 and parimpar == 'P'):
            print(f'você jogou {j} e a ai jogou {ai} e deu Par')
        elif(soma % 2 != 0 and parimpar == 'I'):
            print(f'você jogou {j} e a ai jogou {ai} e deu Impar')
        vitorias +=1
        print('Você venceu, Vamos jogar novamente...')
        print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
    else:
        if(soma % 2 == 0 and parimpar == 'I'):
            print(f'você jogou {j} e a ai jogou {ai} e deu Par')
        elif(soma % 2 != 0 and parimpar == 'P'):
            print(f'você jogou {j} e a ai jogou {ai} e deu Impar')
        print('Você perdeu!!!')
        print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
        break
print(f'você venceu, {vitorias} vezes')
