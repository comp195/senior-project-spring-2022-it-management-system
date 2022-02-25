from playsound import playsound
import tkinter as tk
from tkinter import font  as tkfont # python 3
from re import *

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
        self['bg'] = 'green'

        # Initializing all of our frames within our container
        self.frames = {}
        for F in (PageHeader, MainMenuPage, EquipmentPage, EmployeePage, TicketPage, HelpPage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
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
