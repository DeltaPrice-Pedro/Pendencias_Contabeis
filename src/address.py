from PySide6.QtCore import (
    QSize, Qt
)
from PySide6.QtGui import (
    QFont, QIcon, QColor, QBrush
)
from PySide6.QtWidgets import (
    QFrame,QHBoxLayout, QListWidget,
    QListWidgetItem, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

from change import Change
from tkinter import messagebox
from re import findall

class Address:
    def __init__(self, id, address):
        self.sizePolicy = QSizePolicy(
            QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum
        )
        self.sizePolicy_2 = QSizePolicy(
            QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Expanding
        )
        self.sizePolicy.setHorizontalStretch(0)
        self.sizePolicy.setVerticalStretch(0)

        self.font = QFont()
        self.font.setFamilies([u"Tw Cen MT"])
        self.font.setPointSize(12)

        self.add_brush = QBrush(QColor(179, 255, 178, 255))
        self.add_brush.setStyle(Qt.BrushStyle.Dense1Pattern)

        self.updt_brush = QBrush(QColor(189, 253, 254, 255))
        self.updt_brush.setStyle(Qt.BrushStyle.Dense1Pattern)

        self.remove_brush = QBrush(QColor(254, 139, 139, 255))
        self.remove_brush.setStyle(Qt.BrushStyle.Dense1Pattern)

        self.no_brush = QBrush(Qt.BrushStyle.NoBrush)

        self.page = self.__page()
        self.__fill(id, address)
        pass

    def __call__(self, *args, **kwds):
        return self.page

    def __page(self):
        page_2 = QWidget()
        verticalLayout = QVBoxLayout(page_2)

        self.listWidget_email = self.__list(page_2)
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
        verticalLayout.addWidget(pushButton_send_email)
        return page_2

    def __buttons(self, frame_email_func):
        pushButton_add = QPushButton(frame_email_func)
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.ListAdd))
        pushButton_add.setIcon(icon)
        pushButton_add.clicked.connect(self.add)

        pushButton_remove = QPushButton(frame_email_func)
        icon_2 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.ListRemove))
        pushButton_remove.setIcon(icon_2)
        pushButton_remove.clicked.connect(self.remove)
        return pushButton_add, pushButton_remove

    def __list(self, page_2):
        listWidget_email = QListWidget(page_2)
        
        self.sizePolicy_2.setHeightForWidth(
            listWidget_email.sizePolicy().hasHeightForWidth()
        )
        listWidget_email.setSizePolicy(self.sizePolicy_2)
        
        listWidget_email.setFont(self.font)

        # listWidget_email.itemChanged.connect(self.updt)
        return listWidget_email

    def __fill(self, ids, data):
        for row, value in enumerate(data):
            item = QListWidgetItem()
            item.setFlags(Qt.ItemIsSelectable |Qt.ItemIsEditable |Qt.ItemIsEnabled)
            item.__setattr__('id', ids[row])
            item.__setattr__('edited', False)
            item.setText(str(value))
            self.listWidget_email.addItem(item)

    def add(self):
        item = QListWidgetItem()
        item.setFlags(Qt.ItemIsSelectable |Qt.ItemIsEditable |Qt.ItemIsEnabled)
        item.__setattr__('id', None)
        item.__setattr__('edited', False)
        item.setBackground(self.add_brush)

        self.listWidget_email.addItem(item)

    def updt(self):
        item = self.listWidget_email.selectedItems()[0]
        bush = self.add_brush\
                 if None == item.__getattribute__('id')\
                    else self.updt_brush
        item.__setattr__('edited', True)
        item.setBackground(bush)

    def remove(self):
        try:
            item = self.listWidget_email.selectedItems()[0]
            if item.text() == '':
                    self.listWidget_email.takeItem(
                        self.listWidget_email.row(item)
                    )
            elif item.background() == self.remove_brush:
                if None == item.__getattribute__('id'):
                    bush = self.add_brush
                elif True == item.__getattribute__('edited'):
                    bush = self.updt_brush
                else:
                    bush = self.no_brush
            else:
                bush = self.remove_brush
            item.setBackground(bush)
        except IndexError:
            messagebox.showerror('Aviso', 'Primeiro, selecione o e-mail que deseja remover')

    def change(self):
        changes = Change()
        for row in range(self.listWidget_email.count()):
            item = self.listWidget_email.item(row)
            brush = item.background()
            if brush == self.add_brush:
                text = item.text()
                self.__valid_add(text)
                changes.to_add(text)

            elif brush == self.updt_brush:
                changes.to_updt(
                    item.__getattribute__('id'), 
                    item.text()
                )

            elif brush == self.remove_brush:
                changes.to_remove(item.__getattribute__('id'))
        return changes

    def __valid_add(self, text):
        if text == '':
            raise Exception(
                    'Defina um endereço de e-mail para o espaço adcionado, caso contrário, o remova'
            )
                    
        if len(findall(r'@|\.com', text)) != 2:
            raise Exception(
                    'Defina um endereço de e-mail válido'
            )