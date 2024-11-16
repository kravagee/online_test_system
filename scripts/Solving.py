import sqlite3

from PyQt6 import uic
from PIL.ImageQt import QImage
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QWidget, QFileDialog
import expansion
import MainWindow
import datetime as dt

class Solving(QWidget):
    def __init__(self, userid, testname):
        super().__init__()
        uic.loadUi('../ui/Solving.ui', self)
        self.counter = 1
        self.id = userid

        con = sqlite3.connect('../db/users.db')
        cur = con.cursor()
        query = f'''SELECT tasks, views FROM tests WHERE testname = "{testname}"'''
        data = cur.execute(query).fetchone()
        self.views = data[-1]
        self.tasks = []
        for i in range(len(data) - 1):
            for j in data[i].split('??///??'):
                self.tasks.append(j.split('!!!!---!!!!'))

        for i in range(1, len(self.tasks) + 1):
            self.tabWidget.addTab(MainWindow.MainWindow(self.id), f'Задание №{i}')


class Task(QWidget):
    def __init__(self, question):
        super().__init__()
        uic.loadUi('../ui/Solving.ui', self)