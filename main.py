import subprocess

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):

    def gettextA(self):
        restorePoint = sys.stdout
        sys.stdout = open("StringA.txt", "w")
        print(self.textEdit.toPlainText())
        sys.stdout = restorePoint

    def gettextP(self):
        restorePoint = sys.stdout
        sys.stdout = open("StringP.txt", "w")
        print(self.textEdit.toPlainText())
        sys.stdout = restorePoint

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(840, 600)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(120, 80, 580, 120))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        # self.pushButton = QtWidgets.QPushButton(Form)
        # self.pushButton.setGeometry(QtCore.QRect(240, 360, 141, 71))
        # font = QtGui.QFont()
        # font.setFamily("Amaranth")
        # font.setPointSize(22)
        # font.setBold(True)
        # font.setWeight(75)
        # self.pushButton.setFont(font)
        # self.pushButton.setObjectName("pushButton")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(100, 270, 650, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(350, 360, 141, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(-160, -90, 1071, 691))
        self.label_2.setAutoFillBackground(False)
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("download (2).jpg"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_2.raise_()
        self.label.raise_()
        #self.pushButton.raise_()
        self.textEdit.raise_()
        self.pushButton_2.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Parser"))
        #self.pushButton.setText(_translate("Form", "Analyze"))
        self.pushButton_2.setText(_translate("Form", "Solve"))
        #self.pushButton.clicked.connect((lambda: self.gettextA()))
        #self.pushButton.clicked.connect((lambda: subprocess.call([sys.executable, 'lexical.py'])))
        self.pushButton_2.clicked.connect((lambda: self.gettextP()))
        self.pushButton_2.clicked.connect((lambda: subprocess.call([sys.executable, 'parse.py'])))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
