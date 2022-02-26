from playsound import playsound
import tkinter as tk
from tkinter import font  as tkfont # python 3
from tkinter import *   # for 'Button'
from re import *

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080

class GUIController(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # Basic Configuration Values for Root Tk()
        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")
        self.window_title = "Application"
        self.resolution = "1920x1080"

        # Initializing container that stacks our frames
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # Implementation of Root Tk() Configurations
        self.title(self.window_title)
        self.geometry(self.resolution)
        self['bg'] = 'orange'       # background color of ROOT

        # Initializing all of our frames within our container
        self.frames = {}
        for F in (PageHeader, MainMenuPage, EquipmentPage, EmployeePage, TicketPage, HelpPage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            frame.config(bg='orange')   # background color of individual frame
            self.frames[page_name] = frame

            # Putting all of our frames in the same place on the screen with the top one being active
            frame.grid(row=0, column=0, sticky="nsew")

        # Frame visible at the start of the application
        self.show_frame("PageHeader")

        # Initialize font for button use
        button_font = font.Font(size=30, weight='bold')

        # Create the Equipment screen title label
        Label(self, text="EQUIPMENT", font=('Lucida', 40, 'bold'), bg='orange').place(x=820, y=0)

        # Add label and dropdown menu for selecting the equipment category
        Label(self, text="Equipment Category", font=60, bg='orange').place(x=50, y=170)
        equipment_options = ['Desktop', 'Laptop', 'VoIP Phone', 'Monitor', 'Headset', 'Webcam']
        dropdown_text = StringVar()
        dropdown_text.set('Desktop')
        dropdown_menu = OptionMenu(self, dropdown_text, *equipment_options)
        dropdown_menu.config(activebackground='#C4A484')
        dropdown_menu.place(x=75, y=200)

        # Add exit button
        # USE COMMAND= TO CALL FUNCTION
        Button(self, text="EXIT", font=button_font, bg='red', activebackground='pink',
               command=self.destroy).place(x=0, y=1000)
    
    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class PageHeader(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

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

        # Initializing GUI Controller
        self.controller = controller


class EquipmentPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Initializing GUI Controller
        self.controller = controller


class EmployeePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Initializing GUI Controller
        self.controller = controller


class TicketPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Initializing GUI Controller
        self.controller = controller


class HelpPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Initializing GUI Controller
        self.controller = controller


if __name__ == "__main__":
    app = GUIController()
    app.mainloop()
