from PySide6.QtWidgets import (
    QMainWindow, QApplication, QCheckBox, QTreeWidgetItem, QListWidgetItem, QPushButton, QHBoxLayout, QFrame, QSizePolicy, QTableWidget, QTableWidgetItem
)

class PedencyTable (QTableWidget):
    def __init__(self, keys, data: dict[list]):
        super().__init__(columnCount= len(keys))
        self.setHorizontalHeaderLabels(keys)
        # self.reference = {
        #     'type' : self.valid_type
        # }
        
        ids = data.pop('id_pending')
        self.setRowCount(len(ids))

        for column, column_data in enumerate(data.values()):
            for row, value in enumerate(column_data):
                item = QTableWidgetItem()
                item.__setattr__('id', ids[row])
                item.setText(str(value))
                self.setItem(row, column, item)

        pass

    def add(self):...