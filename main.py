import os
import sys
from datetime import datetime
from pprint import pprint

from PySide6 import QtCore
from PySide6.QtCore import QDate, QRegularExpression, QDateTime
from PySide6.QtGui import Qt, QPalette, QColor

from Database import DataBase

# os.system('''pyside6-rcc res.qrc -o res_rc.py
# pyside6-uic MainWindow.ui > ui_mainwindow.py'''.replace('\n', '&'))

from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QHeaderView, QWidget, QComboBox, QSpinBox, \
    QHBoxLayout, QLabel, QVBoxLayout, QGridLayout, QSpacerItem, QCheckBox, QStyleFactory

from ui_mainwindow import Ui_MainWindow
os.system('''pyside6-uic MainWindow.ui > ui_mainwindow.py''')




class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.mainLayout = None
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.tableBars.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.tableBars.verticalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.ui.tableVisitors.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.tableVisitors.verticalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.ui.tableVTB.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.tableVTB.verticalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.db = DataBase()
        self.ui.CurBar.hide()
        self.ui.ErrorText.hide()
        self.ui.tableBars.setHorizontalHeaderLabels(['Название бара', 'Адресс'])
        self.loadBars()
        self.curIdBar = None
        self.curSelRowTableBar = None
        self.curSelRowTableVis = None
        self.curIdUser = None
        self.countDr = 0
        self.qbD = []
        self.CntD = []
        self.ui.dateTimeVisit.setDateTime(QDateTime().currentDateTime())
        self.ui.dateTimeOrd.setDateTime(QDateTime().currentDateTime())
        self.ui.dateTimeEditFn.setDateTime(QDateTime().currentDateTime())
        self.ui.dateTimeEditSt.setDateTime(QDateTime().currentDateTime())
        self.ui.dateTimeEditSt.setMaximumDateTime(self.ui.dateTimeEditFn.dateTime())
        # Connections
        self.ui.tableBars.cellDoubleClicked.connect(self.toCurBar)
        ### Для таблицы с барами ###
        self.ui.tableBars.currentCellChanged.connect(self.currentRecBars)
        self.ui.pushButtonBack.clicked.connect(self.toAllBars)
        self.ui.pushButtonAdd.clicked.connect(self.addNewBar)
        self.ui.pushButtonEdit.clicked.connect(self.editBar)
        self.ui.pushButtonDel.clicked.connect(self.deleteBar)

        self.ui.inputName.textChanged.connect(self.inputsWasChanged)
        self.ui.inputAddress.textChanged.connect(self.inputsWasChanged)

        self.ui.dateTimeEditFn.dateTimeChanged.connect(self.getMoneyForPeriod)
        self.ui.dateTimeEditSt.dateTimeChanged.connect(self.getMoneyForPeriod)
        ### Для таблицы с Посетителями ###
        self.ui.tableVisitors.currentCellChanged.connect(self.currentRecVis)
        self.ui.pushButtonAddVis.clicked.connect(self.createVis)
        self.ui.pushButtonEditVis.clicked.connect(self.editVis)
        self.ui.pushButtonDelVis.clicked.connect(self.delVis)
        self.ui.tableVTB.currentCellChanged.connect(self.currentRecVTB)

        self.ui.pushButtonAddD.clicked.connect(self.addInputDr)

        self.ui.pushButtonAddVTB.clicked.connect(self.checkedEvent)
        self.ui.inputPh.textChanged.connect(self.inputsWasChangedVis)
        self.ui.inputFir.textChanged.connect(self.inputsWasChangedVis)
        self.ui.inputSec.textChanged.connect(self.inputsWasChangedVis)
        self.ui.inputPat.textChanged.connect(self.inputsWasChangedVis)
        self.ui.comboDis.currentIndexChanged.connect(self.inputsWasChangedVis)

        # self.ui.tabVisOrd.currentChanged.connect()

        self.show()

    ############################ QWIDGET = ALLBARS START ##############################################
    # Загружает данные в таблицу
    def loadBars(self):
        datas = self.db.getBars()
        self.ui.tableBars.clear()
        self.ui.tableBars.setRowCount(0)
        for data in datas:
            row = self.ui.tableBars.rowCount()
            self.ui.tableBars.insertRow(row)
            # print(data['id'])
            self.ui.tableBars.setItem(row, 0, QTableWidgetItem(f'{data["name"]}'))
            self.ui.tableBars.item(row, 0).setData(Qt.UserRole, data['id'])
            self.ui.tableBars.setItem(row, 1, QTableWidgetItem(f'{data["address"]}'))
        self.ui.tableBars.setHorizontalHeaderLabels(['Название бара', 'Адресс'])

    # Заполняет форму текущей выбранной записью
    def currentRecBars(self, row: int):
        if row >= 0:
            self.curSelRowTableBar = row
            #print(row)
            self.curIdBar = int(self.ui.tableBars.item(row, 0).data(Qt.UserRole))
            #print(self.curIdBar)
            name = self.ui.tableBars.item(row, 0).text()
            address = self.ui.tableBars.item(row, 1).text()

            self.ui.inputName.setText(name)
            self.ui.inputAddress.setText(address)


    # Переходит ко всем барам
    def toAllBars(self):
        self.ui.AllBars.setEnabled(True)
        self.ui.inputName.setText('')
        self.ui.inputAddress.setText('')
        self.updateConditionBars()
        self.curIdBar = None
        self.curSelRowTableBar = None
        self.loadBars()
        self.ui.AllBars.show()
        self.ui.CurBar.hide()

    # Делает доступными кнопки удаление и изменения в зависимости от изменения в инпуте
    def inputsWasChanged(self):
        self.updateConditionBars(cond=True)

    # Делает доступными кнопки удаления и изменения
    def updateConditionBars(self, cond=False):
        count = self.ui.tableBars.rowCount()
        self.ui.pushButtonEdit.setEnabled(cond)
        self.ui.pushButtonDel.setEnabled(cond)

    # Добавляет новую запись в таблицу
    def addNewBar(self):
        INPUTS_OK = self.checkInputsBars()
        if INPUTS_OK:
            data = [self.ui.inputName.text(), self.ui.inputAddress.text()]
            self.curIdBar = self.db.createBar(data=data)
            self.loadBars()

            self.curSelRowTableBar = self.findRecordsRowBars(self.curIdBar, data[0])
            self.ui.tableBars.selectRow(self.curSelRowTableBar)

    #  Изменяет запись в таблице
    def editBar(self):
        if self.checkInputsBars():
            data = [self.ui.inputName.text(), self.ui.inputAddress.text(), self.curIdBar]
            self.db.editBar(data)
            self.loadBars()

            self.curSelRowTableBar = self.findRecordsRowBars(self.curIdBar, data[0])
            self.ui.tableBars.selectRow(self.curSelRowTableBar)

    # Удаление записи из таблицы
    def deleteBar(self):
        self.db.deleteBar(self.curIdBar)
        self.loadBars()
        self.ui.tableBars.selectRow(min(self.curSelRowTableBar, self.ui.tableBars.rowCount() - 1))
        self.curSelRowTableBar = self.ui.tableBars.currentRow()
        self.curIdBar = int(self.ui.tableBars.item(self.curSelRowTableBar, 0).data(Qt.UserRole))

    # Ищет запись по id бара в таблице
    def findRecordsRowBars(self, idBar: int, name: str):
        matches = self.ui.tableBars.findItems(name, QtCore.Qt.MatchExactly)
        for match in matches:
            if match.data(Qt.UserRole) == idBar:
                return match.row()

    # Проверяет
    def checkInputsBars(self):
        LEN_NAME = len(str(self.ui.inputName.text()))
        LEN_ADDRESS = len(self.ui.inputAddress.text())
        if LEN_NAME  == 0 or LEN_ADDRESS == 0:
            self.ui.ErrorText.show()
            return 0
        self.ui.ErrorText.hide()
        return 1
    ############################ QWIDGET = ALLBARS FINISH ##############################################

    ############################ QWIDGET = CURBAR START ##############################################
        # Переходит к определенному бару
    def toCurBar(self):
        self.ui.tableBars.clear()
        self.ui.tableBars.setRowCount(0)
        self.ui.AllBars.setDisabled(True)
        self.ui.AllBars.hide()
        self.ui.CurBar.show()
        self.ui.ErrorTextVis.hide()
        self.ui.ErrorTextVTB.hide()
        self.curBarName()
        self.countAllVisBar()
        self.countAllOrdBar()
        self.loadVisitors()
        self.loadDisc()
        self.updateConditionVis()
        self.loadVTB()
        self.loadComboVTB()
        self.loadAllOrders()
        self.ui.groupBox_7.hide()
        self.ui.MessegeOrdNot.hide()
        self.getMoneyForPeriod()

    def curBarName(self):
        data = self.db.getCurBar(self.curIdBar)
        self.ui.BarName.setText(f'Бар "{data["name"]}"')

    def countAllVisBar(self):
        countVis = self.db.getCountAllVisBar(self.curIdBar)
        self.ui.outputVis.setText(str(countVis['cnt']))

    def countAllOrdBar(self):
        countOrd = self.db.getCountAllOrdBar(self.curIdBar)
        self.ui.outputOrd.setText(str(countOrd['cnt']))

    def getMoneyForPeriod(self):
        self.ui.dateTimeEditSt.setMaximumDateTime(self.ui.dateTimeEditFn.dateTime())
        dates = [self.ui.dateTimeEditSt.dateTime().toString('yyyy-MM-dd hh:mm:ss'), self.ui.dateTimeEditFn.dateTime().toString('yyyy-MM-dd hh:mm:ss')]
        data = self.db.getMonForPeriodBar(self.curIdBar, dates)['money']
        print(data)
        self.ui.outputAns.setText(('0' if data is None else str(data)) + ' рублей')

    ####################################### TABLE = VISITORS Start #############################################################
    def loadVisitors(self):
        datas = self.db.getAllVisitors()
        self.ui.tableVisitors.clear()
        self.ui.tableVisitors.setRowCount(0)
        for data in datas:
            row = self.ui.tableVisitors.rowCount()
            self.ui.tableVisitors.insertRow(row)
            # print(data['id'])
            self.ui.tableVisitors.setItem(row, 0, QTableWidgetItem(f'{data["fio"]}'))
            self.ui.tableVisitors.item(row, 0).setData(Qt.UserRole, data['idUser'])
            self.ui.tableVisitors.setItem(row, 1, QTableWidgetItem(f'{data["phone"]}'))
            self.ui.tableVisitors.setItem(row, 2, QTableWidgetItem(f'{data["nameOfDiscount"]}'))
            self.ui.tableVisitors.item(row, 2).setData(Qt.UserRole, data["idAffilateProgramm"])
            self.ui.tableVisitors.setItem(row, 3, QTableWidgetItem(f'{data["disc"]}'))
        self.ui.tableVisitors.setHorizontalHeaderLabels(['ФИО', 'Номер телефона', "Партнёрская программа", "Скидка"])
        self.loadComboVTB()

    def currentRecVis(self, row: int):
        if row >= 0:
            # self.updateConditionVis(True)
            self.curSelRowTableVis = row
            self.curIdUser = int(self.ui.tableVisitors.item(row, 0).data(Qt.UserRole))
            idDisc = self.ui.tableVisitors.item(row, 2).data(Qt.UserRole)
            # print(self.curIdUser)
            fio = self.ui.tableVisitors.item(row, 0).text().split(' ')
            phone = self.ui.tableVisitors.item(row, 1).text()
            nameOfDiscount = self.ui.tableVisitors.item(row, 2).text()
            self.ui.tableVisitors.item(row, 2).text()
            discount = self.ui.tableVisitors.item(row, 3).text()
            self.ui.inputFir.setText(fio[1])
            self.ui.inputSec.setText(fio[0])
            self.ui.inputPat.setText(fio[2])
            self.ui.inputPh.setText(phone)
            for i in range(self.ui.comboDis.count()):
                if self.ui.comboDis.itemData(i) == idDisc:
                    self.ui.comboDis.setCurrentIndex(i)
                    break

    def createVis(self):
        INPUTS_OK = self.checkInputsVis()
        if INPUTS_OK:
            dataUs = [self.ui.inputPh.text()]
            dataVis = [self.ui.inputSec.text(), self.ui.inputFir.text(),  self.ui.inputPat.text(), self.ui.comboDis.itemData(self.ui.comboDis.currentIndex())]
            self.curIdUser = self.db.createVis(dataUs=dataUs, dataVis=dataVis)
            self.loadVisitors()
            self.curSelRowTableVis = self.findRecordsRowVis(self.curIdUser, dataUs[0])
            self.ui.tableVisitors.selectRow(self.curSelRowTableVis)

    def editVis(self):
        if self.checkInputsVis():
            dataUs = [self.ui.inputPh.text()]
            dataVis = [self.ui.inputSec.text(), self.ui.inputFir.text(), self.ui.inputPat.text(),self.ui.comboDis.itemData(self.ui.comboDis.currentIndex())]
            self.db.editVis(self.curIdUser, dataUs, dataVis)
            self.loadVisitors()

            self.curSelRowTableBar = self.findRecordsRowVis(self.curIdBar, dataUs[0])
            self.ui.tableVisitors.selectRow(self.curSelRowTableVis)

    def delVis(self):
        self.db.delVis(self.curIdUser)
        self.loadVisitors()
        self.ui.tableVisitors.selectRow(min(self.curSelRowTableVis, self.ui.tableVisitors.rowCount() - 1))
        self.curSelRowTableVis = self.ui.tableVisitors.currentRow()
        self.curIdUser = int(self.ui.tableVisitors.item(self.curSelRowTableVis, 0).data(Qt.UserRole))

    # Делает доступными кнопки удаление и изменения в зависимости от изменения в инпуте
    def inputsWasChangedVis(self):
        self.updateConditionVis(cond=True)

    # Делает доступными кнопки удаления и изменения
    def updateConditionVis(self, cond=False):
        self.ui.comboDis.setEnabled(cond)
        self.ui.pushButtonDelVis.setEnabled(cond)
        self.ui.pushButtonEditVis.setEnabled(cond)


    def loadDisc(self):
        data = self.db.getAllDiscount()
        for el in data:
            self.ui.comboDis.addItem(el['disc'], el['id'])
            self.ui.comboDis.itemData(self.ui.comboDis.count()-1, role=Qt.UserRole)
        self.ui.comboDis.addItem('Нет партнерской программы - 0%', None)
        self.ui.comboDis.itemData(self.ui.comboDis.count() - 1, role=Qt.UserRole)
        self.ui.comboDis.setCurrentIndex(self.ui.comboDis.count()-1)

    def checkInputsVis(self):
        LEN_FIRSTNAME = len(str(self.ui.inputFir.text()))
        LEN_SECONDNAME = len(self.ui.inputSec.text())
        LEN_PHONENUMBER = len(self.ui.inputPh.text())
        IS_NUM = QRegularExpression('^[0-9]*').match(self.ui.inputPh.text())
        # print(IS_NUM)
        if LEN_FIRSTNAME == 0 or LEN_SECONDNAME == 0 or LEN_PHONENUMBER == 0 or LEN_PHONENUMBER < 11 or LEN_PHONENUMBER > 11:
            self.ui.ErrorTextVis.show()
            return 0
        self.ui.ErrorTextVis.hide()
        return 1

    def findRecordsRowVis(self, idVis: int, phone: str):
        matches = self.ui.tableVisitors.findItems(phone, QtCore.Qt.MatchExactly)
        for match in matches:
            if self.ui.tableVisitors.item(match.row(), 0).data(Qt.UserRole) == idVis:
                return match.row()
    ####################################### TABLE = VISITORS FINISH #############################################################
    def loadVTB(self):
        datas = self.db.allVisitorsOfBar(self.curIdBar)
        self.ui.tableVTB.clear()
        self.ui.tableVTB.setRowCount(0)
        for data in datas:
            row = self.ui.tableVTB.rowCount()
            self.ui.tableVTB.insertRow(row)
            # print(data['id'])
            self.ui.tableVTB.setItem(row, 0, QTableWidgetItem(f'{data["fio"]}'))
            self.ui.tableVTB.item(row, 0).setData(Qt.UserRole, data['id'])
            self.ui.tableVTB.setItem(row, 1, QTableWidgetItem(f'{data["timeOfVisit"]}'))
            self.ui.tableVTB.item(row, 1).setData(Qt.UserRole, data['idVisitor'])
            self.ui.tableVTB.setItem(row, 2, QTableWidgetItem(f'{data["event"]}'))
        self.ui.tableVTB.setHorizontalHeaderLabels(['ФИО', 'Время визита', "Посещение события"])

    # Заполняет комбобокс посетителями
    def loadComboVTB(self):
        data = self.db.getAllVisToCombo()
        for el in data:
            self.ui.comboVisitors.addItem(el['fio'], el['idUser'])
            self.ui.comboVisitors.itemData(self.ui.comboVisitors.count() - 1, role=Qt.UserRole)

        self.ui.comboBoxVis.setCurrentIndex(0)

    # Проверяет поле ввода
    def checkedEvent(self):
        dateVisit = self.ui.dateTimeVisit.dateTime().toString('yyyy-MM-dd hh:mm')
        if self.ui.checkEvent.isChecked():
            IS_EVENT = self.db.getEventFromDataVis(self.curIdBar, dateVisit)
        else: IS_EVENT = True
        if IS_EVENT:
            self.ui.ErrorTextVTB.hide()
            idVTB = self.addVisitVTB()
            self.loadVTB()
            matches = self.ui.tableVTB.findItems(dateVisit, Qt.MatchContains)

            for match in matches:
                print(self.ui.tableVTB.item(match.row(), 0).data(Qt.UserRole))
                if self.ui.tableVTB.item(match.row(), 0).data(Qt.UserRole) == idVTB:
                    self.ui.tableVTB.selectRow(match.row())
                    break
        else:
            self.ui.ErrorTextVTB.show()
    # Переход на определённого пользователя из посещений
    def addVisitVTB(self):
        data = []
        data.append(self.ui.dateTimeVisit.dateTime().toString('yyyy-MM-dd hh:mm'))
        data.append(self.ui.checkEvent.isChecked())
        idUser = self.ui.comboVisitors.currentData(Qt.UserRole)
        return self.db.createVTB(self.curIdBar,idUser, data)

    def currentRecVTB(self, row: int):
        if row >= 0:
            # self.updateConditionVis(True)
            self.curSelRowTableVTB = row
            self.curIdVTB = int(self.ui.tableVTB.item(row, 0).data(Qt.UserRole))
            idVis = self.ui.tableVTB.item(row, 1).data(Qt.UserRole)
            timeOfVisit = QDateTime().fromString(self.ui.tableVTB.item(row, 1).text(), 'yyyy-MM-dd HH:mm:ss')
            event = int(self.ui.tableVTB.item(row, 2).text())
            self.ui.comboVisitors.setCurrentIndex(self.findRecordsRowVTB(idVis))
            self.ui.dateTimeVisit.setDateTime(timeOfVisit)
            self.ui.checkEvent.setChecked(event)

    def findRecordsRowVTB(self, idVis: int):
        match = self.ui.comboVisitors.findData(idVis, role=Qt.UserRole)
        return match

    def loadAllOrders(self):
        data = self.db.getAllOrders(self.curIdBar)
        for i in range(self.ui.toolBoxOrder.count() - 1):
            if self.ui.toolBoxOrder.count() == 2:
                break
            self.ui.toolBoxOrder.removeItem((self.ui.toolBoxOrder.count() - 1 - i))
        # print(len(data))
        if(len(data) > 0):
            self.ui.toolBoxOrder.show()
            for i in range(len(data)):
                if i == 0:
                    dataDr = self.db.getAllDrinksOrd(data[0]['id'])
                    dataFd = self.db.getAllFoodsOrd(data[0]['id'])
                    self.ui.toolBoxOrder.widget(i).setObjectName(f'Order_{i}')
                    self.ui.toolBoxOrder.setItemText(i, f'Заказ № {i+1}')
                    mainLayoot = QGridLayout()
                    mainLayoot.setObjectName(f'mainInfoOrder_{i}')
                    self.ui.toolBoxOrder.widget(i).setLayout(mainLayoot)
                    mainLayoot.addWidget(QLabel('Название напитка:'))
                    for drink in dataDr:
                        bufText = QLabel(f'{drink["nameDrink"]}: {drink["cost"]} X {drink["count"]} ({drink["volume"]})')
                        mainLayoot.addWidget(bufText)
                    mainLayoot.addWidget(QLabel('Название еды:'))
                    for food in dataFd:
                        bufText = QLabel(f'{food["nameFood"]}: {food["cost"]} X {food["count"]} ({food["volume"]})')
                        mainLayoot.addWidget(bufText)
                    textAut = QLabel(f'Оформил заказ: {data[i]["fioStf"]}')
                    mainLayoot.addWidget(textAut, 0, 2)
                    cost = str(self.db.getCostForOrd(data[0]['id'])['cost'])
                    print(self.db.getDiscountVis(data[0]['idUser']))
                    disc = 0 if self.db.getDiscountVis(data[0]['idUser']) is None else self.db.getDiscountVis(data[0]['idUser'])['discount']
                    textCostOrd = QLabel(f'Стоимость заказа с учётом скидки в {disc}% : {cost} рублей')
                    mainLayoot.addWidget(textCostOrd, 2, 2)
                    mainLayoot.addItem(QSpacerItem(20, 200))

                    continue
                if i == 1:
                    dataDr = self.db.getAllDrinksOrd(data[1]['id'])
                    dataFd = self.db.getAllFoodsOrd(data[1]['id'])
                    self.ui.toolBoxOrder.widget(i).setObjectName(f'Order_{i}')
                    self.ui.toolBoxOrder.setItemText(i, f'Заказ № {i + 1}')
                    mainLayoot = QGridLayout()
                    mainLayoot.setObjectName(f'mainInfoOrder_{i}')
                    self.ui.toolBoxOrder.widget(i).setLayout(mainLayoot)
                    mainLayoot.addWidget(QLabel('Название напитка:'))
                    for drink in dataDr:
                        bufText = QLabel(
                            f'{drink["nameDrink"]}: {drink["cost"]} X {drink["count"]} ({drink["volume"]})')
                        mainLayoot.addWidget(bufText)
                    mainLayoot.addWidget(QLabel('Название еды:'))
                    for food in dataFd:
                        bufText = QLabel(f'{food["nameFood"]}: {food["cost"]} X {food["count"]} ({food["volume"]})')
                        mainLayoot.addWidget(bufText)
                    textAut = QLabel(f'Оформил заказ: {data[i]["fioStf"]}')
                    mainLayoot.addWidget(textAut, 0, 2)
                    cost = str(self.db.getCostForOrd(data[1]['id'])['cost'])
                    disc = 0 if self.db.getDiscountVis(data[1]['idUser']) is None else self.db.getDiscountVis(
                        data[1]['idUser'])['discount']
                    textCostOrd = QLabel(f'Стоимость заказа с учётом скидки в {disc}% : {cost} рублей')
                    mainLayoot.addWidget(textCostOrd, 2, 2)
                    mainLayoot.addItem(QSpacerItem(20, 200))
                    continue

                self.ui.toolBoxOrder.addItem(QWidget(), f'Заказ № {i+1}')
                dataDr = self.db.getAllDrinksOrd(data[i]['id'])
                dataFd = self.db.getAllFoodsOrd(data[i]['id'])
                self.ui.toolBoxOrder.widget(i).setObjectName(f'Order_{i}')
                self.ui.toolBoxOrder.setItemText(i, f'Заказ № {i + 1}')
                mainLayoot = QGridLayout()
                mainLayoot.setObjectName(f'mainInfoOrder_{i}')
                self.ui.toolBoxOrder.widget(i).setLayout(mainLayoot)
                mainLayoot.addWidget(QLabel('Название напитка:'))
                for drink in dataDr:
                    bufText = QLabel(f'{drink["nameDrink"]}: {drink["cost"]} X {drink["count"]} ({drink["volume"]})')
                    mainLayoot.addWidget(bufText)
                mainLayoot.addWidget(QLabel('Название еды:'))
                for food in dataFd:
                    bufText = QLabel(f'{food["nameFood"]}: {food["cost"]} X {food["count"]} ({food["volume"]})')
                    mainLayoot.addWidget(bufText)
                textAut = QLabel(f'Оформил заказ: {data[i]["fioStf"]}')
                mainLayoot.addWidget(textAut, 0, 2)
                cost = str(self.db.getCostForOrd(data[i]['id'])['cost'])
                disc = 0 if self.db.getDiscountVis(data[i]['idUser']) is None else self.db.getDiscountVis(
                    data[i]['idUser'])['discount']
                textCostOrd = QLabel(f'Стоимость заказа с учётом скидки в {disc}% : {cost} рублей')
                mainLayoot.addWidget(textCostOrd, 2, 2)
                mainLayoot.addItem(QSpacerItem(20, 200))
        else:
            self.ui.toolBoxOrder.hide()
            self.ui.MessegeOrdNot.show()

    def addInputDr(self):
        mainLayout = QHBoxLayout()
        self.ui.groupBoxD.setLayout(mainLayout)
        sub_btn = QComboBox()
        sub_cnt = QSpinBox()
        sub_cnt.setValue(1)
        self.qbD.append(sub_btn)
        self.CntD.append(sub_cnt)
        mainLayout.addWidget(sub_btn)
        mainLayout.addWidget(sub_cnt)


    ############################ QWIDGET = CURBAR FINISH ##############################################

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle(QStyleFactory.create('Fusion'))
    darkPalette = QPalette()
    darkPalette.setColor(QPalette.Window, QColor(53, 53, 53))
    darkPalette.setColor(QPalette.WindowText, Qt.white)
    darkPalette.setColor(QPalette.Base, QColor(35, 35, 35))
    darkPalette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
    darkPalette.setColor(QPalette.ToolTipBase, QColor(25, 25, 25))
    darkPalette.setColor(QPalette.ToolTipText, Qt.white)
    darkPalette.setColor(QPalette.Text, Qt.white)
    darkPalette.setColor(QPalette.Button, QColor(53, 53, 53))
    darkPalette.setColor(QPalette.ButtonText, Qt.white)
    darkPalette.setColor(QPalette.BrightText, Qt.red)
    darkPalette.setColor(QPalette.Link, QColor(42, 130, 218))
    darkPalette.setColor(QPalette.Highlight, QColor(0, 160, 255))
    darkPalette.setColor(QPalette.HighlightedText, QColor(35, 35, 35))
    darkPalette.setColor(QPalette.Active, QPalette.Button, QColor(53, 53, 53))
    darkPalette.setColor(QPalette.Disabled, QPalette.ButtonText, Qt.darkGray)
    darkPalette.setColor(QPalette.Disabled, QPalette.WindowText, Qt.darkGray)
    darkPalette.setColor(QPalette.Disabled, QPalette.Text, Qt.darkGray)
    darkPalette.setColor(QPalette.Disabled, QPalette.Light, QColor(53, 53, 53))
    darkPalette.setColor(QPalette.PlaceholderText, QColor(100, 100, 100))
    app.setPalette(darkPalette)
    app.setStyleSheet("QToolTip { color: #ffffff; background-color: #2a82da; border: 1px solid white; }")
    window = MyWindow()
    sys.exit(app.exec())
