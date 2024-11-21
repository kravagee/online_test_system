import Registration
import Login
import AuthorizationUI

from PyQt6.QtWidgets import QWidget


class AuthorizationWindow(QWidget, AuthorizationUI.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.loginbtn.clicked.connect(self.login)
        self.registerbtn.clicked.connect(self.register)

    def register(self):
        """Метод для перенаправления на окно с регистрацией"""
        self.reg = Registration.Registration()
        self.reg.show()
        self.hide()

    def login(self):
        """Метод для перенаправления на окно с входом"""
        self.log = Login.Login()
        self.log.show()
        self.hide()