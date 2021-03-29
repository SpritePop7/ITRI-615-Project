from PyQt5 import QtWidgets, QtGui, uic
from PyQt5.QtWidgets import QApplication, QWidget, QPlainTextEdit, QMainWindow, QRadioButton
import sys 
import pandas

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
    def runCrypto(self, main_window):
        #loading file and setting window to show file data before processing
        file_source = main_window.plainTextEdit_5.toPlainText()
        #print(file_source)
        file = open(file_source)
        file_data = file.read().replace("\n", " ")
        file.close()
        print(file_data)
        main_window.plainTextEdit_Plain.setPlainText(file_data)
        #selection made by used in UI
        #use link https://www.codespeedy.com/vigenere-cipher-using-python/ for vigenere example code

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
            #self.model.setFileName( fileName )
            #self.refreshAll()
            #self.appendPlainText(fileName)

    


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    sys.exit(app.exec_())