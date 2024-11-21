import sqlite3

from PyQt6.QtWidgets import QWidget
import AuthorizationWindow
import expansion
import MainWindow
import LoginUI


class Login(QWidget, LoginUI.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.login.clicked.connect(self.login_func)
        self.back_button.clicked.connect(self.back)

    def login_func(self):
        """Метод для входа"""
        con = sqlite3.connect('../db/users.db')
        cur = con.cursor()
        try:
            log, pas = cur.execute(f'SELECT username, hash_password FROM users'
                                   f' WHERE username="{self.username.text()}"').fetchone()
            try:
                print(pas)
                if expansion.hasher.verify(pas, self.password.text()):
                    id = cur.execute(f'''SELECT id FROM users WHERE username="{log}"''').fetchone()[0]
                    con.close()
                    self.mainwind = MainWindow.MainWindow(id)
                    self.hide()
                    self.mainwind.show()
            except:
                self.statusbar.setText('Неверный пароль!')
        except:
            self.statusbar.setText('Пользователь не найден!')

    def back(self):
        """Метод для перенаправления на первое окно"""
        self.author = AuthorizationWindow.AuthorizationWindow()
        self.author.show()
        self.hide()
