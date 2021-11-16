import datetime

from Classes.Conta import Conta
from Classes.db import DB
from Classes.credentials import _host, _dbname, _username, _password
from Classes.Historico import Historico


class Banco:

    dic_contas = {}

    def __init__(self):
        self.db = DB(_host, _dbname, _username, _password)
        self.result = []

    def getNumAccontById(self, id):
        result = None

        try:
            self.db.toConnect()
            #query = "SELECT a.id FROM client AS c INNER JOIN account AS a ON c.id = a.fk_client WHERE a.id = '" + id + "'"
            query = "SELECT a.num FROM client AS c INNER JOIN account AS a ON c.id = a.fk_client WHERE a.id = '" + id + "'"
            result = self.db.fetchOne(query)
            result = result[0]
            self.db.disconnect()
        except:
            result = False
        return result

    def getClientePorCpf(self, cpf) -> bool:
        result = None
        self.db.toConnect()
        query = "SELECT * FROM client WHERE cpf =  '" + cpf + "'"

        result = self.db.fetchOne(query)

        self.db.disconnect()

        if result != None:
            return True
        else:
            return False

    
    def checkNumDaConta(self, num) -> bool:
        result = None
        self.db.toConnect()
        query = "SELECT id FROM account WHERE num =  '" + num + "'"

        result = self.db.fetchOne(query)
        self.db.disconnect()

        if result != None:
            return True
        else:
            return False
    
    def getNumContaPorCpf(self, num):
        for i in self.dic_contas.keys():
            if self.dic_contas[i].numero == num:
                return self.dic_contas[i].cliente.cpf
        return ''

    def getIdAccountByNum(self, num):
        result = None

        try:
            self.db.toConnect()
            query = "SELECT a.id FROM client AS c INNER JOIN account AS a ON c.id = a.fk_client WHERE num = '" + num + "'"
            result = self.db.fetchOne(query)
            result = result[0]
            self.db.disconnect()
        except:
            result = False

        return result
            
    def cria_conta(self, num, cliente):
        
        self.db.toConnect()

        query = 'INSERT INTO client (name, surname, cpf, password) VALUES (%s, %s, %s, %s) '
        self.db.cursor(query, (cliente.nome, cliente.sobrenome, cliente.cpf, cliente.senha) )
            
        query = "SELECT id FROM client WHERE cpf = '" + cliente.cpf +"'"
        result = self.db.fetchOne(query)
        idClient = result[0]
            

        query = 'INSERT INTO account(num, fk_client) VALUES (%s, %s)'
        self.db.cursor(query, (num, idClient))
        
        self.id_account = self.getIdAccountByNum(num)
        historico = Historico(self.db, self.id_account)
        historico.setHistorico('DATA DE ABERTURA: '+str(historico.data_abertura))

            

        self.db.disconnect()
            
        return True
        

    def login(self, CPF, SENHA):
        result = None
        self.db.toConnect()
        query = "SELECT id FROM client WHERE cpf = '"+ CPF +"' AND password = '" + SENHA +"'" 
        result = self.db.fetchOne(query)
        
        if result == None:
            return False
        else:
            self.id_account = self.getIdAccountByIdClient(str(result[0]))
            self.historico = Historico(self.db, self.id_account)
            
            self.db.disconnect()
            return True

    def getBalanceAccount(self, cpf):
        result = None

        self.db.toConnect()
        query = "SELECT a.balance, a.fk_client FROM client AS c INNER JOIN account AS a ON c.id = a.fk_client WHERE cpf = '" + cpf + "'"
        result = self.db.fetchOne(query)
        self.idClient = result[1]

        self.db.disconnect()

        if result == None:
            return -1
        else:
            return result[0]

    def getIdAccountByIdClient(self, idClient):
        result = None
        
        try:
            self.db.toConnect()
            query = "SELECT a.id FROM client AS c INNER JOIN account AS a ON c.id = a.fk_client WHERE a.fk_client = ' "+ idClient +"'"
            result = self.db.fetchOne(query)
            result = result[0]
            self.db.disconnect()
        except:
            result = False

        return result

    def saca(self, id, value, flag=0, destino=""):
        result = None
        
        try:
            self.db.toConnect()
            query = "UPDATE account SET balance = balance - %s WHERE fk_client = %s"
            self.db.cursor(query, (value, id))
            self.db.commit()
            if flag == 0:
                self.historico.setHistorico(f'SAQUE - R$ {value} - DATA: {datetime.date.today()}')
            else:
                idAccountDestiny = self.getIdAccountByNum(destino)
                historico = Historico(self.db, idAccountDestiny)
                numAccount = self.getNumAccontById(str(self.id_account))
                historico.setHistorico(f'TRANSFERENCIA - R$ {value} DE: {numAccount}- DATA: {datetime.date.today()}')
                self.historico.setHistorico(f'TRANSFERENCIA - R$ {value} PARA: {destino}- DATA: {datetime.date.today()}')

            # r = self.historico.setHistorico('DATA DE ABERTURA: ' + str(self.historico.data_abertura))
            self.db.commit()
            self.db.disconnect()
            result = True
        except:
            result = False

        return result

    def depositar(self, id, value):
        result = None
        
        try:
            self.db.toConnect()
            query = "UPDATE account SET balance = balance + %s WHERE fk_client = %s"
            self.db.cursor(query, (value, id))
            self.db.commit()
            self.historico.setHistorico(f'DEPOSITO - R$ {value} - DATA: {datetime.date.today()}')
            result = True
            self.db.disconnect()
        except:
            result = False

        return result

    def depositar2(self, num, value):
        result = None
        
        try:
            self.db.toConnect()
            query = "UPDATE account SET balance = balance + %s WHERE num = %s"
            self.db.cursor(query, (value, num))
            self.db.commit()
            # self.historico.setHistorico(f"""TRANSFERENCIA - R$ {value} CONTA DESTINO > {num}
            #                              - DATA: {datetime.date.today()}""")
            # id_account = self.getIdAccountByNum(num)
            # id_account = id_account[0]
            # historico = Historico(self.db, id_account)
            # historico.setHistorico(f'TRASFERENCIA RECEBIDA +R${value} DE {num}')
            # self.db.commit()
            self.db.disconnect()
            result = True
        except:
            result = False

        return result

    def getIdClientByNumAccount(self, num):
        result = None
        
        try:
            self.db.toConnect()
            query = "SELECT a.balance, a.fk_client FROM client AS c INNER JOIN account AS a ON c.id = a.fk_client WHERE num = '" + num + "'"
            result = self.db.fetchOne(query)
            result = result[1]
            self.db.disconnect()
        except:
            result = False

        return result


