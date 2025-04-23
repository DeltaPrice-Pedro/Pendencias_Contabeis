from ICRUD import ICRUD

from PySide6.QtCore import (
    QSize
)
from PySide6.QtGui import (
    QFont
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

        self.stackedWidget_pedency = QStackedWidget(self.page_4)
        self.stackedWidget_pedency.addWidget(self.__page_1())
        self.stackedWidget_pedency.addWidget(self.__page_2())
        pass

    def __call__(self, *args, **kwds):
        return self.stackedWidget_pedency

    def __page_1(self) -> QWidget:
        page_1 = QWidget()
        verticalLayout = QVBoxLayout(page_1)

        tableWidget_pedency = QTableWidget(page_1)
        verticalLayout.addWidget(tableWidget_pedency)

        line = QFrame(page_1)
        line.setFrameShape(QFrame.Shape.HLine)
        line.setFrameShadow(QFrame.Shadow.Sunken)

        verticalLayout.addWidget(line)

        tableWidget_pedency_show = QTableWidget(page_1)
        verticalLayout.addWidget(tableWidget_pedency_show)
        return page_1

    def __page_2(self) -> QWidget:
        page_2 = QWidget()
        gridLayout = QGridLayout(page_2)

        comboBox = QComboBox(page_2)
        gridLayout.addWidget(comboBox, 0, 1, 1, 1)

        for i in range(5):
            label = self.label_factory(page_2)
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


    def label_factory(self, page_2: QWidget) -> QLabel:
        label = QLabel(page_2)
        self.sizePolicy.setHeightForWidth(label.sizePolicy().hasHeightForWidth())
        label.setSizePolicy(self.sizePolicy)
        label.setFont(self.font)
        return label

    def add(self):
        ...

    def updt(self):...

    def remove(self):...