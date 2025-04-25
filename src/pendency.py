from ICRUD import ICRUD

from PySide6.QtCore import (
    QSize, Qt, QDate, QCoreApplication, 
)
from PySide6.QtGui import (
    QFont, QBrush, QColor, 
)
from PySide6.QtWidgets import (QComboBox, QDateEdit, QDoubleSpinBox,
    QFrame, QGridLayout, QLabel, QPushButton, QSizePolicy,
    QStackedWidget, QTableWidget, QTableWidgetItem,
    QTextEdit, QVBoxLayout, QWidget, QHBoxLayout, QAbstractItemView
)

from re import findall

class Pedency(ICRUD):
    def __init__(self, ids, data):
        self.sizePolicy = QSizePolicy(
            QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum
        )
        self.sizePolicy.setHorizontalStretch(0)
        self.sizePolicy.setVerticalStretch(0)

        self.font = QFont()
        self.font.setPointSize(12)

        self.add_brush = QBrush(QColor(0, 234, 255, 255))
        self.add_brush.setStyle(Qt.BrushStyle.Dense1Pattern)

        self.pedency_header = [
            'Tipo','Valor','Competência','Vencimento','Observações'
        ]
        self.taxes_header = ['Tributo','Valor']
        self.inputs = []
        self.types_options = ['', 'IRPF']
        self.ref_input = {
            QComboBox : lambda value, widget: self.__set_combo(value, widget),
            QDateEdit : lambda value, widget: self.__set_date(value, widget),
            QDoubleSpinBox : lambda value, widget: widget.setValue(float(value)),
            QTextEdit : lambda value, widget: widget.setText(value)
        }

        self.stacked_widget = QStackedWidget()
        self.stacked_widget.addWidget(self.__page_1())
        self.stacked_widget.addWidget(self.__page_2())
        self.__fill(ids, data)
        pass

    def __call__(self, *args, **kwds):
        return self.stacked_widget

    def __page_1(self) -> QWidget:
        page_1 = QWidget()
        verticalLayout = QVBoxLayout(page_1)

        self.table_pedency = QTableWidget(page_1)
        self.table_pedency.itemDoubleClicked.connect(self.updt)
        self.table_pedency.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
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

        for i in range(5):
            label = self.__label_factory(page_2)
            label.setText(self.pedency_header[i])
            gridLayout.addWidget(label, i, 0, 1, 1)

        comboBox = QComboBox(page_2)
        comboBox.addItems(self.types_options)
        self.inputs.append(comboBox)
        gridLayout.addWidget(comboBox, 0, 1, 1, 1)

        doubleSpinBox = QDoubleSpinBox(page_2)
        doubleSpinBox.setSingleStep(100.000000000000000)
        self.inputs.append(doubleSpinBox)
        gridLayout.addWidget(doubleSpinBox, 1, 1, 1, 1)
        
        dateEdit_1 = QDateEdit(page_2)
        dateEdit_1.setDisplayFormat(
            QCoreApplication.translate("MainWindow", u"MM/yyyy", None)
        )
        self.inputs.append(dateEdit_1)
        gridLayout.addWidget(dateEdit_1, 3, 1, 1, 1)

        dateEdit_2 = QDateEdit(page_2)
        dateEdit_2.setCalendarPopup(True)
        self.inputs.append(dateEdit_2)
        gridLayout.addWidget(dateEdit_2, 2, 1, 1, 1)

        textEdit = QTextEdit(page_2)
        self.sizePolicy.setHeightForWidth(textEdit.sizePolicy().hasHeightForWidth())
        textEdit.setSizePolicy(self.sizePolicy)
        textEdit.setMaximumSize(QSize(16777215, 50))
        self.inputs.append(textEdit)
        gridLayout.addWidget(textEdit, 4, 1, 1, 1)

        frame = QFrame(page_2)
        self.sizePolicy.setHeightForWidth(frame.sizePolicy().hasHeightForWidth())
        frame.setSizePolicy(self.sizePolicy)
        frame.setFrameShape(QFrame.Shape.StyledPanel)
        frame.setFrameShadow(QFrame.Shadow.Raised)
        horizontalLayout = QHBoxLayout(frame)

        pushButton = QPushButton(frame)
        pushButton.setText('Cancelar')
        pushButton.clicked.connect( 
            lambda: self.stacked_widget.setCurrentIndex(0)
        )
        horizontalLayout.addWidget(pushButton)

        pushButton_2 = QPushButton(frame)
        pushButton_2.setText('Confirmar')
        pushButton_2.clicked.connect( 
            self.save
        )
        horizontalLayout.addWidget(pushButton_2)

        gridLayout.addWidget(frame, 5, 0, 1, 2)
       
        return page_2

    def __label_factory(self, page_2: QWidget) -> QLabel:
        label = QLabel(page_2)
        self.sizePolicy.setHeightForWidth(label.sizePolicy().hasHeightForWidth())
        label.setSizePolicy(self.sizePolicy)
        label.setFont(self.font)
        return label
    
    def __fill(self, ids: list[str], data: dict[str,str]):
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
        self.table_pedency.setRowCount(row_index)
        for column_index in range(self.table_pedency.columnCount()):
            item = QTableWidgetItem()
            item.__setattr__('id', None)
            # item.setBackground(self.add_brush)
            self.table_pedency.setItem(row_index, column_index, item)
        # self.table_pedency.setCurrentCell(row_index, 0)
        # item.setSelected(True)
        # self.updt()

    def updt(self):
        item = self.table_pedency.selectedItems()[0]
        row = item.row()
        for column in range(self.table_pedency.columnCount()):
            item = self.table_pedency.item(row, column)
            input = self.inputs[column]
            self.ref_input[type(input)](item.text(), input)
        self.stacked_widget.setCurrentIndex(1)

    def __set_combo(self, value, widget):
        if value in self.types_options:
            index = self.types_options.index(value)
            widget.setCurrentIndex(index)
        else:
            QComboBox.setCurrentIndex
            widget.setCurrentIndex(0)

    def __set_date(self, value, widget):
            list_date = findall(r'[0-9]+', value)
            if len(list_date) == 2:
                m, y = list_date
                d = 1
            else:
                d, m, y = list_date
            date = QDate(int(y), int(m), int(d))
            widget.setDate(date)

    def remove(self):...

    def save(self):...