pt = int(input('digite o primeiro termo'))
r = int(input('digite a razão'))
i2 = 0
for i in range(pt,(pt+(9)*r)+r,r):
    print(i)
    i2+=1
    if i2 == 10:
        break