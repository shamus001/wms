from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow,QMessageBox
import sys


from login import Ui_Form_login


class MainWindow(QMainWindow, Ui_Form_login):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__()
        self.setupUi(self)


    def login_click(self):
        
        QMessageBox.information(self,"tishixinxi","确定登录吗？")


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    w = MainWindow()
    w.bt_login.clicked.connect(w.login_click)
    w.show()
    sys.exit(app.exec_())