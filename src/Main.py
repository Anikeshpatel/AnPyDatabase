from andb.connect import Connection
from andb.database import Database
from andb.drop import DropTable, DropDatabase
from andb.table import Table

if Connection.connect("Anikesh"):
    print("Success")

a = 10
maindb = Database()
maindb.createDB("MainDatabase")
loginTB = Table()
loginTB.createTable("Login",maindb)
loginTB.setColumns(["id","name","email"])

print(DropTable.drop(loginTB))
print(DropDatabase.drop(maindb))