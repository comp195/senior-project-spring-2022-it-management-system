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
            print(name + " does exist")
            return True
        else:
            print(name + " does not exist")
            return False

    def db_connect(self):
        try:
            self.connection = mysql.connector.connect(
                host="rds-management-system-mysql.c1frdktaj1ae.us-west-1.rds.amazonaws.com",
                user="admin", password="password", database='dbmanagementsystem')
            self.cursor = self.connection.cursor()
            #print("Connected", self.connection)
        except mysql.connector.Error as db_err:
            if db_err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Check login credentials!")
            elif db_err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Confirm that database exists!")
            else:
                print("ERROR:")
                print(db_err)

    def get_rows(self):
        self.cursor.execute("SELECT * FROM dbmanagementsystem." + self.name)
        result = self.cursor.fetchall()
        # for i in result:
        #     print(i)
        return result

    def get_cols(self):
        self.cursor.execute("SHOW columns FROM dbmanagementsystem." + self.name)
        result = self.cursor.fetchall()
        col = []
        for i in result:
            col.append(i[0])
        return col

    def insert_data(self, data):
        baseCMD = "INSERT INTO dbmanagementsystem." + self.name + " ("
        # build cmd
        col = self.get_cols()
        j = 0
        for i in col:
            if j == len(col) - 1:
                baseCMD += str(i) + ") VALUES ("
            else:
                baseCMD += str(i) + ", "
            j += 1

        j = 0
        for i in data:
            if j == len(data) - 1:
                baseCMD += "'" + str(i) + "')"
            else:
                baseCMD += "'" + str(i) + "', "
            j += 1

        #print(baseCMD)
        self.cursor.execute(baseCMD)

def main():
    tick = dataTable("Tickets")
    print(tick.get_cols())

    data = [2, "Broken Keyboard"]
    tick.insert_data(data)

    data2 = ["3", "Broken Mouse"]
    tick.insert_data(data2)

    print(tick.get_rows())

    dev = dataTable("Devices")
    data3 = ["1", "Monitor", "123", "Kawhi", "Leonard", "1", "Support", "365", "2021-03-05", "300.0"]
    dev.insert_data(data3)
    print(dev.get_rows())

if __name__ == "__main__":
    main()