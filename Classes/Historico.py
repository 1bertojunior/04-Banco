import datetime


class Historico:
    def __init__(self, db, id_account):
        self.data_abertura = datetime.datetime.today()
        self.db = db
        self.id_account = id_account

    def setHistorico(self, msg):
        result = None
        try:
            self.db.toConnect()
            query = 'INSERT INTO historic(historic, fk_account) VALUES (%s, %s)'
            self.db.cursor(query, (msg, self.id_account))

            self.db.commit()
            self.db.disconnect()
            result = True
        except:
            result = False
        return result

    def getHistorico(self):
        result = []
        try:
            self.db.toConnect()
            query = "SELECT historic FROM historic WHERE fk_account =  '" + str(self.id_account) + "'"
            result = self.db.fetchAll(query)
            self.db.disconnect()
        except:
            result = []
        return result
