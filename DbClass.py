class DbClass:
    def __init__(self):
        import mysql.connector as connector

        self.__dsn = {
            "host": "localhost",
            "user": "vincent",
            "passwd": "computer",
            "db": "speedometerdb"
        }

        self.__connection = connector.connect(**self.__dsn)
        self.__cursor = self.__connection.cursor()

    def getDataFromDatabase(self):
        # Query zonder parameters
        sqlQuery = "SELECT * FROM tablename"
        
        self.__cursor.execute(sqlQuery)
        result = self.__cursor.fetchall()
        self.__cursor.close()
        return result

    def getDataFromDatabaseMetVoorwaarde(self, voorwaarde):
        # Query met parameters
        sqlQuery = "SELECT * FROM tablename WHERE columnname = '{param1}'"
        # Combineren van de query en parameter
        sqlCommand = sqlQuery.format(param1=voorwaarde)
        
        self.__cursor.execute(sqlCommand)
        result = self.__cursor.fetchall()
        self.__cursor.close()
        return result

    def setDataToDatabaseSessie(self, value1,value2,value3,value4):
        #Query met parameters
        sqlQuery = "INSERT INTO speedometerdb.Sessie VALUES ('{param1}', '{param2}','{param3}','{param4}')"
        #Combineren van de query en parameter
        sqlCommand = sqlQuery.format(param1=value1, param2=value2, param3 = value3, param4= value4)

        self.__cursor.execute(sqlCommand)
        self.__connection.commit()
        self.__cursor.close()