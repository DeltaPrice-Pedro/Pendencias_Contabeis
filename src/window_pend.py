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
    QHBoxLayout, QHeaderView, QLabel, QListWidget,
    QListWidgetItem, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStackedWidget, QStatusBar, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(520, 526)
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

        self.pushButton_edit_func = QPushButton(self.groupBox_func)
        self.pushButton_edit_func.setObjectName(u"pushButton_edit_func")
        self.pushButton_edit_func.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u"../../../../../Downloads/edit_icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_edit_func.setIcon(icon2)
        self.pushButton_edit_func.setIconSize(QSize(40, 40))
        self.pushButton_edit_func.setFlat(True)

        self.verticalLayout.addWidget(self.pushButton_edit_func)

        self.pushButton_save_func = QPushButton(self.groupBox_func)
        self.pushButton_save_func.setObjectName(u"pushButton_save_func")
        icon3 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.DocumentSave))
        self.pushButton_save_func.setIcon(icon3)
        self.pushButton_save_func.setIconSize(QSize(30, 30))
        self.pushButton_save_func.setFlat(True)

        self.verticalLayout.addWidget(self.pushButton_save_func)


        self.gridLayout.addWidget(self.groupBox_func, 0, 0, 2, 1)

        self.stackedWidget_2 = QStackedWidget(self.centralwidget)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.stackedWidget_2.sizePolicy().hasHeightForWidth())
        self.stackedWidget_2.setSizePolicy(sizePolicy1)
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
        QListWidgetItem(self.listWidget_companie)
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

        self.stackedWidget_2.addWidget(self.page_3)
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
        icon4 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.SystemLogOut))
        self.pushButton_exit_companie.setIcon(icon4)

        self.horizontalLayout.addWidget(self.pushButton_exit_companie)

        self.label_current_companie = QLabel(self.frame_current_companie)
        self.label_current_companie.setObjectName(u"label_current_companie")
        self.label_current_companie.setFont(font1)
        self.label_current_companie.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.label_current_companie)


        self.verticalLayout_3.addWidget(self.frame_current_companie)

        self.tableWidget_pedency = QTableWidget(self.page_4)
        if (self.tableWidget_pedency.columnCount() < 5):
            self.tableWidget_pedency.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_pedency.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_pedency.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget_pedency.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget_pedency.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget_pedency.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tableWidget_pedency.setObjectName(u"tableWidget_pedency")

        self.verticalLayout_3.addWidget(self.tableWidget_pedency)

        self.line = QFrame(self.page_4)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_3.addWidget(self.line)

        self.tableWidget_pedency_show = QTableWidget(self.page_4)
        if (self.tableWidget_pedency_show.columnCount() < 2):
            self.tableWidget_pedency_show.setColumnCount(2)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget_pedency_show.setHorizontalHeaderItem(0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget_pedency_show.setHorizontalHeaderItem(1, __qtablewidgetitem6)
        self.tableWidget_pedency_show.setObjectName(u"tableWidget_pedency_show")
        self.tableWidget_pedency_show.setShowGrid(True)
        self.tableWidget_pedency_show.horizontalHeader().setVisible(True)
        self.tableWidget_pedency_show.horizontalHeader().setHighlightSections(True)
        self.tableWidget_pedency_show.verticalHeader().setVisible(True)
        self.tableWidget_pedency_show.verticalHeader().setHighlightSections(True)

        self.verticalLayout_3.addWidget(self.tableWidget_pedency_show)

        self.stackedWidget_2.addWidget(self.page_4)

        self.gridLayout.addWidget(self.stackedWidget_2, 0, 1, 3, 1)

        self.groupBox_email = QGroupBox(self.centralwidget)
        self.groupBox_email.setObjectName(u"groupBox_email")
        sizePolicy.setHeightForWidth(self.groupBox_email.sizePolicy().hasHeightForWidth())
        self.groupBox_email.setSizePolicy(sizePolicy)
        font4 = QFont()
        font4.setFamilies([u"Tw Cen MT"])
        font4.setPointSize(16)
        font4.setBold(False)
        self.groupBox_email.setFont(font4)
        self.gridLayout_2 = QGridLayout(self.groupBox_email)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.stackedWidget = QStackedWidget(self.groupBox_email)
        self.stackedWidget.setObjectName(u"stackedWidget")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy4)
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
        font5 = QFont()
        font5.setFamilies([u"Sitka"])
        font5.setPointSize(18)
        font5.setBold(False)
        font5.setItalic(True)
        self.label_none_companie.setFont(font5)
        self.label_none_companie.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_3.addWidget(self.label_none_companie, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_2 = QVBoxLayout(self.page_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.listWidget_email = QListWidget(self.page_2)
        self.listWidget_email.setObjectName(u"listWidget_email")
        sizePolicy4.setHeightForWidth(self.listWidget_email.sizePolicy().hasHeightForWidth())
        self.listWidget_email.setSizePolicy(sizePolicy4)
        self.listWidget_email.setMaximumSize(QSize(200, 16777215))

        self.verticalLayout_2.addWidget(self.listWidget_email)

        self.frame_email_func = QFrame(self.page_2)
        self.frame_email_func.setObjectName(u"frame_email_func")
        self.frame_email_func.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_email_func.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_email_func)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pushButton_add_email = QPushButton(self.frame_email_func)
        self.pushButton_add_email.setObjectName(u"pushButton_add_email")
        icon5 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.ListAdd))
        self.pushButton_add_email.setIcon(icon5)

        self.horizontalLayout_3.addWidget(self.pushButton_add_email)

        self.pushButton_remove_email = QPushButton(self.frame_email_func)
        self.pushButton_remove_email.setObjectName(u"pushButton_remove_email")
        icon6 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.ListRemove))
        self.pushButton_remove_email.setIcon(icon6)

        self.horizontalLayout_3.addWidget(self.pushButton_remove_email)

        self.pushButton_email_edit = QPushButton(self.frame_email_func)
        self.pushButton_email_edit.setObjectName(u"pushButton_email_edit")
        icon7 = QIcon(QIcon.fromTheme(u"mail-message-new"))
        self.pushButton_email_edit.setIcon(icon7)

        self.horizontalLayout_3.addWidget(self.pushButton_email_edit)


        self.verticalLayout_2.addWidget(self.frame_email_func)

        self.pushButton_send_email = QPushButton(self.page_2)
        self.pushButton_send_email.setObjectName(u"pushButton_send_email")

        self.verticalLayout_2.addWidget(self.pushButton_send_email)

        self.stackedWidget.addWidget(self.page_2)

        self.gridLayout_2.addWidget(self.stackedWidget, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.groupBox_email, 2, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 520, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.stackedWidget_2.setCurrentIndex(0)
        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Pend\u00eancias Cont\u00e1beis", None))
        self.groupBox_func.setTitle(QCoreApplication.translate("MainWindow", u"Fun\u00e7\u00f5es", None))
        self.pushButton_add_func.setText(QCoreApplication.translate("MainWindow", u"Adcionar", None))
        self.pushButton_remove_func.setText(QCoreApplication.translate("MainWindow", u"Remover", None))
        self.pushButton_edit_func.setText(QCoreApplication.translate("MainWindow", u"Editar    ", None))
        self.pushButton_save_func.setText(QCoreApplication.translate("MainWindow", u"Salvar   ", None))
        self.label_companie_intro.setText(QCoreApplication.translate("MainWindow", u"Empresas Dispon\u00edveis", None))
        self.label_companie_subintro.setText(QCoreApplication.translate("MainWindow", u"Clique 2x para selecionar", None))

        __sortingEnabled = self.listWidget_companie.isSortingEnabled()
        self.listWidget_companie.setSortingEnabled(False)
        ___qlistwidgetitem = self.listWidget_companie.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", u"Empresa", None));
        self.listWidget_companie.setSortingEnabled(__sortingEnabled)

        self.pushButton_exit_companie.setText("")
        self.label_current_companie.setText(QCoreApplication.translate("MainWindow", u"Nome Empresa", None))
        ___qtablewidgetitem = self.tableWidget_pedency.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Tipo", None));
        ___qtablewidgetitem1 = self.tableWidget_pedency.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Valor", None));
        ___qtablewidgetitem2 = self.tableWidget_pedency.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Vencimento", None));
        ___qtablewidgetitem3 = self.tableWidget_pedency.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtablewidgetitem4 = self.tableWidget_pedency.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Observa\u00e7\u00f5es", None));
        ___qtablewidgetitem5 = self.tableWidget_pedency_show.horizontalHeaderItem(0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Tributo", None));
        ___qtablewidgetitem6 = self.tableWidget_pedency_show.horizontalHeaderItem(1)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Valor", None));
        self.groupBox_email.setTitle(QCoreApplication.translate("MainWindow", u"Email", None))
        self.label_none_companie.setText(QCoreApplication.translate("MainWindow", u"Selecione uma \n"
"empresa", None))
        self.pushButton_add_email.setText("")
        self.pushButton_remove_email.setText("")
        self.pushButton_email_edit.setText("")
        self.pushButton_send_email.setText(QCoreApplication.translate("MainWindow", u"Enviar", None))
    # retranslateUi

