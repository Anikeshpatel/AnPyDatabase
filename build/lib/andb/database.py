from andb.connect import Connection
import os

class Database:

    def __init__(self):
        self.__dbName = "db-temp"
        self.__dbStatus = ""
        self.dbDir = ""

    def createDB(self,dbName):
        self.__dbName = "db-"+dbName
        self.dbDir = Connection.dbLocation + os.sep + self.__dbName
        if (not os.path.exists(self.dbDir) and Connection.status):
            os.mkdir(self.dbDir)
            __dbStatus = True
        if (not Connection.status):
            __dbStatus = False
        return self.__dbStatus

    def isDatabaseAvailable(self):
        return os.path.exists(self.dbDir)
    def getDatabaseName(self):
        return self.__dbName[self.__dbName.find("-")+1:-1]

    def getDatabaseStatus(self):
        return self.__dbStatus