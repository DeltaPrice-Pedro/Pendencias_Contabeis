from PySide6.QtWidgets import (
    QMainWindow, QApplication, QCheckBox, QTreeWidgetItem, QListWidgetItem, QPushButton, QHBoxLayout, QFrame, QSizePolicy
)

from window_pend import Ui_MainWindow
from database import DataBase

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent = None) -> None:
        super().__init__(parent)
        self.setupUi(self)
        self.db = DataBase()
        self.fill_companies()
        self.listWidget_companie.itemDoubleClicked.connect(
            self.open_pedency
        )

    def fill_companies(self):
        data = self.db.companies()
        for id, name in data.items():
            item = QListWidgetItem()
            item.setText(name)
            item.__setattr__('id', id)
            self.listWidget_companie.addItem(item)

    def open_pedency(self):
        item = self.listWidget_companie.selectedItems()[0]
        id = item.__getattribute__('id')
        #preencher treeWidget Pedency
        listPedency = self.db.pedency(id)
        self.verticalLayout_3.insertWidget(1, listPedency)
        #mudar métodos func
        self.pushButton_add_func.clicked.connect(
            listPedency.add
        )
        #preencher listWidget emails
        #mudar métodos func
        self.stackedWidget_2.setCurrentIndex(1)
        self.stackedWidget.setCurrentIndex(1)

if __name__ == '__main__':
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec()