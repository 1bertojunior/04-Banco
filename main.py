import sys
import os

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox
from PyQt5.QtCore import QCoreApplication, reset, showbase
from PyQt5.sip import setdestroyonexit

import hashlib

from Views.Login  import Login
from Views.Register import Register
from Views.Dashboard import Dashboard
from Views.Withdraw import Withdraw
from Views.Deposit import Deposit
from Views.Transfer import Transfer
from Views.Historic import Historic

from Classes.Banco import Banco
from Classes.Cliente import Cliente

def MD5hash(arg):
    result = ""
    if not(arg == ""):
        str = hashlib.md5()
        str.update(arg.encode('utf-8'))
        result = str.hexdigest()
    return result

def isEmpty(arg):
        return arg == ""

def operacao(op):
    if op:
        print('Operação realizada com sucesso.')
    else:
        print('Operação invalida!')

banco = Banco()

c1 = Cliente('João', 'Silva', '111', MD5hash('123'))
c2 = Cliente('Maria', 'Sousa', '222', MD5hash('sopademacaco2'))

banco.cria_conta('123', c1)
banco.cria_conta('321', c2)

# STYES
stylePopupErro = ("background-color: rgb(239, 41, 41); border-radius: 5px;")
stylePopupOk = ("background-color: rgb(0, 255, 123); border-radius: 5px;")

class Ui_Main(QtWidgets.QWidget):
    def setupUi(self, Main):
        Main.setObjectName('Main')
        Main.resize(640,480)

        self.QtStack = QtWidgets.QStackedLayout()

        self.stack0 = QtWidgets.QMainWindow()
        self.stack1 = QtWidgets.QMainWindow()
        self.stack2 = QtWidgets.QMainWindow()
        self.stack3 = QtWidgets.QMainWindow()
        self.stack4 = QtWidgets.QMainWindow()
        self.stack5 = QtWidgets.QMainWindow()
        self.stack6 = QtWidgets.QMainWindow()

        self.screenLogin = Login()
        self.screenLogin.setupUi(self.stack0)

        self.screenRegistration = Register()
        self.screenRegistration.setupUi(self.stack1)

        self.screenDash = Dashboard()
        self.screenDash.setupUi(self.stack2)

        self.screenDeposit = Deposit()
        self.screenDeposit.setupUi(self.stack3)

        self.screenHistoric = Historic()
        self.screenHistoric.setupUi(self.stack4)

        self.screenTransfer = Transfer()
        self.screenTransfer.setupUi(self.stack5)
        
        self.screenWithdraw = Withdraw()
        self.screenWithdraw.setupUi(self.stack6)

        self.QtStack.addWidget(self.stack0)
        self.QtStack.addWidget(self.stack1)
        self.QtStack.addWidget(self.stack2)
        self.QtStack.addWidget(self.stack3)
        self.QtStack.addWidget(self.stack4)
        self.QtStack.addWidget(self.stack5)
        self.QtStack.addWidget(self.stack6)


class Main(QMainWindow, Ui_Main):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self.setupUi(self)

        self.cpf = None

        # INIT
        # OCULTANDO POPUP DE MENSSAGEM
        self.hideFrameErro(self.screenLogin)
        self.hideFrameErro(self.screenRegistration)
        self.hideFrameErro(self.screenDash)
        self.hideFrameErro(self.screenWithdraw)
        self.hideFrameErro(self.screenDeposit)
        self.hideFrameErro(self.screenTransfer)
        self.hideFrameErro(self.screenHistoric)

        #BOTÕES
        #BTN FECHAR POPUP
        self.btnClosed(self.screenLogin)
        self.btnClosed(self.screenRegistration)
        self.btnClosed(self.screenDash)
        self.btnClosed(self.screenWithdraw)
        self.btnClosed(self.screenDeposit)
        self.btnClosed(self.screenTransfer)
        self.btnClosed(self.screenHistoric)

        
        #BTN VOLTAR
        self.screenRegistration.btn_back.clicked.connect(self.btnReturn)
        self.screenDash.btn_back.clicked.connect(self.btnReturn)        
        self.screenWithdraw.btn_back.clicked.connect(lambda: self.openScreen(2))
        self.screenDeposit.btn_back.clicked.connect(lambda: self.openScreen(2))
        self.screenHistoric.btn_back.clicked.connect(lambda: self.openScreen(2))
        self.screenTransfer.btn_back.clicked.connect(lambda: self.openScreen(2))




        # LOGIN
        self.screenLogin.btn_login.clicked.connect(self.btnLogin) 
        self.screenLogin.btn_register.clicked.connect(self.openScreenRegistration) 

        # CADASTRO
        self.screenRegistration.btn_registration.clicked.connect(self.btnRegistration)

        # DASH
        self.screenDash.btn_withdraw.clicked.connect(lambda: self.openScreen(6))
        self.screenDash.btn.clicked.connect(lambda: self.openScreen(3))
        self.screenDash.btn_transfer.clicked.connect(lambda: self.openScreen(5))
        self.screenDash.btn_historic.clicked.connect(self.initHistoric)
        
        # SACAR
        self.screenWithdraw.btn_withdraw.clicked.connect(self.btnWithdraw)

        # DEPOSITAR
        self.screenDeposit.btn_deposit.clicked.connect(self.btnDeposit)

        # TRANSFERIR
        self.screenTransfer.btn_transfer.clicked.connect(self.btnTransfer)


    def btnWithdraw(self):
        value = self.screenWithdraw.in_value.value()
        balance = 900
        
        if value > 0 and value <= balance:
            # banco.dic_contas[self.cpf].saldo -= 100
            self.showMenssage(self.screenWithdraw, "Saque realziado com sucesso!",1)
            self.screenWithdraw.in_value.setValue(0)
        elif value <= 0:
            self.showMenssage(self.screenWithdraw, "Valor inválido!")
        elif value > balance:
            self.showMenssage(self.screenWithdraw, "Saldo indisponivel!")
        
    
    def btnDeposit(self):
        value = self.screenDeposit.in_value.value()
        balance = 900

        if value > 0:
            balance += value
            self.showMenssage(self.screenDeposit, "Deposito realziado com sucesso!",1)
            self.screenDeposit.in_value.setValue(0)
        else:
            self.showMenssage(self.screenDeposit, "Valor inválido!")

    def btnTransfer(self):
        value = self.screenTransfer.in_value.value()
        destinationAccount = self.screenTransfer.in_num_account.text()
        balance = 900

        checkAccount = True

        if value > 0 and value <= balance:
            if destinationAccount != "":
                if checkAccount:
                    balance -= value
                    self.showMenssage(self.screenTransfer, "Transferência realziado com sucesso!",1)
                    self.screenTransfer.in_value.setValue(0)
                    self.screenTransfer.in_num_account.setText("")                    
                else:
                    self.showMenssage(self.screenTransfer, "Conta não encontrada!")
            else:
                self.showMenssage(self.screenTransfer, "Preencha o campo conta de destino!")
        else:
            self.showMenssage(self.screenTransfer, "Valor inválido ou saldo indiponivel!")


    def initHistoric(self):
        list_historic = ["Deposito R$100,00 em 15/10/2021", 
                        "Deposito R$70,00 em 15/10/2021",
                        "Deposito R$730,00 em 15/10/2021"]
        self.openScreen(4)
        msg = ""
        for i in list_historic:
            msg +=  i + "\n" 
        
        self.screenHistoric.text_historic.setText(msg)
        
    def btnLogin(self):
        cpf = self.screenLogin.in_cpf.text()
        password = self.screenLogin.in_password.text()
        password = MD5hash(password)

        if isEmpty(cpf) | isEmpty(password):
            msg = "Preencha todos os campos!"
            self.showMenssage(self.screenLogin, msg)
        else:
            if banco.login(cpf,password):
                self.cpf  = banco.dic_contas[cpf]
                self.openScreenDash()
            else:
                msg = "CPF ou senha incorretos!"
                self.showMenssage(self.screenLogin, msg)

    def btnRegistration(self):
        obj = self.screenRegistration
        name = obj.in_name.text()
        surname = obj.in_surname.text()
        cpf = obj.in_cpf.text()
        account = obj.in_account.text()
        password = obj.in_password.text()
        password = MD5hash(password)

        flagTypeMessage = 0
        msg = ""

        if isEmpty(name) or isEmpty(surname) or isEmpty(cpf) or isEmpty(account) or isEmpty(password):
            msg = "Preencha todos os campos!"
        else:
            if banco.getClientePorCpf(cpf):
                msg = "CPF já cadastrado!"
            else:
                if banco.checkNumDaConta(account):
                    msg = "Conta já cadastrada!"
                else:
                    c = Cliente(name, surname, cpf, password)
                    banco.cria_conta(account, c)
                    msg = "Cadastrado com sucesso!"
                    flagTypeMessage = 1
                    self.cpf = cpf
                    self.showMenssage(obj, msg,flagTypeMessage)
                    self.openScreen() 

        self.showMenssage(obj, msg,flagTypeMessage)              


    #FUNÇÕES
    def showMenssage(self, obj, msg="erro", flag=0):
        if flag == 0:
            obj.frame_erro.setStyleSheet(stylePopupErro)
        else:
            obj.frame_erro.setStyleSheet(stylePopupOk)

        obj.label_erro.setText(msg)
        obj.frame_erro.show()

    # ESCONDER FRAME ERRO
    def hideFrameErro(self, obj):
        obj.frame_erro.hide()
    # BOTÃO FECHAR POPUP
    def btnClosed(self, obj):
        obj.btn_x.clicked.connect(lambda: self.hideFrameErro(obj)) # CLOSED FRAME ERRO
    def btnBack(self, obj, i=0):
        self.QtStack.setCurrentIndex(i)
    def teste(self):
        print("teste click")
    
        
    def btnReturn(self, i=0):
        print("Teste")
        self.QtStack.setCurrentIndex(i)   
    def openScreen(self, i=0):
        self.QtStack.setCurrentIndex(i)
    def openScreenRegistration(self):
        self.QtStack.setCurrentIndex(1)
    def openScreenDash(self):
        self.QtStack.setCurrentIndex(2)
    


    



if __name__ == '__main__':
    app = QApplication(sys.argv)
    show_main = Main()
    sys.exit(app.exec_())




