from PySide6 import QtWidgets
from PySide6.QtCore import Qt
from PySide6.QtWidgets import  QWidget, QLabel
from PySide6 import QtGui
import sys

class LoadingScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(200,200)

        self.label = QLabel(self)
        self.label.setPixmap(QtGui.QPixmap('./images/images/loading.png'))
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.show()

    def startAnimation(self):
        pass

    def stopAnimation(self):
        self.close()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = LoadingScreen()
    sys.exit(app.exec_())