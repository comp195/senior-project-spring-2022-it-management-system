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

    def get_cursor(self):
        return self.cursor

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

        print(baseCMD)
        self.cursor.execute(baseCMD)

    # Function to parse a row of EQUIPMENT data
    # Args:     a list containing attributes of only a single row of data
    # Return:   a list pairing each attribute value to its category (EX. "ID: 123")
    # NOTE:     Size of 'row' must be equal to 10
    # NOTE:     currently referring to attributes of "Devices" table; update as necessary
    def obtain_parsed_equipment_row(self, row):
        # attributes = ["equipment_id: ", "category: ", "status: ", "date_purchased: ", "days_in_rotation: ", "cost: ",
        #               "current_user_id: ", "current_department: "]
        categorized_list = []
        attributes = ["device_id: ", "category: ", "current_user_id: ", "user_first_name: ", "user_last_name: ",
                      "department_id: ", "department: ", "days_since_purchase: ", "purchase_date: ", "cost: "]
        for i in range(10):
            paired_string = attributes[i] + str(row[i])     # must ensure row values are strings
            categorized_list.append(paired_string)

        return categorized_list


def main():
    equipment = dataTable("Equipment")
    print(equipment.get_rows())

    # tick = dataTable("Tickets")
    # print(tick.get_cols())
    #
    # data = ['2', 1, 'John', 'Cena', '1', 'Mouses', 'Broken mouse', 'Left click not working', 'Maintenance', 'Medium', 'Supoort']
    # tick.insert_data(data)
    #
    # print(tick.get_rows())
    #
    # dev = dataTable("Devices")
    # data3 = ["1", "Monitor", "123", "Kawhi", "Leonard", "1", "Support", "365", "2021-03-05", "300.0"]
    # dev.insert_data(data3)
    # print(dev.get_rows())


if __name__ == "__main__":
    main()