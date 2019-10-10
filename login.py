# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form_login(object):
    def setupUi(self, Form_login):
        Form_login.setObjectName("Form_login")
        Form_login.setEnabled(True)
        Form_login.resize(400, 300)
        self.widget = QtWidgets.QWidget(Form_login)
        self.widget.setGeometry(QtCore.QRect(80, 60, 191, 108))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(0, 1, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.label.setFont(font)
        self.label.setLineWidth(0)
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.le_loginid = QtWidgets.QLineEdit(self.widget)
        self.le_loginid.setEnabled(True)
        self.le_loginid.setObjectName("le_loginid")
        self.horizontalLayout_3.addWidget(self.le_loginid)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.le_pws = QtWidgets.QLineEdit(self.widget)
        self.le_pws.setEnabled(True)
        self.le_pws.setText("")
        self.le_pws.setEchoMode(QtWidgets.QLineEdit.Password)
        self.le_pws.setObjectName("le_pws")
        self.horizontalLayout_2.addWidget(self.le_pws)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.bt_login = QtWidgets.QPushButton(self.widget)
        self.bt_login.setObjectName("bt_login")
        self.horizontalLayout.addWidget(self.bt_login)
        self.bt_clear = QtWidgets.QPushButton(self.widget)
        self.bt_clear.setObjectName("bt_clear")
        self.horizontalLayout.addWidget(self.bt_clear)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Form_login)
        self.bt_clear.clicked.connect(self.le_loginid.clear)
        self.bt_clear.clicked.connect(self.le_pws.clear)
        self.bt_clear.clicked.connect(self.le_loginid.setFocus)
        QtCore.QMetaObject.connectSlotsByName(Form_login)

    def retranslateUi(self, Form_login):
        _translate = QtCore.QCoreApplication.translate
        Form_login.setWindowTitle(_translate("Form_login", "登录窗口"))
        self.label.setText(_translate("Form_login", "用户登录"))
        self.label_2.setText(_translate("Form_login", "用户名："))
        self.le_loginid.setToolTip(_translate("Form_login", "<html><head/><body><p>请点击填写用户名</p></body></html>"))
        self.label_3.setText(_translate("Form_login", "密  码："))
        self.le_pws.setToolTip(_translate("Form_login", "<html><head/><body><p>请点击输入密码</p></body></html>"))
        self.le_pws.setWhatsThis(_translate("Form_login", "<html><head/><body><p><br/></p></body></html>"))
        self.bt_login.setToolTip(_translate("Form_login", "<html><head/><body><p>点击登录系统</p></body></html>"))
        self.bt_login.setText(_translate("Form_login", "登录"))
        self.bt_clear.setToolTip(_translate("Form_login", "<html><head/><body><p>取消操作</p></body></html>"))
        self.bt_clear.setText(_translate("Form_login", "重填"))
