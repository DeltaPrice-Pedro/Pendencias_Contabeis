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
        self.tableWidget_pedency.itemDoubleClicked.connect(
            self.edit_pedency
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
        # self.verticalLayout_3.addWidget(stackedWidget_pedency)
        self.__pedency_table(id)
        self.__emails_list(id)
        self.stackedWidget_companie.setCurrentIndex(1)
        self.stackedWidget_email.setCurrentIndex(1)

    def __pedency_table(self, companie_id):
        self.tableWidget_pedency.clear()
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
        self.listWidget_email.clear()
        ids, data = self.db.emails(companie_id)
        for row, value in enumerate(data):
            item = QListWidgetItem()
            item.__setattr__('id', ids[row])
            item.setText(str(value))
            self.listWidget_email.addItem(item)

    def add_pedency(self):
        row_index = self.tableWidget_pedency.rowCount() + 1
        brush = QBrush(QColor(0, 234, 255, 255))
        brush.setStyle(Qt.BrushStyle.Dense1Pattern)
        for column_index in range(self.tableWidget_pedency.columnCount()):
            item = QTableWidgetItem()
            item.setBackground(brush)
            self.tableWidget_pedency.setItem(row_index, column_index, item)
        self.tableWidget_pedency.setRowCount(row_index)
        self.tableWidget_pedency.setCurrentCell(row_index, 0)

    def edit_pedency(self):
        self.stackedWidget_pedency.setCurrentIndex(1)

if __name__ == '__main__':
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec()