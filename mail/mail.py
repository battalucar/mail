# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mail.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(794, 614)
        font = QtGui.QFont()
        font.setPointSize(12)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label1 = QtWidgets.QLabel(self.centralwidget)
        self.label1.setGeometry(QtCore.QRect(10, 10, 201, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label1.setFont(font)
        self.label1.setObjectName("label1")
        self.lineEdit1 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit1.setGeometry(QtCore.QRect(220, 10, 461, 51))
        self.lineEdit1.setObjectName("lineEdit1")
        self.label2 = QtWidgets.QLabel(self.centralwidget)
        self.label2.setGeometry(QtCore.QRect(10, 80, 201, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label2.setFont(font)
        self.label2.setObjectName("label2")
        self.lineEdit2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit2.setGeometry(QtCore.QRect(220, 80, 461, 51))
        self.lineEdit2.setObjectName("lineEdit2")
        self.label3 = QtWidgets.QLabel(self.centralwidget)
        self.label3.setGeometry(QtCore.QRect(240, 150, 361, 31))
        self.label3.setObjectName("label3")
        self.lineEdit3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit3.setGeometry(QtCore.QRect(20, 190, 761, 51))
        self.lineEdit3.setObjectName("lineEdit3")
        self.label4 = QtWidgets.QLabel(self.centralwidget)
        self.label4.setGeometry(QtCore.QRect(30, 290, 71, 31))
        self.label4.setObjectName("label4")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(30, 520, 151, 51))
        self.pushButton.setObjectName("pushButton")
        self.label5 = QtWidgets.QLabel(self.centralwidget)
        self.label5.setGeometry(QtCore.QRect(230, 520, 401, 51))
        self.label5.setText("")
        self.label5.setObjectName("label5")
        self.label4_2 = QtWidgets.QLabel(self.centralwidget)
        self.label4_2.setGeometry(QtCore.QRect(370, 270, 51, 31))
        self.label4_2.setObjectName("label4_2")
        self.lineEdit4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit4.setGeometry(QtCore.QRect(420, 260, 361, 51))
        self.lineEdit4.setObjectName("lineEdit4")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(30, 330, 751, 171))
        self.textEdit.setObjectName("textEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 794, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.pushButton.clicked.connect(self.mail)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label1.setText(_translate("MainWindow", "Mail Adresiniz:"))
        self.label2.setText(_translate("MainWindow", "Şifreniz:"))
        self.label3.setText(_translate("MainWindow", "Göndermek İstediğiniz E-Posta Adresi:"))
        self.label4.setText(_translate("MainWindow", "Mesajınız:"))
        self.pushButton.setText(_translate("MainWindow", "Gönder"))
        self.label4_2.setText(_translate("MainWindow", "Konu:"))

    def mail(self):
        mesaj = MIMEMultipart()

        mesaj["From"] = self.lineEdit1.text()
        mesaj["To"] = self.lineEdit3.text()
        mesaj["Subject"] = self.lineEdit4.text()
        yazi = self.textEdit.toPlainText()

        mesaj_govdesi = MIMEText(yazi,"plain")
        mesaj.attach(mesaj_govdesi)

        try:
            mail = smtplib.SMTP("smtp.outlook.com",587)
            mail.ehlo()
            mail.starttls()
            mail.login(self.lineEdit1.text(),self.lineEdit2.text())
            mail.sendmail(mesaj["From"],mesaj["To"],mesaj.as_string())
            self.label5.setText("Mail başarıyla gönderilmiştir.")
            mail.close()
        except:
            self.label5.setText("Bir sorun oluştu. Mail gönderilemedi.")
            sys.stderr.flush()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

