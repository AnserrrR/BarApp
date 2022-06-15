import pymysql


class DataBase:
    def __init__(self):
        self.connection = pymysql.connect(
            host='localhost',
            port=3306,
            user='root',
            password='Konditer123321',
            database='barbd',
            cursorclass=pymysql.cursors.DictCursor)

    def getBars(self):
        query = f'select * from bars order by name'
        with self.connection.cursor() as cursor:
            cursor.execute(query)
            data = cursor.fetchall()
            return data

    def createBar(self, data):
        newId = None
        query = f'insert into bars(name, address) values(%s,%s);'
        with self.connection.cursor() as cursor:
            cursor.execute(query, data)
            newId = cursor.lastrowid
        self.connection.commit()
        return newId

    def editBar(self, data):
        query = f'update bars set name=%s, address=%s where id=%s'
        with self.connection.cursor() as cursor:
            cursor.execute(query, data)

        self.connection.commit()

    def deleteBar(self, idBar: int):
        query = f'delete from bars where id=%s'
        with self.connection.cursor() as cursor:
            cursor.execute(query, [idBar])

        self.connection.commit()

    def getCurBar(self, idBar: int):
        query = f'select * from bars where id=%s'
        with self.connection.cursor() as cursor:
            cursor.execute(query, [idBar])
            data = cursor.fetchone()
            return data

    def getCountAllVisBar(self, idBar: int):
        query = f'select count(*) as cnt from visitors_to_bars where idBar=%s'
        with self.connection.cursor() as cursor:
            cursor.execute(query, [idBar])
            data = cursor.fetchone()
            return data

    def getCountAllOrdBar(self, idBar: int):
        query = f'select count(*) as cnt from orders ' \
                f'join contracts cnt on cnt.id = orders.idContract ' \
                f'where idBar=%s;'
        with self.connection.cursor() as cursor:
            cursor.execute(query, [idBar])
            data = cursor.fetchone()
            return data

    def getAllVisitors(self):
        query = f'select * from allVisitors;'
        with self.connection.cursor() as cursor:
            cursor.execute(query)
            data = cursor.fetchall()
            return data

    def getAllDiscount(self):
        query = f'select id, concat(name, "-",  discount, "%") as disc from affilate_programms;'
        with self.connection.cursor() as cursor:
            cursor.execute(query)
            data = cursor.fetchall()
            return data

    def createVis(self, dataUs, dataVis):
        newIdVis = None
        queryUs = f'insert into users(phoneNumber) values(%s);'

        queryVis = f'insert into visitors(idUser, Firstname, SecondName, Patronymic, idAffilateProgramm) values(%s,%s,%s,%s,%s)'
        with self.connection.cursor() as cursor:
            cursor.execute(queryUs, dataUs)
            newIdVis = cursor.lastrowid
            # print([cursor.lastrowid, *dataVis])
            cursor.execute(queryVis, [cursor.lastrowid, *dataVis])
        self.connection.commit()
        return newIdVis

    def editVis(self, idUser: int, dataUs, dataVis):
        queryU = f'update users set phoneNumber= %s where id=%s; '
        queryV = f'update visitors set Firstname=%s, SecondName=%s, Patronymic=%s, idAffilateProgramm=%s where idUser=%s;'
        with self.connection.cursor() as cursor:
            cursor.execute(queryU, [*dataUs, idUser])
            cursor.execute(queryV, [*dataVis, idUser])
        self.connection.commit()

    def delVis(self, idUser: int):
        query = f'delete from users where id=%s;'
        with self.connection.cursor() as cursor:
            cursor.execute(query, [idUser])
        self.connection.commit()

    def allVisitorsOfBar(self, idBar: int):
        query = f'select * from allVisitorsBar where idBar = %s;'
        with self.connection.cursor() as cursor:
            cursor.execute(query, [idBar])
            data = cursor.fetchall()
            return data

    def getAllVisToCombo(self):
        query = f'select * from visToComboBox;'
        with self.connection.cursor() as cursor:
            cursor.execute(query)
            data = cursor.fetchall()
            return data

    def getEventFromDataVis(self, idBar: int, date: str):
        query = f'select * from events ev where ev.idBar=%s and %s <= adddate(ev.date, interval duration minute) and %s >= ev.date;'
        with self.connection.cursor() as cursor:
            cursor.execute(query, [idBar, date, date])
            data = cursor.fetchone()
            if data is None:
                return 0
            return 1

    def createVTB(self, idBar, idUser, data):
        query = f'insert into visitors_to_bars(idBar,idVisitor,timeOfVisit,event) values (%s,%s,%s,%s)'
        with self.connection.cursor() as cursor:
            cursor.execute(query, [idBar, idUser, *data])
            newId = cursor.lastrowid
        self.connection.commit()
        return newId

    def getAllOrders(self, idBar: int):
        query = f'select * from allOrders where idBar = %s'
        with self.connection.cursor() as cursor:
            cursor.execute(query, idBar)
            data = cursor.fetchall()
            return data

    def getAllDrinksOrd(self, idOrd: int):
        query = f'select name as nameDrink, cost, count, volume from drinks d join drinks_to_orders dto on dto.idDrink=d.id where dto.idOrder = %s'
        with self.connection.cursor() as cursor:
            cursor.execute(query, [idOrd])
            data = cursor.fetchall()
            return data

    def getAllFoodsOrd(self, idOrd: int):
        query = f'select name as nameFood, cost, count, volume from foods d join foods_to_orders fto on fto.idFood=d.id where fto.idOrder = %s'
        with self.connection.cursor() as cursor:
            cursor.execute(query, [idOrd])
            data = cursor.fetchall()
            return data

    def getCostForOrd(self, idOrd: int):
        query = f'select get_money_for_user(id) as cost from orders where id = %s'
        with self.connection.cursor() as cursor:
            cursor.execute(query, [idOrd])
            data = cursor.fetchone()
            return data

    def getDiscountVis(self, idUser: int):
        query = f'select discount from visitors join affilate_Programms ap on ap.id = visitors.idAffilateProgramm where idUser = %s'
        with self.connection.cursor() as cursor:
            cursor.execute(query, [idUser])
            data = cursor.fetchone()
            return data

    def getMonForPeriodBar(self, idBar: int, dates):
        query = f'select sum(money) as money from moneyForPeriodBar where idBar=%s and  dateOfOrder between %s and %s;'
        with self.connection.cursor() as cursor:
            cursor.execute(query, [idBar, *dates])
            data = cursor.fetchone()
            return data

