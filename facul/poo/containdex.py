from Conta import Conta

c1 = Conta(1,"Varnahal",1234354543,0)
c2 = Conta(2,"Jooj",3654673252,0)
print(c1.showBalance())
print(c2.showBalance())
print("--------------------------------------")
c1.deposit(1000)
c1.deposit(1000)
c1.deposit(1000)
c1.deposit(1000)
c1.deposit(1000)
c1.deposit(1000)
print(c1.showBalance())
print(c2.showBalance())
print("--------------------------------------")
c1.transf(c2,500)

print(c1.showBalance())
print(c2.showBalance())
print(c1.extrato())
print("--------------------------------------")