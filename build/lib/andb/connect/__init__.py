import platform
import os
class Connection:
    dbLocation= ""
    __projectName = ""
    status = False
    @staticmethod
    def connect(projectName):
        Connection.__projectName = projectName
        if(platform.system().lower().__contains__("windows")):
            Connection.dbLocation = ("C:\\Users\\"+os.environ.get("USERNAME")+"\\AppData\\Local\\"+Connection.__projectName)
            Connection.status = True
        if (platform.system().lower().__contains__("linux")):
            Connection.dbLocation = r"/home/" + os.environ.get(
                "USERNAME") + os.sep + Connection.__projectName
            Connection.status = True
        return Connection.__initSpace()

    @staticmethod
    def __initSpace():
        isAvailable = False
        try:
            if not os.path.exists(Connection.dbLocation):
                os.mkdir(Connection.dbLocation)
            isAvailable = True
        except Exception:
            isAvailable = False
        finally:
            return isAvailable
