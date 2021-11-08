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
        return result

    def getHistorico(self):
        result = None
        try:
            query = "SELECT historic FROM historic WHERE fk_account =  '" + str(self.id_account) + "'"
            result = self.db.fetchAll(query)
        except:
            result = []
        return result
