qtd = eval(input("quantos deseja comprar?(preço unitario de 10 reais)"))

if(qtd <=10):
    print(f"O valor da compra é: {qtd*10} reais")
elif(qtd <=  20):
    print(f"O valor da compra é {(qtd*10)*0.9}")
else:
    print(f"O valor da compra é {(qtd*10)*0.8}")