# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QCheckBox,
    QComboBox, QDateTimeEdit, QFormLayout, QGridLayout,
    QGroupBox, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QScrollArea,
    QSizePolicy, QStatusBar, QTabWidget, QTableWidget,
    QTableWidgetItem, QToolBox, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1102, 853)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.CurBar = QWidget(self.centralwidget)
        self.CurBar.setObjectName(u"CurBar")
        self.gridLayout_6 = QGridLayout(self.CurBar)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.outputOrd = QLabel(self.CurBar)
        self.outputOrd.setObjectName(u"outputOrd")
        font = QFont()
        font.setPointSize(18)
        self.outputOrd.setFont(font)
        self.outputOrd.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_6.addWidget(self.outputOrd, 8, 5, 1, 1)

        self.label_21 = QLabel(self.CurBar)
        self.label_21.setObjectName(u"label_21")
        font1 = QFont()
        font1.setPointSize(11)
        self.label_21.setFont(font1)

        self.gridLayout_6.addWidget(self.label_21, 10, 0, 1, 1)

        self.tabVisOrd = QTabWidget(self.CurBar)
        self.tabVisOrd.setObjectName(u"tabVisOrd")
        self.tabVisOrd.setFocusPolicy(Qt.TabFocus)
        self.tabVisOrd.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.tabVisOrd.setAcceptDrops(False)
        self.tabVisOrd.setLayoutDirection(Qt.LeftToRight)
        self.tabVisOrd.setInputMethodHints(Qt.ImhNone)
        self.tabVisitors = QWidget()
        self.tabVisitors.setObjectName(u"tabVisitors")
        self.gridLayout_4 = QGridLayout(self.tabVisitors)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.toolBox = QToolBox(self.tabVisitors)
        self.toolBox.setObjectName(u"toolBox")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setGeometry(QRect(0, 0, 696, 290))
        self.gridLayout_8 = QGridLayout(self.page)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.groupBox_4 = QGroupBox(self.page)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.gridLayout_7 = QGridLayout(self.groupBox_4)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.inputSec = QLineEdit(self.groupBox_4)
        self.inputSec.setObjectName(u"inputSec")

        self.gridLayout_7.addWidget(self.inputSec, 0, 2, 1, 1)

        self.label_9 = QLabel(self.groupBox_4)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_7.addWidget(self.label_9, 6, 0, 1, 1)

        self.inputPat = QLineEdit(self.groupBox_4)
        self.inputPat.setObjectName(u"inputPat")

        self.gridLayout_7.addWidget(self.inputPat, 2, 2, 1, 1)

        self.comboDis = QComboBox(self.groupBox_4)
        self.comboDis.setObjectName(u"comboDis")
        self.comboDis.setEnabled(False)
        self.comboDis.setMaxVisibleItems(100000)

        self.gridLayout_7.addWidget(self.comboDis, 6, 2, 1, 1)

        self.label_6 = QLabel(self.groupBox_4)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_7.addWidget(self.label_6, 3, 0, 1, 1)

        self.label_5 = QLabel(self.groupBox_4)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_7.addWidget(self.label_5, 0, 0, 1, 1)

        self.label_7 = QLabel(self.groupBox_4)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_7.addWidget(self.label_7, 1, 0, 1, 1)

        self.inputPh = QLineEdit(self.groupBox_4)
        self.inputPh.setObjectName(u"inputPh")

        self.gridLayout_7.addWidget(self.inputPh, 3, 2, 1, 1)

        self.label_8 = QLabel(self.groupBox_4)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_7.addWidget(self.label_8, 2, 0, 1, 1)

        self.inputFir = QLineEdit(self.groupBox_4)
        self.inputFir.setObjectName(u"inputFir")

        self.gridLayout_7.addWidget(self.inputFir, 1, 2, 1, 1)

        self.ErrorTextVis = QLabel(self.groupBox_4)
        self.ErrorTextVis.setObjectName(u"ErrorTextVis")

        self.gridLayout_7.addWidget(self.ErrorTextVis, 7, 0, 1, 3)


        self.gridLayout_8.addWidget(self.groupBox_4, 0, 2, 1, 1)

        self.groupBox_5 = QGroupBox(self.page)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.gridLayout_9 = QGridLayout(self.groupBox_5)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.pushButtonDelVis = QPushButton(self.groupBox_5)
        self.pushButtonDelVis.setObjectName(u"pushButtonDelVis")
        self.pushButtonDelVis.setEnabled(False)

        self.gridLayout_9.addWidget(self.pushButtonDelVis, 2, 1, 1, 1)

        self.pushButtonEditVis = QPushButton(self.groupBox_5)
        self.pushButtonEditVis.setObjectName(u"pushButtonEditVis")
        self.pushButtonEditVis.setEnabled(False)

        self.gridLayout_9.addWidget(self.pushButtonEditVis, 2, 0, 1, 1)

        self.pushButtonAddVis = QPushButton(self.groupBox_5)
        self.pushButtonAddVis.setObjectName(u"pushButtonAddVis")

        self.gridLayout_9.addWidget(self.pushButtonAddVis, 1, 0, 1, 2)


        self.gridLayout_8.addWidget(self.groupBox_5, 1, 2, 1, 1)

        self.tableVisitors = QTableWidget(self.page)
        if (self.tableVisitors.columnCount() < 4):
            self.tableVisitors.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableVisitors.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableVisitors.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableVisitors.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableVisitors.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tableVisitors.setObjectName(u"tableVisitors")
        self.tableVisitors.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableVisitors.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.tableVisitors.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.gridLayout_8.addWidget(self.tableVisitors, 0, 0, 2, 1)

        self.toolBox.addItem(self.page, u"\u0412\u0441\u0435 \u043f\u043e\u0441\u0435\u0442\u0438\u0442\u0435\u043b\u0438, \u0437\u0430\u0440\u0435\u0433\u0438\u0441\u0442\u0440\u0438\u0440\u043e\u0432\u0430\u043d\u043d\u044b\u0435 \u0432 \u0441\u0438\u0441\u0442\u0435\u043c\u0435")
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setGeometry(QRect(0, 0, 1025, 182))
        self.gridLayout_11 = QGridLayout(self.page_2)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.tableVTB = QTableWidget(self.page_2)
        if (self.tableVTB.columnCount() < 3):
            self.tableVTB.setColumnCount(3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableVTB.setHorizontalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableVTB.setHorizontalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableVTB.setHorizontalHeaderItem(2, __qtablewidgetitem6)
        self.tableVTB.setObjectName(u"tableVTB")
        self.tableVTB.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableVTB.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.gridLayout_11.addWidget(self.tableVTB, 0, 0, 1, 1)

        self.groupBox_6 = QGroupBox(self.page_2)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.gridLayout_10 = QGridLayout(self.groupBox_6)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.label_10 = QLabel(self.groupBox_6)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_10.addWidget(self.label_10, 0, 0, 1, 1)

        self.dateTimeVisit = QDateTimeEdit(self.groupBox_6)
        self.dateTimeVisit.setObjectName(u"dateTimeVisit")

        self.gridLayout_10.addWidget(self.dateTimeVisit, 2, 1, 1, 1)

        self.pushButtonAddVTB = QPushButton(self.groupBox_6)
        self.pushButtonAddVTB.setObjectName(u"pushButtonAddVTB")

        self.gridLayout_10.addWidget(self.pushButtonAddVTB, 4, 0, 1, 2)

        self.comboVisitors = QComboBox(self.groupBox_6)
        self.comboVisitors.setObjectName(u"comboVisitors")

        self.gridLayout_10.addWidget(self.comboVisitors, 0, 1, 1, 1)

        self.label_11 = QLabel(self.groupBox_6)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_10.addWidget(self.label_11, 2, 0, 1, 1)

        self.checkEvent = QCheckBox(self.groupBox_6)
        self.checkEvent.setObjectName(u"checkEvent")

        self.gridLayout_10.addWidget(self.checkEvent, 1, 1, 1, 1)

        self.ErrorTextVTB = QLabel(self.groupBox_6)
        self.ErrorTextVTB.setObjectName(u"ErrorTextVTB")

        self.gridLayout_10.addWidget(self.ErrorTextVTB, 3, 0, 1, 2)


        self.gridLayout_11.addWidget(self.groupBox_6, 0, 1, 1, 1)

        self.toolBox.addItem(self.page_2, u"\u041f\u043e\u0441\u0435\u0449\u0435\u043d\u0438\u0435")

        self.gridLayout_4.addWidget(self.toolBox, 0, 1, 1, 1)

        self.MessegeOrdNot = QLabel(self.tabVisitors)
        self.MessegeOrdNot.setObjectName(u"MessegeOrdNot")

        self.gridLayout_4.addWidget(self.MessegeOrdNot, 1, 1, 1, 1)

        self.tabVisOrd.addTab(self.tabVisitors, "")
        self.tabOrders = QWidget()
        self.tabOrders.setObjectName(u"tabOrders")
        self.gridLayout_12 = QGridLayout(self.tabOrders)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.scrollArea = QScrollArea(self.tabOrders)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 87, 147))
        self.gridLayout_14 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.toolBoxOrder = QToolBox(self.scrollAreaWidgetContents)
        self.toolBoxOrder.setObjectName(u"toolBoxOrder")
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.page_3.setGeometry(QRect(0, 0, 69, 69))
        self.toolBoxOrder.addItem(self.page_3, u"Page 1")
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.page_4.setGeometry(QRect(0, 0, 100, 30))
        self.toolBoxOrder.addItem(self.page_4, u"Page 2")

        self.gridLayout_14.addWidget(self.toolBoxOrder, 0, 1, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_12.addWidget(self.scrollArea, 0, 0, 1, 1)

        self.groupBox_7 = QGroupBox(self.tabOrders)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.gridLayout_13 = QGridLayout(self.groupBox_7)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.comboBoxVis = QComboBox(self.groupBox_7)
        self.comboBoxVis.setObjectName(u"comboBoxVis")

        self.gridLayout_13.addWidget(self.comboBoxVis, 0, 1, 1, 3)

        self.comboBoxStf = QComboBox(self.groupBox_7)
        self.comboBoxStf.setObjectName(u"comboBoxStf")

        self.gridLayout_13.addWidget(self.comboBoxStf, 1, 1, 1, 3)

        self.dateTimeOrd = QDateTimeEdit(self.groupBox_7)
        self.dateTimeOrd.setObjectName(u"dateTimeOrd")

        self.gridLayout_13.addWidget(self.dateTimeOrd, 2, 1, 1, 1)

        self.label_13 = QLabel(self.groupBox_7)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_13.addWidget(self.label_13, 0, 0, 1, 1)

        self.label_12 = QLabel(self.groupBox_7)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_13.addWidget(self.label_12, 1, 0, 1, 1)

        self.label_14 = QLabel(self.groupBox_7)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout_13.addWidget(self.label_14, 2, 0, 1, 1)

        self.containsOrd = QScrollArea(self.groupBox_7)
        self.containsOrd.setObjectName(u"containsOrd")
        self.containsOrd.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 273, 240))
        self.gridLayout_15 = QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.groupBoxFd = QGroupBox(self.scrollAreaWidgetContents_2)
        self.groupBoxFd.setObjectName(u"groupBoxFd")
        self.gridLayout_16 = QGridLayout(self.groupBoxFd)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.pushButtonAddF = QPushButton(self.groupBoxFd)
        self.pushButtonAddF.setObjectName(u"pushButtonAddF")

        self.gridLayout_16.addWidget(self.pushButtonAddF, 0, 0, 1, 1)

        self.label_15 = QLabel(self.groupBoxFd)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout_16.addWidget(self.label_15, 1, 0, 1, 1)

        self.label_16 = QLabel(self.groupBoxFd)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout_16.addWidget(self.label_16, 1, 1, 1, 1)

        self.groupBoxF = QGroupBox(self.groupBoxFd)
        self.groupBoxF.setObjectName(u"groupBoxF")
        self.gridLayout_19 = QGridLayout(self.groupBoxF)
        self.gridLayout_19.setObjectName(u"gridLayout_19")

        self.gridLayout_16.addWidget(self.groupBoxF, 2, 0, 1, 2)

        self.pushButtonRemF = QPushButton(self.groupBoxFd)
        self.pushButtonRemF.setObjectName(u"pushButtonRemF")

        self.gridLayout_16.addWidget(self.pushButtonRemF, 0, 1, 1, 1)


        self.gridLayout_15.addWidget(self.groupBoxFd, 1, 0, 1, 1)

        self.groupBoxDr = QGroupBox(self.scrollAreaWidgetContents_2)
        self.groupBoxDr.setObjectName(u"groupBoxDr")
        self.gridLayout_17 = QGridLayout(self.groupBoxDr)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.label_17 = QLabel(self.groupBoxDr)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout_17.addWidget(self.label_17, 3, 0, 1, 1)

        self.groupBoxD = QGroupBox(self.groupBoxDr)
        self.groupBoxD.setObjectName(u"groupBoxD")
        self.gridLayout_18 = QGridLayout(self.groupBoxD)
        self.gridLayout_18.setObjectName(u"gridLayout_18")

        self.gridLayout_17.addWidget(self.groupBoxD, 4, 0, 1, 2)

        self.label_18 = QLabel(self.groupBoxDr)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout_17.addWidget(self.label_18, 3, 1, 1, 1)

        self.pushButtonAddD = QPushButton(self.groupBoxDr)
        self.pushButtonAddD.setObjectName(u"pushButtonAddD")

        self.gridLayout_17.addWidget(self.pushButtonAddD, 1, 0, 1, 1)

        self.pushButtonRemD = QPushButton(self.groupBoxDr)
        self.pushButtonRemD.setObjectName(u"pushButtonRemD")

        self.gridLayout_17.addWidget(self.pushButtonRemD, 1, 1, 1, 1)


        self.gridLayout_15.addWidget(self.groupBoxDr, 0, 0, 1, 1)

        self.containsOrd.setWidget(self.scrollAreaWidgetContents_2)

        self.gridLayout_13.addWidget(self.containsOrd, 6, 0, 1, 2)


        self.gridLayout_12.addWidget(self.groupBox_7, 0, 1, 1, 1)

        self.tabVisOrd.addTab(self.tabOrders, "")

        self.gridLayout_6.addWidget(self.tabVisOrd, 11, 0, 1, 6)

        self.label_4 = QLabel(self.CurBar)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.gridLayout_6.addWidget(self.label_4, 8, 0, 1, 5)

        self.label_22 = QLabel(self.CurBar)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setFont(font1)

        self.gridLayout_6.addWidget(self.label_22, 10, 2, 1, 1)

        self.label_20 = QLabel(self.CurBar)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setFont(font)

        self.gridLayout_6.addWidget(self.label_20, 9, 0, 1, 6)

        self.outputVis = QLabel(self.CurBar)
        self.outputVis.setObjectName(u"outputVis")
        self.outputVis.setFont(font)
        self.outputVis.setLayoutDirection(Qt.LeftToRight)
        self.outputVis.setScaledContents(True)
        self.outputVis.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_6.addWidget(self.outputVis, 3, 5, 1, 1)

        self.label_3 = QLabel(self.CurBar)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.gridLayout_6.addWidget(self.label_3, 3, 0, 1, 5)

        self.outputAns = QLabel(self.CurBar)
        self.outputAns.setObjectName(u"outputAns")
        self.outputAns.setFont(font)
        self.outputAns.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_6.addWidget(self.outputAns, 10, 5, 1, 1)

        self.dateTimeEditSt = QDateTimeEdit(self.CurBar)
        self.dateTimeEditSt.setObjectName(u"dateTimeEditSt")

        self.gridLayout_6.addWidget(self.dateTimeEditSt, 10, 1, 1, 1)

        self.dateTimeEditFn = QDateTimeEdit(self.CurBar)
        self.dateTimeEditFn.setObjectName(u"dateTimeEditFn")

        self.gridLayout_6.addWidget(self.dateTimeEditFn, 10, 3, 1, 1)

        self.pushButtonBack = QPushButton(self.CurBar)
        self.pushButtonBack.setObjectName(u"pushButtonBack")

        self.gridLayout_6.addWidget(self.pushButtonBack, 1, 0, 1, 1)

        self.BarName = QLabel(self.CurBar)
        self.BarName.setObjectName(u"BarName")
        font2 = QFont()
        font2.setPointSize(20)
        font2.setBold(True)
        self.BarName.setFont(font2)

        self.gridLayout_6.addWidget(self.BarName, 1, 3, 1, 3)


        self.gridLayout.addWidget(self.CurBar, 2, 0, 1, 1)

        self.AllBars = QWidget(self.centralwidget)
        self.AllBars.setObjectName(u"AllBars")
        self.gridLayout_5 = QGridLayout(self.AllBars)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.groupBox_2 = QGroupBox(self.AllBars)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_3 = QGridLayout(self.groupBox_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.pushButtonAdd = QPushButton(self.groupBox_2)
        self.pushButtonAdd.setObjectName(u"pushButtonAdd")

        self.gridLayout_3.addWidget(self.pushButtonAdd, 1, 0, 1, 2)

        self.groupBox_3 = QGroupBox(self.groupBox_2)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.formLayout = QFormLayout(self.groupBox_3)
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(self.groupBox_3)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.label_2 = QLabel(self.groupBox_3)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.inputName = QLineEdit(self.groupBox_3)
        self.inputName.setObjectName(u"inputName")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.inputName)

        self.inputAddress = QLineEdit(self.groupBox_3)
        self.inputAddress.setObjectName(u"inputAddress")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.inputAddress)

        self.ErrorText = QLabel(self.groupBox_3)
        self.ErrorText.setObjectName(u"ErrorText")
        self.ErrorText.setScaledContents(False)
        self.ErrorText.setMargin(15)

        self.formLayout.setWidget(2, QFormLayout.SpanningRole, self.ErrorText)


        self.gridLayout_3.addWidget(self.groupBox_3, 0, 0, 1, 2)

        self.pushButtonDel = QPushButton(self.groupBox_2)
        self.pushButtonDel.setObjectName(u"pushButtonDel")
        self.pushButtonDel.setEnabled(False)

        self.gridLayout_3.addWidget(self.pushButtonDel, 3, 0, 1, 2)

        self.pushButtonEdit = QPushButton(self.groupBox_2)
        self.pushButtonEdit.setObjectName(u"pushButtonEdit")
        self.pushButtonEdit.setEnabled(False)

        self.gridLayout_3.addWidget(self.pushButtonEdit, 2, 0, 1, 2)


        self.gridLayout_5.addWidget(self.groupBox_2, 0, 1, 1, 1)

        self.groupBox = QGroupBox(self.AllBars)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_2 = QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.tableBars = QTableWidget(self.groupBox)
        if (self.tableBars.columnCount() < 2):
            self.tableBars.setColumnCount(2)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableBars.setHorizontalHeaderItem(0, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableBars.setHorizontalHeaderItem(1, __qtablewidgetitem8)
        self.tableBars.setObjectName(u"tableBars")
        self.tableBars.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.tableBars.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableBars.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableBars.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.tableBars.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableBars.setTextElideMode(Qt.ElideRight)
        self.tableBars.setSortingEnabled(False)
        self.tableBars.horizontalHeader().setVisible(True)
        self.tableBars.horizontalHeader().setHighlightSections(True)

        self.gridLayout_2.addWidget(self.tableBars, 1, 0, 1, 1)


        self.gridLayout_5.addWidget(self.groupBox, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.AllBars, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1102, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabVisOrd.setCurrentIndex(0)
        self.toolBox.setCurrentIndex(1)
        self.toolBoxOrder.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.outputOrd.setText("")
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"\u043e\u0442:", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043b\u0435 \u0432\u0432\u043e\u0434\u0430", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u0442\u043d\u0451\u0440\u0441\u043a\u0430\u044f \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0430:", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u043c\u0435\u0440 \u0442\u0435\u043b\u0435\u0444\u043e\u043d\u0430:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0430\u043c\u0438\u043b\u0438\u044f:", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043c\u044f:", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u0447\u0435\u0441\u0442\u0432\u043e:", None))
        self.ErrorTextVis.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ff0000;\">\u041d\u0435\u043e\u0431\u0445\u043e\u0434\u0438\u043c\u043e, \u0447\u0442\u043e\u0431\u044b \u0431\u044b\u043b\u0438 \u0432\u0432\u0435\u0434\u0435\u043d\u044b \u0432\u0441\u0435 \u043f\u043e\u043b\u044f \u0432\u0432\u043e\u0434\u0430, \u0430 \u043d\u043e\u043c\u0435\u0440 \u0442\u0435\u043b\u0435\u0444\u043e\u043d\u0430 \u0431\u044b\u043b \u0437\u0430\u043f\u0438\u0441\u0430\u043d \u0432 \u0432\u0438\u0434\u0435 - (88005553535)</span></p></body></html>", None))
        self.groupBox_5.setTitle("")
        self.pushButtonDelVis.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.pushButtonEditVis.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.pushButtonAddVis.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        ___qtablewidgetitem = self.tableVisitors.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0418\u041e", None));
        ___qtablewidgetitem1 = self.tableVisitors.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u043c\u0435\u0440 \u0442\u0435\u043b\u0435\u0444\u043e\u043d\u0430", None));
        ___qtablewidgetitem2 = self.tableVisitors.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u0442\u043d\u0451\u0440\u0441\u043a\u0430\u044f \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0430", None));
        ___qtablewidgetitem3 = self.tableVisitors.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043a\u0438\u0434\u043a\u0430", None));
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), QCoreApplication.translate("MainWindow", u"\u0412\u0441\u0435 \u043f\u043e\u0441\u0435\u0442\u0438\u0442\u0435\u043b\u0438, \u0437\u0430\u0440\u0435\u0433\u0438\u0441\u0442\u0440\u0438\u0440\u043e\u0432\u0430\u043d\u043d\u044b\u0435 \u0432 \u0441\u0438\u0441\u0442\u0435\u043c\u0435", None))
        ___qtablewidgetitem4 = self.tableVTB.horizontalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0418\u041e", None));
        ___qtablewidgetitem5 = self.tableVTB.horizontalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u0430 \u043f\u043e\u0441\u0435\u0449\u0435\u043d\u0438\u044f", None));
        ___qtablewidgetitem6 = self.tableVTB.horizontalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0438\u0448\u0435\u043b \u043d\u0430 \u0441\u043e\u0431\u044b\u0442\u0438\u0435", None));
        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0441\u0435\u0442\u0438\u0442\u0435\u043b\u044c", None))
        self.pushButtonAddVTB.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c \u043f\u043e\u0441\u0435\u0449\u0435\u043d\u0438\u0435", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0440\u0435\u043c\u044f \u043f\u043e\u0441\u0435\u0449\u0435\u043d\u0438\u044f", None))
        self.checkEvent.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0438\u0448\u0451\u043b \u043d\u0430 \u0441\u043e\u0431\u044b\u0442\u0438\u0435", None))
        self.ErrorTextVTB.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ff0000;\">\u0412 \u0443\u043a\u0430\u0437\u0430\u043d\u043d\u043e\u0435 \u0432\u0440\u0435\u043c\u044f \u043d\u0435\u0442 \u0441\u043e\u0431\u044b\u0442\u0438\u0439.</span></p></body></html>", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0441\u0435\u0449\u0435\u043d\u0438\u0435", None))
        self.MessegeOrdNot.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043a\u0430\u0437\u043e\u0432 \u043d\u0435\u0442", None))
        self.tabVisOrd.setTabText(self.tabVisOrd.indexOf(self.tabVisitors), QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0441\u0435\u0442\u0438\u0442\u0435\u043b\u0438", None))
        self.toolBoxOrder.setItemText(self.toolBoxOrder.indexOf(self.page_3), QCoreApplication.translate("MainWindow", u"Page 1", None))
        self.toolBoxOrder.setItemText(self.toolBoxOrder.indexOf(self.page_4), QCoreApplication.translate("MainWindow", u"Page 2", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0441\u0435\u0442\u0438\u0442\u0435\u043b\u044c", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0431\u043e\u0442\u043d\u0438\u043a", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u0430 \u0437\u0430\u043a\u0430\u0437\u0430", None))
        self.groupBoxFd.setTitle(QCoreApplication.translate("MainWindow", u"\u0415\u0434\u0430", None))
        self.pushButtonAddF.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0435\u0434\u0443", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e", None))
        self.groupBoxF.setTitle("")
        self.pushButtonRemF.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0431\u0440\u0430\u0442\u044c \u0435\u0434\u0443", None))
        self.groupBoxDr.setTitle(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u043f\u0438\u0442\u043a\u0438", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435", None))
        self.groupBoxD.setTitle("")
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e", None))
        self.pushButtonAddD.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u043d\u0430\u043f\u0438\u0442\u043e\u043a \u043a \u0437\u0430\u043a\u0430\u0437\u0443", None))
        self.pushButtonRemD.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0431\u0440\u0430\u0442\u044c \u0435\u0434\u0443", None))
        self.tabVisOrd.setTabText(self.tabVisOrd.indexOf(self.tabOrders), QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043a\u0430\u0437\u044b", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043b-\u0432\u043e \u0437\u0430\u043a\u0430\u0437\u043e\u0432 \u0437\u0430 \u0432\u0441\u0451 \u0432\u0440\u0435\u043c\u044f:", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"\u0434\u043e:", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0434\u0441\u0447\u0435\u0442 \u043f\u0440\u0438\u0431\u044b\u043b\u0438 \u0437\u0430 \u043e\u043f\u0440\u0435\u0434\u0435\u043b\u0435\u043d\u043d\u044b\u0439 \u043f\u0440\u043e\u043c\u0435\u0436\u0443\u0442\u043e\u043a \u0432\u0440\u0435\u043c\u0435\u043d\u0438", None))
        self.outputVis.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043b-\u0432\u043e \u043f\u043e\u0441\u0435\u0442\u0438\u0442\u0435\u043b\u0435\u0439 \u0437\u0430 \u0432\u0441\u0451 \u0432\u0440\u0435\u043c\u044f:", None))
        self.outputAns.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.pushButtonBack.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0430\u0434", None))
        self.BarName.setText("")
        self.groupBox_2.setTitle("")
        self.pushButtonAdd.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043b\u0435 \u0432\u0432\u043e\u0434\u0430:", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0410\u0434\u0440\u0435\u0441\u0441:", None))
        self.ErrorText.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ff0101;\">\u041d\u0435\u043e\u0431\u0445\u043e\u0434\u0438\u043c\u043e, \u0447\u0442\u043e\u0431\u044b \u0432\u0441\u0435 \u043f\u043e\u043b\u044f \u0431\u044b\u043b\u0438 \u0437\u0430\u043f\u043e\u043b\u043d\u0435\u043d\u044b</span></p></body></html>", None))
        self.pushButtonDel.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.pushButtonEdit.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.groupBox.setTitle("")
        ___qtablewidgetitem7 = self.tableBars.horizontalHeaderItem(0)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0431\u0430\u0440\u0430", None));
        ___qtablewidgetitem8 = self.tableBars.horizontalHeaderItem(1)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"\u0410\u0434\u0440\u0435\u0441\u0441", None));
    # retranslateUi

