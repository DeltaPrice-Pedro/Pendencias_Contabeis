from PySide6.QtWidgets import (
    QMainWindow, QApplication, QCheckBox, QTreeWidgetItem, QListWidgetItem, QPushButton, QHBoxLayout, QFrame, QSizePolicy, QTableWidgetItem
)
from PySide6.QtGui import (
  QColor, QBrush, Qt, QIcon, 
)

from window_pend import Ui_MainWindow
from database import DataBase
from pathlib import Path

class MainWindow(QMainWindow, Ui_MainWindow):
    
    icon_path = Path(__file__).parent / 'imgs' / '{0}_icon.png'

    def __init__(self, parent = None) -> None:
        super().__init__(parent)
        self.setupUi(self)
        self.db = DataBase()

        self.__fill_companies()
        self.__init_icons()
        self.listWidget_companie.itemDoubleClicked.connect(
            self.open_pedency
        )

    def __init_icons(self):
        icon_ref ={
            self.pushButton_add_func: 'add',
            self.pushButton_remove_func: 'remove'
        }
        for btn, icon_type in icon_ref.items():
            icon = QIcon()
            icon.addFile(str(self.icon_path).format(icon_type))
            btn.setIcon(icon)

    def __fill_companies(self):
        data = self.db.companies()
        for id, name in data.items():
            item = QListWidgetItem()
            item.setText(name)
            item.__setattr__('id', id)
            self.listWidget_companie.addItem(item)

    def open_pedency(self):
        item = self.listWidget_companie.selectedItems()[0]
        id = item.__getattribute__('id')

        self.pedency = self.__pedency(id)
        self.address = self.db.emails(id)
        self.stackedWidget_email.addWidget(self.address())

        self.stackedWidget_companie.setCurrentIndex(1)
        self.stackedWidget_email.setCurrentIndex(1)

    def __pedency(self, id):
        pedency = self.db.pedency(id)
        self.pushButton_add_func.clicked.connect(
            lambda: pedency.add()
        )
        self.pushButton_remove_func.clicked.connect(
            lambda: pedency.remove()
        )

        stacked_widget = pedency()
        stacked_widget.setParent(self.page_4)
        self.verticalLayout_3.addWidget(stacked_widget)
        return pedency

if __name__ == '__main__':
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec()