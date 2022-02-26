import mysql.connector
from mysql.connector import errorcode

# db = mysql.connector.connect(host="rds-management-system-mysql.c1frdktaj1ae.us-west-1.rds.amazonaws.com", user="admin",
#                              password="password", database="dbmanagementsystem")
# print(db)
#
# # Show all databases
# cursor = db.cursor()
# cursor.execute("show databases")
# for i in cursor:
#     print("Databases:",i[0])
#
# # Show all tables
# cursor.execute("show tables")
# for i in cursor:
#     print("Table:",i[0])
#
# # Inserting data in Ticket table
# sqlCMD = "INSERT INTO dbmanagementsystem.Tickets (ID, TicketTitle) VALUES ('2', 'Broken Monitor')"
# cursor.execute(sqlCMD)
#
# # Show columns from Ticket table
# cursor.execute("SHOW columns FROM dbmanagementsystem.Tickets")
# result = cursor.fetchall()
# j = 0
# for i in result:
#     j += 1
#     print ("Column number:", j, i[0])
#
# # Show data from Ticket table
# cursor.execute("SELECT * FROM dbmanagementsystem.Tickets")
# result = cursor.fetchall()
# for i in result:
#     print(i)
#
# # When you want to make actual changes to the database
# # db.commit()

# CONNECT TO DB INSTANCE AND RUN QUERY TO CREATE TABLE IF IT DOES NOT YET EXIST
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
# cursor.execute("DROP TABLE IF EXISTS Devices")

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