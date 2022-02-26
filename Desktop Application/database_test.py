import mysql.connector

db = mysql.connector.connect(host="rds-management-system-mysql.c1frdktaj1ae.us-west-1.rds.amazonaws.com", user="admin",
                             password="password", database="dbmanagementsystem")
print(db)

# Show all databases
cursor = db.cursor()
cursor.execute("show databases")
for i in cursor:
    print("Databases:",i[0])

# Show all tables
cursor.execute("show tables")
for i in cursor:
    print("Table:",i[0])

# Inserting data in Ticket table
sqlCMD = "INSERT INTO dbmanagementsystem.Tickets (ID, TicketTitle) VALUES ('2', 'Broken Monitor')"
cursor.execute(sqlCMD)

# Show columns from Ticket table
cursor.execute("SHOW columns FROM dbmanagementsystem.Tickets")
result = cursor.fetchall()
j = 0
for i in result:
    j += 1
    print ("Column number:", j, i[0])

# Show data from Ticket table
cursor.execute("SELECT * FROM dbmanagementsystem.Tickets")
result = cursor.fetchall()
for i in result:
    print(i)

# When you want to make actual changes to the database
# db.commit()