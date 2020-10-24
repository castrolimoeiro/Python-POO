from Agregacao.classes import *

carrinho = CarrinhoDeCompras()


p1 = Produto('Camiseta', 50)
p2 = Produto('Celular', 1500)
p3 = Produto('Calça', 120)

carrinho.inserir_produto(p1)
carrinho.inserir_produto(p2)
carrinho.inserir_produto(p3)

carrinho.lista_produto()
carrinho.soma_total()
print(carrinho.soma_total())
