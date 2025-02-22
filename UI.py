# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'nonLinier.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QTabWidget, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.NonModal)
        MainWindow.setEnabled(True)
        MainWindow.resize(1082, 776)
        MainWindow.setMinimumSize(QSize(670, 450))
        MainWindow.setMaximumSize(QSize(1082, 776))
        MainWindow.setBaseSize(QSize(1082, 784))
        font = QFont()
        font.setFamilies([u"Vazirmatn"])
        font.setPointSize(10)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"QWidget{\n"
"background-color: #023e7d;\n"
"}\n"
"QLabel{\n"
"color: white;\n"
"}\n"
"QLineEdit{\n"
"background-color: white;\n"
"color: black;\n"
"}\n"
"QTableWidget{\n"
"background-color: white;\n"
"color: black;\n"
"gridline-color: black;\n"
"font: 13px;\n"
"}\n"
"QHeaderView::section{\n"
"background-color:#3e5c76;\n"
"color: white;\n"
"font: 13px;\n"
"font-weight: medium;\n"
"}\n"
"QScrollBar:vertical{\n"
"background: #8d99ae;\n"
"}\n"
"QScrollBar:horizontal{\n"
"background: #8d99ae;\n"
"}")
        MainWindow.setTabShape(QTabWidget.Triangular)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pilihMetode = QWidget(self.centralwidget)
        self.pilihMetode.setObjectName(u"pilihMetode")
        sizePolicy.setHeightForWidth(self.pilihMetode.sizePolicy().hasHeightForWidth())
        self.pilihMetode.setSizePolicy(sizePolicy)
        self.pilihMetode.setStyleSheet(u"")
        self.verticalLayout_2 = QVBoxLayout(self.pilihMetode)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.widget_2 = QWidget(self.pilihMetode)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.widget_2.setStyleSheet(u"QWidget{\n"
"background-color: #03045e;\n"
"border-radius: 10px;\n"
"padding:5;\n"
"}\n"
"QPushButton{\n"
"background-color: #3c6e71;\n"
"color: #edf6f9;\n"
"font: 14px;\n"
"font-weight: bold;\n"
"font-family: Varzitsmant;\n"
"width: 140px;\n"
"height: 30px;\n"
"}\n"
"QLineEdit{\n"
"background-color: white;\n"
"color: black;\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: #83c5be;\n"
"}")
        self.verticalLayout_5 = QVBoxLayout(self.widget_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_9 = QLabel(self.widget_2)
        self.label_9.setObjectName(u"label_9")
        font1 = QFont()
        font1.setBold(True)
        font1.setItalic(True)
        self.label_9.setFont(font1)
        self.label_9.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_9, 0, Qt.AlignTop)

        self.ketikFungsi = QLineEdit(self.widget_2)
        self.ketikFungsi.setObjectName(u"ketikFungsi")
        font2 = QFont()
        font2.setBold(True)
        self.ketikFungsi.setFont(font2)

        self.verticalLayout_5.addWidget(self.ketikFungsi)

        self.verticalSpacer_4 = QSpacerItem(20, 2, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_4)

        self.simpanFungsi = QPushButton(self.widget_2)
        self.simpanFungsi.setObjectName(u"simpanFungsi")
        font3 = QFont()
        font3.setFamilies([u"Varzitsmant"])
        font3.setBold(True)
        font3.setItalic(False)
        self.simpanFungsi.setFont(font3)

        self.verticalLayout_5.addWidget(self.simpanFungsi)


        self.verticalLayout_2.addWidget(self.widget_2)

        self.verticalSpacer_5 = QSpacerItem(20, 15, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_5)

        self.widget = QWidget(self.pilihMetode)
        self.widget.setObjectName(u"widget")
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setFont(font2)
        self.widget.setStyleSheet(u"QWidget{\n"
"border-radius: 7px;\n"
"background-color: #03045e;\n"
"margin: 1;\n"
"}\n"
"QPushButton{\n"
"background-color: #3c6e71;\n"
"color: #edf6f9;\n"
"font: 14px;\n"
"font-family: Varzitsmant;\n"
"font-weight: bold;\n"
"width: 140px;\n"
"height: 40;\n"
"margin: 5;\n"
"}\n"
"QLineEdit{\n"
"background-color: white;\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: #83c5be;\n"
"}")
        self.verticalLayout_4 = QVBoxLayout(self.widget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.tombolBiseksi = QPushButton(self.widget)
        self.tombolBiseksi.setObjectName(u"tombolBiseksi")
        sizePolicy.setHeightForWidth(self.tombolBiseksi.sizePolicy().hasHeightForWidth())
        self.tombolBiseksi.setSizePolicy(sizePolicy)
        self.tombolBiseksi.setFont(font3)
        self.tombolBiseksi.setCheckable(False)

        self.verticalLayout_4.addWidget(self.tombolBiseksi)

        self.verticalSpacer = QSpacerItem(20, 15, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.tombolRegulaFalsi = QPushButton(self.widget)
        self.tombolRegulaFalsi.setObjectName(u"tombolRegulaFalsi")
        sizePolicy.setHeightForWidth(self.tombolRegulaFalsi.sizePolicy().hasHeightForWidth())
        self.tombolRegulaFalsi.setSizePolicy(sizePolicy)
        self.tombolRegulaFalsi.setFont(font3)
        self.tombolRegulaFalsi.setCheckable(False)

        self.verticalLayout_4.addWidget(self.tombolRegulaFalsi)

        self.verticalSpacer_2 = QSpacerItem(20, 15, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.tombolNewtonRaphson = QPushButton(self.widget)
        self.tombolNewtonRaphson.setObjectName(u"tombolNewtonRaphson")
        sizePolicy.setHeightForWidth(self.tombolNewtonRaphson.sizePolicy().hasHeightForWidth())
        self.tombolNewtonRaphson.setSizePolicy(sizePolicy)
        self.tombolNewtonRaphson.setFont(font3)
        self.tombolNewtonRaphson.setCheckable(False)

        self.verticalLayout_4.addWidget(self.tombolNewtonRaphson)

        self.verticalSpacer_3 = QSpacerItem(20, 15, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_3)

        self.tombolSecant = QPushButton(self.widget)
        self.tombolSecant.setObjectName(u"tombolSecant")
        sizePolicy.setHeightForWidth(self.tombolSecant.sizePolicy().hasHeightForWidth())
        self.tombolSecant.setSizePolicy(sizePolicy)
        self.tombolSecant.setFont(font3)
        self.tombolSecant.setCheckable(False)

        self.verticalLayout_4.addWidget(self.tombolSecant)


        self.verticalLayout_2.addWidget(self.widget, 0, Qt.AlignHCenter|Qt.AlignBottom)


        self.horizontalLayout.addWidget(self.pilihMetode, 0, Qt.AlignTop)

        self.tempatMetode = QWidget(self.centralwidget)
        self.tempatMetode.setObjectName(u"tempatMetode")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(90)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.tempatMetode.sizePolicy().hasHeightForWidth())
        self.tempatMetode.setSizePolicy(sizePolicy1)
        self.tempatMetode.setStyleSheet(u"QPushButton{\n"
"background-color: #800e13;\n"
"color: white;\n"
"font-family: Varzitsmant;\n"
"}")
        self.verticalLayout_6 = QVBoxLayout(self.tempatMetode)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.stackedWidget = QStackedWidget(self.tempatMetode)
        self.stackedWidget.setObjectName(u"stackedWidget")
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.halamanBiseksi = QWidget()
        self.halamanBiseksi.setObjectName(u"halamanBiseksi")
        sizePolicy.setHeightForWidth(self.halamanBiseksi.sizePolicy().hasHeightForWidth())
        self.halamanBiseksi.setSizePolicy(sizePolicy)
        self.verticalLayout_7 = QVBoxLayout(self.halamanBiseksi)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.widget_3 = QWidget(self.halamanBiseksi)
        self.widget_3.setObjectName(u"widget_3")
        self.verticalLayout = QVBoxLayout(self.widget_3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(self.widget_3)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font4 = QFont()
        font4.setFamilies([u"Vazirmatn"])
        font4.setPointSize(30)
        self.label_2.setFont(font4)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_2, 0, Qt.AlignTop)

        self.widget_7 = QWidget(self.widget_3)
        self.widget_7.setObjectName(u"widget_7")
        self.widget_7.setFont(font)
        self.gridLayout = QGridLayout(self.widget_7)
        self.gridLayout.setObjectName(u"gridLayout")
        self.labelTolBiseksi = QLabel(self.widget_7)
        self.labelTolBiseksi.setObjectName(u"labelTolBiseksi")
        self.labelTolBiseksi.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.labelTolBiseksi, 0, 2, 1, 1)

        self.labelBBiseksi = QLabel(self.widget_7)
        self.labelBBiseksi.setObjectName(u"labelBBiseksi")
        self.labelBBiseksi.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.labelBBiseksi, 0, 1, 1, 1)

        self.toleransiBiseksi = QLineEdit(self.widget_7)
        self.toleransiBiseksi.setObjectName(u"toleransiBiseksi")

        self.gridLayout.addWidget(self.toleransiBiseksi, 1, 2, 1, 1)

        self.aBiseksi = QLineEdit(self.widget_7)
        self.aBiseksi.setObjectName(u"aBiseksi")

        self.gridLayout.addWidget(self.aBiseksi, 1, 0, 1, 1)

        self.labelABiseksi = QLabel(self.widget_7)
        self.labelABiseksi.setObjectName(u"labelABiseksi")
        self.labelABiseksi.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.labelABiseksi, 0, 0, 1, 1)

        self.bBiseksi = QLineEdit(self.widget_7)
        self.bBiseksi.setObjectName(u"bBiseksi")

        self.gridLayout.addWidget(self.bBiseksi, 1, 1, 1, 1)

        self.cariHasilBiseksi = QPushButton(self.widget_7)
        self.cariHasilBiseksi.setObjectName(u"cariHasilBiseksi")

        self.gridLayout.addWidget(self.cariHasilBiseksi, 1, 3, 1, 1)


        self.verticalLayout.addWidget(self.widget_7, 0, Qt.AlignHCenter)

        self.tabelBiseksi = QTableWidget(self.widget_3)
        if (self.tabelBiseksi.columnCount() < 8):
            self.tabelBiseksi.setColumnCount(8)
        __qtablewidgetitem = QTableWidgetItem()
        self.tabelBiseksi.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tabelBiseksi.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tabelBiseksi.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tabelBiseksi.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tabelBiseksi.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tabelBiseksi.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tabelBiseksi.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tabelBiseksi.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        if (self.tabelBiseksi.rowCount() < 20):
            self.tabelBiseksi.setRowCount(20)
        self.tabelBiseksi.setObjectName(u"tabelBiseksi")
        font5 = QFont()
        font5.setFamilies([u"Vazirmatn"])
        font5.setBold(False)
        font5.setItalic(False)
        self.tabelBiseksi.setFont(font5)
        self.tabelBiseksi.setFrameShape(QFrame.HLine)
        self.tabelBiseksi.setFrameShadow(QFrame.Sunken)
        self.tabelBiseksi.setShowGrid(True)
        self.tabelBiseksi.setGridStyle(Qt.DotLine)
        self.tabelBiseksi.setSortingEnabled(False)
        self.tabelBiseksi.setWordWrap(True)
        self.tabelBiseksi.setCornerButtonEnabled(True)
        self.tabelBiseksi.setRowCount(20)
        self.tabelBiseksi.horizontalHeader().setProperty(u"showSortIndicator", False)
        self.tabelBiseksi.verticalHeader().setVisible(False)

        self.verticalLayout.addWidget(self.tabelBiseksi)


        self.verticalLayout_7.addWidget(self.widget_3)

        self.stackedWidget.addWidget(self.halamanBiseksi)
        self.halamanNewtonRaphson = QWidget()
        self.halamanNewtonRaphson.setObjectName(u"halamanNewtonRaphson")
        sizePolicy.setHeightForWidth(self.halamanNewtonRaphson.sizePolicy().hasHeightForWidth())
        self.halamanNewtonRaphson.setSizePolicy(sizePolicy)
        self.verticalLayout_9 = QVBoxLayout(self.halamanNewtonRaphson)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.widget_4 = QWidget(self.halamanNewtonRaphson)
        self.widget_4.setObjectName(u"widget_4")
        self.verticalLayout_11 = QVBoxLayout(self.widget_4)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_3 = QLabel(self.widget_4)
        self.label_3.setObjectName(u"label_3")
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setFont(font4)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.label_3, 0, Qt.AlignTop)

        self.widget_8 = QWidget(self.widget_4)
        self.widget_8.setObjectName(u"widget_8")
        self.widget_8.setFont(font)
        self.gridLayout_2 = QGridLayout(self.widget_8)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.cariHasilNewtonRaphson = QPushButton(self.widget_8)
        self.cariHasilNewtonRaphson.setObjectName(u"cariHasilNewtonRaphson")

        self.gridLayout_2.addWidget(self.cariHasilNewtonRaphson, 1, 2, 1, 1)

        self.labelxNewRap = QLabel(self.widget_8)
        self.labelxNewRap.setObjectName(u"labelxNewRap")
        self.labelxNewRap.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.labelxNewRap, 0, 0, 1, 1)

        self.xNewtonRaphson = QLineEdit(self.widget_8)
        self.xNewtonRaphson.setObjectName(u"xNewtonRaphson")

        self.gridLayout_2.addWidget(self.xNewtonRaphson, 1, 0, 1, 1)

        self.toleransiNewtonRaphson = QLineEdit(self.widget_8)
        self.toleransiNewtonRaphson.setObjectName(u"toleransiNewtonRaphson")

        self.gridLayout_2.addWidget(self.toleransiNewtonRaphson, 1, 1, 1, 1)

        self.label_6 = QLabel(self.widget_8)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_2.addWidget(self.label_6, 0, 1, 1, 1, Qt.AlignHCenter)


        self.verticalLayout_11.addWidget(self.widget_8, 0, Qt.AlignHCenter)

        self.tabelNewtonRaphson = QTableWidget(self.widget_4)
        if (self.tabelNewtonRaphson.columnCount() < 5):
            self.tabelNewtonRaphson.setColumnCount(5)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tabelNewtonRaphson.setHorizontalHeaderItem(0, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tabelNewtonRaphson.setHorizontalHeaderItem(1, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tabelNewtonRaphson.setHorizontalHeaderItem(2, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tabelNewtonRaphson.setHorizontalHeaderItem(3, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tabelNewtonRaphson.setHorizontalHeaderItem(4, __qtablewidgetitem12)
        if (self.tabelNewtonRaphson.rowCount() < 20):
            self.tabelNewtonRaphson.setRowCount(20)
        self.tabelNewtonRaphson.setObjectName(u"tabelNewtonRaphson")
        self.tabelNewtonRaphson.setMinimumSize(QSize(518, 0))
        self.tabelNewtonRaphson.setFont(font5)
        self.tabelNewtonRaphson.setFrameShape(QFrame.HLine)
        self.tabelNewtonRaphson.setFrameShadow(QFrame.Sunken)
        self.tabelNewtonRaphson.setShowGrid(True)
        self.tabelNewtonRaphson.setGridStyle(Qt.DotLine)
        self.tabelNewtonRaphson.setSortingEnabled(False)
        self.tabelNewtonRaphson.setWordWrap(True)
        self.tabelNewtonRaphson.setCornerButtonEnabled(True)
        self.tabelNewtonRaphson.setRowCount(20)
        self.tabelNewtonRaphson.horizontalHeader().setProperty(u"showSortIndicator", False)
        self.tabelNewtonRaphson.verticalHeader().setVisible(False)

        self.verticalLayout_11.addWidget(self.tabelNewtonRaphson, 0, Qt.AlignHCenter)


        self.verticalLayout_9.addWidget(self.widget_4)

        self.stackedWidget.addWidget(self.halamanNewtonRaphson)
        self.halamanSecant = QWidget()
        self.halamanSecant.setObjectName(u"halamanSecant")
        sizePolicy.setHeightForWidth(self.halamanSecant.sizePolicy().hasHeightForWidth())
        self.halamanSecant.setSizePolicy(sizePolicy)
        self.halamanSecant.setMinimumSize(QSize(0, 0))
        self.verticalLayout_8 = QVBoxLayout(self.halamanSecant)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.widget_6 = QWidget(self.halamanSecant)
        self.widget_6.setObjectName(u"widget_6")
        self.verticalLayout_3 = QVBoxLayout(self.widget_6)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_5 = QLabel(self.widget_6)
        self.label_5.setObjectName(u"label_5")
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setFont(font4)
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_5, 0, Qt.AlignTop)

        self.widget_10 = QWidget(self.widget_6)
        self.widget_10.setObjectName(u"widget_10")
        self.widget_10.setFont(font)
        self.gridLayout_4 = QGridLayout(self.widget_10)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_8 = QLabel(self.widget_10)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_8, 0, 1, 1, 1)

        self.toleransiSecant = QLineEdit(self.widget_10)
        self.toleransiSecant.setObjectName(u"toleransiSecant")

        self.gridLayout_4.addWidget(self.toleransiSecant, 1, 2, 1, 1)

        self.label_13 = QLabel(self.widget_10)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_13, 0, 2, 1, 1)

        self.label_7 = QLabel(self.widget_10)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_7, 0, 0, 1, 1)

        self.x0Secant = QLineEdit(self.widget_10)
        self.x0Secant.setObjectName(u"x0Secant")

        self.gridLayout_4.addWidget(self.x0Secant, 1, 0, 1, 1)

        self.cariHasilSecant = QPushButton(self.widget_10)
        self.cariHasilSecant.setObjectName(u"cariHasilSecant")

        self.gridLayout_4.addWidget(self.cariHasilSecant, 1, 3, 1, 1)

        self.x1Secant = QLineEdit(self.widget_10)
        self.x1Secant.setObjectName(u"x1Secant")

        self.gridLayout_4.addWidget(self.x1Secant, 1, 1, 1, 1)


        self.verticalLayout_3.addWidget(self.widget_10, 0, Qt.AlignHCenter)

        self.tabelSecant = QTableWidget(self.widget_6)
        if (self.tabelSecant.columnCount() < 4):
            self.tabelSecant.setColumnCount(4)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tabelSecant.setHorizontalHeaderItem(0, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tabelSecant.setHorizontalHeaderItem(1, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tabelSecant.setHorizontalHeaderItem(2, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tabelSecant.setHorizontalHeaderItem(3, __qtablewidgetitem16)
        if (self.tabelSecant.rowCount() < 20):
            self.tabelSecant.setRowCount(20)
        self.tabelSecant.setObjectName(u"tabelSecant")
        self.tabelSecant.setEnabled(True)
        sizePolicy.setHeightForWidth(self.tabelSecant.sizePolicy().hasHeightForWidth())
        self.tabelSecant.setSizePolicy(sizePolicy)
        self.tabelSecant.setMinimumSize(QSize(418, 0))
        self.tabelSecant.setMaximumSize(QSize(16777215, 16777215))
        self.tabelSecant.setFont(font5)
        self.tabelSecant.setFrameShape(QFrame.HLine)
        self.tabelSecant.setGridStyle(Qt.DotLine)
        self.tabelSecant.setRowCount(20)
        self.tabelSecant.verticalHeader().setVisible(False)

        self.verticalLayout_3.addWidget(self.tabelSecant, 0, Qt.AlignHCenter)


        self.verticalLayout_8.addWidget(self.widget_6)

        self.stackedWidget.addWidget(self.halamanSecant)
        self.halamanRegulaFalsi = QWidget()
        self.halamanRegulaFalsi.setObjectName(u"halamanRegulaFalsi")
        sizePolicy.setHeightForWidth(self.halamanRegulaFalsi.sizePolicy().hasHeightForWidth())
        self.halamanRegulaFalsi.setSizePolicy(sizePolicy)
        self.verticalLayout_10 = QVBoxLayout(self.halamanRegulaFalsi)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.widget_5 = QWidget(self.halamanRegulaFalsi)
        self.widget_5.setObjectName(u"widget_5")
        self.verticalLayout_12 = QVBoxLayout(self.widget_5)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_4 = QLabel(self.widget_5)
        self.label_4.setObjectName(u"label_4")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy2)
        self.label_4.setFont(font4)

        self.verticalLayout_12.addWidget(self.label_4, 0, Qt.AlignHCenter)

        self.widget_9 = QWidget(self.widget_5)
        self.widget_9.setObjectName(u"widget_9")
        self.widget_9.setFont(font)
        self.gridLayout_3 = QGridLayout(self.widget_9)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.aRegulaFalsi = QLineEdit(self.widget_9)
        self.aRegulaFalsi.setObjectName(u"aRegulaFalsi")

        self.gridLayout_3.addWidget(self.aRegulaFalsi, 1, 0, 1, 1)

        self.toleransiRegulaFalsi = QLineEdit(self.widget_9)
        self.toleransiRegulaFalsi.setObjectName(u"toleransiRegulaFalsi")

        self.gridLayout_3.addWidget(self.toleransiRegulaFalsi, 1, 2, 1, 1)

        self.label_11 = QLabel(self.widget_9)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_11, 0, 1, 1, 1)

        self.label_12 = QLabel(self.widget_9)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_12, 0, 2, 1, 1)

        self.label_10 = QLabel(self.widget_9)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_10, 0, 0, 1, 1)

        self.bRegulaFalsi = QLineEdit(self.widget_9)
        self.bRegulaFalsi.setObjectName(u"bRegulaFalsi")

        self.gridLayout_3.addWidget(self.bRegulaFalsi, 1, 1, 1, 1)

        self.cariHasilRegulaFalsi = QPushButton(self.widget_9)
        self.cariHasilRegulaFalsi.setObjectName(u"cariHasilRegulaFalsi")

        self.gridLayout_3.addWidget(self.cariHasilRegulaFalsi, 1, 3, 1, 1)


        self.verticalLayout_12.addWidget(self.widget_9, 0, Qt.AlignHCenter)

        self.tabelRegulaFalsi = QTableWidget(self.widget_5)
        if (self.tabelRegulaFalsi.columnCount() < 8):
            self.tabelRegulaFalsi.setColumnCount(8)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tabelRegulaFalsi.setHorizontalHeaderItem(0, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tabelRegulaFalsi.setHorizontalHeaderItem(1, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tabelRegulaFalsi.setHorizontalHeaderItem(2, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tabelRegulaFalsi.setHorizontalHeaderItem(3, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tabelRegulaFalsi.setHorizontalHeaderItem(4, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tabelRegulaFalsi.setHorizontalHeaderItem(5, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tabelRegulaFalsi.setHorizontalHeaderItem(6, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.tabelRegulaFalsi.setHorizontalHeaderItem(7, __qtablewidgetitem24)
        if (self.tabelRegulaFalsi.rowCount() < 20):
            self.tabelRegulaFalsi.setRowCount(20)
        self.tabelRegulaFalsi.setObjectName(u"tabelRegulaFalsi")
        self.tabelRegulaFalsi.setFont(font5)
        self.tabelRegulaFalsi.setFrameShape(QFrame.HLine)
        self.tabelRegulaFalsi.setGridStyle(Qt.DotLine)
        self.tabelRegulaFalsi.setRowCount(20)
        self.tabelRegulaFalsi.verticalHeader().setVisible(False)

        self.verticalLayout_12.addWidget(self.tabelRegulaFalsi)


        self.verticalLayout_10.addWidget(self.widget_5)

        self.stackedWidget.addWidget(self.halamanRegulaFalsi)

        self.verticalLayout_6.addWidget(self.stackedWidget)


        self.horizontalLayout.addWidget(self.tempatMetode)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Perhitungan Non-Linear", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Fungsi [f(x)]", None))
#if QT_CONFIG(tooltip)
        self.ketikFungsi.setToolTip(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Cantarell'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-style:italic;\">Masukkan fungsi non-linier (harus dalam format Python)</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.simpanFungsi.setText(QCoreApplication.translate("MainWindow", u"Simpan", None))
        self.tombolBiseksi.setText(QCoreApplication.translate("MainWindow", u"Biseksi", None))
        self.tombolRegulaFalsi.setText(QCoreApplication.translate("MainWindow", u"Regula-Falsi", None))
        self.tombolNewtonRaphson.setText(QCoreApplication.translate("MainWindow", u"Newton-Raphson", None))
        self.tombolSecant.setText(QCoreApplication.translate("MainWindow", u"Secant", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Biseksi", None))
        self.labelTolBiseksi.setText(QCoreApplication.translate("MainWindow", u"Toleransi (e)", None))
        self.labelBBiseksi.setText(QCoreApplication.translate("MainWindow", u"b", None))
        self.labelABiseksi.setText(QCoreApplication.translate("MainWindow", u"a", None))
        self.cariHasilBiseksi.setText(QCoreApplication.translate("MainWindow", u"Cari Hasil", None))
        ___qtablewidgetitem = self.tabelBiseksi.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Iterasi", None));
        ___qtablewidgetitem1 = self.tabelBiseksi.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"a", None));
        ___qtablewidgetitem2 = self.tabelBiseksi.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"b", None));
        ___qtablewidgetitem3 = self.tabelBiseksi.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"x", None));
        ___qtablewidgetitem4 = self.tabelBiseksi.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"f(x)", None));
        ___qtablewidgetitem5 = self.tabelBiseksi.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"f(a)", None));
        ___qtablewidgetitem6 = self.tabelBiseksi.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"f(b)", None));
        ___qtablewidgetitem7 = self.tabelBiseksi.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Status |f(x)| < e", None));
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Newton-Raphson", None))
        self.cariHasilNewtonRaphson.setText(QCoreApplication.translate("MainWindow", u"Cari Hasil", None))
        self.labelxNewRap.setText(QCoreApplication.translate("MainWindow", u"x", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Toleransi (e)", None))
        ___qtablewidgetitem8 = self.tabelNewtonRaphson.horizontalHeaderItem(0)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Iterasi", None));
        ___qtablewidgetitem9 = self.tabelNewtonRaphson.horizontalHeaderItem(1)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"x", None));
        ___qtablewidgetitem10 = self.tabelNewtonRaphson.horizontalHeaderItem(2)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"f(x)", None));
        ___qtablewidgetitem11 = self.tabelNewtonRaphson.horizontalHeaderItem(3)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"f'(x)", None));
        ___qtablewidgetitem12 = self.tabelNewtonRaphson.horizontalHeaderItem(4)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Status |f(x)| < e", None));
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Secant", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"x1", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Toleransi (e)", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"x0", None))
        self.cariHasilSecant.setText(QCoreApplication.translate("MainWindow", u"Cari Hasil", None))
        ___qtablewidgetitem13 = self.tabelSecant.horizontalHeaderItem(0)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Iterasi", None));
        ___qtablewidgetitem14 = self.tabelSecant.horizontalHeaderItem(1)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"x", None));
        ___qtablewidgetitem15 = self.tabelSecant.horizontalHeaderItem(2)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"y/f(x)", None));
        ___qtablewidgetitem16 = self.tabelSecant.horizontalHeaderItem(3)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"Status |f(x)| < e", None));
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Regula-Falsi", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"b", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Toleransi (e)", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"a", None))
        self.cariHasilRegulaFalsi.setText(QCoreApplication.translate("MainWindow", u"Cari Hasil", None))
        ___qtablewidgetitem17 = self.tabelRegulaFalsi.horizontalHeaderItem(0)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"Iterasi", None));
        ___qtablewidgetitem18 = self.tabelRegulaFalsi.horizontalHeaderItem(1)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"a", None));
        ___qtablewidgetitem19 = self.tabelRegulaFalsi.horizontalHeaderItem(2)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"b", None));
        ___qtablewidgetitem20 = self.tabelRegulaFalsi.horizontalHeaderItem(3)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"x", None));
        ___qtablewidgetitem21 = self.tabelRegulaFalsi.horizontalHeaderItem(4)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"f(x)", None));
        ___qtablewidgetitem22 = self.tabelRegulaFalsi.horizontalHeaderItem(5)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"f(a)", None));
        ___qtablewidgetitem23 = self.tabelRegulaFalsi.horizontalHeaderItem(6)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"f(b)", None));
        ___qtablewidgetitem24 = self.tabelRegulaFalsi.horizontalHeaderItem(7)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"Status |f(x)| < e", None));
    # retranslateUi

