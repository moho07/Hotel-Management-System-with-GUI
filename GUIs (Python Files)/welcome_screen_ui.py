from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def __init__(self):
        self.setupUi(self)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(515, 889)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.checkin = QtWidgets.QPushButton(self.centralwidget)
        self.checkin.setGeometry(QtCore.QRect(110, 260, 301, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.checkin.setFont(font)
        self.checkin.setObjectName("checkin")
        self.checkout = QtWidgets.QPushButton(self.centralwidget)
        self.checkout.setGeometry(QtCore.QRect(110, 360, 301, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.checkout.setFont(font)
        self.checkout.setObjectName("checkout")
        self.guestlist = QtWidgets.QPushButton(self.centralwidget)
        self.guestlist.setGeometry(QtCore.QRect(110, 460, 301, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.guestlist.setFont(font)
        self.guestlist.setObjectName("guestlist")
        self.reservation = QtWidgets.QPushButton(self.centralwidget)
        self.reservation.setGeometry(QtCore.QRect(110, 160, 301, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.reservation.setFont(font)
        self.reservation.setObjectName("reservation")
        self.exit = QtWidgets.QPushButton(self.centralwidget)
        self.exit.setGeometry(QtCore.QRect(110, 660, 301, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.exit.setFont(font)
        self.exit.setObjectName("exit")
        self.Hotel_label = QtWidgets.QLabel(self.centralwidget)
        self.Hotel_label.setGeometry(QtCore.QRect(60, 60, 391, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Hotel_label.setFont(font)
        self.Hotel_label.setObjectName("Hotel_label")
        self.settings = QtWidgets.QPushButton(self.centralwidget)
        self.settings.setGeometry(QtCore.QRect(110, 560, 301, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.settings.setFont(font)
        self.settings.setObjectName("settings")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.checkin.setText(_translate("MainWindow", "Check In"))
        self.checkout.setText(_translate("MainWindow", "Check Out"))
        self.guestlist.setText(_translate("MainWindow", "Guest List"))
        self.reservation.setText(_translate("MainWindow", "Reservation"))
        self.exit.setText(_translate("MainWindow", "Exit"))
        self.Hotel_label.setText(_translate("MainWindow", "Hotel Management System"))
        self.settings.setText(_translate("MainWindow", "Settings"))