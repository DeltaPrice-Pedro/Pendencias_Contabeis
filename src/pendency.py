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
    """
    Gerencia a interface e as operações relacionadas às pendências contábeis de uma empresa.
    Permite adicionar, editar, remover e validar pendências, além de controlar as alterações para persistência.
    """
    def __init__(self, ids:list[str], data:dict[str,list[str]], taxes:list[str]):
        """
        Inicializa o widget de pendências com os dados fornecidos.
        Args:
            ids (list): Lista de IDs das pendências.
            data (dict): Dados das pendências.
            taxes (list): Lista de impostos disponíveis.
        """
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
        self.season_updts = []
        
        self.current_operation = ''
        self.ref_operation = {
            'add': self.confirm_add,
            'updt': self.confirm_updt
        }

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
        """
        Retorna a tabela de pendências e o widget empilhado.
        """
        return self.table_pedency, self.stacked_widget

    def __page_1(self) -> QWidget:
        """
        Cria a página principal com as tabelas de pendências e impostos.
        """
        page_1 = QWidget()
        verticalLayout = QVBoxLayout(page_1)

        self.table_pedency = QTableWidget(page_1)
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
        """
        Cria a página de edição/adicionar pendência.
        """
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
       
        return page_2
    
    def cancel(self):
        """
        Cancela a operação de edição/adicionar e retorna à página principal.
        """
        self.stacked_widget.setCurrentIndex(0)

    def __label_factory(self, page_2: QWidget) -> QLabel:
        """
        Cria um QLabel com formatação padrão.
        """
        label = QLabel(page_2)
        self.sizePolicy.setHeightForWidth(label.sizePolicy().hasHeightForWidth())
        label.setSizePolicy(self.sizePolicy)
        label.setFont(self.font)
        return label
    
    def fill(self, ids: list[str], data: dict[str,str]):
        """
        Preenche a tabela de pendências com os dados fornecidos.
        """
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
        """
        Atualiza a tabela de impostos conforme as pendências.
        """
        self.table_taxes.clear()
        self.table_taxes.setRowCount(0)
        self.table_taxes.setColumnCount(len(self.taxes_header))
        self.table_taxes.setHorizontalHeaderLabels(self.taxes_header)
        for row in range(self.table_pedency.rowCount()):
            pen_type = self.table_pedency.item(row, 0).text()
            value = self.table_pedency.item(row, 1).text()
            self.__fill_taxes(pen_type, value)

    def value_float(self, value):
        """
        Converte valor monetário de string para float.
        """
        return float(value.replace('.','').replace(',','.'))
    
    def value_str(self, value):
        """
        Converte valor monetário de float para string formatada.
        """
        return currency(value, symbol= False, grouping= True)

    def __fill_taxes(self, type: str, value: str):
        """
        Atualiza ou adiciona o valor do imposto na tabela de impostos.
        """
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
        """
        Busca o índice de um imposto na tabela de impostos.
        """
        for row in range(self.table_taxes.rowCount()):
            item = self.table_taxes.item(row, 0)
            if item.text() == type:
                return row
        return None
    
    def confirm(self):
        """
        Confirma a operação atual (adicionar ou editar pendência).
        """
        self.ref_operation[self.current_operation]()

    def add(self):
        """
        Inicia o processo de adição de uma nova pendência.
        """
        for column in range(self.table_pedency.columnCount()):
            input = self.inputs[column]
            self.ref_input[type(input)](self.default_resp[column], input)

        self.current_operation = 'add'
        self.stacked_widget.setCurrentIndex(1)

    def confirm_add(self):
        """
        Confirma e adiciona a nova pendência à tabela.
        """
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

    def updt(self):
        """
        Inicia o processo de edição da pendência selecionada.
        """
        item = self.table_pedency.selectedItems()[0]
        row = item.row()
        for column in range(self.table_pedency.columnCount()):
            item = self.table_pedency.item(row, column)
            input = self.inputs[column]
            self.ref_input[type(input)](item.text(), input)

        self.current_operation = 'updt'
        self.stacked_widget.setCurrentIndex(1)

    def __set_combo(self, value, widget):
        """
        Define o valor de um QComboBox.
        """
        if value in self.taxes_options:
            index = self.taxes_options.index(value)
            widget.setCurrentIndex(index)
        else:
            widget.setCurrentIndex(0)

    def __set_date(self, value, widget):
        """
        Define o valor de um QDateEdit.
        """
        list_date = findall(r'[0-9]+', value)
        if len(list_date) == 2:
            m, y = list_date
            d = 1
        else:
            d, m, y = list_date
        date = QDate(int(y), int(m), int(d))
        widget.setDate(date)

    def confirm_updt(self):
        """
        Confirma e aplica a edição da pendência selecionada.
        """
        bush = ''
        edited = True

        resp = self.__inputs_response()
        item = self.table_pedency.selectedItems()[0]
        row = item.row()

        #Mudou mesmo?
        if self.__check_updt(resp, row) == False:
            return self.stacked_widget.setCurrentIndex(0)
        
        #Esses dados já existiram nessa sessão?
        elif self.__check_season_updt(resp) == True:
            bush = self.no_brush
            edited = False

        else:
            self.season_updts.append(self.pedency_items(row))
            if None == item.__getattribute__('id'):
                bush = self.add_brush
            else:
                bush = self.updt_brush
        
        old_value = self.value_float(self.table_pedency.item(row, 1).text())
        old_type = self.table_pedency.item(row, 0).text()

        for column in range(self.table_pedency.columnCount()):
            item = self.table_pedency.item(row, column)
            item.__setattr__('edited', edited)
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

    def __check_season_updt(self, resp):
        """
        Verifica se a edição já foi realizada nesta sessão.
        """
        for old_updt in self.season_updts:
            if resp == old_updt:
                self.season_updts.remove(old_updt)
                return True
        return False

    def pedency_items(self, row):
        """
        Retorna os valores das colunas de uma linha da tabela de pendências.
        """
        items = []
        for column in range(self.table_pedency.columnCount()):
            items.append(self.table_pedency.item(row, column).text())
        return items

    def __inputs_response(self):
        """
        Coleta os valores dos inputs do formulário de pendência.
        """
        resp = []
        for input in self.inputs:
            text = self.ref_input_text[type(input)](input)
            resp.append(text)
        return resp

    def __check_updt(self, resp, row):
        """
        Verifica se houve alteração nos dados da pendência.
        """
        for column in range(self.table_pedency.columnCount()):
            item = self.table_pedency.item(row, column)
            if item.text() != resp[column]:
                return True
        return False
        
    def remove(self):
        """
        Marca ou remove uma pendência da tabela, conforme o contexto.
        """
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
        """
        Retorna um objeto Change com as alterações feitas nas pendências.
        """
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
        """
        Verifica se há alterações pendentes nas pendências.
        """
        for row in range(self.table_pedency.rowCount()):
            item = self.table_pedency.item(row, 0)
            if item.background() != self.no_brush:
                return True
        return False

    def __data_row(self, row) -> dict[str]:
        """
        Retorna os dados de uma linha da tabela de pendências como dicionário.
        """
        data = {}
        for column in range(self.table_pedency.columnCount()):
            item = self.table_pedency.item(row, column)
            key = self.table_pedency.horizontalHeaderItem(column)
            data[key.text()] = item.text()
        return data
    
    def save(self):
        """
        Aplica as alterações visuais e remove pendências marcadas para remoção.
        """
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
        """
        Retorna os dados atuais das pendências e impostos.
        """
        data_pedency = self.__data_column(self.table_pedency)
        data_taxes = self.__data_column(self.table_taxes)
        return data_pedency, data_taxes

    def __data_column(self, table):
        """
        Retorna os dados de uma tabela como dicionário de listas por coluna.
        """
        data_column = {}
        for column in range(table.columnCount()):
            key = table.horizontalHeaderItem(column)
            data_row = []
            for row in range(table.rowCount()):
                item = table.item(row, column)
                data_row.append(item.text())
            data_column[key.text()] = data_row
        return data_column