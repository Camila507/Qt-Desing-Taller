from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
import sys

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1037, 692)
        MainWindow.setStyleSheet("background-color: rgb(232, 237, 240);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 30, 121, 16))
        self.label.setStyleSheet("font: 8pt \"OCR A Extended\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 350, 71, 16))
        self.label_2.setStyleSheet("font: 8pt \"OCR A Extended\";")
        self.label_2.setObjectName("label_2")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(30, 380, 961, 221))
        self.frame.setStyleSheet("background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(0, 0, 0, 255), stop:0.19397 rgba(0, 0, 0, 255), stop:0.202312 rgba(122, 97, 0, 255), stop:0.495514 rgba(76, 58, 0, 255), stop:0.504819 rgba(255, 255, 255, 255), stop:0.79 rgba(255, 255, 255, 255), stop:1 rgba(255, 158, 158, 255));\n"
"background-color: rgb(219, 233, 239);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(20, 30, 81, 16))
        self.label_8.setStyleSheet("font: 9pt \"OCR A Extended\";")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.frame)
        self.label_9.setGeometry(QtCore.QRect(20, 100, 91, 16))
        self.label_9.setStyleSheet("font: 9pt \"OCR A Extended\";")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.frame)
        self.label_10.setGeometry(QtCore.QRect(430, 20, 181, 41))
        self.label_10.setStyleSheet("font: 9pt \"OCR A Extended\";")
        self.label_10.setObjectName("label_10")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_6.setGeometry(QtCore.QRect(630, 30, 221, 31))
        self.lineEdit_6.setStyleSheet("background-color: rgb(232, 237, 240);\n"
"font: 9pt \"OCR A Extended\";")
        self.lineEdit_6.setText("")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(760, 160, 151, 31))
        self.pushButton_2.setStyleSheet("background-color: rgb(232, 237, 240);\n"
"font: 9pt \"OCR A Extended\";")
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_7.setGeometry(QtCore.QRect(150, 30, 221, 31))
        self.lineEdit_7.setStyleSheet("background-color: rgb(232, 237, 240);\n"
"font: 9pt \"OCR A Extended\";")
        self.lineEdit_7.setText("")
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_8.setGeometry(QtCore.QRect(150, 90, 221, 31))
        self.lineEdit_8.setStyleSheet("background-color: rgb(232, 237, 240);\n"
"font: 9pt \"OCR A Extended\";")
        self.lineEdit_8.setText("")
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(30, 60, 961, 261))
        self.frame_2.setStyleSheet("background-color: rgb(219, 233, 239);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setGeometry(QtCore.QRect(20, 30, 191, 16))
        self.label_3.setStyleSheet("font: 9pt \"OCR A Extended\";")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame_2)
        self.label_4.setGeometry(QtCore.QRect(20, 80, 91, 16))
        self.label_4.setStyleSheet("font: 9pt \"OCR A Extended\";")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.frame_2)
        self.label_5.setGeometry(QtCore.QRect(20, 140, 91, 16))
        self.label_5.setStyleSheet("font: 9pt \"OCR A Extended\";")
        self.label_5.setObjectName("label_5")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(130, 70, 221, 31))
        self.lineEdit_2.setStyleSheet("background-color: rgb(232, 237, 240);\n"
"font: 9pt \"OCR A Extended\";")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_3.setGeometry(QtCore.QRect(130, 130, 221, 31))
        self.lineEdit_3.setStyleSheet("background-color: rgb(232, 237, 240);\n"
"font: 9pt \"OCR A Extended\";")
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit.setGeometry(QtCore.QRect(220, 20, 271, 31))
        self.lineEdit.setStyleSheet("background-color: rgb(232, 237, 240);\n"
"font: 9pt \"OCR A Extended\";")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.label_6 = QtWidgets.QLabel(self.frame_2)
        self.label_6.setGeometry(QtCore.QRect(430, 140, 91, 16))
        self.label_6.setStyleSheet("font: 9pt \"OCR A Extended\";")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.frame_2)
        self.label_7.setGeometry(QtCore.QRect(430, 80, 61, 16))
        self.label_7.setStyleSheet("font: 9pt \"OCR A Extended\";")
        self.label_7.setObjectName("label_7")
        self.pushButton = QtWidgets.QPushButton(self.frame_2)
        self.pushButton.setGeometry(QtCore.QRect(750, 210, 181, 31))
        self.pushButton.setStyleSheet("background-color: rgb(232, 237, 240);\n"
"font: 9pt \"OCR A Extended\";")
        self.pushButton.setObjectName("pushButton")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_5.setGeometry(QtCore.QRect(570, 70, 221, 31))
        self.lineEdit_5.setStyleSheet("background-color: rgb(232, 237, 240);\n"
"font: 9pt \"OCR A Extended\";")
        self.lineEdit_5.setText("")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_4.setGeometry(QtCore.QRect(570, 130, 221, 31))
        self.lineEdit_4.setStyleSheet("background-color: rgb(232, 237, 240);\n"
"font: 9pt \"OCR A Extended\";")
        self.lineEdit_4.setText("")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(20, 10, 991, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(20, 330, 981, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(10, 20, 20, 611))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(1000, 20, 20, 611))
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setGeometry(QtCore.QRect(20, 620, 991, 20))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1037, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Propietario"))
        self.label_2.setText(_translate("MainWindow", "Finca"))
        self.label_8.setText(_translate("MainWindow", "Cultivo:"))
        self.label_9.setText(_translate("MainWindow", "Municipio:"))
        self.label_10.setText(_translate("MainWindow", "Registro catastral:"))
        self.pushButton_2.setText(_translate("MainWindow", "Agregar Finca"))
        self.label_3.setText(_translate("MainWindow", "Documento identidad:"))
        self.label_4.setText(_translate("MainWindow", "Nombre:"))
        self.label_5.setText(_translate("MainWindow", "Tel/Cel:"))
        self.label_6.setText(_translate("MainWindow", "Apellido:"))
        self.label_7.setText(_translate("MainWindow", "Correo:"))
        self.pushButton.setText(_translate("MainWindow", "Agregar Propietario"))

    def agregarDatosPropietario(self):        
        documentoIdentidad = self.lineEdit.text()
        nombre = self.lineEdit_2.text()
        telCel = self.lineEdit_3.text()
        correo = self.lineEdit_5.text()
        apellido = self.lineEdit_4.text()

        if not documentoIdentidad or not nombre or not telCel or not correo or not apellido:
                QMessageBox.warning(MainWindow, "Advertencia", "No se ingresaron todos los datos del propietario")
        else: 
                QMessageBox.information(MainWindow, "Información", "Datos del propietario agregados correctamente")

    def agregarDatosFinca(self):        
        cultivo = self.lineEdit_7.text()
        municipio = self.lineEdit_8.text()
        registroCatastral = self.lineEdit_6.text()

        if not cultivo or not municipio or not registroCatastral:
                QMessageBox.warning(MainWindow, "Advertencia", "No se ingresaron todos los datos de la finca")
        else: 
                QMessageBox.information(MainWindow, "Información", "Datos de la finca agregados correctamente")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.pushButton.clicked.connect(ui.agregarDatosPropietario)
    ui.pushButton_2.clicked.connect(ui.agregarDatosFinca)

    MainWindow.show()
    sys.exit(app.exec_())