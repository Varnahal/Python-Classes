j = False
while j == False:
    s = str(input('Digite [M/F]')).upper()
    if s == 'M' or s == 'F':
        j = True
    else:
        j = False
print('finalmente!')