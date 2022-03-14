from playsound import playsound
import tkinter as tk
from tkinter import font  as tkfont # python 3
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
        # self.geometry(self.resolution)
        self['bg'] = stormcloud       # background color of ROOT

        # Initializing all of our frames within our container
        self.frames = {}
        for F in (PageHeader, MainMenuPage, EquipmentPage, EmployeePage, TicketPage, HelpPage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            # frame.config(bg=stormcloud)   # background color of individual frame
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

        # Assign MenuBar after it has been initialized
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
        # self.title_label = Label(self.equipment_mainframe, text="Equipment", font=('Rubik', 40, "bold"), bg=stormcloud, fg=gainsboro)\
        #     .place(x=65, y=30)
        #
        # # Subframe
        # self.equipment_subframe = tk.Frame(self.equipment_mainframe, bg=gainsboro, highlightbackground=coconut,
        #                                    highlightthickness=1, width=1920, height=955) \
        #     .place(x=0, y=500)
        #
        # # Add label and dropdown menu for selecting the equipment category
        # self.category_label = Label(self.equipment_subframe, text="Category", font=('Rubik', 13), bg="#ECA62D", fg="#363030")\
        #     .place(x=77, y=170)
        #
        # # Category Dropdown List
        # equipment_options = ['Desktop', 'Laptop', 'VoIP Phone', 'Monitor', 'Headset', 'Webcam']
        # self.dropdown_text = StringVar()
        # self.dropdown_text.set('Desktop')
        # self.category_menu = OptionMenu(self.equipment_mainframe, self.dropdown_text, *equipment_options, command=self.present_data)
        # self.category_menu.config(activebackground='#C4A484')
        # self.category_menu.place(x=70, y=195)
        #
        # # Search Bar
        # self.search_bar = Entry(self.equipment_mainframe, highlightbackground="#363030", highlightthickness=1,
        #                         width=258)\
        #     .place(x=170, y=200)
        #
        # # Search Button
        # self.search_button = Button(self.equipment_mainframe, text="Search", fg="#363030", width=15)\
        #     .place(x=1735, y=197)

#NOTE:  COMMENTED OUT AS THE TEXTBOX+SCROLLBAR MAY REPLACE THIS
        # Frame for Equipment Tabs
        # self.equipment_searchframe = tk.Frame(self.equipment_mainframe, bg="white", highlightbackground="#363030",
        #                                    highlightthickness=2, width=1780, height=680)\
        #     .place(x=70, y=250)

        # Add scrollbar & corresponding textbox
        # self.vertical_scrollbar = Scrollbar(self.equipment_mainframe, orient=VERTICAL)
        # self.vertical_scrollbar.pack(side=RIGHT, fill=BOTH)
        # # self.vertical_scrollbar.place(x=1000, y=200)
        #
        # self.text_box = Text(self.equipment_mainframe, width=224, height=40, wrap=NONE,
        #                      yscrollcommand=self.vertical_scrollbar.set, bg='orange')
        # for i in range(1000):
        #     self.text_box.insert(END, "sample text " + str(i) + "\n")
        # self.text_box.pack(side=TOP)#, expand=TRUE)
        # # self.text_box.place(x=72, y=250)
        # self.vertical_scrollbar.config(command=self.text_box.yview)

        # Create 'table' instance as part of equipment screen
        # NOTE: change table name of "Devices" to "Equipment" in db
        equipment_table = table.dataTable("Devices")
        equipment_data = ["1", "Monitor", "456", "Tom", "Jerry", "1", "Support", "365", "2021-03-12", "300.0"]
        equipment_table.insert_data(equipment_data)
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
        i = 0
        for device in cursor:
            print("Device: ")
            print(device)
            print("testing\n")
            for j in range(len(device)):
                entry = Entry(self, width=10, fg='red')
                entry.grid(row=i, column=j, sticky=W)
                entry.insert(END, device[j])
            i = i + 1



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


if __name__ == "__main__":
    app = GUIController()
    app.mainloop()
