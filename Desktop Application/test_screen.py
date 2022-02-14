from tkinter import *
from tkinter import ttk


# CONNECTING TO MYSQL SERVER USING CONNECTOR/PYTHON
# import mysql.connector
# connection = mysql.connector.connect(user='user_here', password='password_here',
#                                      host='111.1.1.1',
#                                      database='employees')
# connection.close()

# QUERIES
# connection = mysql.connector.connect(user='user_here', database='employees')
# cursor = connection.cursor()
# query = ("SELECT f_name, l_name, IT_status FROM employees "
#          "WHERE IT_status = 1")
# cursor.execute(query)
# for listing in cursor:
#     print(listing)


root = Tk()
frame = ttk.Frame(root, padding=400)
frame.grid()
ttk.Label(frame, text="Testing").grid(column=0, row=0)
ttk.Button(frame, text="Exit", command=root.destroy).grid(column=0, row=20)
root.mainloop()
