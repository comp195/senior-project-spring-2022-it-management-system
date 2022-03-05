import mysql
from mysql.connector import errorcode


class dataTable:
    def __init__(self, table_name):
        self.cursor = None
        self.connection = None
        self.row_list = None
        self.name = table_name
        self.db_connect()
        self.valid_table = self.check_table(table_name)

    def check_table(self, name):
        check = "SHOW TABLES LIKE '{}'".format(name)
        self.cursor.execute(check)
        result = self.cursor.fetchone()
        if result:
            print("Table does exist")
            return True
        else:
            print("Table does not exist")
            return False

    def db_connect(self):
        try:
            self.connection = mysql.connector.connect(
                host="rds-management-system-mysql.c1frdktaj1ae.us-west-1.rds.amazonaws.com",
                user="admin", password="password", database='dbmanagementsystem')
            self.cursor = self.connection.cursor()
            print("Connected", self.connection)
        except mysql.connector.Error as db_err:
            if db_err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Check login credentials!")
            elif db_err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Confirm that database exists!")
            else:
                print("ERROR:")
                print(db_err)

    def list_rows(self):
        self.cursor.execute("SELECT * FROM dbmanagementsystem." + self.name)
        result = self.cursor.fetchall()
        # for i in result:
        #     print(i)
        return result


def main():
    test = dataTable("Tickets")
    rows = test.list_rows()
    print(rows)

if __name__ == "__main__":
    main()