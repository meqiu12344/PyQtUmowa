# Form implementation generated from reading ui file 'layout.ui'
#
# Created by: PyQt6 UI code generator 6.5.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(401, 652)
        self.label = QtWidgets.QLabel(parent=Dialog)
        self.label.setGeometry(QtCore.QRect(20, 20, 361, 71))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=Dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 120, 61, 31))
        self.label_2.setObjectName("label_2")
        self.name = QtWidgets.QLineEdit(parent=Dialog)
        self.name.setGeometry(QtCore.QRect(110, 120, 261, 31))
        self.name.setObjectName("name")
        self.label_3 = QtWidgets.QLabel(parent=Dialog)
        self.label_3.setGeometry(QtCore.QRect(30, 170, 61, 31))
        self.label_3.setObjectName("label_3")
        self.lastName = QtWidgets.QLineEdit(parent=Dialog)
        self.lastName.setGeometry(QtCore.QRect(110, 170, 261, 31))
        self.lastName.setObjectName("lastName")
        self.label_4 = QtWidgets.QLabel(parent=Dialog)
        self.label_4.setGeometry(QtCore.QRect(30, 220, 61, 31))
        self.label_4.setObjectName("label_4")
        self.pesel = QtWidgets.QLineEdit(parent=Dialog)
        self.pesel.setGeometry(QtCore.QRect(110, 220, 261, 31))
        self.pesel.setObjectName("pesel")
        self.label_5 = QtWidgets.QLabel(parent=Dialog)
        self.label_5.setGeometry(QtCore.QRect(30, 270, 61, 31))
        self.label_5.setObjectName("label_5")
        self.tel = QtWidgets.QLineEdit(parent=Dialog)
        self.tel.setGeometry(QtCore.QRect(110, 270, 261, 31))
        self.tel.setObjectName("tel")
        self.umowa = QtWidgets.QCheckBox(parent=Dialog)
        self.umowa.setGeometry(QtCore.QRect(250, 320, 121, 20))
        self.umowa.setObjectName("umowa")
        self.horizontalLayoutWidget = QtWidgets.QWidget(parent=Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(29, 359, 341, 60))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.save = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        self.save.setStyleSheet("padding: 10 0")
        self.save.setObjectName("save")
        self.horizontalLayout.addWidget(self.save)
        self.saveToFile = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        self.saveToFile.setStyleSheet("padding: 10 0")
        self.saveToFile.setObjectName("saveToFile")
        self.horizontalLayout.addWidget(self.saveToFile)
        self.label_6 = QtWidgets.QLabel(parent=Dialog)
        self.label_6.setGeometry(QtCore.QRect(30, 450, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.comboBox = QtWidgets.QComboBox(parent=Dialog)
        self.comboBox.setGeometry(QtCore.QRect(30, 490, 341, 31))
        self.comboBox.setObjectName("comboBox")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Umowa"))
        self.label_2.setText(_translate("Dialog", "Imię:"))
        self.label_3.setText(_translate("Dialog", "Nazwisko:"))
        self.label_4.setText(_translate("Dialog", "PESEL:"))
        self.label_5.setText(_translate("Dialog", "Nr. Tel:"))
        self.umowa.setText(_translate("Dialog", "Umowa o prace."))
        self.save.setText(_translate("Dialog", "Zapisz"))
        self.saveToFile.setText(_translate("Dialog", "Zapisz do pliku"))
        self.label_6.setText(_translate("Dialog", "Pracownicy:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())
