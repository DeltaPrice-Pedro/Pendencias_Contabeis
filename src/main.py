from PySide6.QtWidgets import (
    QMainWindow, QApplication, QCheckBox, QTreeWidgetItem, QListWidgetItem, QPushButton, QHBoxLayout, QFrame, QSizePolicy
)
from PySide6.QtGui import (
    QIcon
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

        self.fill_companies()
        self.listWidget_companie.itemDoubleClicked.connect(
            self.open_pedency
        )

        icon_ref ={
            self.pushButton_add_func: 'add',
            self.pushButton_edit_func: 'edit',
            self.pushButton_remove_func: 'remove'
        }
        for btn, icon_type in icon_ref.items():
            icon = QIcon()
            icon.addFile(str(self.icon_path).format(icon_type))
            btn.setIcon(icon)

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
        #preencher Pedency
        self.__pedency_table(id)
        #preencher listWidget emails
        #mudar métodos email
        self.stackedWidget_2.setCurrentIndex(1)
        self.stackedWidget.setCurrentIndex(1)

    def __pedency_table(self, id):
        pedencyTable = self.db.pedency(id)
        self.verticalLayout_3.insertWidget(1, pedencyTable)
        #mudar métodos func
        self.pushButton_add_func.clicked.connect(
            pedencyTable.add
        )
        self.pushButton_edit_func.clicked.connect(
            pedencyTable.updt
        )
        self.pushButton_remove_func.clicked.connect(
            pedencyTable.remove
        )

if __name__ == '__main__':
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec()