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
    QHBoxLayout, QLabel, QListWidget, QListWidgetItem,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStackedWidget, QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(531, 472)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox_func = QGroupBox(self.centralwidget)
        self.groupBox_func.setObjectName(u"groupBox_func")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_func.sizePolicy().hasHeightForWidth())
        self.groupBox_func.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"Tw Cen MT"])
        font.setPointSize(16)
        self.groupBox_func.setFont(font)
        self.verticalLayout = QVBoxLayout(self.groupBox_func)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pushButton_add_func = QPushButton(self.groupBox_func)
        self.pushButton_add_func.setObjectName(u"pushButton_add_func")
        self.pushButton_add_func.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u"../../../../../Downloads/add_icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_add_func.setIcon(icon)
        self.pushButton_add_func.setIconSize(QSize(40, 40))
        self.pushButton_add_func.setFlat(True)

        self.verticalLayout.addWidget(self.pushButton_add_func)

        self.pushButton_remove_func = QPushButton(self.groupBox_func)
        self.pushButton_remove_func.setObjectName(u"pushButton_remove_func")
        self.pushButton_remove_func.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u"../../../../../Downloads/remove_icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_remove_func.setIcon(icon1)
        self.pushButton_remove_func.setIconSize(QSize(35, 35))
        self.pushButton_remove_func.setFlat(True)

        self.verticalLayout.addWidget(self.pushButton_remove_func)

        self.pushButton_save_func = QPushButton(self.groupBox_func)
        self.pushButton_save_func.setObjectName(u"pushButton_save_func")
        icon2 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.DocumentSave))
        self.pushButton_save_func.setIcon(icon2)
        self.pushButton_save_func.setIconSize(QSize(30, 30))
        self.pushButton_save_func.setFlat(True)

        self.verticalLayout.addWidget(self.pushButton_save_func)


        self.gridLayout.addWidget(self.groupBox_func, 0, 0, 2, 1)

        self.stackedWidget_companie = QStackedWidget(self.centralwidget)
        self.stackedWidget_companie.setObjectName(u"stackedWidget_companie")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.stackedWidget_companie.sizePolicy().hasHeightForWidth())
        self.stackedWidget_companie.setSizePolicy(sizePolicy1)
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
        sizePolicy.setHeightForWidth(self.label_companie_subintro.sizePolicy().hasHeightForWidth())
        self.label_companie_subintro.setSizePolicy(sizePolicy)
        font2 = QFont()
        font2.setFamilies([u"Tw Cen MT"])
        font2.setPointSize(12)
        font2.setBold(False)
        self.label_companie_subintro.setFont(font2)
        self.label_companie_subintro.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_companie_subintro)


        self.gridLayout_4.addWidget(self.frame_title_companie, 0, 0, 1, 1)

        self.listWidget_companie = QListWidget(self.page_3)
        self.listWidget_companie.setObjectName(u"listWidget_companie")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.listWidget_companie.sizePolicy().hasHeightForWidth())
        self.listWidget_companie.setSizePolicy(sizePolicy2)
        font3 = QFont()
        font3.setPointSize(14)
        self.listWidget_companie.setFont(font3)

        self.gridLayout_4.addWidget(self.listWidget_companie, 2, 0, 1, 1)

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
        icon3 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.SystemLogOut))
        self.pushButton_exit_companie.setIcon(icon3)

        self.horizontalLayout.addWidget(self.pushButton_exit_companie)

        self.line_2 = QFrame(self.frame_current_companie)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.VLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout.addWidget(self.line_2)

        self.pushButton_3 = QPushButton(self.frame_current_companie)
        self.pushButton_3.setObjectName(u"pushButton_3")
        sizePolicy3.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy3)
        icon4 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.SyncSynchronizing))
        self.pushButton_3.setIcon(icon4)

        self.horizontalLayout.addWidget(self.pushButton_3)

        self.label_current_companie = QLabel(self.frame_current_companie)
        self.label_current_companie.setObjectName(u"label_current_companie")
        self.label_current_companie.setFont(font1)
        self.label_current_companie.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.label_current_companie)


        self.verticalLayout_3.addWidget(self.frame_current_companie)

        self.stackedWidget_companie.addWidget(self.page_4)

        self.gridLayout.addWidget(self.stackedWidget_companie, 0, 1, 3, 1)

        self.groupBox_email = QGroupBox(self.centralwidget)
        self.groupBox_email.setObjectName(u"groupBox_email")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.groupBox_email.sizePolicy().hasHeightForWidth())
        self.groupBox_email.setSizePolicy(sizePolicy4)
        font4 = QFont()
        font4.setFamilies([u"Tw Cen MT"])
        font4.setPointSize(16)
        font4.setBold(False)
        self.groupBox_email.setFont(font4)
        self.gridLayout_2 = QGridLayout(self.groupBox_email)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.stackedWidget_email = QStackedWidget(self.groupBox_email)
        self.stackedWidget_email.setObjectName(u"stackedWidget_email")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Expanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.stackedWidget_email.sizePolicy().hasHeightForWidth())
        self.stackedWidget_email.setSizePolicy(sizePolicy5)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setStyleSheet(u"background-color: rgb(222, 222, 222);\n"
"")
        self.gridLayout_3 = QGridLayout(self.page)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_none_companie = QLabel(self.page)
        self.label_none_companie.setObjectName(u"label_none_companie")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.label_none_companie.sizePolicy().hasHeightForWidth())
        self.label_none_companie.setSizePolicy(sizePolicy6)
        font5 = QFont()
        font5.setFamilies([u"Sitka"])
        font5.setPointSize(18)
        font5.setBold(False)
        font5.setItalic(True)
        self.label_none_companie.setFont(font5)
        self.label_none_companie.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_3.addWidget(self.label_none_companie, 0, 0, 1, 1)

        self.stackedWidget_email.addWidget(self.page)

        self.gridLayout_2.addWidget(self.stackedWidget_email, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.groupBox_email, 2, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 531, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.stackedWidget_companie.setCurrentIndex(0)
        self.stackedWidget_email.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Pend\u00eancias Cont\u00e1beis", None))
        self.groupBox_func.setTitle(QCoreApplication.translate("MainWindow", u"Fun\u00e7\u00f5es", None))
        self.pushButton_add_func.setText(QCoreApplication.translate("MainWindow", u"Adcionar", None))
        self.pushButton_remove_func.setText(QCoreApplication.translate("MainWindow", u"Remover", None))
        self.pushButton_save_func.setText(QCoreApplication.translate("MainWindow", u"Salvar   ", None))
        self.label_companie_intro.setText(QCoreApplication.translate("MainWindow", u"Empresas Dispon\u00edveis", None))
        self.label_companie_subintro.setText(QCoreApplication.translate("MainWindow", u"Clique 2x para selecionar", None))
        self.pushButton_exit_companie.setText("")
        self.pushButton_3.setText("")
        self.label_current_companie.setText(QCoreApplication.translate("MainWindow", u"Nome Empresa", None))
        self.groupBox_email.setTitle(QCoreApplication.translate("MainWindow", u"Email", None))
        self.label_none_companie.setText(QCoreApplication.translate("MainWindow", u"Selecione uma \n"
"empresa", None))
    # retranslateUi

