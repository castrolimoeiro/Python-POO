from Composicao.classes import *

cliente1 = Cliente('David', 31)
cliente1.insere_endereco('Limoeiro do N.', 'CE')

cliente2 = Cliente('Simone', 32)
cliente2.insere_endereco('Limoeiro do N.', 'CE')

cliente3 = Cliente('Zezo', 50)
cliente3.insere_endereco('Sao Paulo', 'SP')

print(cliente1.nome)
cliente1.lista_endereco()
del cliente1
print()

print(cliente2.nome)
cliente2.lista_endereco()
del cliente2
print()

print(cliente3.nome)
cliente3.lista_endereco()
del cliente3
