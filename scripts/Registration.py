import sqlite3

from PyQt6 import uic
from PyQt6.QtWidgets import QWidget
import AuthorizationWindow
import expansion
import MainWindow
import RegistrationUI

class Registration(QWidget, RegistrationUI.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.register_button.clicked.connect(self.register)
        self.back_button.clicked.connect(self.back)

    def register(self):
        """Метод для регистрации"""
        con = sqlite3.connect('../db/users.db')
        cur = con.cursor()
        log = self.login.text()
        result = cur.execute(f'SELECT username FROM users WHERE username="{log}"').fetchone()
        if result:
            self.statusbar.setText('Пользователь с таким именем уже существует!')
        else:
            if self.password.text() != self.repeat_password.text():
                self.statusbar.setText('Пароль не совпадает!')
            else:
                cur.execute(f'INSERT INTO users ("username", "hash_password") VALUES ("{log}", '
                            f'"{expansion.hasher.hash(self.password.text())}")')
                id = cur.execute(f'''SELECT id FROM users WHERE username="{log}"''').fetchall()[0]
                con.commit()
                con.close()
                self.mainwind = MainWindow.MainWindow(id[0])
                self.hide()
                self.mainwind.show()


    def back(self):
        """Метод для перенаправления на первое окно"""
        self.author = AuthorizationWindow.AuthorizationWindow()
        self.author.show()
        self.hide()