import sqlite3

from PyQt6 import uic
from PyQt6.QtWidgets import QWidget
import AuthorizationWindow
import expansion
import MainWindow

class Registration(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('../ui/Registration.ui', self)

        self.register_button.clicked.connect(self.register)
        self.back_button.clicked.connect(self.back)

    def register(self):
        con = sqlite3.connect('../db/users.db')
        cur = con.cursor()

        result = cur.execute(f'SELECT username FROM users WHERE username="{self.login.text()}"').fetchone()
        if result:
            self.statusbar.setText('Пользователь с таким именем уже существует!')
        else:
            if self.password.text() != self.repeat_password.text():
                self.statusbar.setText('Пароль не совпадает!')
            else:
                cur.execute(f'INSERT INTO users ("username", "hash_password") VALUES ("{self.login.text()}", '
                            f'"{expansion.hasher.hash(self.password.text())}")')
                con.commit()
                con.close()
                self.mainwind = MainWindow.MainWindow()
                self.hide()
                self.mainwind.show()


    def back(self):
        self.author = AuthorizationWindow.AuthorizationWindow()
        self.author.show()
        self.hide()