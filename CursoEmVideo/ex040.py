al = float(input('digite sua altura'))
p = float(input('digite seu peso'))

imc = p/(al*al)

if imc <= 18.5:
    print(f'abaixo do peso, imc: {imc}')
elif imc <= 25:
    print(f'peso ideal, imc: {imc}')
elif imc <= 30:
    print(f'sobrepeso, imc: {imc}')
elif imc <= 40:
    print(f'obesidade, imc: {imc}')
else:
    print(f'obesidade morbida, imc: {imc}')