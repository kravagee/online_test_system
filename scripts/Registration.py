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
                con.commit()
                con.close()
                id = cur.execute(f'''SELECT id FROM users WHERE username={log}''').fetchall()[0]
                self.mainwind = MainWindow.MainWindow(id)
                self.hide()
                self.mainwind.show()


    def back(self):
        self.author = AuthorizationWindow.AuthorizationWindow()
        self.author.show()
        self.hide()