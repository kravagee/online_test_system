import sqlite3

from PyQt6 import uic
from PyQt6.QtWidgets import QWidget
import AuthorizationWindow
import expansion
import MainWindow

class Login(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('../ui/Login.ui', self)

        self.login.clicked.connect(self.login_func)
        self.back_button.clicked.connect(self.back)

    def login_func(self):
        con = sqlite3.connect('../db/users.db')
        cur = con.cursor()
        try:
            log, pas = cur.execute(f'SELECT username, hash_password FROM users'
                                   f' WHERE username="{self.username.text()}"').fetchone()
            try:
                if expansion.hasher.verify(pas, self.password.text()):
                    pass
            except:
                self.statusbar.setText('Неверный пароль!')
        except:
            self.statusbar.setText('Пользователь не найден!')
        con.close()
        self.mainwind = MainWindow.MainWindow()
        self.hide()
        self.mainwind.show()

    def back(self):
        self.author = AuthorizationWindow.AuthorizationWindow()
        self.author.show()
        self.hide()