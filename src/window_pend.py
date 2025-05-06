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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QListWidget,
    QListWidgetItem, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QStatusBar,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(593, 520)
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
        self.stackedWidget_companie = QStackedWidget(self.page_2)
        self.stackedWidget_companie.setObjectName(u"stackedWidget_companie")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stackedWidget_companie.sizePolicy().hasHeightForWidth())
        self.stackedWidget_companie.setSizePolicy(sizePolicy)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.gridLayout_4 = QGridLayout(self.page_3)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.listWidget_companie = QListWidget(self.page_3)
        QListWidgetItem(self.listWidget_companie)
        self.listWidget_companie.setObjectName(u"listWidget_companie")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.listWidget_companie.sizePolicy().hasHeightForWidth())
        self.listWidget_companie.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setPointSize(14)
        self.listWidget_companie.setFont(font)

        self.gridLayout_4.addWidget(self.listWidget_companie, 1, 0, 1, 1)

        self.frame_title_companie = QFrame(self.page_3)
        self.frame_title_companie.setObjectName(u"frame_title_companie")
        self.frame_title_companie.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_title_companie.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_title_companie)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_companie_intro = QLabel(self.frame_title_companie)
        self.label_companie_intro.setObjectName(u"label_companie_intro")
        font1 = QFont()
        font1.setFamilies([u"Tw Cen MT"])
        font1.setPointSize(18)
        font1.setBold(True)
        self.label_companie_intro.setFont(font1)
        self.label_companie_intro.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_companie_intro)

        self.label_companie_subintro = QLabel(self.frame_title_companie)
        self.label_companie_subintro.setObjectName(u"label_companie_subintro")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_companie_subintro.sizePolicy().hasHeightForWidth())
        self.label_companie_subintro.setSizePolicy(sizePolicy2)
        font2 = QFont()
        font2.setFamilies([u"Tw Cen MT"])
        font2.setPointSize(12)
        font2.setBold(False)
        self.label_companie_subintro.setFont(font2)
        self.label_companie_subintro.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_companie_subintro)


        self.gridLayout_4.addWidget(self.frame_title_companie, 0, 0, 1, 1)

        self.stackedWidget_companie.addWidget(self.page_3)
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
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.pushButton_exit_companie.sizePolicy().hasHeightForWidth())
        self.pushButton_exit_companie.setSizePolicy(sizePolicy3)
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.SystemLogOut))
        self.pushButton_exit_companie.setIcon(icon)

        self.horizontalLayout.addWidget(self.pushButton_exit_companie)

        self.line_2 = QFrame(self.frame_current_companie)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.VLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout.addWidget(self.line_2)

        self.label_current_companie = QLabel(self.frame_current_companie)
        self.label_current_companie.setObjectName(u"label_current_companie")
        self.label_current_companie.setFont(font1)
        self.label_current_companie.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.label_current_companie)


        self.verticalLayout_3.addWidget(self.frame_current_companie)

        self.stackedWidget_companie.addWidget(self.page_4)

        self.gridLayout_5.addWidget(self.stackedWidget_companie, 0, 2, 2, 1)

        self.groupBox_email = QGroupBox(self.page_2)
        self.groupBox_email.setObjectName(u"groupBox_email")
        sizePolicy2.setHeightForWidth(self.groupBox_email.sizePolicy().hasHeightForWidth())
        self.groupBox_email.setSizePolicy(sizePolicy2)
        font3 = QFont()
        font3.setFamilies([u"Tw Cen MT"])
        font3.setPointSize(16)
        font3.setBold(False)
        self.groupBox_email.setFont(font3)
        self.gridLayout_2 = QGridLayout(self.groupBox_email)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.stackedWidget_email = QStackedWidget(self.groupBox_email)
        self.stackedWidget_email.setObjectName(u"stackedWidget_email")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.stackedWidget_email.sizePolicy().hasHeightForWidth())
        self.stackedWidget_email.setSizePolicy(sizePolicy4)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setStyleSheet(u"background-color: rgb(222, 222, 222);\n"
"")
        self.gridLayout_3 = QGridLayout(self.page)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_none_companie = QLabel(self.page)
        self.label_none_companie.setObjectName(u"label_none_companie")
        sizePolicy4.setHeightForWidth(self.label_none_companie.sizePolicy().hasHeightForWidth())
        self.label_none_companie.setSizePolicy(sizePolicy4)
        font4 = QFont()
        font4.setFamilies([u"Sitka"])
        font4.setPointSize(18)
        font4.setBold(False)
        font4.setItalic(True)
        self.label_none_companie.setFont(font4)
        self.label_none_companie.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_3.addWidget(self.label_none_companie, 0, 0, 1, 1)

        self.stackedWidget_email.addWidget(self.page)
        self.page_7 = QWidget()
        self.page_7.setObjectName(u"page_7")
        self.verticalLayout_6 = QVBoxLayout(self.page_7)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label = QLabel(self.page_7)
        self.label.setObjectName(u"label")
        sizePolicy4.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy4)
        font5 = QFont()
        font5.setFamilies([u"Tw Cen MT"])
        font5.setPointSize(16)
        font5.setBold(False)
        font5.setItalic(True)
        self.label.setFont(font5)

        self.verticalLayout_6.addWidget(self.label)

        self.lineEdit_name_func = QLineEdit(self.page_7)
        self.lineEdit_name_func.setObjectName(u"lineEdit_name_func")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Maximum)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.lineEdit_name_func.sizePolicy().hasHeightForWidth())
        self.lineEdit_name_func.setSizePolicy(sizePolicy5)
        font6 = QFont()
        font6.setFamilies([u"Arial"])
        font6.setPointSize(12)
        font6.setBold(False)
        self.lineEdit_name_func.setFont(font6)

        self.verticalLayout_6.addWidget(self.lineEdit_name_func)

        self.frame_3 = QFrame(self.page_7)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy6)
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pushButton_cancel_email = QPushButton(self.frame_3)
        self.pushButton_cancel_email.setObjectName(u"pushButton_cancel_email")
        icon1 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.DocumentRevert))
        self.pushButton_cancel_email.setIcon(icon1)

        self.horizontalLayout_3.addWidget(self.pushButton_cancel_email)

        self.pushButton_send_email = QPushButton(self.frame_3)
        self.pushButton_send_email.setObjectName(u"pushButton_send_email")
        icon2 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.DocumentSend))
        self.pushButton_send_email.setIcon(icon2)

        self.horizontalLayout_3.addWidget(self.pushButton_send_email)


        self.verticalLayout_6.addWidget(self.frame_3)

        self.stackedWidget_email.addWidget(self.page_7)

        self.gridLayout_2.addWidget(self.stackedWidget_email, 0, 0, 1, 1)


        self.gridLayout_5.addWidget(self.groupBox_email, 1, 0, 1, 1)

        self.groupBox_func = QGroupBox(self.page_2)
        self.groupBox_func.setObjectName(u"groupBox_func")
        sizePolicy2.setHeightForWidth(self.groupBox_func.sizePolicy().hasHeightForWidth())
        self.groupBox_func.setSizePolicy(sizePolicy2)
        font7 = QFont()
        font7.setFamilies([u"Tw Cen MT"])
        font7.setPointSize(16)
        self.groupBox_func.setFont(font7)
        self.verticalLayout = QVBoxLayout(self.groupBox_func)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pushButton_add_func = QPushButton(self.groupBox_func)
        self.pushButton_add_func.setObjectName(u"pushButton_add_func")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.pushButton_add_func.sizePolicy().hasHeightForWidth())
        self.pushButton_add_func.setSizePolicy(sizePolicy7)
        self.pushButton_add_func.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u"../../../../../Downloads/add_icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_add_func.setIcon(icon3)
        self.pushButton_add_func.setIconSize(QSize(40, 40))
        self.pushButton_add_func.setFlat(True)

        self.verticalLayout.addWidget(self.pushButton_add_func)

        self.pushButton_remove_func = QPushButton(self.groupBox_func)
        self.pushButton_remove_func.setObjectName(u"pushButton_remove_func")
        sizePolicy7.setHeightForWidth(self.pushButton_remove_func.sizePolicy().hasHeightForWidth())
        self.pushButton_remove_func.setSizePolicy(sizePolicy7)
        self.pushButton_remove_func.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u"../../../../../Downloads/remove_icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_remove_func.setIcon(icon4)
        self.pushButton_remove_func.setIconSize(QSize(35, 35))
        self.pushButton_remove_func.setFlat(True)

        self.verticalLayout.addWidget(self.pushButton_remove_func)

        self.pushButton_edit_func = QPushButton(self.groupBox_func)
        self.pushButton_edit_func.setObjectName(u"pushButton_edit_func")
        sizePolicy7.setHeightForWidth(self.pushButton_edit_func.sizePolicy().hasHeightForWidth())
        self.pushButton_edit_func.setSizePolicy(sizePolicy7)
        icon5 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.MailMessageNew))
        self.pushButton_edit_func.setIcon(icon5)
        self.pushButton_edit_func.setIconSize(QSize(30, 30))
        self.pushButton_edit_func.setFlat(True)

        self.verticalLayout.addWidget(self.pushButton_edit_func)

        self.pushButton_save_func = QPushButton(self.groupBox_func)
        self.pushButton_save_func.setObjectName(u"pushButton_save_func")
        sizePolicy7.setHeightForWidth(self.pushButton_save_func.sizePolicy().hasHeightForWidth())
        self.pushButton_save_func.setSizePolicy(sizePolicy7)
        icon6 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.DocumentSave))
        self.pushButton_save_func.setIcon(icon6)
        self.pushButton_save_func.setIconSize(QSize(30, 30))
        self.pushButton_save_func.setFlat(True)

        self.verticalLayout.addWidget(self.pushButton_save_func)

        self.pushButton_sheet_func = QPushButton(self.groupBox_func)
        self.pushButton_sheet_func.setObjectName(u"pushButton_sheet_func")
        sizePolicy4.setHeightForWidth(self.pushButton_sheet_func.sizePolicy().hasHeightForWidth())
        self.pushButton_sheet_func.setSizePolicy(sizePolicy4)
        icon7 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.EditPaste))
        self.pushButton_sheet_func.setIcon(icon7)
        self.pushButton_sheet_func.setIconSize(QSize(30, 30))
        self.pushButton_sheet_func.setFlat(True)

        self.verticalLayout.addWidget(self.pushButton_sheet_func)


        self.gridLayout_5.addWidget(self.groupBox_func, 0, 0, 1, 1)

        self.frame_2 = QFrame(self.page_2)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.pushButton_reload_companie = QPushButton(self.frame_2)
        self.pushButton_reload_companie.setObjectName(u"pushButton_reload_companie")
        sizePolicy4.setHeightForWidth(self.pushButton_reload_companie.sizePolicy().hasHeightForWidth())
        self.pushButton_reload_companie.setSizePolicy(sizePolicy4)
        icon8 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.SyncSynchronizing))
        self.pushButton_reload_companie.setIcon(icon8)

        self.verticalLayout_5.addWidget(self.pushButton_reload_companie)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer)


        self.gridLayout_5.addWidget(self.frame_2, 0, 3, 2, 1)

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
        font8 = QFont()
        font8.setFamilies([u"Tw Cen MT"])
        font8.setPointSize(36)
        font8.setBold(True)
        font8.setItalic(True)
        self.label_2.setFont(font8)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_2)

        self.stackedWidget_body.addWidget(self.page_5)

        self.gridLayout.addWidget(self.stackedWidget_body, 1, 0, 1, 2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 593, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.stackedWidget_body.setCurrentIndex(0)
        self.stackedWidget_companie.setCurrentIndex(0)
        self.stackedWidget_email.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Pend\u00eancias Cont\u00e1beis", None))

        __sortingEnabled = self.listWidget_companie.isSortingEnabled()
        self.listWidget_companie.setSortingEnabled(False)
        ___qlistwidgetitem = self.listWidget_companie.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", u"New Item", None));
        self.listWidget_companie.setSortingEnabled(__sortingEnabled)

        self.label_companie_intro.setText(QCoreApplication.translate("MainWindow", u"Empresas Dispon\u00edveis", None))
        self.label_companie_subintro.setText(QCoreApplication.translate("MainWindow", u"Clique 2x para selecionar", None))
        self.pushButton_exit_companie.setText("")
        self.label_current_companie.setText(QCoreApplication.translate("MainWindow", u"Nome Empresa", None))
        self.groupBox_email.setTitle(QCoreApplication.translate("MainWindow", u"Email", None))
        self.label_none_companie.setText(QCoreApplication.translate("MainWindow", u"Selecione uma \n"
"empresa", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Nome & Sobrenome:", None))
        self.pushButton_cancel_email.setText(QCoreApplication.translate("MainWindow", u"Voltar", None))
        self.pushButton_send_email.setText(QCoreApplication.translate("MainWindow", u"Enviar", None))
        self.groupBox_func.setTitle(QCoreApplication.translate("MainWindow", u"Fun\u00e7\u00f5es", None))
        self.pushButton_add_func.setText(QCoreApplication.translate("MainWindow", u"Adcionar", None))
        self.pushButton_remove_func.setText(QCoreApplication.translate("MainWindow", u" Remover", None))
        self.pushButton_edit_func.setText(QCoreApplication.translate("MainWindow", u"  Editar", None))
        self.pushButton_save_func.setText(QCoreApplication.translate("MainWindow", u"  Salvar   ", None))
        self.pushButton_sheet_func.setText(QCoreApplication.translate("MainWindow", u"Relat\u00f3rio", None))
        self.pushButton_reload_companie.setText("")
        self.label_load_gif.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Enviando Email...", None))
    # retranslateUi

