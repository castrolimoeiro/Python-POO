from CLasses_abstratas.classes.contapoupanca import ContaPoupanca
from CLasses_abstratas.classes.cc import ContaCorrente

cp = ContaPoupanca(1111, 2222, 0)
cp.depositar(10)
cp.sacar(11)

print('#' * 50)

cc = ContaCorrente(agencia=1111, conta=5555, saldo=500)
cc.sacar(600)
cc.depositar(1000)