import tkinter
import tkinter as tk
from tkinter import *
from tkinter.font import Font
from tkinter import font as tkfont, ttk  # python 3
import table

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080

# CONSTANTS TO KEEP TRACK OF INDICES OF EACH DB TABLE FIELD WITHIN THE LIST(S)
ID_INDEX = 0
EQUIPMENT_ID_INDEX = 0
CATEGORY_INDEX = 1
STATUS_INDEX = 2
CURRENT_USER_ID_INDEX = 3
DATE_PURCHASED_INDEX = 4
DAYS_IN_ROTATION_INDEX = 5
COST_INDEX = 6
USER_FIRST_NAME_INDEX = 7
USER_LAST_NAME_INDEX = 8
DEPARTMENT_ID_INDEX = 9
DEPARTMENT_INDEX = 10

global current_data_rows

coconut = "#9B582E"
quick_silver = "#A7A39E"
gainsboro = "#E0DDD9"
rajah = "#F5B15E"
stormcloud = "#4D646A"

global username_verify, password_verify


class SeeDismissPanel(ttk.Frame):
    def __init__(self, master):
        ttk.Frame.__init__(self, master)
        self.pack(side=BOTTOM, fill=X)  # resize with parent
        # set resize constraints
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

class GUIController(tk.Tk):

    def __init__(self, *args, **kwargs):
        global SCREEN_WIDTH, SCREEN_HEIGHT, coconut, gainsboro, stormcloud
        tk.Tk.__init__(self, *args, **kwargs)

        # Basic Configuration Values for Root Tk()
        self.active_frame = "LoginPage"
        self.active_table = "Equipment"
        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")
        self.window_title = "Application"
        # self.resolution = str(SCREEN_WIDTH) + "x" + str(SCREEN_HEIGHT)

        # self.geometry(self.resolution)
        # Initializing container that stacks our frames

        container = tk.Frame(self, bg=stormcloud)

        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # Implementation of Root Tk() Configurations
        self.title(self.window_title)
        self['bg'] = stormcloud       # background color of ROOT

        # Initializing all of our frames within our container
        self.frames = {}

        for F in (MainPage, LoginPage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            frame.config(bg=stormcloud)   # background color of individual frame
            self.frames[page_name] = frame
            print(page_name)

            # Putting all of our frames in the same place on the screen with the top one being active
            frame.grid(row=0, column=0)

        # Frame visible at the start of the application
        self.show_frame(self.active_frame)

    def key_pressed(self, event):
        print(event.char)
        if event.keysym == 'Return' and self.active_frame == "LoginPage":
            self.frames["LoginPage"].login()


    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        self.active_frame = page_name
        for f in self.frames.values():
            f.grid_forget()

        frame = self.frames[page_name]
        frame.grid(row=0, column=0)

    def login_verification(self):
        global username_verify, password_verify
        username = str(username_verify.get())
        password = str(password_verify.get())
        login = table.dataTable("Login_Credentials")
        verified = login.password_check(username, password)
        if verified:
            self.show_frame("MainPage")
        return verified


class LoginPage(tk.Frame):
    def __init__(self, parent, controller):
        global username_verify, password_verify, stormcloud
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.controller = controller
        self.config(width=self.controller.winfo_reqwidth(), height=self.controller.winfo_reqheight(), bg=stormcloud)


        self.user_label = tk.Label(self, text="Username:", bg=stormcloud).pack()
        self.username_login_entry = tk.Entry(self, textvariable=username_verify).pack()
        self.space_label = tk.Label(self, text="", bg=stormcloud).pack()
        self.password_label = tk.Label(self, text="Password:",bg=stormcloud)
        self.password_label.pack()
        self.password_login_entry = tk.Entry(self, textvariable=password_verify, show='*')
        self.password_login_entry.pack()
        self.space_label_2 = Label(self, text=" ", fg="red", bg=stormcloud)
        self.space_label_2.pack()

        self.login_button = Button(self, text="Login", width=10, height=1, command=self.login)
        self.login_button.pack()

        self.registration_button = Button(self, text="Register", width=10, height=1, command = self.register)
        self.registration_button.pack()

    def login(self):
        texts = [" ", "Invalid Credentials"]
        logged_in = self.controller.login_verification()
        self.space_label_2['text'] = texts[int(not logged_in)]

    def register(self):
        self.credentials = [StringVar(), StringVar(), StringVar(), StringVar()]

        self.registration_screen = Toplevel(self.controller)
        self.registration_screen.title("Register")
        self.registration_screen.config(bg=stormcloud)


        self.user_label = tk.Label(self.registration_screen, text="Username:", bg=stormcloud).pack()
        self.username_login_entry = tk.Entry(self.registration_screen, textvariable=self.credentials[0]).pack()
        self.register_space_label_0 = tk.Label(self.registration_screen, text="", bg=stormcloud).pack()
        self.register_email_label = tk.Label(self.registration_screen, text="Email:", bg=stormcloud).pack()
        self.register_email_login_entry = tk.Entry(self.registration_screen, textvariable=self.credentials[1]).pack()
        self.register_space_label_1 = tk.Label(self.registration_screen, text="", bg=stormcloud).pack()
        self.register_password_label = tk.Label(self.registration_screen, text="Password:", bg=stormcloud)
        self.register_password_label.pack()
        self.register_password_login_entry = tk.Entry(self.registration_screen, textvariable=self.credentials[2], show='*')
        self.register_password_login_entry.pack()
        self.register_space_label_2 = Label(self.registration_screen, text=" ", fg="red", bg=stormcloud)
        self.register_space_label_2.pack()
        self.register_confirm_password_label = tk.Label(self.registration_screen, text="Confirm Password:", bg=stormcloud)
        self.register_confirm_password_label.pack()
        self.register_confirm_password_login_entry = tk.Entry(self.registration_screen, textvariable=self.credentials[3], show='*')
        self.register_confirm_password_login_entry.pack()
        self.register_space_label_3 = Label(self.registration_screen, text=" ", fg="red", bg=stormcloud)
        self.register_space_label_3.pack()

        self.registration_submit_button = tk.Button(self.registration_screen, text="Submit", width=10, height=1, command= self.registration_submit)
        self.registration_submit_button.pack()

    def registration_submit(self):
        success = True

        if self.credentials[2].get() != self.credentials[3].get():
            success = False
            self.register_space_label_3.config(text="Password Mismatch")

        if success is True:
            self.registration_screen.destroy()





class PageHeader(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        global SCREEN_WIDTH, SCREEN_HEIGHT, coconut, quick_silver, gainsboro, stormcloud, username_verify, password_verify
        # Initializing GUI Controller
        self.controller = controller
        self.button_names = ["Equipment", "Employees", "Tickets", "Help"]
        self.buttons = []
        self.button_dict = {}   # Maps button name to button index
        username_verify = StringVar()
        password_verify = StringVar()
        for i in range(len(self.button_names)):
            curr_button_name = self.button_names[i]
            # Temp conditions; change table names possibly
            if curr_button_name == "Employees":
                curr_button_name = "Employee"

            button = tk.Button(self, text=curr_button_name, command=lambda identifier=curr_button_name: self.press_button(identifier), bg=stormcloud,
                               fg=gainsboro, highlightthickness=0, bd=0)
            button.config(width=15, height=4, font=("Montserrat", 20))
            button.grid(row=0, column=i, sticky=W)
            self.buttons.append(button)
            self.button_dict[curr_button_name] = i
        self.buttons[0].config(fg=quick_silver)

    def press_button(self, identifier):
        for button in self.buttons:
            button.config(fg=gainsboro)
        self.buttons[self.button_dict.get(identifier)].config(fg=quick_silver)
        if identifier != "Help":
            self.controller.frames["MainPage"].update_on_button_press(identifier)


class DataFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        # Initializing GUI Controller
        self.controller = controller
        self.detail_frame = DetailFrame(self, controller)
        self.detail_frame.grid(row=1, column=1)
        self.entry_string_list = []

        self.frames = {}
        self.frames["DetailFrame"] = self.detail_frame

        self.search_table = SearchFrame(self, controller, self.frames)
        self.search_table.grid(row=1, column=0)

        self.tool_bar = ToolBarFrame(self, controller)
        self.tool_bar.grid(row=0, column=1, sticky="w")

    def clear_entry_string_list(self):
        self.entry_string_list = []

    def add_row(self):
        print("add row button clicked")
        self.search_table.search_grid.tree.selection_clear()
        curr_entries = self.detail_frame.get_current_entries()
        for entry in curr_entries:
            self.entry_string_list.append(entry.get())
        print(self.entry_string_list)
        # TODO: incorporate proper checks to ensure all required rows have proper values; DO NOT ALLOW CODE BELOW TO RUN IF NOT ALL REQUIRED FIELDS ARE VALID

        # TODO: After the checks to ensure that all required fields are valid and the row has been added, clear entry string list AND the actual strings that appear within the entry boxes
        # MOVE THE TWO LINES BELOW SO THAT THEY ARE CALLED AFTER THE ROW IS ADDED SUCCESSFULLY
        self.clear_entry_string_list()
        self.detail_frame.clear_entries()

        # TODO: Implement Logic to add a row

        # assuming that they are going to press the add row button twice
        # pressing first time
        # need a variable for table name like how the method update_on_button_press has an argument like screen_name
        # create a datatable object
        # self.current_table = table.dataTable("name of the table")
        # pressing second time
        # should call method to check if all the fields are inputted and if so then it should put all the values within the fields into a list
        # self.current_table.insert_data(a list of all the values the user has inputted into the fields)
        # if this command runs without problem then it is good then
        # you will probably need to run
        # self.current_table.get_rows()
        # to get a new list of the rows and then pass the list into whatever function to redisplay the rows
        self.tool_bar.change_mode(2)
        return

    def cancel_row(self):
        # TODO: Implement Logic to cancel current row
        # create a datatable object
        # self.current_table = table.dataTable("name of the table")
        # you should have a like a list of the ids of the newly added rows and then call a method to check if the row the user is highlighting is a newly added row that should return a bool
        # if the above method is true then run the command at the bottom
        # self.current_table.cancel_row(column,value) column can be like equipment_id and value is the id number u wawnt to delete
        # if that command works then its good
        self.tool_bar.change_mode(0)

    def update_database(self):
        # TODO: Implement Logic to update database
        self.tool_bar.change_mode(2)

    def submit_data(self):
        self.tool_bar.change_mode(0)
        # TODO: Update data to Database


    def refresh(self):
        # TODO: Pull latest data from database
        return


class MainPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        # Initializing GUI Controller
        self.controller = controller
        self.config(bg=stormcloud)
        # Create instance of database connection and use the data as argument
        self.equipment_table = table.dataTable("Equipment")

        header = PageHeader(parent=self, controller=self.controller)
        header.pack(side="top", anchor="nw")

        global current_data_rows
        current_data_rows = self.equipment_table.get_rows()

        self.search = SearchBarFrame(self, controller)
        self.search.pack(side=tk.TOP, anchor="w")

        self.data_frame = DataFrame(self, controller)
        self.data_frame.pack(side=tk.BOTTOM)


        # self.detail_frame = DetailFrame(self, controller)
        # self.detail_frame.pack(side=tk.RIGHT)

        # Create frames dictionary so the SearchFrame/MCList can access the DetailFrame's functions
        # (needed to update the details based on a click within the MCList)



        # self.frames = {}
        # self.frames["DetailFrame"] = self.detail_frame
        #
        # self.search_table = SearchFrame(self, controller, self.frames)
        # self.search_table.pack(side=tk.LEFT)

    def update_on_button_press(self, screen_name):
        self.equipment_table = table.dataTable(screen_name)
        # Update the global current_data_rows value based on the new table
        global current_data_rows
        current_data_rows = self.equipment_table.get_rows()

        # Update the labels and entry boxes that appear based on the new table
        self.data_frame.detail_frame.refresh_detail_components(screen_name)

        self.column_indices_to_retrieve = [ID_INDEX, 1, 2, 3, 4]
        self.MCList_values_struct = MCListValuesStruct(screen_name)
        self.data_tuples_list = self.MCList_values_struct.get_tuple_list(self.column_indices_to_retrieve)
        self.details_struct = DetailFrameValuesStruct(self.data_frame.frames["DetailFrame"], screen_name)
        self.column_titles = self.details_struct.get_specific_columns(self.column_indices_to_retrieve)
        self.data_frame.search_table.search_grid.replace_contents(self.column_titles, self.data_tuples_list)

        # self.search_table.search_grid._replace_contents(columns, data)


class ToolBarFrame(tk.Frame):
    def __init__(self, parent, controller):
        global stormcloud
        tk.Frame.__init__(self, parent)
        # Initializing GUI Controller
        self.controller = controller
        self.parent = parent
        self.change_mode(0)

    def change_mode(self, mode):
        if mode == 0:
            for i in range(len(self.winfo_children())-1, -1, -1):
                self.winfo_children()[i].destroy()
            self.refresh_button = tk.Button(self, text="Refresh", command=lambda: self.parent.refresh())
            self.refresh_button.grid(row=0, column=0)
            self.space_label_1 = tk.Label(self, width=1)
            self.space_label_1.grid(row=0, column=1)
            self.add_button = tk.Button(self, text="Add Row", command=lambda: self.parent.add_row())
            self.add_button.grid(row=0, column=2)
        elif mode == 1:
            for i in range(len(self.winfo_children())-1, -1, -1):
                self.winfo_children()[i].destroy()
            self.refresh_button = tk.Button(self, text="Refresh", command=lambda: self.parent.refresh())
            self.refresh_button.grid(row=0, column=0)
            self.space_label_1 = tk.Label(self, width=1)
            self.space_label_1.grid(row=0, column=1)
            self.add_button = tk.Button(self, text="Add Row", command=lambda: self.parent.add_row())
            self.add_button.grid(row=0, column=2)
            self.space_label_1 = tk.Label(self, width=1)
            self.space_label_1.grid(row=0, column=3)
            self.update_button = tk.Button(self, text="Update", command=lambda: self.parent.update_database())
            self.update_button.grid(row=0, column=4)
        elif mode == 2:
            for i in range(len(self.winfo_children())-1, -1, -1):
                self.winfo_children()[i].destroy()
            self.refresh_button = tk.Button(self, text="Refresh", command=lambda: self.parent.refresh())
            self.refresh_button.grid(row=0, column=0)
            self.space_label_1 = tk.Label(self, width=1)
            self.space_label_1.grid(row=0, column=1)
            self.add_button = tk.Button(self, text="Submit", command=lambda: self.parent.submit_data())
            self.add_button.grid(row=0, column=2)
            self.space_label_1 = tk.Label(self, width=1)
            self.space_label_1.grid(row=0, column=3)
            self.cancel_button = tk.Button(self, text="Cancel", command=lambda: self.parent.cancel_row())
            self.cancel_button.grid(row=0, column=4)


class SearchBarFrame(tk.Frame):
    def __init__(self, parent, controller):
        global stormcloud
        tk.Frame.__init__(self, parent)
        self.config(bg=stormcloud)
        # Initializing GUI Controller
        self.controller = controller

        self.search_var = StringVar()
        self.search_text = ""
        self.search_bar = tk.Entry(self, highlightbackground="#363030", textvariable=self.search_var, highlightthickness=1,
                              width=258)
        self.search_bar.grid(row=0, column=0)

        self.search_space = tk.Label(self, width=1, bg=stormcloud)
        self.search_space.grid(row=0, column=1)

        self.search_button = tk.Button(self, text="Search", command=lambda: self.search(), width=10)
        self.search_button.grid(row=0, column=2)

    def search(self):
        return None


class DetailFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        global SCREEN_WIDTH, SCREEN_HEIGHT, coconut, gainsboro, stormcloud
        self.config(bg=stormcloud)
        # Initializing GUI Controller
        self.controller = controller
        self.detail_frame = tk.Frame(self, bg="white", highlightbackground="#363030", highlightthickness=2, width=1300, height=670)
        self.detail_frame.grid_propagate(False)     # Needed so that detail frame does not resize to minimum space needed
        self.detail_frame.pack(side=tk.RIGHT)

        # Variables to keep track of grid positions
        self.curr_row = 0
        self.curr_col = 0

        # Create instance of DetailsStruct and retrieve labels & entries
        self.details_struct = DetailFrameValuesStruct(self.detail_frame, "Equipment")
        self.labels_to_add = self.details_struct.get_labels()
        self.add_labels()

        # Update grid positions to handle entries (to the right of the labels)
        self.update_grid_positions()

        self.entries_to_add = self.details_struct.get_entries()
        self.add_entries()

    # Function is called when switching from one screen to another (ex. Equipment to Employees)
    def refresh_detail_components(self, new_screen_type):
        self.clear_screen_components()
        self.details_struct.clear_component_lists()
        self.details_struct.set_screen_type(new_screen_type)
        self.refresh_grid_positions()
        self.refresh_labels()
        self.update_grid_positions()
        self.refresh_entries()

    def clear_screen_components(self):
        for label in self.labels_to_add:
            label.destroy()
        for entry in self.entries_to_add:
            entry.destroy()

    def refresh_grid_positions(self):
        self.curr_row = 0
        self.curr_col = 0

    def refresh_labels(self):
        self.labels_to_add = self.details_struct.get_labels()
        self.add_labels()

    def refresh_entries(self):
        self.entries_to_add = self.details_struct.get_entries()
        self.add_entries()

    def add_labels(self):
        for label in self.labels_to_add:
            label.grid(row=self.curr_row, column=self.curr_col)
            self.curr_row = self.curr_row + 1

    def update_grid_positions(self):
        self.curr_row = 0
        self.curr_col = 1

    def add_entries(self):
        for entry in self.entries_to_add:
            entry.grid(row=self.curr_row, column=self.curr_col)
            self.curr_row = self.curr_row + 1
        # self.update_entries()

    # Function used to update the details of a specific item when the corresponding row is clicked in the Treeview
    # NOTE: This function is called from the MCList class
    # args: item ID (such as equipment_id), passed from ID obtained from the MCList row-click
    def update_entries(self, id):

        self.clear_entries()    # first clear the entry boxes' texts
        # Find the data row that matches the row clicked in the treeview (based on ID), then update the details according
        # to that specific data row
        global current_data_rows
        row_to_use = []
        for row in current_data_rows:
            if row[ID_INDEX] == id:
                row_to_use = row

        # Insert that row's data into the entries
        for i in range(len(self.entries_to_add)):
            self.entries_to_add[i].insert(0, row_to_use[i])

    def clear_entries(self):
        for entry in self.entries_to_add:
            entry.delete(0, len(entry.get()))

    def get_current_entries(self):
        return self.entries_to_add

# Struct used to handle creating the appropriate Label & Entry objects based on indicated screen type
class DetailFrameValuesStruct:
    # NOTE: 'frame' will always be the detail frame
    # NOTE: 'screen_type' refers to a string indicating the screen in which labels & entries are needed
    def __init__(self, frame, screen_type):
        self.frame = frame
        self.screen_type = screen_type
        self.column_titles = None
        self.labels = []
        self.entries = []
        self.equipment_columns = ["equipment_id", "category", "status", "current_user_id", "date_purchased",
                                  "days_in_rotation", "cost", "user_first_name", "user_last_name", "department_id",
                                  "department"]
        self.employee_columns = ["employee_id", "first_name", "last_name", "email", "num_equipment_used", "department",
                                "phone_extension"]
        self.tickets_columns = ["ticket_number", "ticket_status", "client_id", "client_first_name", "client_last_name",
                                "equipment_id", "ticket_category", "short_description", "full_description", "issue_scope",
                                "priority", "department"]
        if self.screen_type == "Equipment":
            self.column_titles = self.equipment_columns
        elif self.screen_type == "Employee":
            self.column_titles = self.employee_columns
        elif self.screen_type == "Tickets":
            self.column_titles = self.tickets_columns

    def set_screen_type(self, screen_type):
        if screen_type == "Equipment":
            self.column_titles = self.equipment_columns
        elif screen_type == "Employee":
            self.column_titles = self.employee_columns
        elif screen_type == "Tickets":
            self.column_titles = self.tickets_columns

    def clear_component_lists(self):
        self.labels = []
        self.entries = []

    # This function will run and return ONLY the column titles specified by the list of indices (ex. those needed for the treeview).
    def get_specific_columns(self, column_indices_to_retrieve):
        column_ret_list = []
        for index in column_indices_to_retrieve:
            column_ret_list.append(self.column_titles[index])
        return column_ret_list

    def get_columns(self):
        return self.column_titles

    def get_labels(self):
        # Create appropriate Label objects
        for title in self.column_titles:
            new_label = Label(self.frame, text=title, font=("Montserrat", 14), width=25, borderwidth=2, relief='ridge', anchor='center', bg='#b5651d')
            self.labels.append(new_label)
        return self.labels

    # Create Entry objects based on number of columns to be displayed in Details Subframe
    def get_entries(self):
        for i in range(len(self.column_titles)):
            new_entry = Entry(self.frame, font=("Montserrat", 14), width=80, bg='#C4A484', borderwidth=2, relief='solid')
            # new_entry.insert(0, "test1231312215215512")
            self.entries.append(new_entry)
        return self.entries


# Struct used to handle obtaining the database values needed for the SearchFrame (NOT the DetailFrame)
class MCListValuesStruct:
    def __init__(self, screen_type):
        self.screen_type = screen_type
        self.data_tuple_list = []
    # Function to obtain the list of tuples of data to be shown in the SearchFrame (formatted appropriately)
    # args:     list of indices to retrieve from

    def get_tuple_list(self, indices):
        global current_data_rows
        print(current_data_rows)
        for row in current_data_rows:
            data_list = []
            for index in indices:
                data_list.append(row[index])
            curr_tuple = tuple(data_list)
            self.data_tuple_list.append(curr_tuple)
        return self.data_tuple_list


class SearchFrame(tk.Frame):
    def __init__(self, parent, controller, frames):
        tk.Frame.__init__(self, parent)
        self.config(width=10)
        global SCREEN_WIDTH, SCREEN_HEIGHT, coconut, gainsboro, stormcloud
        # Initializing GUI Controller
        self.controller = controller
        self.frames = frames
        self.search_grid = MCListDemo(self, controller, frames)

        # Default values to appear
        # NOTE: this index list will be used in both MCListValuesStruct AND DetailFrameValuesStruct
        self.column_indices_to_retrieve = [ID_INDEX, CATEGORY_INDEX, STATUS_INDEX, DAYS_IN_ROTATION_INDEX, COST_INDEX,
                                           DEPARTMENT_INDEX]
        self.MCList_values_struct = MCListValuesStruct("Equipment")
        self.data_tuples_list = self.MCList_values_struct.get_tuple_list(self.column_indices_to_retrieve)
        self.details_struct = DetailFrameValuesStruct(self.frames["DetailFrame"], "Equipment")
        # self.column_indices_to_retrieve = [ID_INDEX, CATEGORY_INDEX, DEPARTMENT_INDEX]
        self.column_titles = self.details_struct.get_specific_columns(self.column_indices_to_retrieve)
        self.search_grid.replace_contents(self.column_titles, self.data_tuples_list)


class MCListDemo(ttk.Frame):
    # class variable to track direction of column
    # header sort
    SortDir = True  # descending
    # def __init__(self, isapp=True, name='mclistdemo'):

    def __init__(self, parent, controller, frames, isapp=True, name='mclistdemo', columns=[], grid=[]):
        self.parent = parent
        self.controller = controller
        self.frames = frames
        self.name = name
        self.columns = columns
        self.grid=grid
        ttk.Frame.__init__(self, self.parent, name=self.name)
        self.config(width=10)
        self.pack(expand=Y )
        """, fill=BOTH"""
        self.isapp = isapp
        # test
        self.tree = None
        ##
        self._create_widgets(columns, grid)

    def _create_widgets(self, columns, grid):
        if self.isapp:
            SeeDismissPanel(self)

        self._create_demo_panel(columns, grid)

    def _set_data(self, data):
        self.data = data

    def replace_contents(self, columns=[], grid=[]):
        self.destroy()
        ttk.Frame.__init__(self, self.parent, name=self.name)
        self.pack(expand=Y, fill=BOTH)
        self._create_widgets(columns, grid)

    def _delete_tree(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

    def _create_demo_panel(self, columns, grid):
        demoPanel = Frame(self)
        demoPanel.pack(side=TOP, fill=BOTH, expand=Y)
        if not grid:
            return
        if not columns:
            if len(grid[0]) != len(self.columns):
                return
            columns = self.columns

        self._create_treeview(demoPanel, columns)
        self._load_data(grid)

    def _create_treeview(self, parent, columns):
        f = ttk.Frame(parent)
        f.pack(side=TOP, fill=BOTH, expand=Y)
        # create the tree and scrollbars
        self.dataCols = columns
        self.tree = ttk.Treeview(columns=self.dataCols,
                               show='headings', height=31)

        ysb = ttk.Scrollbar(orient=VERTICAL, command=self.tree.yview)
        xsb = ttk.Scrollbar(orient=HORIZONTAL, command=self.tree.xview)
        self.tree['yscroll'] = ysb.set
        self.tree['xscroll'] = xsb.set

        # add tree and scrollbars to frame
        self.tree.grid(in_=f, row=0, column=0, sticky=NSEW)
        ysb.grid(in_=f, row=0, column=1, sticky=NS)
        xsb.grid(in_=f, row=1, column=0, sticky=EW)

        # set frame resize priorities
        f.rowconfigure(0, weight=1)
        f.columnconfigure(0, weight=1)

    def _load_data(self, grid):
        self.data = grid
        if self.data:
            # configure column headings
            for c in self.dataCols:
                self.tree.heading(c, text=c.title(),
                                  command=lambda c=c: self._column_sort(c, MCListDemo.SortDir))
                self.tree.column(c, width=Font().measure(c.title()))

            # add data to the tree
            for item in self.data:
                self.tree.insert('', 'end', values=item)

            # and adjust column widths if necessary
            for idx, val in enumerate(item):
                width = Font().measure(val)
                if self.tree.column(self.dataCols[idx], 'width') < width:
                    self.tree.column(self.dataCols[idx], width=width)

            # Apply binding so that currently-selected values can be retrieved
            self.tree.bind('<<TreeviewSelect>>', self.obtain_selected_row)

    def _column_sort(self, col, descending=False):
        # grab values to sort as a list of tuples (column value, column id)
        # e.g. [('Argentina', 'I001'), ('Australia', 'I002'), ('Brazil', 'I003')]
        data = [(self.tree.set(child, col), child) for child in self.tree.get_children('')]

        # reorder data
        # tkinter looks after moving other items in
        # the same row
        data.sort(reverse=descending)
        for indx, item in enumerate(data):
            self.tree.move(item[1], '', indx)  # item[1] = item Identifier

        # reverse sort direction for next sort operation
        MCListDemo.SortDir = not descending

    # NOTE: Row is obtained as a dictionary in the following format:
    # {'text': '', 'image': '', 'values': [13, 'Monitor', 'Support'], 'open': 0, 'tags': ''}
    def obtain_selected_row(self, event):
        curr_item = self.tree.focus()
        curr_row = (self.tree.item(curr_item))      # Obtain row as dictionary
        self.controller.frames['MainPage'].data_frame.tool_bar.change_mode(1)
        list_of_values = curr_row.get('values')
        self.frames["DetailFrame"].update_entries(list_of_values[ID_INDEX])


if __name__ == "__main__":
    app = GUIController()
    app.bind("<Key>", app.key_pressed)
    app.mainloop()