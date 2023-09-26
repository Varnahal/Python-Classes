import urllib.request

try:
    url= urllib.request.urlopen('http://www.pudding.com')
    print('O Site esta acessivel')
except Exception as e:
    print("Site inacessivel no momento. Erro:", e)