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
        self.__pedency_table(id)
        self.__emails_list(id)
        self.stackedWidget_2.setCurrentIndex(1)
        self.stackedWidget.setCurrentIndex(1)

    def __pedency_table(self, companie_id):
        ids, data = self.db.pedency(companie_id)
        self.tableWidget_pedency.setColumnCount(len(data.keys()))
        self.tableWidget_pedency.setHorizontalHeaderLabels(data.keys())
        self.tableWidget_pedency.setRowCount(len(ids))

        for column, column_data in enumerate(data.values()):
            for row, value in enumerate(column_data):
                item = QTableWidgetItem()
                item.__setattr__('id', ids[row])
                item.setText(str(value))
                self.tableWidget_pedency.setItem(row, column, item)

    def __emails_list(self, companie_id):
        ids, data = self.db.emails(companie_id)
        for row, value in enumerate(data):
            item = QListWidgetItem()
            item.__setattr__('id', ids[row])
            item.setText(str(value))
            self.listWidget_email.addItem(item)

if __name__ == '__main__':
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec()