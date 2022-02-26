from playsound import playsound
import tkinter as tk
from tkinter import font  as tkfont # python 3
from tkinter import *   # for 'Button'
from re import *

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080

coconut = "#9B582E"
quick_silver = "A7A39E"
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
        self['bg'] = coconut       # background color of ROOT

        # Initializing all of our frames within our container
        self.frames = {}
        for F in (PageHeader, MainMenuPage, EquipmentPage, EmployeePage, TicketPage, HelpPage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            frame.config(bg=coconut)   # background color of individual frame
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
        self.title_label = Label(self.equipment_mainframe, text="EQUIPMENT", font=('Rubik', 40), bg=coconut, fg=stormcloud)\
            .place(x=65, y=30)

        # Subframe
        self.equipment_subframe = tk.Frame(self.equipment_mainframe, bg="#ECA62D", highlightbackground=rajah,
                                           highlightthickness=1, width=1920, height=955) \
            .place(x=0, y=125)

        # Add label and dropdown menu for selecting the equipment category
        self.category_label = Label(self.equipment_subframe, text="Category", font=('Rubik', 13), bg="#ECA62D", fg="#363030")\
            .place(x=77, y=170)

        # Category Dropdown List
        equipment_options = ['Desktop', 'Laptop', 'VoIP Phone', 'Monitor', 'Headset', 'Webcam']
        dropdown_text = StringVar()
        dropdown_text.set('Desktop')
        self.category_menu = OptionMenu(self.equipment_mainframe, dropdown_text, *equipment_options)
        self.category_menu.config(activebackground='#C4A484')
        self.category_menu.place(x=70, y=195)

        # Search Bar
        self.search_bar = Entry(self.equipment_mainframe, highlightbackground="#363030", highlightthickness=1,
                                width=258)\
            .place(x=170, y=200)

        # Search Button
        self.search_button = Button(self.equipment_mainframe, text="Search", fg="#363030", width=15)\
            .place(x=1735, y=197)


        # Frame for Equipment Tabs
        self.equipment_searchframe = tk.Frame(self.equipment_mainframe, bg="white", highlightbackground="#363030",
                                           highlightthickness=2, width=1780, height=680)\
            .place(x=70, y=250)


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
