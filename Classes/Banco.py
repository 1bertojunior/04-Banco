from Classes.Conta import Conta
from Classes.db import DB
from Classes.credentials import _host, _dbname, _username, _password


class Banco:

    dic_contas = {}

    def __init__(self):
        self.db = DB(_host, _dbname, _username, _password)
        self.db.toConnect()
        self.result = []

    def getClientePorCpf(self, cpf) -> bool:
        result = None
        query = "SELECT * FROM client WHERE cpf =  '" + cpf + "'"

        result = self.db.fetchOne(query)

        if result != None:
            return True
        else:
            return False

    
    def checkNumDaConta(self, num) -> bool:
        result = None
        query = "SELECT id FROM account WHERE num =  '" + num + "'"

        result = self.db.fetchOne(query)

        if result != None:
            return True
        else:
            return False
    
    def getNumContaPorCpf(self, num):
        for i in self.dic_contas.keys():
            if self.dic_contas[i].numero == num:
                return self.dic_contas[i].cliente.cpf
        return ''

            
    def cria_conta(self, num, cliente):
        conta = Conta(num, cliente, 100.0, 100.0)
        if not (self.dic_contas.get(conta.cliente.cpf)):

            query = 'INSERT INTO client (name, surname, cpf, password) VALUES (%s, %s, %s, %s) '
            self.db.cursor(query, (cliente.nome, cliente.sobrenome, cliente.cpf, cliente.senha) )
            
            query = "SELECT id FROM client WHERE cpf = '" + cliente.cpf +"'"
            result = self.db.fetchOne(query)
            idClient = result[0]
            

            query = 'INSERT INTO account(num, fk_client) VALUES (%s, %s)'
            self.db.cursor(query, (num, idClient))

            query = "SELECT * FROM account"
            result = self.db.fetchAll(query)        
            
            self.db.commit()
            
            return True
        else:
            return False

    def login(self, CPF, SENHA):
        result = None
        query = "SELECT id FROM client WHERE cpf = '"+ CPF +"' AND password = '" + SENHA +"'" 
        result = self.db.fetchOne(query)

        if result == None:
            return False
        else:
            return True

    def getBalanceAccount(self, cpf) -> int:
        result = None
        query = "SELECT a.balance, a.fk_client FROM client AS c INNER JOIN account AS a ON c.id = a.fk_client WHERE cpf = '" + cpf + "'"
        result = self.db.fetchOne(query)
        self.idClient = result[1]

        if result == None:
            return -1
        else:
            return result[0]

    def saca(self, id, value):
        result = None
        try:
            query = "UPDATE account SET balance = balance - %s WHERE fk_client = %s"
            self.db.cursor(query, (value, id))
            self.db.commit()
            result = True
        except:
            result = False

        return result

    def depositar(self, id, value):
        result = None
        try:
            query = "UPDATE account SET balance = balance + %s WHERE fk_client = %s"
            self.db.cursor(query, (value, id))
            self.db.commit()
            result = True
        except:
            result = False

        return result

    def depositar2(self, num, value):
        result = None
        try:
            query = "UPDATE account SET balance = balance + %s WHERE num = %s"
            self.db.cursor(query, (value, num))
            self.db.commit()
            result = True
        except:
            result = False

        return result

    def getIdClientByNumAccount(self, num):
        result = None

        try:
            query = "SELECT a.balance, a.fk_client FROM client AS c INNER JOIN account AS a ON c.id = a.fk_client WHERE cpf = '" + cpf + "'"
            result = self.db.fetchOne(query)
            result = result[1]
        except:
            result = False

        return result
