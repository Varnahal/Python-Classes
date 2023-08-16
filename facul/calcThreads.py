from time import sleep
from threading import Thread

def cubo(s,n,m):
    print(m)
    n =n**3
    sleep(s)
    print(f"execução finalizada, resultado do cubo:{n}")


def quadrado(s,n,m):
    print(m)
    n =n**2
    sleep(s)
    print(f"execução finalizada, resultado do quadrado:{n}")

t1 = Thread(target=cubo,args=(3,10,"iniciada thread 1"))
t2 = Thread(target=quadrado,args=(2,10,"iniciada thread 2"))

t1.start()
t2.start()

t1.join()
t1.join()

print("Fim da execução")
