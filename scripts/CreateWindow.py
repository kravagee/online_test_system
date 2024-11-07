import sqlite3

from PyQt6 import uic
from PyQt6.QtWidgets import QWidget
import expansion
import MainWindow

class CreateWindow(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('../ui/CreateWindow.ui', self)
        self.counter = 1
        self.task_count.display(self.counter)

        self.addImage.clicked.connect(self.add_image)
        self.backbtn.clicked.connect(self.back)
        self.endEdit.clicked.connect(self.end_edit)
        self.nextTask.clicked.connect(self.next_task)

    def add_image(self):
        pass

    def back(self):
        pass

    def end_edit(self):
        pass

    def next_task(self):
        pass