import colorama  
colorama.init()
print(colorama.Back.LIGHTMAGENTA_EX,'~'*30,colorama.Style.RESET_ALL)
print(f"{colorama.Back.LIGHTMAGENTA_EX}{'Sistema PyHelp':^32}{colorama.Style.RESET_ALL}")
print(colorama.Back.LIGHTMAGENTA_EX,'~'*30,colorama.Style.RESET_ALL)
while True:
    ajuda = input(f'{colorama.Back.LIGHTCYAN_EX} Oque deseja?["fim" termina o programa]{colorama.Style.RESET_ALL}')
    print(colorama.Back.GREEN)
    help(ajuda)
    print(colorama.Style.RESET_ALL)
    if ajuda == 'fim':
        print(colorama.Style.RESET_ALL)
        break