import time

def maior(* nums):
    print('-='*30)
    print('Analisando valores.....')
    for letra in nums:
        print(letra, end=' ', flush=True)  # 'end=''': não pula para a próxima linha
        time.sleep(0.2)
    print(f'Foram informados ao todo {len(nums)} valores')

    maior = 0
    for n in nums:
        if n > maior:
            maior = n
    print(f'O maior valor foi o {maior}')

maior(2,9,4,5,7,1)
maior(4,0,7)
maior(2,9,4,5,7,1)
maior(2,9,4,5,7,1)