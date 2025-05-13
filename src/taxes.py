from PySide6.QtCore import (
    QSize, Qt
)
from PySide6.QtGui import (
    QFont, QIcon, QColor, QBrush
)
from PySide6.QtWidgets import (
    QFrame,QHBoxLayout, QListWidget,
    QListWidgetItem, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget, QAbstractItemView
)

from tkinter import messagebox

class Taxes:
    def __init__(self, id, address):
        self.page = self.__page()
        self.fill(id, address)
        pass

    def __call__(self, *args, **kwds):
        return self.page

    def __page(self):
        page_2 = QWidget()
        verticalLayout = QVBoxLayout(page_2)

        self.listWidget_email = self.__list(page_2)
        self.listWidget_email.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        verticalLayout.addWidget(self.listWidget_email)

        frame_email_func = QFrame(page_2)
        frame_email_func.setFrameShape(QFrame.Shape.StyledPanel)
        frame_email_func.setFrameShadow(QFrame.Shadow.Raised)
        horizontalLayout = QHBoxLayout(frame_email_func)

        pushButton_add, pushButton_remove = self.__buttons(frame_email_func)
        horizontalLayout.addWidget(pushButton_add)
        horizontalLayout.addWidget(pushButton_remove)

        verticalLayout.addWidget(frame_email_func)

        pushButton_send_email = QPushButton(page_2)
        pushButton_send_email.setText('Próximo  ')
        pushButton_send_email.setStyleSheet(
            u"background-color: rgb(255, 255, 255);\n"
            "border: 1px solid rgb(85, 170, 255);\n"
            "padding: 5px;\n"
            "border-radius: 8px;"
        )
        pushButton_send_email.setFont(self.font2)
        pushButton_send_email.setIcon(
            QIcon(QIcon.fromTheme(QIcon.ThemeIcon.MediaSkipForward))
        )
        pushButton_send_email.setLayoutDirection(
            Qt.LayoutDirection.RightToLeft
        )
        verticalLayout.addWidget(pushButton_send_email)
        return pushButton_send_email, page_2

    def __list(self, page_2):
        listWidget_email = QListWidget(page_2)
        
        self.sizePolicy_2.setHeightForWidth(
            listWidget_email.sizePolicy().hasHeightForWidth()
        )
        listWidget_email.setSizePolicy(self.sizePolicy_2)
        
        listWidget_email.setFont(self.font)

        listWidget_email.itemChanged.connect(self.updt)
        return listWidget_email

    def fill(self, ids, data):
        self.listWidget_email.clear()
        for row, value in enumerate(data):
            item = QListWidgetItem()
            item.setFlags(Qt.ItemIsSelectable |Qt.ItemIsEditable |Qt.ItemIsEnabled)
            item.__setattr__('id', ids[row])
            item.setText(str(value))
            self.listWidget_email.addItem(item)

    def add(self):
        item = QListWidgetItem()
        item.setFlags(Qt.ItemIsSelectable |Qt.ItemIsEditable |Qt.ItemIsEnabled)
        item.__setattr__('id', None)
        item.setBackground(self.add_brush)

        self.listWidget_email.addItem(item)
        self.listWidget_email.openPersistentEditor(item)
        self.listWidget_email.editItem(item)
        item.setSelected(True)

    def updt(self):
        item = self.listWidget_email.selectedItems()[0]
        if item.__getattribute__('not_updatable') == True:
            item.__setattr__('not_updatable', False)
            return 
        
        self.listWidget_email.closePersistentEditor(item)
        bush = self.add_brush\
                if None == item.__getattribute__('id')\
                    else self.updt_brush
        item.__setattr__('edited', True)
        item.setBackground(bush)

    def remove(self):
        try:
            item = self.listWidget_email.selectedItems()[0]
            if item.text() == '' or item.__getattribute__('id') == None:
                    self.listWidget_email.takeItem(
                        self.listWidget_email.row(item)
                    )
            else:
                bush = self.remove_brush
                if item.background() == self.remove_brush:
                    bush = self.updt_brush\
                        if True == item.__getattribute__('edited')\
                            else self.no_brush
                item.__setattr__('not_updatable', True)
                item.setBackground(bush)
        except IndexError:
            messagebox.showerror('Aviso', 'Primeiro, selecione o e-mail que deseja remover')

    def __valid_add(self, text):
        if text == '':
            raise Exception(
                    'Defina um endereço de e-mail para o espaço adcionado, caso contrário, o remova'
            )