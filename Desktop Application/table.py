import mysql
import bcrypt
from mysql.connector import errorcode


class dataTable:
    def __init__(self, table_name):
        self.cursor = None
        self.connection = None
        self.row_list = None
        self.name = table_name
        self.db_connect()
        self.valid_table = self.check_table(table_name)

    def commit(self):
        self.connection.commit()

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
            # print("Connected", self.connection)
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

    def print_rows(self):
        rows = self.get_rows()
        for i in rows:
            print(i)

    def insert_data(self, data):
        baseCMD = "INSERT INTO dbmanagementsystem." + self.name + " ("
        # build cmd
        col = self.get_cols()
        col.pop(0)
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
            paired_string = attributes[i] + str(row[i])  # must ensure row values are strings
            categorized_list.append(paired_string)

        return categorized_list

    def insert_password(self, pw):
        print("inserting password")

    def encrypt_password(self, pw):
        password = pw
        # encode password
        password = password.encode('utf-8')
        # encrypt pasword
        hashed = bcrypt.hashpw(password, bcrypt.gensalt(10))
        de_hashed = hashed.decode()
        return de_hashed

    def password_check(self, user, pw):
        valid = (self.name == "Login_Credentials")
        if valid:
            row = self.filter_rows("username", user)
            if row:
                check = pw.encode('utf-8')
                hashed = row[0][2]
                hashed = str.encode(hashed)
                if bcrypt.checkpw(check, hashed):
                    return True
        return False

    def filter_rows(self, col, value):
        cmd = "select * from dbmanagementsystem." + self.name + " where " + col + " = " + "'" + str(value) + "'"
        print(cmd)
        if col in self.get_cols():
            self.cursor.execute(cmd)
            result = self.cursor.fetchall()
            return result
            # for i in result:
            #     print(i)
        else:
            print("Column doesn't exist")
            return None

    def alter_row(self, columns_to_change, new_values, column_to_filter, filter_value):
        # UPDATE dbmanagementsystem.Login_Credentials SET admin = 'False' WHERE employee_id = 1
        # UPDATE dbmanagementsystem.Login_Credentials SET admin = 'False', `active` = 'False', `permission_level` = '2' WHERE employee_id = '2'
        valid = True
        check_col = self.get_cols()
        for col in columns_to_change:
            if col not in check_col:
                valid = False
        if valid:
            cmd = "UPDATE dbmanagementsystem." + self.name + " SET "
            for i in range(len(columns_to_change)):
                cmd += columns_to_change[i] + " = '" + new_values[i] + "'"
                if i < len(columns_to_change)-1:
                    cmd += ", "
            cmd += " WHERE " + column_to_filter + " = '" + filter_value + "'"
            print(cmd)
            self.cursor.execute(cmd)
        else:
            print("Invalid columns name")

    def sort_table_ascending(self, column):
        cmd = "SELECT * from dbmanagementsystem." + self.name + " ORDER BY " + column + " ASC"
        self.cursor.execute(cmd)
        result = self.cursor.fetchall()
        return result

    def sort_table_descending(self, column):
        cmd = "SELECT * from dbmanagementsystem." + self.name + " ORDER BY " + column + " DESC"
        self.cursor.execute(cmd)
        result = self.cursor.fetchall()
        return result

    def cancel_row(self, column, value):
        cmd = "DELETE from dbmanagementsystem." + self.name + " where " + column + " = '" + value + "'"
        print(cmd)
        self.cursor.execute(cmd)

    def username_exists(self, value):
        # SELECT EXISTS(SELECT * from dbmanagementsystem.Login_Credentials WHERE username="k_leonard")
        valid = (self.name == "Login_Credentials")
        if valid:
            cmd = "SELECT EXISTS(SELECT * from dbmanagementsystem." + self.name + " WHERE username='" + value + "')"
            self.cursor.execute(cmd)
            if self.cursor.fetchone()[0]:
                print("Username exists")
                return True
            else:
                print("Username doesn't exist")
                return False
        else:
            print("You can only use this method for Login_Credentials table")

    def email_exists(self, value):
        cmd = "SELECT EXISTS(SELECT * from dbmanagementsystem." + self.name + " WHERE email='" + value + "')"
        self.cursor.execute(cmd)
        if self.cursor.fetchone()[0]:
            print("Email exists")
            return True
        else:
            print("Email doesn't exist")
            return False


def main():
    # # password encryption
    # password = "juice"
    # print(password)
    #
    # # encode password
    # password = password.encode('utf-8')
    # print(password)
    #
    # # encrypt pasword
    # hashed = bcrypt.hashpw(password, bcrypt.gensalt(10))
    # print(hashed)
    # de_hashed = hashed.decode()
    # print(de_hashed)

    # # password input
    # check = "juice"
    # print(check)
    #
    # # encode the authenticating password
    # check = check.encode('utf-8')
    # print(check)
    #
    # # check:
    # if bcrypt.checkpw(check, hashed):
    #     print("correct password")
    # else:
    #     print("incorrect password")

    log = dataTable("Login_Credentials")
    log.username_exists("k_leonard")

    emp = dataTable("Employee")
    emp.email_exists("k_leonard@gmail.com")

if __name__ == "__main__":
    main()
