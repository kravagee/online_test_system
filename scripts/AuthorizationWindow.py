import sqlite3
import Registration
import Login

from PyQt6 import uic
from PyQt6.QtWidgets import QWidget


class AuthorizationWindow(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('../ui/Authorization.ui', self)

        self.loginbtn.clicked.connect(self.login)
        self.registerbtn.clicked.connect(self.register)

    def register(self):
        self.reg = Registration.Registration()
        self.reg.show()
        self.hide()

    def login(self):
        self.log = Login.Login()
        self.log.show()
        self.hide()