# Form implementation generated from reading ui file '.\UI\qrCodeUI.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.frame.setFont(font)
        self.frame.setAutoFillBackground(False)
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(parent=self.frame)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(17)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label, 0, QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignTop)
        self.frame_2 = QtWidgets.QFrame(parent=self.frame)
        self.frame_2.setMinimumSize(QtCore.QSize(762, 247))
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_2.setBaseSize(QtCore.QSize(0, 0))
        self.frame_2.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEdit = QtWidgets.QLineEdit(parent=self.frame_2)
        font = QtGui.QFont()
        font.setItalic(True)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.passwd_line = QtWidgets.QLineEdit(parent=self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setItalic(True)
        self.passwd_line.setFont(font)
        self.passwd_line.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.passwd_line.setObjectName("passwd_line")
        self.verticalLayout.addWidget(self.passwd_line)
        self.generate_btn = QtWidgets.QPushButton(parent=self.frame_2)
        self.generate_btn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.generate_btn.setObjectName("generate_btn")
        self.verticalLayout.addWidget(self.generate_btn, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.qr_image_frame = QtWidgets.QFrame(parent=self.frame_2)
        self.qr_image_frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.qr_image_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.qr_image_frame.setObjectName("qr_image_frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.qr_image_frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.qr_place = QtWidgets.QLabel(parent=self.qr_image_frame)
        self.qr_place.setText("")
        self.qr_place.setObjectName("qr_place")
        self.gridLayout_2.addWidget(self.qr_place, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.qr_image_frame)
        self.verticalLayout_2.addWidget(self.frame_2)
        self.frame_2.raise_()
        self.label.raise_()
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 31))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "GENERATE A QR-CODE WITH YOUR WIFI PASSWORD"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Enter your wifi name"))
        self.passwd_line.setPlaceholderText(_translate("MainWindow", "Enter your wifi password"))
        self.generate_btn.setText(_translate("MainWindow", "GENERATE"))
