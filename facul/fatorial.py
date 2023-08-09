def fat(n):
    f = 1
    for n in range(n,0,-1):
        f = f*(n)
    return f

print(fat(5))