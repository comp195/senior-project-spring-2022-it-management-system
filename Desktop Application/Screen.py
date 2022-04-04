from playsound import playsound
from fuzzywuzzy import fuzz
import tkinter as tk
from tkinter import font as tkfont # python 3
from tkinter import *   # for 'Button'
# from re import *
import table

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080

coconut = "#9B582E"
quick_silver = "#A7A39E"
gainsboro = "#E0DDD9"
rajah = "#F5B15E"
stormcloud = "#4D646A"


class GUIController(tk.Tk):

    def __init__(self, *args, **kwargs):
        global SCREEN_WIDTH, SCREEN_HEIGHT, coconut, gainsboro, stormcloud
        tk.Tk.__init__(self, *args, **kwargs)

        # Basic Configuration Values for Root Tk()
        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")
        self.window_title = "Application"
        self.resolution = str(SCREEN_WIDTH) + "x" + str(SCREEN_HEIGHT)

        # Initializing container that stacks our frames
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # Implementation of Root Tk() Configurations
        self.title(self.window_title)
        self.geometry(self.resolution)
        self['bg'] = stormcloud       # background color of ROOT

        # Initializing all of our frames within our container
        self.frames = {}
        for F in (PageHeader, MainMenuPage, EquipmentPage, EmployeePage, TicketPage, HelpPage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            frame.config(bg=stormcloud)   # background color of individual frame
            self.frames[page_name] = frame

            # Putting all of our frames in the same place on the screen with the top one being active
            frame.grid(row=0, column=0, sticky="nsew")

        # Frame visible at the start of the application
        self.show_frame("PageHeader")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class PageHeader(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        global SCREEN_WIDTH, SCREEN_HEIGHT, coconut, gainsboro, stormcloud
        # Initializing GUI Controller
        self.controller = controller

        # Setting Up the MenuBar
        self.menubar = tk.Menu(master=controller)
        self.menubar.add_command(label="Main Menu", command=lambda: self.controller.show_frame("MainMenuPage"))
        self.menubar.add_command(label="Equipment", command=lambda: self.controller.show_frame("EquipmentPage"))
        self.menubar.add_command(label="Employees", command=lambda: self.controller.show_frame("EmployeePage"))
        self.menubar.add_command(label="Tickets", command=lambda: self.controller.show_frame("TicketPage"))
        self.menubar.add_command(label="Help", command=lambda: self.controller.show_frame("HelpPage"))

        # Assign MenuBhttps://github.com/comp195/senior-project-spring-2022-it-management-system/wiki/Snapshot-1ar after it has been initialized
        self.controller.config(menu=self.menubar)


class MainMenuPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        global SCREEN_WIDTH, SCREEN_HEIGHT, coconut, gainsboro, stormcloud
        # Initializing GUI Controller
        self.controller = controller


class EquipmentPage(tk.Frame):
    def __init__(self, parent, controller):
        self.equipment_mainframe = tk.Frame.__init__(self, parent)
        global SCREEN_WIDTH, SCREEN_HEIGHT, coconut, gainsboro, stormcloud
        # Initializing GUI Controller
        self.controller = controller

        # Initialize font for button use
        button_font = tkfont.Font(size=30, weight='bold')

        # Create the Equipment screen title label
        self.title_label = Label(self.equipment_mainframe, text="Equipment", font=('Rubik', 40, "bold"), bg=stormcloud, fg=gainsboro)\
            .place(x=65, y=30)

        # Subframe
        self.equipment_subframe = tk.Frame(self.equipment_mainframe, bg=gainsboro, highlightbackground=coconut,
                                           highlightthickness=1, width=1920, height=1000) \
            .place(x=0, y=100)

        # Add label and dropdown menu for selecting the equipment category
        self.category_label = Label(self.equipment_mainframe, text="Category", font=('Rubik', 13), bg="#ECA62D", fg="#363030")\
            .place(x=77, y=170)

        # Category Dropdown List
        equipment_options = ['Desktop', 'Laptop', 'VoIP Phone', 'Monitor', 'Headset', 'Webcam']
        self.dropdown_text = StringVar()
        self.dropdown_text.set('Desktop')
        self.category_menu = OptionMenu(self.equipment_mainframe, self.dropdown_text, *equipment_options, command=self.present_data)
        self.category_menu.config(activebackground='#C4A484')
        self.category_menu.place(x=70, y=195)

        # Search Bar
        self.search_bar = Entry(self.equipment_mainframe, highlightbackground="#363030", highlightthickness=1,
                                width=258)\
            .place(x=170, y=200)

        # Search Button
        self.search_button = Button(self.equipment_mainframe, text="Search", fg="#363030", width=15)\
            .place(x=1735, y=197)

#NOTE:  COMMENTED OUT AS THE TEXTBOX+SCROLLBAR MAY REPLACE THIS
        # Frame for Equipment Tabs
        self.equipment_searchframe = tk.Frame(self.equipment_mainframe, bg="white", highlightbackground="#363030",
                                           highlightthickness=2, width=960, height=655)\
            .place(x=70, y=250)
        equipment_table = table.dataTable("Devices")
        equipment_data = ["1", "Monitor", "456", "Tom", "Jerry", "1", "Support", "365", "2021-03-12", "300.0"]
        equipment_data2 = ["2", "Laptop", "456", "A", "V", "1", "Support", "365", "2021-06-06", "200.0"]
        equipment_table.insert_data(equipment_data)
        equipment_table.insert_data(equipment_data2)

        next_id = 3
        for i in range(14):
            equipment_data = [next_id] + ["Monitor", "456", "Tom", "Jerry", "1", "Support", "365", "2021-03-12", "300.0"]
            next_id = next_id + 1
            equipment_data2 = [next_id] + ["Laptop", "456", "A", "V", "1", "Support", "365", "2021-06-06", "200.0"]
            next_id = next_id + 1
            equipment_table.insert_data(equipment_data)
            equipment_table.insert_data(equipment_data2)
        list_of_equipment_rows = equipment_table.get_rows()
        # print(list_of_equipment_rows)
        # print()
        # parsed_equipment_row = equipment_table.obtain_parsed_equipment_row(list_of_equipment_rows[0])
        # print(parsed_equipment_row)
        # self.text_box.insert('1.0', "\n")
        # self.text_box.insert('1.0', parsed_equipment_row)
        # Text widget insert index notation: 'line.column'

        cursor = equipment_table.get_cursor()
        cursor.execute("SELECT * FROM Devices")
        # i = 0

        # Add column headers for data display

        id_label = Label(self.equipment_mainframe, text="device_id", borderwidth=2, relief='ridge', anchor='center', bg='#b5651d', width=12)
        category_label = Label(self.equipment_mainframe, text="category", borderwidth=2, relief='ridge', anchor='center', bg='#b5651d', width=12)
        user_id_label = Label(self.equipment_mainframe, text="current_user_id", borderwidth=2, relief='ridge', anchor='center', bg='#b5651d', width=13)
        first_name_label = Label(self.equipment_mainframe, text="user_first_name", borderwidth=2, relief='ridge', anchor='center', bg='#b5651d', width=13)
        last_name_label = Label(self.equipment_mainframe, text="user_last_name", borderwidth=2, relief='ridge', anchor='center', bg='#b5651d', width=13)
        department_id_label = Label(self.equipment_mainframe, text="department_id", borderwidth=2, relief='ridge', anchor='center', bg='#b5651d', width=12)
        department_label = Label(self.equipment_mainframe, text="department", borderwidth=2, relief='ridge', anchor='center', bg='#b5651d', width=12)
        days_since_purchase_label = Label(self.equipment_mainframe, text="days_since_purchase", borderwidth=2, relief='ridge', anchor='center', bg='#b5651d', width=17)
        purchase_date_label = Label(self.equipment_mainframe, text="purchase_date", borderwidth=2, relief='ridge', anchor='center', bg='#b5651d', width=12)
        cost_label = Label(self.equipment_mainframe, text="cost", borderwidth=2, relief='ridge', anchor='center', bg='#b5651d', width=12)

        labels = ColumnLabels(self.equipment_mainframe, self)

        # Need to store x-coordinate for starting positions of data values in table
        x_positions = []
        starting_x = 72
        starting_y = 252
        curr_x = starting_x
        curr_y = starting_y
        x_positions.append(curr_x)

        for i in range(len(labels.labels)):
            labels.labels[i].place(x=starting_x, y=starting_y)
            self.update()
            curr_x = curr_x + id_label.winfo_width()
            x_positions.append(curr_x)

        # id_label.place(x=starting_x, y=starting_y)
        # self.update()
        # curr_x = curr_x + id_label.winfo_width()
        # x_positions.append(curr_x)
        #
        # category_label.place(x=curr_x, y=starting_y)
        # self.update()
        # curr_x = curr_x + category_label.winfo_width()
        # x_positions.append(curr_x)
        #
        # user_id_label.place(x=curr_x, y=starting_y)
        # self.update()
        # curr_x = curr_x + user_id_label.winfo_width()
        # x_positions.append(curr_x)
        #
        # first_name_label.place(x=curr_x, y=starting_y)
        # self.update()
        # curr_x = curr_x + first_name_label.winfo_width()
        # x_positions.append(curr_x)
        #
        # last_name_label.place(x=curr_x, y=starting_y)
        # self.update()
        # curr_x = curr_x + last_name_label.winfo_width()
        # x_positions.append(curr_x)
        #
        # department_id_label.place(x=curr_x, y=starting_y)
        # self.update()
        # curr_x = curr_x + department_id_label.winfo_width()
        # x_positions.append(curr_x)
        #
        # department_label.place(x=curr_x, y=starting_y)
        # self.update()
        # curr_x = curr_x + department_label.winfo_width()
        # x_positions.append(curr_x)
        #
        # days_since_purchase_label.place(x=curr_x, y=starting_y)
        # self.update()
        # curr_x = curr_x + days_since_purchase_label.winfo_width()
        # x_positions.append(curr_x)
        #
        # purchase_date_label.place(x=curr_x, y=starting_y)
        # self.update()
        # curr_x = curr_x + purchase_date_label.winfo_width()
        # x_positions.append(curr_x)
        #
        # cost_label.place(x=curr_x, y=starting_y)
        # self.update()
        # curr_x = curr_x + cost_label.winfo_width()

        for device in cursor:
            x_iterator = 0
            curr_y = curr_y + cost_label.winfo_height()
            print("Device: ")
            print(device)
            for j in range(len(device)):
                my_width = 14
                if j == 7:
                    my_width = 20

                entry = Entry(self.equipment_mainframe, width=my_width, fg='red', justify=CENTER)
                # entry.grid(row=i, column=j, sticky=W)
                entry.place(x=x_positions[x_iterator], y=curr_y)
                x_iterator = x_iterator + 1
                entry.insert(END, device[j])


    # Function to pull data from database based on category selection & show results on screen
    def present_data(self, category):
        category = self.get_category_selection()
        print('Return value from helper method: ' + category)
        # NOTE: use 'category' as value for retrieving data from database then show on screen here
        #       (assign returned value of retrieve_data() to a variable)
        self.retrieve_data(category)

    # Function to obtain the currently-selected option in the 'Categories' dropdown menu
    def get_category_selection(self):
        selection = self.dropdown_text.get()
        print(selection)
        return selection

    # Function to pull data from database
    # Parameter: category is used to determine which section of database to pull data from
    def retrieve_data(self, category):
        print()
        # NOTE: return proper structs here


class EmployeePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        global SCREEN_WIDTH, SCREEN_HEIGHT, coconut, gainsboro, stormcloud
        # Initializing GUI Controller
        self.controller = controller


class TicketPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        global SCREEN_WIDTH, SCREEN_HEIGHT, coconut, gainsboro, stormcloud
        # Initializing GUI Controller
        self.controller = controller


class HelpPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        global SCREEN_WIDTH, SCREEN_HEIGHT, coconut, gainsboro, stormcloud
        # Initializing GUI Controller
        self.controller = controller


class ColumnLabels:
    def __init__(self, frame=None, page=None):
        self.frame = frame
        self.titles = self.get_headers(page)
        self.labels = []

        for i in range(len(self.titles)):
            self.labels.append(Label(self.frame, text=self.titles[i], borderwidth=2, relief='ridge', anchor='center', bg='#b5651d', width=12))

    def get_headers(self, page):
        if isinstance(page, EquipmentPage):
            columns = ["device_id", "category", "current_user_id", "user_first_name", "user_last_name", "department_id", "department", "days_since_purchase", "purchase_date", "cost"]
        elif isinstance(page, EmployeePage):
            columns = []
        elif isinstance(page, TicketPage):
            columns = []
        else:
            columns = []
        return columns


if __name__ == "__main__":
    app = GUIController()
    app.mainloop()
