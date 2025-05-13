from ICRUD import ICRUD
from locale import setlocale, currency, LC_MONETARY

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
from tkinter import messagebox
from change import Change
from datetime import datetime

setlocale(LC_MONETARY, 'pt_BR.UTF-8')

class Pedency(ICRUD):
    def __init__(self, ids:list[str], data:dict[str,list[str]], taxes:list[str]):
        self.sizePolicy = QSizePolicy(
            QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum
        )
        self.sizePolicy.setHorizontalStretch(0)
        self.sizePolicy.setVerticalStretch(0)

        self.font = QFont()
        self.font.setFamilies([u"Tw Cen MT"])
        self.font.setPointSize(16)

        self.font2 = QFont()
        self.font2.setFamilies([u"Tw Cen MT"])
        self.font2.setPointSize(20)

        self.add_brush = QBrush(QColor(179, 255, 178, 255))
        self.add_brush.setStyle(Qt.BrushStyle.Dense1Pattern)

        self.updt_brush = QBrush(QColor(189, 253, 254, 255))
        self.updt_brush.setStyle(Qt.BrushStyle.Dense1Pattern)

        self.remove_brush = QBrush(QColor(254, 139, 139, 255))
        self.remove_brush.setStyle(Qt.BrushStyle.Dense1Pattern)

        self.no_brush = QBrush(Qt.BrushStyle.NoBrush)

        self.pedency_header = [
            'Tipo','Valor','Competência', 'Vencimento','Observações'
        ]
        self.taxes_header = ['Tributo','Valor']
        self.taxes_options = taxes
        self.inputs = []
        self.confirm_connection = None

        now = datetime.now()
        self.default_resp = [
            'IRPF', '0,0', now.strftime('%d/%m/%Y'), now.strftime('%m/%Y'), ''
        ]

        self.ref_fill = {
            'value': self.value_str,
            'competence': lambda value: value.strftime('%m/%Y'),
            'maturity': lambda value: value.strftime('%d/%m/%Y'),
        }

        self.ref_input = {
            QComboBox : lambda value, widget: self.__set_combo(value, widget),
            QDateEdit : lambda value, widget: self.__set_date(value, widget),
            QDoubleSpinBox : lambda value, widget: widget.setValue(self.value_float(value)),
            QTextEdit : lambda value, widget: widget.setText(value)
        }

        self.ref_input_text = {
            QComboBox : lambda widget: widget.currentText(),
            QTextEdit : lambda widget: widget.toPlainText(),
            QDateEdit : lambda widget: widget.text(),
            QDoubleSpinBox : lambda widget: widget.text(),
        }

        self.stacked_widget = QStackedWidget()
        self.stacked_widget.addWidget(self.__page_1())
        self.stacked_widget.addWidget(self.__page_2())
        self.fill(ids, data)
        pass

    def __call__(self, *args, **kwds):
        return self.stacked_widget

    def __page_1(self) -> QWidget:
        page_1 = QWidget()
        verticalLayout = QVBoxLayout(page_1)

        self.table_pedency = QTableWidget(page_1)
        self.table_pedency.itemDoubleClicked.connect(self.updt)
        self.table_pedency.setEditTriggers(
            QAbstractItemView.EditTrigger.NoEditTriggers
        )
        self.table_pedency.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        verticalLayout.addWidget(self.table_pedency)

        line = QFrame(page_1)
        line.setFrameShape(QFrame.Shape.HLine)
        line.setFrameShadow(QFrame.Shadow.Sunken)
        verticalLayout.addWidget(line)

        self.table_taxes = QTableWidget(page_1)
        self.table_taxes.setEditTriggers(
            QAbstractItemView.EditTrigger.NoEditTriggers
        )
        self.table_taxes.setStyleSheet(u"background-color: rgb(255, 255, 255);")
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
        comboBox.addItems(self.taxes_options)
        self.inputs.append(comboBox)
        comboBox.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        gridLayout.addWidget(comboBox, 0, 1, 1, 1)

        doubleSpinBox = QDoubleSpinBox(page_2)
        doubleSpinBox.setSingleStep(100.00)
        doubleSpinBox.setMaximum(999999.99)
        doubleSpinBox.setGroupSeparatorShown(True)
        self.inputs.append(doubleSpinBox)
        doubleSpinBox.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        gridLayout.addWidget(doubleSpinBox, 1, 1, 1, 1)
        
        dateEdit_1 = QDateEdit(page_2)
        dateEdit_1.setDisplayFormat(
            QCoreApplication.translate("MainWindow", u"MM/yyyy", None)
        )
        self.inputs.append(dateEdit_1)
        dateEdit_1.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        gridLayout.addWidget(dateEdit_1, 2, 1, 1, 1)

        dateEdit_2 = QDateEdit(page_2)
        dateEdit_2.setCalendarPopup(True)
        self.inputs.append(dateEdit_2)
        dateEdit_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        gridLayout.addWidget(dateEdit_2, 3, 1, 1, 1)

        textEdit = QTextEdit(page_2)
        self.sizePolicy.setHeightForWidth(textEdit.sizePolicy().hasHeightForWidth())
        textEdit.setSizePolicy(self.sizePolicy)
        textEdit.setMaximumSize(QSize(16777215, 50))
        self.inputs.append(textEdit)
        textEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        gridLayout.addWidget(textEdit, 4, 1, 1, 1)

        frame = QFrame(page_2)
        self.sizePolicy.setHeightForWidth(frame.sizePolicy().hasHeightForWidth())
        frame.setSizePolicy(self.sizePolicy)
        frame.setFrameShape(QFrame.Shape.StyledPanel)
        frame.setFrameShadow(QFrame.Shadow.Raised)
        horizontalLayout = QHBoxLayout(frame)

        pushButton = QPushButton(frame)
        pushButton.setText('Cancelar')
        pushButton.setFont(self.font2)
        pushButton.clicked.connect( 
            lambda: self.stacked_widget.setCurrentIndex(0)
        )
        pushButton.setStyleSheet(
            u"background-color: rgb(255, 255, 255);\n"
            "border: 1px solid rgb(85, 170, 255);\n"
            "padding: 5px;\n"
            "border-radius: 8px;"
        )
        horizontalLayout.addWidget(pushButton)

        self.confirm_btn = QPushButton(frame)
        self.confirm_btn.setText('Confirmar')
        self.confirm_btn.setFont(self.font2)
        self.confirm_btn.setStyleSheet(
            u"background-color: rgb(255, 255, 255);\n"
            "border: 1px solid rgb(85, 170, 255);\n"
            "padding: 5px;\n"
            "border-radius: 8px;"
        )

        horizontalLayout.addWidget(self.confirm_btn)

        gridLayout.addWidget(frame, 5, 0, 1, 2)
       
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

        for key, func in self.ref_fill.items():
            data[key] = map(func, data[key])

        for column, column_data in enumerate(data.values()):
            for row, value in enumerate(column_data):
                item = QTableWidgetItem()
                item.__setattr__('id', ids[row])
                item.__setattr__('edited', False)
                item.setText(str(value))
                self.table_pedency.setItem(row, column, item)
        
        self.__taxes()

    def __taxes(self):
        self.table_taxes.clear()
        self.table_taxes.setRowCount(0)
        self.table_taxes.setColumnCount(len(self.taxes_header))
        self.table_taxes.setHorizontalHeaderLabels(self.taxes_header)
        for row in range(self.table_pedency.rowCount()):
            pen_type = self.table_pedency.item(row, 0).text()
            value = self.table_pedency.item(row, 1).text()
            self.__fill_taxes(pen_type, value)

    def value_float(self, value):
        return float(value.replace('.','').replace(',','.'))
    
    def value_str(self, value):
        return currency(value, symbol= False, grouping= True)

    def __fill_taxes(self, type: str, value: str):
        row = self.__taxes_find(type)
        if row != None:
            value_item = self.table_taxes.item(row, 1)
            current_value = value_item.text()
            value_item.setText(
                self.value_str(
                    self.value_float(current_value) + self.value_float(value)
                )
            )
        else:
            row = self.table_taxes.rowCount()
            self.table_taxes.setRowCount(row + 1)
            for column, data in enumerate([type, value]):
                item = QTableWidgetItem()
                item.setText(data)
                self.table_taxes.setItem(row, column, item)

    def __taxes_find(self, type):
        for row in range(self.table_taxes.rowCount()):
            item = self.table_taxes.item(row, 0)
            if item.text() == type:
                return row
        return None

    def add(self):
        for column in range(self.table_pedency.columnCount()):
            input = self.inputs[column]
            self.ref_input[type(input)](self.default_resp[column], input)

        self.confirm_connection = self.confirm_btn.clicked.connect( 
            self.confirm_add
        )
        self.stacked_widget.setCurrentIndex(1)

    def confirm_add(self):
        resp = self.__inputs_response()

        row = self.table_pedency.rowCount()
        self.table_pedency.setRowCount(row + 1)
        for column in range(self.table_pedency.columnCount()):
            item = QTableWidgetItem()
            item.__setattr__('id', None)
            item.__setattr__('edited', False)
            item.setText(resp[column])
            item.setBackground(self.add_brush)
            self.table_pedency.setItem(row, column, item)
            
        self.__fill_taxes(
            resp[0], 
            self.value_str(
                self.value_float(resp[1])
            )
        )
        self.stacked_widget.setCurrentIndex(0)
        self.confirm_btn.disconnect(self.confirm_connection)

    def updt(self):
        item = self.table_pedency.selectedItems()[0]
        row = item.row()
        for column in range(self.table_pedency.columnCount()):
            item = self.table_pedency.item(row, column)
            input = self.inputs[column]
            self.ref_input[type(input)](item.text(), input)

        self.confirm_connection = self.confirm_btn.clicked.connect( 
            self.confirm_updt
        )
        self.stacked_widget.setCurrentIndex(1)

    def __set_combo(self, value, widget):
        if value in self.taxes_options:
            index = self.taxes_options.index(value)
            widget.setCurrentIndex(index)
        else:
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

    def confirm_updt(self):
        resp = self.__inputs_response()
        item = self.table_pedency.selectedItems()[0]
        row = item.row()
        if self.__check_updt(resp, row) == False:
            return self.stacked_widget.setCurrentIndex(0)

        bush = ''
        old_value = self.value_float(self.table_pedency.item(row, 1).text())
        old_type = self.table_pedency.item(row, 0).text()
        if None == item.__getattribute__('id'):
            bush = self.add_brush
        else:
            bush = self.updt_brush

        for column in range(self.table_pedency.columnCount()):
            item = self.table_pedency.item(row, column)
            item.__setattr__('edited', True)
            item.setBackground(bush)
            item.setText(resp[column])

        new_value = self.value_float(resp[1])
        if old_type != resp[0]:
            row = self.__taxes_find(old_type)
            self.table_taxes.removeRow(row)

            self.__fill_taxes(
                resp[0], 
                self.value_str(new_value)
            )
        else:
            self.__fill_taxes(
                resp[0], 
                self.value_str(new_value - old_value)
            )
        self.stacked_widget.setCurrentIndex(0)
        self.confirm_btn.disconnect(self.confirm_connection)

    def __inputs_response(self):
        resp = []
        for input in self.inputs:
            text = self.ref_input_text[type(input)](input)
            resp.append(text)
        return resp

    def __check_updt(self, resp, row):
        for column in range(self.table_pedency.columnCount()):
            item = self.table_pedency.item(row, column)
            if item.text() != resp[column]:
                return True
        return False
        
    def remove(self):
        try:
            item = self.table_pedency.selectedItems()[0]
            row = item.row()
            if item.background() == self.add_brush:
                self.table_pedency.removeRow(row)
            else:
                pen_type = self.table_pedency.item(row, 0).text()
                value = self.table_pedency.item(row, 1).text()
                bush = self.remove_brush
                if item.background() == self.remove_brush:
                    bush = self.updt_brush\
                        if True == item.__getattribute__('edited')\
                            else self.no_brush
                    self.__fill_taxes(pen_type, value)
                else:
                    self.__fill_taxes(pen_type, f'-{value}')

                for column in range(self.table_pedency.columnCount()):
                    item = self.table_pedency.item(row, column)
                    item.setBackground(bush)
        except IndexError:
            messagebox.showerror('Aviso', 'Primeiro, selecione a pendência que deseja remover')

    def change(self) -> Change | None:
        changes = Change()
        for row in range(self.table_pedency.rowCount()):
            item = self.table_pedency.item(row, 0)
            brush = item.background()
            if brush == self.no_brush:
                continue

            elif brush == self.add_brush:
                data = self.__data_row(row)
                changes.to_add(data)

            elif brush == self.updt_brush:
                data = self.__data_row(row)
                changes.to_updt(
                    self.table_pedency.item(row, 0)\
                        .__getattribute__('id'), 
                    data
                )

            elif brush == self.remove_brush:
                changes.to_remove(
                    self.table_pedency.item(row, 0)\
                        .__getattribute__('id')
                )
        return changes
    
    def has_change(self)-> bool:
        for row in range(self.table_pedency.rowCount()):
            item = self.table_pedency.item(row, 0)
            if item.background() != self.no_brush:
                return True
        return False

    def __data_row(self, row) -> dict[str]:
        data = {}
        for column in range(self.table_pedency.columnCount()):
            item = self.table_pedency.item(row, column)
            key = self.table_pedency.horizontalHeaderItem(column)
            data[key.text()] = item.text()
        return data
    
    def save(self):
        remove_count = 0
        for row in range(self.table_pedency.rowCount()):
            current_row = row - remove_count
            item = self.table_pedency.item(current_row, 0)
            brush = item.background()
            if brush == self.remove_brush:
                self.table_pedency.removeRow(current_row)
                remove_count = remove_count + 1
            elif brush in [self.add_brush, self.updt_brush]:
                for column in range(self.table_pedency.columnCount()):
                    item = self.table_pedency.item(current_row, column)
                    item.setBackground(self.no_brush)

    def data(self) -> dict[list]:
        data_pedency = self.__data_column(self.table_pedency)
        data_taxes = self.__data_column(self.table_taxes)
        return data_pedency, data_taxes

    def __data_column(self, table):
        data_column = {}
        for column in range(table.columnCount()):
            key = table.horizontalHeaderItem(column)
            data_row = []
            for row in range(table.rowCount()):
                item = table.item(row, column)
                data_row.append(item.text())
            data_column[key.text()] = data_row
        return data_column