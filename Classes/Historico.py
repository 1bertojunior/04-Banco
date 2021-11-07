import datetime


class Historico:
    def __init__(self, db, id_account):
        self.data_abertura = datetime.datetime.today()
        self.db = db
        self.id_account = id_account

    def setHistorico(self, msg):
        result = None
        try:
            query = 'INSERT INTO historic(historic, fk_account) VALUES (%s, %s)'
            self.db.cursor(query, (msg, self.id_account))

            self.db.commit()
            result = True
        except:
            result = False
        print('result in set his', result)
        return result

    def getHistorico(self, id_client):
        # "SELECT id FROM account WHERE num =  '" + num + "'" '" + id_client + "' ON a.id = a.fk_account
        print('ID getHistorico >> ', id_client)
        # query = "SELECT a.balance, a.fk_client FROM client AS c INNER JOIN account AS a ON c.id = a.fk_client WHERE cpf = '" + cpf + "'"
        query = "SELECT h.fk_account FROM account AS a INNER JOIN historic AS h WHERE id = '" + str(id_client) + "'"

        result = self.db.fetchOne(query)
        return result

        # pass
        # msg = f'Data de abertura: {self.data_abertura}'
        # self.transacoes.insert(0, 'Data de Abertura: ' + str(self.data_abertura))
        # return self.transacoes


