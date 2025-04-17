from PySide6.QtWidgets import (
    QMainWindow, QApplication, QCheckBox, QTreeWidgetItem, QPushButton, QHBoxLayout, QFrame, QSizePolicy
)

from window_pend import Ui_MainWindow
from database import DataBase

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent = None) -> None:
        super().__init__(parent)
        self.setupUi(self)
        self.db = DataBase()

    def fill_companies(self):
        ...


if __name__ == '__main__':
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec()