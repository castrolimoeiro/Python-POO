from classes import Pessoa
from produto import *

p1 = Pessoa('David', 31)
p2 = Pessoa('Noah', 6)


# p1.falar('POO')
# p2.comer('biscoito')
# print(p1.ano_atual)
# p2.get_ano_nascimento()
# p1.get_ano_nascimento()

# p1 = Pessoa.por_ano_nascimento('Simone', 1988)
# print(p1)
# print(p1.nome, p1.idade)
# p1.get_ano_nascimento()
# print(Pessoa.gera_id())
# print(p1.gera_id())

produto1 = Produto('Blusa', 50)
produto1.desconto(10)
print(produto1.nome, produto1.preco)

produto2 = Produto('Calça', 'R$150')
produto2.desconto(15)
print(produto2.nome, produto2.preco)

