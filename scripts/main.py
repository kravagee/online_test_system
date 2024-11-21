import AuthorizationWindow
from PyQt6.QtWidgets import QApplication
import sys


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    authorization = AuthorizationWindow.AuthorizationWindow()
    authorization.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
