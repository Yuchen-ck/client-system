import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class Third(QTabWidget):
    def __init__(self):
        super(Third, self).__init__()
        DBstring = "mongodb+srv://root:kershaw1027@myfldb.tclbx48.mongodb.net/?retryWrites=true&w=majority"
        self.DBstring = DBstring
        self.initUI()

    def initUI(self):
        self.setWindowTitle('client訓練上傳系統')
        self.resize(400,200)
        self.clientNameEdit =  QLineEdit()
        self.clientNameEdit.setPlaceholderText('輸入模型名稱')
        self.clientTrainBtn = QPushButton('client訓練', self)
        self.logoutBtn = QPushButton('logout', self)
        self.systemLabel = QLabel(" ", self)
        self.timeLabel = QLabel(" ", self)
        # self.clientTrainBtn.setStyleSheet('''
        #                 background:#ff0;
        #                 color:#f00;
        #                 font-size:80px;
        #                 border:3px solid #000;
        #                 ''')

        self.inputLayout = QFormLayout()