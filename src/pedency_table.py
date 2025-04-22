from PySide6.QtWidgets import (
  QTableWidget, QTableWidgetItem
)

class PedencyTable (QTableWidget):
    def __init__(self, id_companie: str, data: dict[list] | None):
        super().__init__(columnCount= len(data.keys()))
        self.setHorizontalHeaderLabels(data.keys())
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
    def updt(self):...
    def remove(self):...
