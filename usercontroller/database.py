import mysql.connector

class Database():
    def __init__(self):
        self.__connection = mysql.connector.connect(host='', user='admin', password='', database='')

    def select_records(self,statement):
        cursor = self.__connection.cursor()
        cursor.execute(statement)
        return cursor.fetchall()

    def query(self,statement):
        cursor = self.__connection.cursor()
        cursor.execute(statement)
        self.__connection.commit()
        cursor.close()

    def __del__(self):
        self.__connection.close()