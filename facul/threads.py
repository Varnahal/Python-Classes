from threading import Thread
import time
def func1(n,m):    
    print(m)
    time.sleep(n)
    print("func1 finalizada")

def func2(n,m):
    print(m)
    time.sleep(n)
    print("func2 finalizada")
    
t1 = Thread(target=func1,args=(3,"Thread 1 iniciada"))

t2 = Thread(target=func2,args=(2,"Thread 2 iniciada"))
t1.start()
t2.start()
t1.join()
t2.join()



print("Programa finalizado")
