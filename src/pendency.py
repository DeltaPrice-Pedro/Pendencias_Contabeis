from ICRUD import ICRUD

from PySide6.QtCore import (
    QSize, Qt
)
from PySide6.QtGui import (
    QFont, QBrush, QColor
)
from PySide6.QtWidgets import (QComboBox, QDateEdit, QDoubleSpinBox,
    QFrame, QGridLayout, QLabel, QPushButton, QSizePolicy,
    QStackedWidget, QTableWidget, QTableWidgetItem,
    QTextEdit, QVBoxLayout, QWidget
)

class Pedency(ICRUD):
    def __init__(self):
        self.sizePolicy = QSizePolicy(
            QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum
        )
        self.sizePolicy.setHorizontalStretch(0)
        self.sizePolicy.setVerticalStretch(0)

        self.font = QFont()
        self.font.setPointSize(12)

        self.pedency_header = ['Tipo','Valor','Competência','Vencimento','Observações']
        self.taxes_header = ['Tributo','Valor']

        self.stacked_widget = QStackedWidget()
        self.stacked_widget.addWidget(self.__page_1())
        self.stacked_widget.addWidget(self.__page_2())
        pass

    def __call__(self, *args, **kwds):
        return self.stacked_widget

    def __page_1(self) -> QWidget:
        page_1 = QWidget()
        verticalLayout = QVBoxLayout(page_1)

        self.table_pedency = QTableWidget(page_1)
        verticalLayout.addWidget(self.table_pedency)

        line = QFrame(page_1)
        line.setFrameShape(QFrame.Shape.HLine)
        line.setFrameShadow(QFrame.Shadow.Sunken)

        verticalLayout.addWidget(line)

        self.table_taxes = QTableWidget(page_1)
        verticalLayout.addWidget(self.table_taxes)
        return page_1

    def __page_2(self) -> QWidget:
        page_2 = QWidget()
        gridLayout = QGridLayout(page_2)

        comboBox = QComboBox(page_2)
        gridLayout.addWidget(comboBox, 0, 1, 1, 1)

        for i in range(5):
            label = self.__label_factory(page_2)
            gridLayout.addWidget(label, i, 0, 1, 1)

        dateEdit_1 = QDateEdit(page_2)
        gridLayout.addWidget(dateEdit_1, 3, 1, 1, 1)

        dateEdit_2 = QDateEdit(page_2)
        dateEdit_2.setCalendarPopup(True)
        gridLayout.addWidget(dateEdit_2, 2, 1, 1, 1)

        doubleSpinBox = QDoubleSpinBox(page_2)
        doubleSpinBox.setSingleStep(100.000000000000000)
        gridLayout.addWidget(doubleSpinBox, 1, 1, 1, 1)

        pushButton = QPushButton(page_2)
        gridLayout.addWidget(pushButton, 6, 1, 1, 1)

        pushButton_2 = QPushButton(page_2)
        gridLayout.addWidget(pushButton_2, 6, 0, 1, 1)

        textEdit = QTextEdit(page_2)
        self.sizePolicy.setHeightForWidth(textEdit.sizePolicy().hasHeightForWidth())
        textEdit.setSizePolicy(self.sizePolicy)
        textEdit.setMaximumSize(QSize(16777215, 50))
        gridLayout.addWidget(textEdit, 4, 1, 1, 1)
        return page_2

    def __label_factory(self, page_2: QWidget) -> QLabel:
        label = QLabel(page_2)
        self.sizePolicy.setHeightForWidth(label.sizePolicy().hasHeightForWidth())
        label.setSizePolicy(self.sizePolicy)
        label.setFont(self.font)
        return label
    
    def fill(self, ids: list[str], data: dict[str,str]):
        self.table_pedency.clear()
        self.table_pedency.setColumnCount(len(data.keys()))
        self.table_pedency.setHorizontalHeaderLabels(self.pedency_header)
        self.table_pedency.setRowCount(len(ids))

        for column, column_data in enumerate(data.values()):
            for row, value in enumerate(column_data):
                item = QTableWidgetItem()
                item.__setattr__('id', ids[row])
                item.setText(str(value))
                self.table_pedency.setItem(row, column, item)

    def add(self):
        row_index = self.table_pedency.rowCount() + 1
        brush = QBrush(QColor(0, 234, 255, 255))
        brush.setStyle(Qt.BrushStyle.Dense1Pattern)
        for column_index in range(self.table_pedency.columnCount()):
            item = QTableWidgetItem()
            item.setBackground(brush)
            self.table_pedency.setItem(row_index, column_index, item)
        self.table_pedency.setRowCount(row_index)
        self.table_pedency.setCurrentCell(row_index, 0)

    def updt(self):...

    def remove(self):...