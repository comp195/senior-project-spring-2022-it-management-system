import mysql.connector

db = mysql.connector.connect(host="rds-management-system-mysql.c1frdktaj1ae.us-west-1.rds.amazonaws.com", user="admin",
                             password="password")

print(db)
print("hi")
