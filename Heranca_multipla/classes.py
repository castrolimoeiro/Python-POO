class Eletronico:
    def __init__(self, nome):
        self._nome = nome
        self._ligado = False

    def ligar(self):
        if self._ligado:
            return
        print(f'{self._nome} está ligando...')
        self._ligado = True

    def desligar(self):
        if not self._ligado:
            return
        print('Desligando smartphone...')
        self._ligado = False


from Heranca_multipla.log import LogMixin


# HERANÇA MULTIPLA
class Smartphone(Eletronico, LogMixin):
    def __init__(self, nome):
        super().__init__(nome)
        self._conectado = False

    def conectar(self):
        if not self._ligado:
            info = f'{self._nome} não está ligado'
            print(info)
            self.log_error(info)
            return

        if self._conectado:
            error = f'{self._nome} já está conectado'
            print(error)
            self.log_error(error)
            return

        info = f'{self._nome} não está ligado'
        print(info)
        self.log_info(info)
        self._conectado = True

    def desconectar(self):
        if not self._conectado:
            error = f'{self._nome} não está conectado'
            print(error)
            self.log_error(error)
            return
        info = f'{self.nome} foi desconectado com sucesso'
        print(info)
        self.log_info(info)
        self._conectado = False
