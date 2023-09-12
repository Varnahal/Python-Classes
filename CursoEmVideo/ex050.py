frase = str(input('digite um palindromo'))
frase1 = ''
frase = ''.join(frase.upper().split())


frase1 = frase[::-1]

print(frase)
print(frase1)

if frase1 == frase:
    print('palindromo')
else:
    print('não é palindromo')
