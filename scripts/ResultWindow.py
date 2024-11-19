import sqlite3
from idlelib.configdialog import changes

from PyQt6 import uic
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QWidget, QFileDialog
import MainWindow
import expansion


class ResultWindow(QWidget):
    def __init__(self, userid, anwsers, tasks):
        super().__init__()
        uic.loadUi('../ui/StatisticFirst.ui', self)
        self.id = userid

        self.right_count = 0
        self.wrong_count = 0
        self.wrongs = []

        try:
            for i in tasks:
                if anwsers[i[0]]:
                    if anwsers[i[0]] == i[1]:
                        self.right_count += 1
                    else:
                        self.wrong_count += 1
                        self.wrongs.append(tasks.index(i) + 1)
                else:
                    self.wrong_count += 1
                    self.wrongs.append(tasks.index(i) + 1)

            self.wrong.setText(str(self.wrong_count))
            self.right.setText(str(self.right_count))
            self.wrongNumbers.setText(', '.join([str(i) for i in self.wrongs]))
        except:
            pass

        self.backbtn.clicked.connect(self.back)

    def back(self):
        self.main = MainWindow.MainWindow(self.id)
        self.main.show()
        self.hide()