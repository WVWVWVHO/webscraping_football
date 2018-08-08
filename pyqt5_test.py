import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtCore import QSize

class Uiform(QWidget):
    def __init__(self, WebscrapApp):
        super().__init__()
        self.title = 'Football'
        self.left = 10
        self.top = 50
        self.width = 640
        self.height = 480
        self.initUI(WebscrapApp)

    def initUI(self, WebscrapApp):
        self.setWindowTitle(self.title)
        #self.setGeometry(self.left, self.top, self.width, self.height)
        self.setMinimumSize(QSize(320, 140))

        self.nameLabel = QLabel(self)
        self.nameLabel.setText('Website:')
        self.line = QLineEdit(self)

        self.line.move(80, 20)
        self.line.resize(200, 32)
        self.nameLabel.move(20, 20)

        pybutton = QPushButton('Download Data', self)
        pybutton.clicked.connect(WebscrapApp.on_click)
        pybutton.resize(200, 32)
        pybutton.move(80, 60)

        self.show()

    @pyqtSlot()
    def on_click(self):
        print('PyQt5 button click')
        self.show()


'''if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Uiform()
    sys.exit(app.exec_())'''