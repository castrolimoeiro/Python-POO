from Associacao.associacao import *

escritor = Escritor('Joãozinho')
caneta = Caneta('Bic')
maquina = MaquinaDeEscrever()

escritor.ferramenta = maquina



print(caneta.marca)
maquina.escrever()

