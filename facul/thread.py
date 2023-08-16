from threading import Thread
import time

def func(n,m):
    print(m)
    time.sleep(n)
    print("final")

t = Thread(target=func,args=(2,"executando"))
t.start()
print("aguardando a execução da thread")
t.join()
print("thread finalizada com sucesso")
 