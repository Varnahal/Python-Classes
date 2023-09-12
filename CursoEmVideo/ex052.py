p = []
for i in range(0,4):
    p.append(int(input('um peso')))
p = sorted(p)
print(p[len(p)-1])