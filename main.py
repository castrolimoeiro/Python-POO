from classes import Pessoa

p1 = Pessoa('David', 31)
p2 = Pessoa('Noah', 6)


# p1.falar('POO')
# p2.comer('biscoito')
# print(p1.ano_atual)
# p2.get_ano_nascimento()
# p1.get_ano_nascimento()

p1 = Pessoa.por_ano_nascimento('Simone', 1988)
print(p1)
print(p1.nome, p1.idade)
p1.get_ano_nascimento()