
import sys
import os

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox
from PyQt5.QtCore import QCoreApplication, showbase
from PyQt5.sip import setdestroyonexit

from Login import Login
from Register import Register
from Dashboard import Dashboard
from Withdraw import Withdraw
from Deposit import Deposit
from Transfer import Transfer
from Historic import Historic

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

        # self.screenDash = Dashboard()
        # self.screenDash.setupUi(self.stack0)

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

        # INIT
        # OCULTANDO POPUP DE MENSSAGEM
        self.hideFrameErro(self.screenLogin)
        self.hideFrameErro(self.screenDash)
        self.hideFrameErro(self.screenRegistration)
        self.hideFrameErro(self.screenWithdraw)
        
        #BOTÕES
        #BTN FECHAR POPUP
        self.btnClosed(self.screenLogin)
        self.btnClosed(self.screenDash)
        self.btnClosed(self.screenRegistration)
        self.btnClosed(self.screenWithdraw)

        
        #BTN VOLTAR
        self.screenRegistration.btn_back.clicked.connect(self.btnReturn)
        self.screenDash.btn_back.clicked.connect(self.btnReturn)        
        self.screenWithdraw.btn_back.clicked.connect(lambda: self.openScreen(2))        



        # LOGIN
        # BTN LOGIN
        self.screenLogin.btn_login.clicked.connect(self.btnLogin) 
        # BTN CADASTRO
        self.screenLogin.btn_register.clicked.connect(self.openScreenRegistration) 
        
        # DASH
        # BTN SACAR
        self.screenDash.btn_withdraw.clicked.connect(lambda: self.openScreen(6))

        # SACAR
        # BTN SACAR
        self.screenWithdraw.btn_withdraw.clicked.connect(self.btnWithdraw)


    def btnWithdraw(self):
        value = self.screenWithdraw.in_value.value()
        balance = 900
        
        if value > 0 and value <= balance:
            balance -= value
            self.showMenssage(self.screenWithdraw, "Saque realziado com sucesso!",1)
            self.screenWithdraw.in_value.setValue(0)
        elif value <= 0:
            self.showMenssage(self.screenWithdraw, "Valor inválido!")
        elif value > balance:
            self.showMenssage(self.screenWithdraw, "Saldo indisponivel!")




        
    def btnLogin(self):
        cpf = self.screenLogin.in_cpf.text()
        account = self.screenLogin.in_num_account.text()

        if self.isEmpty(cpf) | self.isEmpty(account):
            msg = "Preencha todos os campos!"
            self.showMenssage(self.screenLogin, msg)
        else:
            # msg = "Logado com sucesso!"
            # self.showMenssage(self.screenLogin, msg,1)
            self.openScreenDash()
        

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
    def isEmpty(self,arg):
        return arg == ""
        
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



