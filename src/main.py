from PySide6.QtWidgets import (
    QMainWindow, QApplication, QListWidgetItem, QAbstractItemView
)
from PySide6.QtGui import (
    QIcon, QMovie
)

from PySide6.QtCore import (
    QThread, QDate
)

from dateutil.relativedelta import relativedelta
from window_pend import Ui_MainWindow
from re import compile, findall
from tkinter import messagebox
from database import DataBase
from datetime import datetime
from pendency import Pedency
from address import Address
from postman import Postman
from os import startfile
from pathlib import Path
from taxes import Taxes
from sheet import Sheet
from pymysql import err
import sys

class MainWindow(QMainWindow, Ui_MainWindow):
    icon_path = Path(__file__).parent / 'imgs' / '{0}_icon.png'
    current_companie_id = ''

    def __init__(self, parent = None) -> None:
        super().__init__(parent)
        self.message_error_docker = 'Falha na conexão com o banco de dados. Favor verificar se o aplicativo "DOCKER" está inicializado no servidor, caso constrário, entre em contato com o suporte disponível\n\n{}'

        self.db = self.try_conection()
        self.setupUi(self)

        self.setWindowIcon(
            QIcon(
                (Path(__file__).parent / 'imgs' / 'GerenPedenContab.ico').__str__())
        )

        self.message_select = 'Primeiro, clique 1 vez na empresa que deseja {0}'
        self.message_remove = 'Confirma a remoção desta empresa?\nTodas suas pendências e emails cadastrados também serão excluídos'
        self.message_save = 'Tem certeza que deseja salvar estas alterações?'
        self.message_pending_save = 'Antes de recarregar os dados, faça ou cancele o salvamento das alterações pendentes'
        self.message_no_save = 'Não há alterações a serem salvas'
        self.message_exit_save = 'Tem certeza que deseja sair da empresa SEM SALVAR as mudanças feitas nela?\n\nCaso não queira PERDER as alterações, selecione "não" e as salve'
        self.message_send_email = 'Confirma o envio dessas pendências aos emails cadastrados?'

        self.__init_date_sheet()

        from local_changes import LocalChanges

        self.local_changes = LocalChanges()
        sender_name = self.local_changes.sender_name()
        self.lineEdit_name_func.setText(sender_name)

        self.connections = {}
        self.enable_status = True

        self.taxes = Taxes(*self.db.taxes())
        page = self.taxes()
        self.stackedWidget_companie.addWidget(page)

        self.ref_universal = {
            'companie': [
                {
                    self.pushButton_add_func: self.add_companie,
                    self.pushButton_remove_func: self.remove_companie,
                    self.pushButton_edit_func: self.edit_companie,
                    self.pushButton_reload_companie: self.__fill_companies,
                },
                {
                    self.pushButton_add_func: 'Adciona empresa a lista de empresas cadastradas',
                    self.pushButton_remove_func: 'Remove empresa cadastrada',
                    self.pushButton_edit_func: 'Edita o nome de empresa cadastrada',
                    self.pushButton_sheet_func: 'Gera relatório de envio de todas empresas cadastradas',
                }
            ],
            'pending': [
                {
                    self.pushButton_reload_companie: self.reload_pedency,
                },
                {
                    self.pushButton_add_func: 'Adciona pendência contábil a empresa selecionada',
                    self.pushButton_remove_func: 'Remove a pendência contábil selecionada com 1 clique',
                    self.pushButton_edit_func: 'Edita a pendência contábil selecionada com 1 clique',
                    self.pushButton_sheet_func: 'Gera relatório de envios exclusivo da empresa atual',
                }
            ],
            'taxes': [
                {
                    self.pushButton_add_func: self.taxes.add,
                    self.pushButton_edit_func: self.taxes.updt,
                    self.pushButton_remove_func: self.taxes.remove,
                    self.pushButton_reload_companie: self.taxes.fill,
                },
                {
                    self.pushButton_add_func: 'Adciona imposto a lista de impostos cadastrados',
                    self.pushButton_remove_func: 'Remove imposto cadastrado',
                    self.pushButton_edit_func: 'Edita o nome de imposto cadastrado',
                }
            ]
        }

        self.ref_connection_companie = {
            self.pushButton_reload_companie: self.__fill_companies,
            self.pushButton_add_func: self.add_companie,
            self.pushButton_remove_func: self.remove_companie,
        }    

        self.ref_connection_pedency = {
            self.pushButton_reload_companie: self.reload_pedency,
        }

        self.ref_connection_taxes = {
            self.pushButton_reload_companie: self.taxes.fill,
            self.pushButton_add_func: self.taxes.add,
            self.pushButton_remove_func: self.taxes.remove,
        }

        self.ref_disable_btns = [
            self.pushButton_add_func,
            self.pushButton_remove_func,
            self.pushButton_edit_func,
            self.pushButton_save_func,
            self.pushButton_send_email,
            self.pushButton_sheet_func,
            self.pushButton_exit_companie,
            self.pushButton_reload_companie
        ]

        self.ref_tool_tip_pedency = {
            self.pushButton_add_func: 'Adciona pendência contábil a empresa selecionada',
            self.pushButton_remove_func: 'Remove a pendência contábil selecionada com 1 clique',
            self.pushButton_edit_func: 'Edita a pendência contábil selecionada com 1 clique',
            self.pushButton_sheet_func: 'Gera relatório de envios exclusivo da empresa atual',
        }

        self.ref_tool_tip_companie = {
            self.pushButton_add_func: 'Adciona empresa a lista de empresas cadastradas',
            self.pushButton_remove_func: 'Remove empresa cadastrada',
            self.pushButton_edit_func: 'Edita o nome de empresa cadastrada',
            self.pushButton_sheet_func: 'Gera relatório de envio de todas empresas cadastradas',
        }

        self.ref_date_sheet = [self.dateEdit_from, self.dateEdit_until]

        self.movie = QMovie(
            (Path(__file__).parent / 'imgs' / 'load.gif').__str__()
        )
        self.label_load_gif.setMovie(self.movie)

        self.open_pedency_connection = None
        self.re_connect_pedency()
        self.__fill_companies()
        self.__init_icons()

        self.listWidget_companie.itemChanged.connect(self.confirm_companie)

        self.pushButton_cancel_email.clicked.connect(
            lambda: self.stackedWidget_email.setCurrentIndex(2)
        )
        self.pushButton_send_email.clicked.connect(self.send_email)
        self.pushButton_save_func.clicked.connect(self.save)
        self.pushButton_exit_companie.clicked.connect(self.exit)
        self.pushButton_sheet_func.clicked.connect(self.sheet)
        self.pushButton_save_func.setHidden(True)

    def re_connect_pedency(self):
        if self.open_pedency_connection == None:
            self.open_pedency_connection = self.listWidget_companie\
                .itemDoubleClicked.connect(self.open_pedency)
        else:
            self.listWidget_companie.disconnect(self.open_pedency_connection)
            self.open_pedency_connection = None

    def try_conection(self):
        try:
            return DataBase()
        except err.OperationalError as e:
            messagebox.showerror('Aviso!', self.message_error_docker.format(e))
            sys.exit()

    def __init_date_sheet(self):
        now = datetime.now()
        regex = compile(r'[0-9]+')
        ref = {
            self.dateEdit_until: now,
            self.dateEdit_from: now - relativedelta(months = 1)
        }

        for widget, date in ref.items():
            list_date = findall(regex, date.strftime('%d/%m/%Y'))
            d, m, y = list_date
            date = QDate(int(y), int(m), int(d))
            widget.setDate(date)

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
        self.listWidget_companie.clear()
        for id, name in data.items():
            item = QListWidgetItem()
            item.setText(name)
            item.__setattr__('id', id)
            self.listWidget_companie.addItem(item)

        self.switch_focus(0)

    def add_companie(self):
        item = QListWidgetItem()
        item.setText('Nome da empresa')
        item.__setattr__('id', None)

        self.listWidget_companie.addItem(item)
        self.listWidget_companie.openPersistentEditor(item)
        self.listWidget_companie.editItem(item)

    def edit_companie(self):
        try:
            items = self.listWidget_companie.selectedItems()
            if len(items) == 0:
                raise Exception(self.message_select.format('editar'))
            
            self.disable_btns()
            self.re_connect_pedency()

            item = items[0]
            self.listWidget_companie.openPersistentEditor(item)
            self.listWidget_companie.editItem(item)

        except Exception as error: 
            messagebox.showwarning('Aviso', error)

    def confirm_companie(self, item: QListWidgetItem):
        try:
            name = item.text()
            if name == '':
                raise Exception('Nome de empresa inválida')
            
            self.listWidget_companie.closePersistentEditor(item)

            id = item.__getattribute__('id')
            if id == None:
                id = self.db.add_companie(name)
                item.__setattr__('id', id)
            else:
                self.db.edit_companie(id, name)

            self.re_connect_pedency()
            self.disable_btns()
        except Exception as error:
            messagebox.showwarning('Aviso', error)

    def remove_companie(self):
        try:
            self.disable_btns()
            items = self.listWidget_companie.selectedItems()
            if len(items) == 0:
                raise Exception(self.message_select.format('remover'))
            
            if messagebox.askyesno('Aviso', self.message_remove) == False:
                return None
            
            item = items[0]
            self.db.remove_companie(item.__getattribute__('id'))
            self.listWidget_companie.takeItem(
                self.listWidget_companie.row(item)
            )
        except Exception as error:
            self.disable_btns()
            messagebox.showwarning('Aviso', error)

    def open_taxes(self):
        self.stackedWidget_companie.setCurrentIndex(1)
        self.switch_focus(2)

    def open_pedency(self):
        self.switch_focus(1)
        item = self.listWidget_companie.selectedItems()[0]
        self.label_current_companie.setText(item.text())
        self.current_companie_id = item.__getattribute__('id')

        self.pedency = self.__pedency(self.current_companie_id)
        self.address = Address(*self.db.emails(self.current_companie_id))

        next_btn, page = self.address()
        next_btn.clicked.connect(self.open_assign)
        self.stackedWidget_email.addWidget(page)

        self.pushButton_save_func.setHidden(False)
        self.pushButton_edit_func.setHidden(True)
        self.stackedWidget_companie.setCurrentIndex(2)
        self.stackedWidget_email.setCurrentIndex(2)

    def __pedency(self, id):
        pedency = Pedency(*self.db.pedency(id))

        self.connections[self.pushButton_add_func] =\
            self.pushButton_add_func.clicked.connect(
                lambda: pedency.add()
            )

        self.connections[self.pushButton_remove_func] =\
            self.pushButton_remove_func.clicked.connect(
                lambda: pedency.remove()
            )

        stacked_widget = pedency()
        stacked_widget.setParent(self.page_4)
        self.verticalLayout_3.addWidget(stacked_widget)
        return pedency
    
    def reload_pedency(self):
        try:
            if any([self.pedency.has_change(), self.address.has_change()]):
                raise Exception(self.message_pending_save)
                
            self.pedency.fill(*self.db.pedency(self.current_companie_id))
            self.address.fill(*self.db.emails(self.current_companie_id))
        except Exception as err:
            messagebox.showerror('Aviso', err)

    def sheet(self):
        try:
            self.disable_btns()
            date = self.__date_sheet_cast()
            if self.stackedWidget_companie.currentIndex() != 0:
                date.append(self.current_companie_id)
                
            data = self.db.history(*date)
            self._sheet = Sheet(data)

            self._sheet.upload()
            
            self.exec_load(True)
            self._thread2 = QThread()

            self._sheet.moveToThread(self._thread2)
            self._thread2.started.connect(self._sheet.write)
            self._sheet.end.connect(self._thread2.quit)
            self._sheet.end.connect(self._thread2.deleteLater)
            self._sheet.result.connect(self.open_file)
            self._thread2.finished.connect(self._sheet.deleteLater)
            self._thread2.start()
        except Exception as err:
            self.exec_load(False)
            messagebox.showerror('Aviso', err)

    def __date_sheet_cast(self):
        dates = []
        for widget in self.ref_date_sheet:
            var = widget.text().split('/')
            var.reverse()
            var = map(lambda x: int(x), var)
            dates.append(datetime(*var))
        return dates

    def open_file(self, path):
        self.exec_load(False)
        startfile(path)

    def save(self):
        try:
            self.disable_btns()
            stats_pedenc = self.pedency.has_change()
            stats_address = self.address.has_change()

            if any([stats_pedenc, stats_address]) != True:
                raise Exception(self.message_no_save)
            
            if messagebox.askyesno('Aviso', self.message_save) == False:
                return None
            
            ref_change = {}
            if stats_pedenc == True:
                ref_change[self.pedency] = self.db.changes_pedency
            
            if stats_address == True:
                ref_change[self.address] = self.db.changes_address
            
            for widget, func in ref_change.items():
                widget_change = widget.change()
                func(self.current_companie_id, widget_change)
                widget.save()
            
            self.disable_btns()
        except Exception as err:
            self.disable_btns()
            messagebox.showerror('Aviso', err)

    def exit(self):
        if any([self.pedency.has_change(), self.address.has_change()]):
            if messagebox.askyesno('Aviso', self.message_exit_save) == False:
                return None

        self.pushButton_edit_func.setHidden(False)
        self.pushButton_save_func.setHidden(True)
        self.stackedWidget_companie.setCurrentIndex(0)
        self.stackedWidget_email.setCurrentIndex(0)
        self.switch_focus(0)
        
        send_btn, page = self.address()
        page.deleteLater()
        self.stackedWidget_email.removeWidget(page)

        stacked_widget = self.pedency()
        stacked_widget.deleteLater()
        self.verticalLayout_3.removeWidget(stacked_widget)

    def switch_focus(self, current_index: int):
        ref_connection = {}
        ref_tool_tip = {}

        if current_index == 0:
            ref_connection = self.ref_connection_companie
            ref_tool_tip = self.ref_tool_tip_companie 
        else:
            ref_connection = self.ref_connection_pedency
            ref_tool_tip = self.ref_tool_tip_pedency

        self.re_connection(ref_connection)
        self.re_tool_tip(ref_tool_tip)

    def re_connection(self, ref):
        for widget, connection in self.connections.items():
            widget.disconnect(connection)
        self.connections.clear()

        for widget, func in ref.items():
            self.connections[widget] = widget.clicked.connect(func)

    def re_tool_tip(self, ref):
        for widget, text in ref.items():
            widget.setToolTip(text)

    def open_assign(self):
        try:
            stats_pedenc = self.pedency.has_change()
            stats_address = self.address.has_change()

            if any([stats_pedenc, stats_address]):
                raise Exception('Aviso', 'Salve as alterações pendentes antes de prosseguir')
                
            self.groupBox_email.setTitle('Assinatura')
            self.stackedWidget_email.setCurrentIndex(1)
        
        except Exception as error:
            messagebox.showwarning(title='Aviso', message= error)

    def send_email(self):
        try:
            self.disable_btns()
            name_func = self.lineEdit_name_func.text()

            if name_func == '':
                raise Exception('Nome inválido')
            
            if messagebox.askyesno('Aviso', self.message_send_email) == False:
                return None

            self.exec_load(True)
            address = self.address.data()
            pedency, taxes = self.pedency.data()

            if all([address, pedency]) == False:
                raise Exception('Não há pendências ou e-mail cadastrados para essa empresa, clique em "Voltar" e adcione a informação faltante')

            self._postman = Postman(
                name_func,
                self.label_current_companie.text(),
                address, 
                pedency,
                taxes
            )
            self._thread = QThread()

            self._postman.moveToThread(self._thread)
            self._thread.started.connect(self._postman.execute)
            self._postman.end.connect(self._thread.quit)
            self._postman.end.connect(self._thread.deleteLater)
            self._postman.result.connect(self.conclusion)
            self._postman.sended.connect(self.save_history)
            self._thread.finished.connect(self._postman.deleteLater)
            self._thread.start()

        except Exception as error:
            self.disable_btns()
            self.exec_load(False)
            messagebox.showwarning(title='Aviso', message= error)

    def conclusion(self, result: str):
        self.local_changes.updt_sender(self.lineEdit_name_func.text())
        self.groupBox_email.setTitle('Email')
        self.stackedWidget_email.setCurrentIndex(2)
        self.exec_load(False)
        messagebox.showinfo(title='Aviso', message= result)

    def save_history(self, *args):
        name_func, companie, taxes = args

        result = []
        for i, j in list(zip(*taxes)):
            result.append(f'{i}: {j}')

        self.db.add_history(
            name_func, companie, ' | '.join(result), self.current_companie_id
        )

    def disable_btns(self):
        self.enable_status = not self.enable_status
        for item in self.ref_disable_btns:
            item.setEnabled(self.enable_status)

    def exec_load(self, action: bool):
        if action == True:
            self.movie.start()
            self.stackedWidget_body.setCurrentIndex(1)
        else:
            self.disable_btns()
            self.movie.stop()
            self.stackedWidget_body.setCurrentIndex(0)

if __name__ == '__main__':
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec()