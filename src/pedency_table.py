from PySide6.QtWidgets import (
  QTableWidget, QTableWidgetItem
)

from PySide6.QtGui import (
  QColor, QBrush, Qt
)

class PedencyTable (QTableWidget):
    def __init__(self, id_companie: str, data: dict[list] | None):
        super().__init__(columnCount= len(data.keys()))
        self.setHorizontalHeaderLabels(data.keys())
        ids = data.pop('id_pending')
        self.setRowCount(len(ids))

        for column, column_data in enumerate(data.values()):
            for row, value in enumerate(column_data):
                item = QTableWidgetItem()
                item.__setattr__('id', ids[row])
                item.setText(str(value))
                self.setItem(row, column, item)

        pass

    def add(self):
        row_index = self.rowCount() + 1
        brush = QBrush(QColor(0, 234, 255, 255))
        brush.setStyle(Qt.BrushStyle.Dense1Pattern)
        for column_index in range(self.columnCount()):
            item = QTableWidgetItem()
            item.setBackground(brush)
            self.setItem(row_index, column_index, item)
        self.setRowCount(row_index)
        self.setCurrentCell(row_index, 0)

    def updt(self):...
    def remove(self):...
