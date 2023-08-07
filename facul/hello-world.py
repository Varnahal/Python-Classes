print('Hello World')
nome = 'varnahal'
if(1<2):
    print(f"1 é menor que 2 {nome}")
print("1 é pebis que 2")

#Listas

array = [1,2,3,4,'arroz']
print(array[4])

#dicionarios
obj = {1:{'nome':'varnahal','idade':18},2:{'nome':'carlos','idade':25}}
print(f"cliente 1 = {obj[1]['nome']} com idade = {obj[1]['idade']}")
print(f"cliente 2 = {obj[2]['nome']} com idade = {obj[2]['idade']}")

#entrada de dados

num = eval(input("Entre com um numero inteiro"))

print(f'o resultado de {num} e 100 ={num+100}')


def gay():
    print('gay')


gay()
