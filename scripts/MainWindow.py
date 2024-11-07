import sqlite3

from PyQt6 import uic
from PyQt6.QtWidgets import QWidget
import AuthorizationWindow
import CreateWindow
import expansion

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('../ui/Main.ui', self)

        self.logoutbtn.clicked.connect(self.logout)
        self.go_to_catalog.clicked.connect(self.go_to_catalog_func)
        self.go_to_create_tests.clicked.connect(self.go_to_create_tests_func)
        self.go_to_private_office.clicked.connect(self.go_to_private_office_func)

    def logout(self):
        self.auth = AuthorizationWindow.AuthorizationWindow()
        self.hide()
        self.auth.show()

    def go_to_catalog_func(self):
        pass

    def go_to_create_tests_func(self):
        self.crt = CreateWindow.CreateWindow()
        self.hide()
        self.crt.show()

    def go_to_private_office_func(self):
        pass