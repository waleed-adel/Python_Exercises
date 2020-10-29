# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Print.ui'
##
## Created by: Qt User Interface Compiler version 5.14.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *

import sys

class Ui_Form(object):
    def setupUi(self, Form):
        if Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(395, 93)
        self.PushButton_Print = QPushButton(Form)
        self.PushButton_Print.setObjectName(u"PushButton_Print")
        self.PushButton_Print.setGeometry(QRect(240, 30, 111, 31))
        self.Text_LineEdit = QLineEdit(Form)
        self.Text_LineEdit.setObjectName(u"Text_LineEdit")
        self.Text_LineEdit.setGeometry(QRect(30, 30, 171, 31))
        self.Text_LineEdit.setFocusPolicy(Qt.StrongFocus)

        self.retranslateUi(Form)
        self.PushButton_Print.clicked.connect(self.MyFunction)

        QMetaObject.connectSlotsByName(Form)
    # setupUi
    
    # A Function written By me that's Called When PushButton Is Clicked
    def MyFunction(self):
      print(self.Text_LineEdit.text())
      self.Text_LineEdit.clear()
    # MyFunction
    
    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Simple_Tool", None))
        self.PushButton_Print.setText(QCoreApplication.translate("Form", u"Print", None))
        self.Text_LineEdit.setText(QCoreApplication.translate("Form", u"Enter A Text", None))
    # retranslateUi


# Create the Qt Application
app = QApplication(sys.argv)
# Create the Qt Widget that will hold the Form/s
widget = QWidget()
# Create and show the form
form = Ui_Form()
form.setupUi(widget)
# Show what's inside the widget
widget.show()
# Run the main Qt loop
# Run the Application or execute it
app.exec_()
sys.exit()