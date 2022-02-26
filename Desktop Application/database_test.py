import mysql.connector
from mysql.connector import errorcode

try:
    connection = mysql.connector.connect(host="rds-management-system-mysql.c1frdktaj1ae.us-west-1.rds.amazonaws.com",
                                 user="admin", password="password", database='dbmanagementsystem')
    cursor = connection.cursor()
except mysql.connector.Error as db_err:
    if db_err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Check login credentials!")
    elif db_err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Confirm that database exists!")
    else:
        print("ERROR:")
        print(db_err)

# Drop table if it already exists
cursor.execute("DROP TABLE IF EXISTS Devices")

query = (
    "CREATE TABLE `Devices` ("
    " `device_id` int(11) NOT NULL,"
    " `category` ENUM('Desktop', 'Laptop', 'VoIP Phone', 'Monitor', 'Headset', 'Webcam') NOT NULL,"
    " `current_user_id` int(11),"
    " `user_first_name` varchar(20),"
    " `user_last_name` varchar(20),"
    " `department_id` int(11),"
    " `department` varchar(40),"
    " `days_since_purchase` int(11) NOT NULL,"
    " `purchase_date` date NOT NULL,"
    " `cost` decimal(10,2) NOT NULL,"
    " PRIMARY KEY (`device_id`)"
    ") ENGINE=InnoDB")

try:
    cursor.execute(query)
except mysql.connector.Error as creation_error:
    if creation_error.errno == errorcode.ER_TABLE_EXISTS_ERROR:
        print("Table already exists!")
    else:
        print(creation_error.msg)
else:
    print("Table created!")
cursor.close()
connection.close()