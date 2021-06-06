
from Transposition import *
from Vigenere import *
from Vernam import *
from posixpath import expanduser
from PyQt5 import QtWidgets, QtGui, uic
#from PyQt5.QtCore import EncodedCbor
from PyQt5.QtWidgets import QApplication, QWidget, QPlainTextEdit, QMainWindow, QRadioButton
import sys 
import pandas
import binascii, os
import math

class Ui(QMainWindow):
    # Set connections from UI to functions here
    def __init__(self):
        super().__init__()
        self.init_ui()    

    def init_ui(self):
        #UI objects
        main_window = uic.loadUi('UserInterface_Alpha.ui', self)

        #Browse button actions
        self.button = self.findChild(QtWidgets.QPushButton, 'pushButton')
        self.button.clicked.connect(lambda: self.getfile(main_window))
        self.show()

        #Run button action
        self.button_run = self.findChild(QtWidgets.QPushButton, 'btn_Run')
        self.button_run.clicked.connect(lambda: self.runCrypto(main_window))

    # Own functions that are called from the UI
    def getfile(self, main_window):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        self.fileName, _ = QtWidgets.QFileDialog.getOpenFileName(
                        None,
                        "QFileDialog.getOpenFileName()",
                        "",
                        "All Files (*);;Python Files (*.py)",
                        options=options)
        if self.fileName:
            print( "setting file name: " + self.fileName )
            main_window.plainTextEdit_5.setPlainText(self.fileName)

    def runCrypto(self, main_window):
        #loading file and setting window to show file data before processing
        file_source = main_window.plainTextEdit_5.toPlainText()
        #print(file_source)
        name, extension = os.path.splitext(file_source)
        filename = name.rpartition('/')[2]
        print(filename)
        print(extension)

        file = open(file_source)
        file_data = file.read() #.replace("\n", " ")
        #plaintext = binascii.hexlify(file.read())
        file.close()
        print(file_data)
        #print(plaintext)
        main_window.plainTextEdit_Plain.setPlainText(file_data)
        key = main_window.plainTextEdit_4.toPlainText()
        #f = open("password.txt", 'w')
        #f.write(key)
        #f.close()

        #selection made by user in UI
        if main_window.rad_Vig.isChecked() & main_window.radioButton.isChecked():
            vigEncryptedText = vigenereEncrypt(self, main_window, key, file_data, filename, extension)
        if main_window.rad_Vig.isChecked() & main_window.radioButton_2.isChecked():
            vigDecryptedText = vigenereDecrypt(self, main_window, key, file_data, filename, extension)
        if main_window.rad_Ver.isChecked() & main_window.radioButton.isChecked():
            verEncryptedText = vernamEnc(self ,main_window, key, file_data, filename, extension)
        if main_window.rad_Ver.isChecked() & main_window.radioButton_2.isChecked():
            verDecryptedText = vernamDecr(self, main_window, key, file_data, filename, extension)
        if main_window.rad_Tra.isChecked() & main_window.radioButton.isChecked():
            traEncryptedText = transpositionEncrypt(self, main_window, key, file_data, filename, extension)
            print(traEncryptedText)
        
        #use link https://www.codespeedy.com/vigenere-cipher-using-python/ for vigenere example code


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    sys.exit(app.exec_())