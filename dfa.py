import subprocess

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FullDFA(object):
    def setupUi(self, FullDFA):
        FullDFA.setObjectName("FullDFA")
        FullDFA.resize(978, 752)
        self.label = QtWidgets.QLabel(FullDFA)
        self.label.setGeometry(QtCore.QRect(0, 0, 981, 661))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("YiVdpYSeHp.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(FullDFA)
        self.pushButton.setGeometry(QtCore.QRect(70, 660, 231, 91))
        font = QtGui.QFont()
        font.setFamily("Amaranth")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_3 = QtWidgets.QPushButton(FullDFA)
        self.pushButton_3.setGeometry(QtCore.QRect(370, 660, 231, 91))
        font = QtGui.QFont()
        font.setFamily("Amaranth")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(FullDFA)
        self.pushButton_4.setGeometry(QtCore.QRect(660, 660, 231, 91))
        font = QtGui.QFont()
        font.setFamily("Amaranth")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")

        self.retranslateUi(FullDFA)
        QtCore.QMetaObject.connectSlotsByName(FullDFA)

    def retranslateUi(self, FullDFA):
        _translate = QtCore.QCoreApplication.translate
        FullDFA.setWindowTitle(_translate("FullDFA", "Project"))
        self.pushButton.setText(_translate("FullDFA", "Num Node"))
        self.pushButton_3.setText(_translate("FullDFA", "ID Node"))
        self.pushButton_4.setText(_translate("FullDFA", "Bracket Node"))
        self.pushButton.clicked.connect((lambda: subprocess.call([sys.executable, 'num.py'])))
        self.pushButton_3.clicked.connect((lambda: subprocess.call([sys.executable, 'id.py'])))
        self.pushButton_4.clicked.connect((lambda: subprocess.call([sys.executable, 'bracket.py'])))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FullDFA = QtWidgets.QWidget()
    ui = Ui_FullDFA()
    ui.setupUi(FullDFA)
    FullDFA.show()
    sys.exit(app.exec_())
