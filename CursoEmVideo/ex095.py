def fatorial(n = 1,  show = False):
    """"
     -> Calcula o fatorial de um valor
        int n: valor a calcular o fatorial
        (Opcional) bool show: determina se vai ser apresentado ou não o processo da conta 
    """
    
    f = 1
    if show:
        for i in range(n,1,-1):
            print(f'{i} X ',end='')
            f*=i
        print(f'{1} = ',end='')  
    else:
        for i in range(n,0,-1):
            f*=i
    
    return(f)

print(fatorial(int(input('digite um valor inteiro')),True))
help(fatorial)