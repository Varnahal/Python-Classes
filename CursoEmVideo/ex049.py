n = int(input('digite um numero'))
primo = True
for i in range(n-1,1,-1):
    if n%i == 0:
        primo = False
if primo:
    print('primo')
else:
    print('não é primo')