import tkinter
import tkinter as tk
from tkinter import *
from tkinter.font import Font
from tkinter import font as tkfont, ttk  # python 3

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080

coconut = "#9B582E"
quick_silver = "#A7A39E"
gainsboro = "#E0DDD9"
rajah = "#F5B15E"
stormcloud = "#4D646A"


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
        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")
        self.window_title = "Application"
        # self.resolution = str(SCREEN_WIDTH) + "x" + str(SCREEN_HEIGHT)

        # Initializing container that stacks our frames
        header = PageHeader(parent=self, controller=self)
        header.pack(side="top", anchor="nw")
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # Implementation of Root Tk() Configurations
        self.title(self.window_title)
        #self.geometry(self.resolution)
        self['bg'] = stormcloud       # background color of ROOT


        # Initializing all of our frames within our container
        self.frames = {}

        for F in (MainPage, SearchBarFrame):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            frame.config(bg=stormcloud)   # background color of individual frame
            self.frames[page_name] = frame

            # Putting all of our frames in the same place on the screen with the top one being active
            frame.grid(row=0, column=0)

        # Frame visible at the start of the application
        self.show_frame("MainPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class PageHeader(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        global SCREEN_WIDTH, SCREEN_HEIGHT, coconut, quick_silver, gainsboro, stormcloud
        # Initializing GUI Controller
        self.controller = controller
        self.button_names = ["Equipment", "Employees", "Tickets", "Help"]
        self.buttons = []
        self.button_dict = {}   # Maps button name to button index
        for i in range(len(self.button_names)):
            curr_button_name = self.button_names[i]
            button = tk.Button(self, text=curr_button_name, command=lambda identifier=curr_button_name: self.press_button(identifier), bg=stormcloud,
                               fg=gainsboro, highlightthickness=0, bd=0)
            button.config(width=15, height=4, font=("Montserrat", 20))
            button.grid(row=0, column=i, sticky=W)
            self.buttons.append(button)
            self.button_dict[curr_button_name] = i
        # self.buttons[0].config(fg=quick_silver)

    def press_button(self, identifier):
        for button in self.buttons:
            button.config(fg=gainsboro)
        print(identifier)
        self.buttons[self.button_dict.get(identifier)].config(fg=quick_silver)

        # button_name = self.button_names[index]
        # page_name = button_name+"Page"
        # self.controller.show_frame(page_name)


class MainPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        # Initializing GUI Controller
        self.controller = controller
        self.search = SearchBarFrame(self, controller)
        self.search.pack(side=tk.TOP)
        self.search_table = SearchFrame(self, controller)
        self.search_table.pack(side=tk.LEFT)
        self.detail_frame = DetailFrame(self, controller)
        self.detail_frame.pack(side=tk.RIGHT)


class SearchBarFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        # Initializing GUI Controller
        self.controller = controller
        self.search_bar = tk.Entry(self, highlightbackground="#363030", highlightthickness=1,
                              width=258)
        self.search_bar.grid(row=0, column=0)

        self.search_space = tk.Label(self, width=10)
        self.search_space.grid(row=0, column=1)

        self.search_button = tk.Button(self, text="Search",
                                      command=lambda: self.search())
        self.search_button.grid(row=0, column=2)

    def search(self):
        return None


class DetailFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        global SCREEN_WIDTH, SCREEN_HEIGHT, coconut, gainsboro, stormcloud
        # Initializing GUI Controller
        self.controller = controller
        self.detail_frame = tk.Frame(self, bg="white", highlightbackground="#363030", highlightthickness=2, width=1300, height=670)
        self.detail_frame.pack(side=tk.RIGHT)


class SearchFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        global SCREEN_WIDTH, SCREEN_HEIGHT, coconut, gainsboro, stormcloud
        # Initializing GUI Controller
        self.controller = controller
        # TODO
        self.search_grid = MCListDemo(self)
        self.search_grid.pack()
        # self.search_grid.pack(side=tk.LEFT)


class MCListDemo(ttk.Frame):
    # class variable to track direction of column
    # header sort
    SortDir = True  # descending

    # def __init__(self, isapp=True, name='mclistdemo'):
    def __init__(self, parent, isapp=True, name='mclistdemo'):
        # ttk.Frame.__init__(self, name=name)
        ttk.Frame.__init__(self, parent, name=name)
        self.pack(expand=Y, fill=BOTH)
        # self.pack(side=tk.LEFT)
        self.isapp = isapp
        self._create_widgets()

    def _create_widgets(self):
        if self.isapp:
            SeeDismissPanel(self)

        self._create_demo_panel()

    def _create_demo_panel(self):
        demoPanel = Frame(self)
        demoPanel.pack(side=TOP, fill=BOTH, expand=Y)
        # demoPanel.pack(side=tk.LEFT)

        self._create_treeview(demoPanel)
        self._load_data()

    def _create_treeview(self, parent):
        f = ttk.Frame(parent)
        f.pack(side=TOP, fill=BOTH, expand=Y)
        # f.pack(side=tk.LEFT)

        # create the tree and scrollbars
        self.dataCols = ('country', 'capital', 'currency')
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

    def _load_data(self):
        self.data = [
            ("Argentina", "Buenos Aires", "ARS"),
            ("Australia", "Canberra", "AUD"),
            ("Brazil", "Brazilia", "BRL"),
            ("Canada", "Ottawa", "CAD"),
            ("China", "Beijing", "CNY"),
            ("France", "Paris", "EUR"),
            ("Germany", "Berlin", "EUR"),
            ("India", "New Delhi", "INR"),
            ("Italy", "Rome", "EUR"),
            ("Japan", "Tokyo", "JPY"),
            ("Mexico", "Mexico City", "MXN"),
            ("Russia", "Moscow", "RUB"),
            ("South Africa", "Pretoria", "ZAR"),
            ("United Kingdom", "London", "GBP"),
            ("United States", "Washington, D.C.", "USD")]

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

if __name__ == "__main__":
    app = GUIController()
    app.mainloop()