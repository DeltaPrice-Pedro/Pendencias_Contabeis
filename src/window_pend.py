# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'window_pend.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDateEdit, QFrame, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QLineEdit,
    QListWidget, QListWidgetItem, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(847, 626)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"background-color: rgb(227, 227, 227);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.stackedWidget_body = QStackedWidget(self.centralwidget)
        self.stackedWidget_body.setObjectName(u"stackedWidget_body")
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.gridLayout_5 = QGridLayout(self.page_2)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.groupBox_sheet = QGroupBox(self.page_2)
        self.groupBox_sheet.setObjectName(u"groupBox_sheet")
        font = QFont()
        font.setFamilies([u"Tw Cen MT"])
        font.setPointSize(18)
        font.setBold(True)
        self.groupBox_sheet.setFont(font)
        self.groupBox_sheet.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.groupBox_sheet.setFlat(True)
        self.verticalLayout_7 = QVBoxLayout(self.groupBox_sheet)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.frame_4 = QFrame(self.groupBox_sheet)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_6 = QGridLayout(self.frame_4)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.label_util_sheet = QLabel(self.frame_4)
        self.label_util_sheet.setObjectName(u"label_util_sheet")
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(12)
        font1.setBold(False)
        self.label_util_sheet.setFont(font1)

        self.gridLayout_6.addWidget(self.label_util_sheet, 1, 3, 1, 1)

        self.label_from_sheet = QLabel(self.frame_4)
        self.label_from_sheet.setObjectName(u"label_from_sheet")
        self.label_from_sheet.setFont(font1)

        self.gridLayout_6.addWidget(self.label_from_sheet, 1, 0, 1, 1)

        self.dateEdit_from = QDateEdit(self.frame_4)
        self.dateEdit_from.setObjectName(u"dateEdit_from")
        font2 = QFont()
        font2.setFamilies([u"Tw Cen MT"])
        font2.setPointSize(12)
        font2.setBold(False)
        self.dateEdit_from.setFont(font2)
        self.dateEdit_from.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_6.addWidget(self.dateEdit_from, 1, 1, 1, 1)

        self.dateEdit_until = QDateEdit(self.frame_4)
        self.dateEdit_until.setObjectName(u"dateEdit_until")
        self.dateEdit_until.setFont(font2)
        self.dateEdit_until.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_6.addWidget(self.dateEdit_until, 1, 4, 1, 1)

        self.line = QFrame(self.frame_4)
        self.line.setObjectName(u"line")
        self.line.setMinimumSize(QSize(3, 0))
        self.line.setStyleSheet(u"background-color: rgb(85, 170, 255);")
        self.line.setFrameShadow(QFrame.Shadow.Plain)
        self.line.setLineWidth(-1)
        self.line.setFrameShape(QFrame.Shape.VLine)

        self.gridLayout_6.addWidget(self.line, 1, 2, 1, 1)


        self.verticalLayout_7.addWidget(self.frame_4)

        self.pushButton_sheet_func = QPushButton(self.groupBox_sheet)
        self.pushButton_sheet_func.setObjectName(u"pushButton_sheet_func")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_sheet_func.sizePolicy().hasHeightForWidth())
        self.pushButton_sheet_func.setSizePolicy(sizePolicy)
        font3 = QFont()
        font3.setFamilies([u"Tw Cen MT"])
        font3.setPointSize(16)
        font3.setBold(False)
        self.pushButton_sheet_func.setFont(font3)
        self.pushButton_sheet_func.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_sheet_func.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: 1px solid rgb(85, 170, 255);\n"
"padding: 5px;\n"
"border-radius: 8px;")
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.EditPaste))
        self.pushButton_sheet_func.setIcon(icon)
        self.pushButton_sheet_func.setIconSize(QSize(30, 30))

        self.verticalLayout_7.addWidget(self.pushButton_sheet_func)


        self.gridLayout_5.addWidget(self.groupBox_sheet, 5, 0, 1, 1)

        self.frame_operation = QFrame(self.page_2)
        self.frame_operation.setObjectName(u"frame_operation")
        self.frame_operation.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_operation.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_operation)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.pushButton_cancel_operation = QPushButton(self.frame_operation)
        self.pushButton_cancel_operation.setObjectName(u"pushButton_cancel_operation")
        self.pushButton_cancel_operation.setMinimumSize(QSize(0, 35))
        font4 = QFont()
        font4.setFamilies([u"Tw Cen MT"])
        font4.setPointSize(13)
        font4.setItalic(True)
        font4.setUnderline(True)
        self.pushButton_cancel_operation.setFont(font4)
        self.pushButton_cancel_operation.setStyleSheet(u"background-color: rgb(235, 235, 235);")

        self.horizontalLayout_8.addWidget(self.pushButton_cancel_operation)

        self.line_4 = QFrame(self.frame_operation)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setMinimumSize(QSize(3, 0))
        self.line_4.setStyleSheet(u"background-color: rgb(85, 170, 255);")
        self.line_4.setFrameShadow(QFrame.Shadow.Plain)
        self.line_4.setLineWidth(-1)
        self.line_4.setFrameShape(QFrame.Shape.VLine)

        self.horizontalLayout_8.addWidget(self.line_4)

        self.pushButton_confirm_operation = QPushButton(self.frame_operation)
        self.pushButton_confirm_operation.setObjectName(u"pushButton_confirm_operation")
        self.pushButton_confirm_operation.setMinimumSize(QSize(0, 35))
        self.pushButton_confirm_operation.setFont(font4)
        self.pushButton_confirm_operation.setStyleSheet(u"background-color: rgb(235, 235, 235);")

        self.horizontalLayout_8.addWidget(self.pushButton_confirm_operation)


        self.gridLayout_5.addWidget(self.frame_operation, 1, 0, 1, 1)

        self.groupBox_email = QGroupBox(self.page_2)
        self.groupBox_email.setObjectName(u"groupBox_email")
        sizePolicy.setHeightForWidth(self.groupBox_email.sizePolicy().hasHeightForWidth())
        self.groupBox_email.setSizePolicy(sizePolicy)
        self.groupBox_email.setFont(font)
        self.groupBox_email.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.groupBox_email.setFlat(True)
        self.groupBox_email.setCheckable(False)
        self.gridLayout_2 = QGridLayout(self.groupBox_email)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.stackedWidget_email = QStackedWidget(self.groupBox_email)
        self.stackedWidget_email.setObjectName(u"stackedWidget_email")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.stackedWidget_email.sizePolicy().hasHeightForWidth())
        self.stackedWidget_email.setSizePolicy(sizePolicy1)
        self.stackedWidget_email.setMinimumSize(QSize(350, 0))
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setStyleSheet(u"background-color: rgb(194, 194, 194);")
        self.gridLayout_3 = QGridLayout(self.page)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_none_companie = QLabel(self.page)
        self.label_none_companie.setObjectName(u"label_none_companie")
        sizePolicy1.setHeightForWidth(self.label_none_companie.sizePolicy().hasHeightForWidth())
        self.label_none_companie.setSizePolicy(sizePolicy1)
        font5 = QFont()
        font5.setFamilies([u"Sitka"])
        font5.setPointSize(18)
        font5.setBold(False)
        font5.setItalic(True)
        self.label_none_companie.setFont(font5)
        self.label_none_companie.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_3.addWidget(self.label_none_companie, 0, 0, 1, 1)

        self.stackedWidget_email.addWidget(self.page)
        self.page_7 = QWidget()
        self.page_7.setObjectName(u"page_7")
        self.verticalLayout_6 = QVBoxLayout(self.page_7)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label = QLabel(self.page_7)
        self.label.setObjectName(u"label")
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        font6 = QFont()
        font6.setFamilies([u"Tw Cen MT"])
        font6.setPointSize(16)
        font6.setBold(False)
        font6.setItalic(True)
        self.label.setFont(font6)

        self.verticalLayout_6.addWidget(self.label)

        self.lineEdit_name_func = QLineEdit(self.page_7)
        self.lineEdit_name_func.setObjectName(u"lineEdit_name_func")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.lineEdit_name_func.sizePolicy().hasHeightForWidth())
        self.lineEdit_name_func.setSizePolicy(sizePolicy2)
        font7 = QFont()
        font7.setFamilies([u"Arial"])
        font7.setPointSize(9)
        font7.setBold(False)
        self.lineEdit_name_func.setFont(font7)
        self.lineEdit_name_func.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.lineEdit_name_func.setMaxLength(25)
        self.lineEdit_name_func.setClearButtonEnabled(True)

        self.verticalLayout_6.addWidget(self.lineEdit_name_func)

        self.frame_3 = QFrame(self.page_7)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy3)
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pushButton_cancel_email = QPushButton(self.frame_3)
        self.pushButton_cancel_email.setObjectName(u"pushButton_cancel_email")
        self.pushButton_cancel_email.setFont(font3)
        self.pushButton_cancel_email.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: 1px solid rgb(85, 170, 255);\n"
"padding: 5px;\n"
"border-radius: 8px;")
        icon1 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.DocumentRevert))
        self.pushButton_cancel_email.setIcon(icon1)

        self.horizontalLayout_3.addWidget(self.pushButton_cancel_email)

        self.pushButton_send_email = QPushButton(self.frame_3)
        self.pushButton_send_email.setObjectName(u"pushButton_send_email")
        self.pushButton_send_email.setFont(font3)
        self.pushButton_send_email.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: 1px solid rgb(85, 170, 255);\n"
"padding: 5px;\n"
"border-radius: 8px;")
        icon2 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.DocumentSend))
        self.pushButton_send_email.setIcon(icon2)

        self.horizontalLayout_3.addWidget(self.pushButton_send_email)


        self.verticalLayout_6.addWidget(self.frame_3)

        self.stackedWidget_email.addWidget(self.page_7)

        self.gridLayout_2.addWidget(self.stackedWidget_email, 0, 0, 1, 1)


        self.gridLayout_5.addWidget(self.groupBox_email, 3, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_2, 2, 0, 1, 1)

        self.frame_2 = QFrame(self.page_2)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.pushButton_reload_companie = QPushButton(self.frame_2)
        self.pushButton_reload_companie.setObjectName(u"pushButton_reload_companie")
        sizePolicy1.setHeightForWidth(self.pushButton_reload_companie.sizePolicy().hasHeightForWidth())
        self.pushButton_reload_companie.setSizePolicy(sizePolicy1)
        self.pushButton_reload_companie.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_reload_companie.setStyleSheet(u"background-color: rgb(235, 235, 235);")
        icon3 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.SyncSynchronizing))
        self.pushButton_reload_companie.setIcon(icon3)

        self.verticalLayout_5.addWidget(self.pushButton_reload_companie)

        self.frame_5 = QFrame(self.frame_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.line_3 = QFrame(self.frame_5)
        self.line_3.setObjectName(u"line_3")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.line_3.sizePolicy().hasHeightForWidth())
        self.line_3.setSizePolicy(sizePolicy4)
        self.line_3.setMinimumSize(QSize(5, 0))
        self.line_3.setStyleSheet(u"background-color: rgb(85, 170, 255);")
        self.line_3.setLineWidth(0)
        self.line_3.setMidLineWidth(0)
        self.line_3.setFrameShape(QFrame.Shape.VLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_4.addWidget(self.line_3)


        self.verticalLayout_5.addWidget(self.frame_5)


        self.gridLayout_5.addWidget(self.frame_2, 0, 3, 6, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_3, 4, 0, 1, 1)

        self.stackedWidget_companie = QStackedWidget(self.page_2)
        self.stackedWidget_companie.setObjectName(u"stackedWidget_companie")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.stackedWidget_companie.sizePolicy().hasHeightForWidth())
        self.stackedWidget_companie.setSizePolicy(sizePolicy5)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.gridLayout_4 = QGridLayout(self.page_3)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.frame_title_companie = QFrame(self.page_3)
        self.frame_title_companie.setObjectName(u"frame_title_companie")
        self.frame_title_companie.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_title_companie.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_title_companie)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame_7 = QFrame(self.frame_title_companie)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.frame_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.pushButton_companies = QPushButton(self.frame_7)
        self.pushButton_companies.setObjectName(u"pushButton_companies")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.pushButton_companies.sizePolicy().hasHeightForWidth())
        self.pushButton_companies.setSizePolicy(sizePolicy6)
        font8 = QFont()
        font8.setFamilies([u"Tw Cen MT"])
        font8.setPointSize(12)
        self.pushButton_companies.setFont(font8)
        self.pushButton_companies.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_companies.setStyleSheet(u"background-color: rgb(235, 235, 235);")
        icon4 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.EditCopy))
        self.pushButton_companies.setIcon(icon4)

        self.horizontalLayout_6.addWidget(self.pushButton_companies)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_3)


        self.verticalLayout_4.addWidget(self.frame_7)

        self.label_companie_intro = QLabel(self.frame_title_companie)
        self.label_companie_intro.setObjectName(u"label_companie_intro")
        font9 = QFont()
        font9.setFamilies([u"Tw Cen MT"])
        font9.setPointSize(28)
        font9.setBold(True)
        self.label_companie_intro.setFont(font9)
        self.label_companie_intro.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_companie_intro)

        self.label_companie_subintro = QLabel(self.frame_title_companie)
        self.label_companie_subintro.setObjectName(u"label_companie_subintro")
        sizePolicy.setHeightForWidth(self.label_companie_subintro.sizePolicy().hasHeightForWidth())
        self.label_companie_subintro.setSizePolicy(sizePolicy)
        self.label_companie_subintro.setFont(font2)
        self.label_companie_subintro.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_companie_subintro)


        self.gridLayout_4.addWidget(self.frame_title_companie, 0, 0, 1, 1)

        self.listWidget_companie = QListWidget(self.page_3)
        QListWidgetItem(self.listWidget_companie)
        self.listWidget_companie.setObjectName(u"listWidget_companie")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.listWidget_companie.sizePolicy().hasHeightForWidth())
        self.listWidget_companie.setSizePolicy(sizePolicy7)
        font10 = QFont()
        font10.setFamilies([u"Century"])
        font10.setPointSize(18)
        font10.setItalic(True)
        self.listWidget_companie.setFont(font10)
        self.listWidget_companie.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.listWidget_companie.setAlternatingRowColors(True)
        self.listWidget_companie.setSortingEnabled(True)

        self.gridLayout_4.addWidget(self.listWidget_companie, 1, 0, 1, 1)

        self.stackedWidget_companie.addWidget(self.page_3)
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.verticalLayout = QVBoxLayout(self.page_6)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_8 = QFrame(self.page_6)
        self.frame_8.setObjectName(u"frame_8")
        sizePolicy3.setHeightForWidth(self.frame_8.sizePolicy().hasHeightForWidth())
        self.frame_8.setSizePolicy(sizePolicy3)
        self.frame_8.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.pushButton_taxes = QPushButton(self.frame_8)
        self.pushButton_taxes.setObjectName(u"pushButton_taxes")
        self.pushButton_taxes.setFont(font8)
        self.pushButton_taxes.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_taxes.setStyleSheet(u"background-color: rgb(235, 235, 235);")
        icon5 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.GoHome))
        self.pushButton_taxes.setIcon(icon5)

        self.horizontalLayout_7.addWidget(self.pushButton_taxes)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_4)


        self.verticalLayout.addWidget(self.frame_8)

        self.label_title_taxes = QLabel(self.page_6)
        self.label_title_taxes.setObjectName(u"label_title_taxes")
        sizePolicy3.setHeightForWidth(self.label_title_taxes.sizePolicy().hasHeightForWidth())
        self.label_title_taxes.setSizePolicy(sizePolicy3)
        self.label_title_taxes.setFont(font9)
        self.label_title_taxes.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label_title_taxes)

        self.listWidget_taxes = QListWidget(self.page_6)
        self.listWidget_taxes.setObjectName(u"listWidget_taxes")
        font11 = QFont()
        font11.setFamilies([u"Arial"])
        font11.setPointSize(22)
        self.listWidget_taxes.setFont(font11)
        self.listWidget_taxes.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.listWidget_taxes.setAlternatingRowColors(True)
        self.listWidget_taxes.setSortingEnabled(True)

        self.verticalLayout.addWidget(self.listWidget_taxes)

        self.stackedWidget_companie.addWidget(self.page_6)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.verticalLayout_3 = QVBoxLayout(self.page_4)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_current_companie = QFrame(self.page_4)
        self.frame_current_companie.setObjectName(u"frame_current_companie")
        self.frame_current_companie.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_current_companie.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_current_companie)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_exit_companie = QPushButton(self.frame_current_companie)
        self.pushButton_exit_companie.setObjectName(u"pushButton_exit_companie")
        sizePolicy4.setHeightForWidth(self.pushButton_exit_companie.sizePolicy().hasHeightForWidth())
        self.pushButton_exit_companie.setSizePolicy(sizePolicy4)
        self.pushButton_exit_companie.setStyleSheet(u"background-color: rgb(235, 235, 235);")
        icon6 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.SystemLogOut))
        self.pushButton_exit_companie.setIcon(icon6)

        self.horizontalLayout.addWidget(self.pushButton_exit_companie)

        self.line_2 = QFrame(self.frame_current_companie)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.VLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout.addWidget(self.line_2)

        self.label_current_companie = QLabel(self.frame_current_companie)
        self.label_current_companie.setObjectName(u"label_current_companie")
        self.label_current_companie.setFont(font)
        self.label_current_companie.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.label_current_companie)


        self.verticalLayout_3.addWidget(self.frame_current_companie)

        self.stackedWidget_companie.addWidget(self.page_4)

        self.gridLayout_5.addWidget(self.stackedWidget_companie, 0, 2, 6, 1)

        self.groupBox_func = QGroupBox(self.page_2)
        self.groupBox_func.setObjectName(u"groupBox_func")
        sizePolicy.setHeightForWidth(self.groupBox_func.sizePolicy().hasHeightForWidth())
        self.groupBox_func.setSizePolicy(sizePolicy)
        self.groupBox_func.setFont(font)
        self.groupBox_func.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.groupBox_func.setFlat(True)
        self.gridLayout_7 = QGridLayout(self.groupBox_func)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.pushButton_add_func = QPushButton(self.groupBox_func)
        self.pushButton_add_func.setObjectName(u"pushButton_add_func")
        sizePolicy8 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.pushButton_add_func.sizePolicy().hasHeightForWidth())
        self.pushButton_add_func.setSizePolicy(sizePolicy8)
        self.pushButton_add_func.setFont(font3)
        self.pushButton_add_func.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_add_func.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: 1px solid rgb(85, 170, 255);\n"
"padding: 5px;\n"
"border-radius: 8px;")
        icon7 = QIcon()
        icon7.addFile(u"../../../../../Downloads/add_icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_add_func.setIcon(icon7)
        self.pushButton_add_func.setIconSize(QSize(40, 40))

        self.gridLayout_7.addWidget(self.pushButton_add_func, 0, 0, 1, 1)

        self.pushButton_save_func = QPushButton(self.groupBox_func)
        self.pushButton_save_func.setObjectName(u"pushButton_save_func")
        sizePolicy8.setHeightForWidth(self.pushButton_save_func.sizePolicy().hasHeightForWidth())
        self.pushButton_save_func.setSizePolicy(sizePolicy8)
        self.pushButton_save_func.setFont(font3)
        self.pushButton_save_func.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_save_func.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: 1px solid rgb(85, 170, 255);\n"
"padding: 5px;\n"
"border-radius: 8px;")
        icon8 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.DocumentSave))
        self.pushButton_save_func.setIcon(icon8)
        self.pushButton_save_func.setIconSize(QSize(35, 35))

        self.gridLayout_7.addWidget(self.pushButton_save_func, 2, 1, 1, 1)

        self.pushButton_remove_func = QPushButton(self.groupBox_func)
        self.pushButton_remove_func.setObjectName(u"pushButton_remove_func")
        sizePolicy8.setHeightForWidth(self.pushButton_remove_func.sizePolicy().hasHeightForWidth())
        self.pushButton_remove_func.setSizePolicy(sizePolicy8)
        self.pushButton_remove_func.setFont(font3)
        self.pushButton_remove_func.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_remove_func.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: 1px solid rgb(85, 170, 255);\n"
"padding: 5px;\n"
"border-radius: 8px;")
        icon9 = QIcon()
        icon9.addFile(u"../../../../../Downloads/remove_icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_remove_func.setIcon(icon9)
        self.pushButton_remove_func.setIconSize(QSize(35, 35))

        self.gridLayout_7.addWidget(self.pushButton_remove_func, 2, 0, 1, 1)

        self.pushButton_edit_func = QPushButton(self.groupBox_func)
        self.pushButton_edit_func.setObjectName(u"pushButton_edit_func")
        sizePolicy8.setHeightForWidth(self.pushButton_edit_func.sizePolicy().hasHeightForWidth())
        self.pushButton_edit_func.setSizePolicy(sizePolicy8)
        self.pushButton_edit_func.setFont(font3)
        self.pushButton_edit_func.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_edit_func.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: 1px solid rgb(85, 170, 255);\n"
"padding: 5px;\n"
"border-radius: 8px;")
        icon10 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.MailMessageNew))
        self.pushButton_edit_func.setIcon(icon10)
        self.pushButton_edit_func.setIconSize(QSize(35, 35))

        self.gridLayout_7.addWidget(self.pushButton_edit_func, 0, 1, 1, 1)


        self.gridLayout_5.addWidget(self.groupBox_func, 0, 0, 1, 1)

        self.stackedWidget_body.addWidget(self.page_2)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.verticalLayout_2 = QVBoxLayout(self.page_5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(self.page_5)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(60, 40, 60, 40)
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.label_load_gif = QLabel(self.frame)
        self.label_load_gif.setObjectName(u"label_load_gif")
        self.label_load_gif.setMinimumSize(QSize(200, 200))
        self.label_load_gif.setPixmap(QPixmap(u"../imgs/load.gif"))
        self.label_load_gif.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.label_load_gif)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout_2.addWidget(self.frame)

        self.label_2 = QLabel(self.page_5)
        self.label_2.setObjectName(u"label_2")
        font12 = QFont()
        font12.setFamilies([u"Tw Cen MT"])
        font12.setPointSize(36)
        font12.setBold(True)
        font12.setItalic(True)
        self.label_2.setFont(font12)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_2)

        self.stackedWidget_body.addWidget(self.page_5)

        self.gridLayout.addWidget(self.stackedWidget_body, 1, 0, 1, 2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 847, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        self.statusbar.setStyleSheet(u"background-color: rgb(85, 170, 255);")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.stackedWidget_body.setCurrentIndex(0)
        self.stackedWidget_email.setCurrentIndex(0)
        self.stackedWidget_companie.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Pend\u00eancias Cont\u00e1beis", None))
#if QT_CONFIG(tooltip)
        self.groupBox_sheet.setToolTip(QCoreApplication.translate("MainWindow", u"Gerar relat\u00f3rio", None))
#endif // QT_CONFIG(tooltip)
        self.groupBox_sheet.setTitle(QCoreApplication.translate("MainWindow", u"Relat\u00f3rio", None))
        self.label_util_sheet.setText(QCoreApplication.translate("MainWindow", u"At\u00e9:", None))
        self.label_from_sheet.setText(QCoreApplication.translate("MainWindow", u"De:", None))
        self.pushButton_sheet_func.setText(QCoreApplication.translate("MainWindow", u" Gerar", None))
        self.pushButton_cancel_operation.setText(QCoreApplication.translate("MainWindow", u"Cancelar", None))
        self.pushButton_confirm_operation.setText(QCoreApplication.translate("MainWindow", u"Confirmar", None))
        self.groupBox_email.setTitle(QCoreApplication.translate("MainWindow", u"Email", None))
        self.label_none_companie.setText(QCoreApplication.translate("MainWindow", u"Primeiro, selecione\n"
"uma empresa", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Respons\u00e1vel pelo envio:", None))
        self.lineEdit_name_func.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Insira nome e sobrenome", None))
#if QT_CONFIG(tooltip)
        self.pushButton_cancel_email.setToolTip(QCoreApplication.translate("MainWindow", u"Voltar para sele\u00e7\u00e3o de e-mails da empresa", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_cancel_email.setText(QCoreApplication.translate("MainWindow", u"Voltar", None))
#if QT_CONFIG(tooltip)
        self.pushButton_send_email.setToolTip(QCoreApplication.translate("MainWindow", u"Envia e-mail com assinatura do respons\u00e1vel", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_send_email.setText(QCoreApplication.translate("MainWindow", u"Enviar", None))
#if QT_CONFIG(tooltip)
        self.pushButton_reload_companie.setToolTip(QCoreApplication.translate("MainWindow", u"Atualizar dados recentes", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_reload_companie.setText("")
        self.pushButton_companies.setText(QCoreApplication.translate("MainWindow", u" Impostos cadastrados", None))
        self.label_companie_intro.setText(QCoreApplication.translate("MainWindow", u"Empresas Dispon\u00edveis", None))
        self.label_companie_subintro.setText(QCoreApplication.translate("MainWindow", u"Clique 2x para selecionar", None))

        __sortingEnabled = self.listWidget_companie.isSortingEnabled()
        self.listWidget_companie.setSortingEnabled(False)
        ___qlistwidgetitem = self.listWidget_companie.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", u"New Item", None));
        self.listWidget_companie.setSortingEnabled(__sortingEnabled)

        self.pushButton_taxes.setText(QCoreApplication.translate("MainWindow", u"Empresas Cadastradas", None))
        self.label_title_taxes.setText(QCoreApplication.translate("MainWindow", u"Impostos Dispon\u00edveis", None))
#if QT_CONFIG(tooltip)
        self.pushButton_exit_companie.setToolTip(QCoreApplication.translate("MainWindow", u"Voltar para a lista de empresas cadastradas", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_exit_companie.setText("")
        self.label_current_companie.setText(QCoreApplication.translate("MainWindow", u"Nome Empresa", None))
        self.groupBox_func.setTitle(QCoreApplication.translate("MainWindow", u"Fun\u00e7\u00f5es", None))
        self.pushButton_add_func.setText(QCoreApplication.translate("MainWindow", u"Adcionar", None))
#if QT_CONFIG(tooltip)
        self.pushButton_save_func.setToolTip(QCoreApplication.translate("MainWindow", u"Salva as altera\u00e7\u00f5es descritas em cores", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_save_func.setText(QCoreApplication.translate("MainWindow", u"  Salvar   ", None))
        self.pushButton_remove_func.setText(QCoreApplication.translate("MainWindow", u" Remover", None))
        self.pushButton_edit_func.setText(QCoreApplication.translate("MainWindow", u"  Editar    ", None))
        self.label_load_gif.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Enviando Email...", None))
    # retranslateUi

