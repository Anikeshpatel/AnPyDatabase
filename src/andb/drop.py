import os
from andb.database import Database
from andb.table import Table


class DropDatabase:

    def drop(dropDatabase ):
        dropStatus = False
        try:
            os.rmdir(dropDatabase.dbDir)
            dropStatus = True
        except Exception:
            dropStatus = False
        finally:
            return dropStatus


class DropTable:

    def drop(dropTable):
        dropStatus = False
        try:
            os.remove(dropTable.tbDir)
            dropStatus = True
        except Exception:
            dropStatus = False
        finally:
            return dropStatus