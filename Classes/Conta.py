from Classes.Historico import Historico


class Conta:
    _total_contas = 0

    __slots__ = ['_numero', '_cliente', '_saldo', '_limite', '_historico']

    def __init__(self, numero, cliente, saldo, limite=100.0):
        self._numero = numero
        self._cliente = cliente
        self._saldo = saldo
        self._limite = limite
        self._historico = Historico()
        Conta._total_contas += 1

    @staticmethod
    def get_total_contas():
        return Conta._total_contas

    @property
    def numero(self):
        return self._numero

    @numero.setter
    def numero(self, new_numero):
        self._numero = new_numero

    @property
    def cliente(self):
        return self._cliente

    @cliente.setter
    def cliente(self, new_cliente):
        self._cliente = new_cliente

    @property
    def saldo(self):
        return self._saldo

    @property
    def limite(self):
        return self._limite

    @limite.setter
    def limite(self, new_limite):
        self._limite = new_limite

    @property
    def historico(self):
        return self._historico

    def deposita(self, valor):
        if valor < 0:
            return False
        self._saldo += valor
        self._historico.transacoes.append(f'Deposito de R$ {valor}.')
        return True

    def saca(self, valor):
        if self._saldo < valor:
            return False
        self._saldo -= valor
        self._historico.transacoes.append(f'Saque de R$ {valor}.')
        return True

    def extrato(self):
        print(f'Numero: {self._numero}\nSaldo: {self._saldo}')
        self._historico.transacoes.append('Tirou Extrato.')

    def transferir(self, destino, valor):
        if not self.saca(valor) or not destino.deposita(valor):
            return False
        self._historico.transacoes.append(f'Transferencia de R$ {valor}.')
        return True
