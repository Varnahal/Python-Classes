lista = [21,432,65,8,45,4,12321,2]
res = 0

for num in lista:
    if(num%2==0):
        res+=num

print(f"A soma da lista é: {res}")