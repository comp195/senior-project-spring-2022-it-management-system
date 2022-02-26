import mysql.connector
from mysql.connector import errorcode

try:
    db = mysql.connector.connect(host="rds-management-system-mysql.c1frdktaj1ae.us-west-1.rds.amazonaws.com",
                                 user="admin", password="password")
except mysql.connector.Error as db_err:
    if db_err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Check login credentials!")
    elif db_err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Confirm that database exists!")
    else:
        print(db_err)
else:
    db.close()

print(db)
print("hi")
