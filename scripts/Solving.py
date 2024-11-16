import sqlite3

from PyQt6 import uic
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QWidget, QFileDialog
import expansion
import MainWindow
import datetime as dt

class Solving(QWidget):
    def __init__(self, userid, testname):
        super().__init__()
        uic.loadUi('../ui/Solving.ui', self)
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
            self.tabWidget.addTab(Task(self.tasks[i - 1]), f'Задание №{i}')


class Task(QWidget):
    def __init__(self, question):
        super().__init__()
        uic.loadUi('../ui/Task.ui', self)
        print(question)

        self.questiontext.setText(question[0])
        self.pixmap = QPixmap(question[-1]).scaled(self.Image.width(), self.Image.height())
        self.Image.setPixmap(self.pixmap)
