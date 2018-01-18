from andb.database import Database
import os

class Table:

    def __init__(self):
        self.__tbName = "tb-temp"
        self.tbDir = ""
        self.table = ''
        self.__objectCallCounter = 0
        self.__status = False
        self.__column = ""
        self.__columnNames = []
        self.__colInfo = {}

    def createTable(self,tbName, database):
        self.__objectCallCounter += 1
        if(self.__objectCallCounter >1 ):
            return False
        else:
            self.__tbName = "tb-"+tbName
            self.tbDir = database.dbDir + os.sep + self.__tbName + ".andb"
            if(database.isDatabaseAvailable() and not(os.path.exists(self.tbDir))):
                table = open(self.tbDir,'a+')
                self.__status = True
            return self.__status

    def isTableAvailable(self):
        return os.path.exists(self.tbDir)

    def setColumns(self,columnNames = []):
        self.__column = len(columnNames)
        self.__columnNames = columnNames
        self.__setColInfo(columnNames)
        table_file = open(self.tbDir,"a+")
        temp = table_file.read()
        if os.path.getsize(self.tbDir) == 0:
            for i in range(self.__columnNames.__len__()):
                table_file.write("¤"+columnNames[i])
            table_file.write("¤")
            table_file.close()

    def __setColInfo(self,columnNames):
        for i in range(len(columnNames)):
            self.__colInfo.setdefault(columnNames[i] , i+1)

    def addRow(self,rowData = []):
        table_file = open(self.tbDir,"a")
        table_file.write("\n")
        for i in range(rowData.__len__()):
            #if(i+1 > self.__column):
            #   raise Exception("Column Index Out Of Bound Exception")
            table_file.write("¤"+rowData[i])
        table_file.write("¤")
        table_file.close()

    def __counter(self,rowData = "",target = ''):
        data = list(rowData)
        count = 0
        for i in range(data.__len__()):
            if(data[i] == target):
                count += 1

        return count

    def __searcher(self,data = "",colName = ""):
        rowNo = int(self.__colInfo.get(colName))
        dataNo = 0
        finalData = []
        with open(self.tbDir) as tb:
            for line in tb:
                if data in line:
                    dataNo = self.__counter(line[0:line.find(data)],'¤')
                    if(rowNo == dataNo):
                        finalData.append(line)

        return finalData

    def deleteElement(self,colName,target):
        deleteStatus = False
        deleteRow = ""
        rows = []
        finalRow = self.__searcher(target,colName)
        if(finalRow.__len__() > 0):
            deleteRow = finalRow[0]

        try:
            with open(self.tbDir) as tb:
                for line in tb:
                    if(not(line == deleteRow)):
                        rows.append(line)

            cleanTable = open(self.tbDir,'w')
            cleanTable.write("")
            cleanTable.close()

            tableWriter = open(self.tbDir,"a+")
            for i in range(rows.__len__()):
                if(not(rows[i] == "")):
                    tableWriter.write(rows[i])


            deleteStatus = True
        except Exception:
            deleteStatus = False

        return deleteStatus

    def __getFetchedData(self,fullRow):
        symbolPosition = []
        fetchedData = []
        if(not (fullRow == None)):
            dataList = list(fullRow)
            for i in range(dataList.__len__()):
                if dataList[i] == "¤":
                    symbolPosition.append(i)

            try:
                for j in range(symbolPosition.__sizeof__()):
                    fetchedData.append(fullRow[symbolPosition[j]+1:symbolPosition[j+1]])
            except Exception:
                ignores = ""
        else:
            fetchedData.append(None)
        return fetchedData

    def getRow(self,colName,target):
        row = None
        try:
            row = self.__searcher(target,colName)[0]
        except Exception:
            ignored = ""
        finally:
            return self.__getFetchedData(row)

    def getTable(self):
        tableData = []

        with open(self.tbDir) as tb:
            for line in tb:
                tableData.append(self.__getFetchedData(line))

        return tableData

    def exportToCSV(self,csvFile):
        status = False
        COMMA_DELIMITER = ","
        NEW_LINE_SEPARATOR = "\n"

        tableData = self.getTable()

        try:
            csv_writer = open(csvFile,"a+")
            counter = -1
            for i in tableData:
                counter += 1
                for j in tableData[counter]:
                    csv_writer.write(j+COMMA_DELIMITER)
                csv_writer.write(NEW_LINE_SEPARATOR)
            status = True
            csv_writer.close()
        except Exception:
            status = False
        finally:
            return status
