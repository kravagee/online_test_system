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

        self.rights = []
        self.wrongs = []

        try:
            for i in tasks:
                if anwsers[i[0]]:
                    if anwsers[i[0]] == i[1]:
                        self.rights.append(tasks.index(i) + 1)
                    else:
                        self.wrongs.append(tasks.index(i) + 1)
                else:
                    self.wrongs.append(tasks.index(i) + 1)

            self.wrong.setText(str(len([str(i) for i in self.wrongs])))
            self.right.setText(str(len([str(i) for i in self.rights])))
            self.wrongNumbers.setText(', '.join([str(i) for i in self.wrongs]))
        except:
            pass

        con = sqlite3.connect('../db/users.db')
        cur = con.cursor()
        query = f'''UPDATE test_solutions SET wrong_anwsers = "{"".join(self.wrongs)}" AND 
        right_anwsers = "{"".join(self.rights)}"'''
        cur.execute(query)
        con.commit()
        con.close()

        self.backbtn.clicked.connect(self.back)

    def back(self):
        self.main = MainWindow.MainWindow(self.id)
        self.main.show()
        self.hide()