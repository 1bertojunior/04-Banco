import datetime


class Historico:
    def __init__(self):
        self.data_abertura = datetime.datetime.today()
        self.transacoes = []

    def getHistorico(self):
        #msg = f'Data de abertura: {self.data_abertura}'
        self.transacoes.insert(0, 'Data de Abertura: ' + str(self.data_abertura))
        return self.transacoes
