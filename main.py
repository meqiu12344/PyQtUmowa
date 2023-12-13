import re
import sys

from PyQt6.QtWidgets import QApplication, QDialog, QMessageBox
from layout import Ui_Dialog


class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.save.clicked.connect(self.get_user_data)

    def get_user_data(self):
        name = self.ui.name.text()
        last_name = self.ui.lastName.text()
        PESEL = self.ui.pesel.text()
        tel = self.ui.tel.text()

        def check_pesel(pesel):
            if (re.match('[0-9]{11}$', pesel)):
                pass
            else:
                return 0
            l = int(pesel[10])
            suma = ((l * int(pesel[0])) + (3 * int(pesel[l])) + (7 * int(pesel[2])) + (9 * int(pesel[3])) + (
            (l * int(pesel[4]))) + (3 * int(pesel[5])) + (7 * int(pesel[6])) + (9 * int(pesel[7])) + (
                                l * int(pesel[8])) + (3 * int(pesel[9])))
            kontrolka = 10 - (suma % 10)
            if kontrolka == 10:
                kontrolka = 0
            else:
                kontrolka = kontrolka

            if ((kontrolka == 10) or (kontrolka == 0)):
                return False
            else:
                return True

        if check_pesel(PESEL):
            self.ui.comboBox.addItem(name + " " + last_name)
            with open('imie_nazwisko.txt', 'a') as file:
                file.write(name + " " + last_name + '\n')
        else:
            msg_pesel_box = QMessageBox()
            msg_pesel_box.setText("Pesel został wypełniony nieprawidłowo.")
            msg_pesel_box.exec()

        if not tel.isnumeric():
            msg_pesel_box = QMessageBox()
            msg_pesel_box.setText("Nr telefonu został wypełniony nieprawidłowo.")
            msg_pesel_box.exec()

            return 0

        return {'name': name, 'last_name': last_name, 'pesel': PESEL, 'tel': tel}


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec())