def digite():
    try:
        num = int(input("Digite um numero:"))
        print(num)
    except ValueError:
        print("Valor digitado inválido")
        digite()
    
    
digite()

