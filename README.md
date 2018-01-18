# AnPyDatabase

# `Just Focus On What To Do, Not In How To Do`


AnPyDatabase is a Library that provides a AnDatabase Support For Python Language Thats Help In In Python Base Desktop Softwares .


# _>>> Features_ : 
 1. No SQL Required, SQL Free Database
 2. Fast and Flexible  
 3. Table Exportation Support (To CSV File)
 
# _>>> Install_ :    
### Type Command In Terminal Or CMD   
```  
  pip install AnPyDatabase
  
```
# _>>> Projects Using AnDatabase_ :   

* <a href="https://github.com/anongrp/ThunderGet">ThunderGet</a>
* <a href="https://github.com/Anikeshpatel/Lucid-Smart-Buddy">Lucid-Smart-Buddy</a>
* <a href="https://github.com/anikeshpatel/colorcode-pro">ColorCode Pro</a>  
 
# _>>> Basic Implementation_ :
 
 ### Import All Modules  
 ```python
from andb.connect import Connection
from andb.database import Database
from andb.table import Table
from andb.drop import DropTable, DropDatabase
 ```
 1. For Connecting To The AnDatabase `Connection.connect()` It Simply Returns Boolean Value True If Database is Connected Otherwise False.     
 
 2. Creating Database  
 ```python 
mainDatabase = Database()  
mainDatabase.createDB("NameOfDatabase")
 ```  
 3. Creating Table Inside mainDatabase  
 ```python  
loginFormTable = Table();  
loginFormTable.createTable("TableName",mainDatabase);
 ```
 
 4. Add Columns Inside Table  
 ```python  
 loginFormTable.setColumns(["id", "name","email","password"]);
 ```
 
 5. Ok That's It You Have Good To Go With AnDatabase And For Adding Data To Table Or Column Use  
 ```python 
 studentTB.addRow(["1","UserName","UserEmail@Example.com"])
 ```
 
 # >>> Security Example : 

For Password Security AnDatabase Provide A Security Class That Encrypt Your Password With A Special Key Inside Program Then Add Into Column.  
Eg.  
```java 
Security.encrypt(Data,Key);
Security.decrypt(EncryptedData,key);
```  

 
![Anon Database](https://github.com/Anikeshpatel/AnDatabase/blob/master/images/AnonDatabase.png)  
