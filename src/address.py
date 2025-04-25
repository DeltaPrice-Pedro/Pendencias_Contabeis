from PySide6.QtCore import (
    QSize, 
)
from PySide6.QtGui import (
    QFont, QIcon,
)
from PySide6.QtWidgets import (
    QFrame,QHBoxLayout, QListWidget,
    QListWidgetItem, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Address:
    def __init__(self, id, address):
        self.sizePolicy = QSizePolicy(
            QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum
        )
        self.sizePolicy.setHorizontalStretch(0)
        self.sizePolicy.setVerticalStretch(0)

        self.font = QFont()
        self.font.setFamilies([u"Tw Cen MT"])
        self.font.setPointSize(12)
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

        pushButton_add_email = QPushButton(frame_email_func)
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.ListAdd))
        pushButton_add_email.setIcon(icon)
        horizontalLayout.addWidget(pushButton_add_email)

        pushButton_remove_email = QPushButton(frame_email_func)
        icon_2 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.ListRemove))
        pushButton_remove_email.setIcon(icon_2)
        horizontalLayout.addWidget(pushButton_remove_email)

        verticalLayout.addWidget(frame_email_func)

        pushButton_send_email = QPushButton(page_2)
        verticalLayout.addWidget(pushButton_send_email)
        return page_2

    def __list(self, page_2):
        listWidget_email = QListWidget(page_2)
        listWidget_email.setMaximumSize(QSize(200, 16777215))
        
        self.sizePolicy.setHeightForWidth(
            listWidget_email.sizePolicy().hasHeightForWidth()
        )
        listWidget_email.setSizePolicy(self.sizePolicy)
        
        listWidget_email.setFont(self.font)
        return listWidget_email

    def __fill(self, ids, data):
        for row, value in enumerate(data):
            item = QListWidgetItem()
            item.__setattr__('id', ids[row])
            item.setText(str(value))
            self.listWidget_email.addItem(item)