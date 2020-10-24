class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nomeclasse = self.__class__.__name__

    def falar(self):
        print(f'{self.nomeclasse} está falando...')


#  Classe Cliente e Aluno estão herdando a classe Pessoa
class Cliente(Pessoa):
    def comprar(self):
        print(f'{self.nomeclasse} está comprando...')

    def falar(self):
        print('Estou em cliente')


class ClienteVIP(Cliente):
    def __init__(self, nome, idade, sobrenome):
        Pessoa.__init__(self, nome, idade)
        self.sobrenome = sobrenome

    def falar(self):
        Pessoa.falar(self)
        Cliente.falar(self)
        print(f'{self.nome} {self.sobrenome}')

    # def falar(self):
    #     Pessoa.falar(self)
    #     super().falar()  # chama primeiro a função de uma classe acima
    #     print(f'outra coisa qualquer...')


class Aluno(Pessoa):
    def estudar(self):
        print(f'{self.nomeclasse} está estudando...')
