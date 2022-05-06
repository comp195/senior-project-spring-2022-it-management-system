import os
import tkinter as tk
from fuzzywuzzy import fuzz as fz
from tkinter import *
from tkinter.font import Font
from tkinter import font as tkfont, ttk  # python 3
from copy import deepcopy
import tkinter.font as font

import table
import paramiko
from PIL import ImageTk, Image

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

# CONSTANT ONLY FOR TICKETS TABLE
IMAGE_INDEX = 12

global current_data_rows
global displayed_data_rows

coconut = "#9B582E"
quick_silver = "#A7A39E"
gainsboro = "#E0DDD9"
rajah = "#F5B15E"
stormcloud = "#4D646A"

global username_verify, password_verify, administrator


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
        self.window_title = "IT Management System"


        # Initializing container that stacks our frames


        container = tk.Frame(self, bg="#540A2F")

        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # Implementation of Root Tk() Configurations
        self.title(self.window_title)
        self['bg'] = stormcloud       # background color of ROOT

        # Initializing all of our frames within our container
        self.frames = {}
        self.edit_mode = True
        for F in (HelpPage, MainPage, LoginPage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            frame.config(bg=stormcloud)   # background color of individual frame
            self.frames[page_name] = frame

            # Putting all of our frames in the same place on the screen with the top one being active
            frame.grid(row=0, column=0)

        self.frames["MainPage"].config(bg="#540A2F")

        # Frame visible at the start of the application
        self.show_frame(self.active_frame)

    def key_pressed(self, event):
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
        global username_verify, password_verify, administrator
        username = str(username_verify.get())
        password = str(password_verify.get())
        login = table.dataTable("Login_Credentials")
        verified = login.password_check(username, password)
        if verified:
            active = login.check_active(username)
            if active:
                administrator = login.check_admin(username)
                self.show_frame("MainPage")
        # return verified
        return False

    def toggle_edit_mode(self):
        self.edit_mode = not self.edit_mode


class HelpPage(tk.Frame):
    def __init__(self, parent, controller):
        global username_verify, password_verify, stormcloud
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.controller = controller
        self.header = PageHeader(self, self.controller)
        self.header.pack()
        self.text6 = tk.Label(self,text="At the top the user is able to select which table they would like to view")
        self.text = tk.Label(self, text="The refresh button will update the row view area with the latest data from the database")
        self.text1 = tk.Label(self, text="The add row button allows users to add additional rows to a table")
        self.text2 = tk.Label(self, text="The update button allows users to modify the information in the selected row")
        self.text3 = tk.Label(self, text="The submit button finalizes the changes/additions")
        self.text4 = tk.Label(self, text="The cancel button will take the user out of the add/update mode")
        self.text5 = tk.Label(self, text="The remove button will remove the selected row from the table")
        text_list = [self.text6, self.text, self.text1, self.text2, self.text3, self.text4, self.text5]
        # self.text.pack()
        for i in text_list:
            i.place(x=0)
            i.pack(anchor="w")



class LoginPage(tk.Frame):
    def __init__(self, parent, controller):
        global username_verify, password_verify, stormcloud
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.controller = controller
        self.config(width=self.controller.winfo_reqwidth(), height=self.controller.winfo_reqheight(), bg=stormcloud)

        self.user_label = tk.Label(self, text="Username:", bg=stormcloud)
        self.user_label.pack()
        self.username_login_entry = tk.Entry(self, textvariable=username_verify).pack()
        self.space_label = tk.Label(self, text="", bg=stormcloud).pack()
        self.password_label = tk.Label(self, text="Password:" ,bg=stormcloud)
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
        self.credentials = [StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), StringVar()]

        self.registration_screen = Toplevel(self.controller)
        self.registration_screen.title("Register")
        self.registration_screen.config(bg=stormcloud)

        self.user_label = tk.Label(self.registration_screen, text="Username:", bg=stormcloud).pack()
        self.username_login_entry = tk.Entry(self.registration_screen, textvariable=self.credentials[0]).pack()
        self.register_space_label_0 = tk.Label(self.registration_screen, text="", bg=stormcloud).pack()
        self.register_email_label = tk.Label(self.registration_screen, text="Email:", bg=stormcloud).pack()
        self.register_email_login_entry = tk.Entry(self.registration_screen, textvariable=self.credentials[1]).pack()
        self.register_space_label_1 = tk.Label(self.registration_screen, text="", bg=stormcloud).pack()
        self.register_firstname_label = tk.Label(self.registration_screen, text="First Name", bg=stormcloud).pack()
        self.register_firstname_entry = tk.Entry(self.registration_screen, textvariable=self.credentials[2]).pack()
        self.register_space_label_2 = tk.Label(self.registration_screen, text="", bg=stormcloud).pack()
        self.register_lastname_label = tk.Label(self.registration_screen, text="Last Name", bg=stormcloud).pack()
        self.register_lastname_entry = tk.Entry(self.registration_screen, textvariable=self.credentials[3]).pack()
        self.register_space_label_3 = tk.Label(self.registration_screen, text="", bg=stormcloud)
        self.register_space_label_3.pack()
        self.register_password_label = tk.Label(self.registration_screen, text="Password:", bg=stormcloud)
        self.register_password_label.pack()
        self.register_password_login_entry = tk.Entry(self.registration_screen, textvariable=self.credentials[4], show='*')
        self.register_password_login_entry.pack()
        self.register_space_label_4 = Label(self.registration_screen, text=" ", fg="red", bg=stormcloud)
        self.register_space_label_4.pack()
        self.register_confirm_password_label = tk.Label(self.registration_screen, text="Confirm Password:", bg=stormcloud)
        self.register_confirm_password_label.pack()
        self.register_confirm_password_login_entry = tk.Entry(self.registration_screen, textvariable=self.credentials[5], show='*')
        self.register_confirm_password_login_entry.pack()
        self.register_space_label_5 = Label(self.registration_screen, text=" ", fg="red", bg=stormcloud)
        self.register_space_label_5.pack()

        self.registration_submit_button = tk.Button(self.registration_screen, text="Submit", width=10, height=1, command= self.registration_submit)
        self.registration_submit_button.pack()

    def registration_submit(self):
        success = True
        login = table.dataTable("Login_Credentials")
        employee = table.dataTable("Employee")

        # check if username exists
        if login.username_exists(self.credentials[0].get()):
            success = False
            self.register_space_label_5.config(text="Username exists")

        # check if email exists
        if employee.email_exists(self.credentials[1].get()):
            success = False
            self.register_space_label_5.config(text="Email exists")

        # check if email is valid format
        if not employee.valid_email(self.credentials[1].get()):
            success = False
            self.register_space_label_5.config(text="Invalid email format")

        if self.credentials[4].get() != self.credentials[5].get():
            success = False
            self.register_space_label_5.config(text="Password Mismatch")

        # check if first and last name are valid
        if not employee.valid_first_last_names(self.credentials[2].get(), self.credentials[3].get()):
            success = False
            self.register_space_label_5.config(text="Invalid name")

        if success is True:
            employee.insert_new_user(self.credentials[0].get(), self.credentials[1].get(), self.credentials[2].get(), self.credentials[3].get(),self.credentials[4].get())
            # employee.print_rows()
            # login.print_rows()
            self.registration_screen.destroy()


class PageHeader(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        global SCREEN_WIDTH, SCREEN_HEIGHT, coconut, quick_silver, gainsboro, stormcloud, username_verify, password_verify
        # Initializing GUI Controller
        self.controller = controller
        self.button_names = ["Equipment", "Employees", "Tickets", "Help", "Logout"]
        self.buttons = []
        self.button_dict = {}   # Maps button name to button index
        username_verify = StringVar()
        password_verify = StringVar()
        for i in range(len(self.button_names)):
            curr_button_name = self.button_names[i]
            # Temp conditions; change table names possibly
            if curr_button_name == "Employees":
                curr_button_name = "Employee"

            button = tk.Button(self, text=curr_button_name, command=lambda identifier=curr_button_name: self.press_button(identifier), bg="#540A2F",
                               fg=gainsboro, highlightthickness=0, bd=0)
            button.bind("<Enter>", highlight_button)
            button.bind("<Leave>", unhighlight_navigation_button)

            button.config(width=15, height=4, font=("Montserrat", 20))
            button.grid(row=0, column=i, sticky=W)
            self.buttons.append(button)
            self.button_dict[curr_button_name] = i
        self.buttons[0].config(fg=quick_silver)

    def press_button(self, identifier):
        for button in self.buttons:
            button.config(fg=gainsboro)
        self.buttons[self.button_dict.get(identifier)].config(fg=quick_silver)
        if identifier == "Logout":
            global username_verify, password_verify
            self.controller.show_frame("LoginPage")
            username_verify.set("")
            password_verify.set("")
            self.controller.frames["LoginPage"].user_label.config(text="")
            self.controller.frames["LoginPage"].password_label.config(text="")

        elif identifier == "Help":
            self.controller.show_frame("HelpPage")
        else:
            self.controller.show_frame("MainPage")
            self.controller.frames["MainPage"].update_on_button_press(identifier)


class DataFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.config(bg="#522B3F")
        # Initializing GUI Controller
        self.parent = parent
        self.update_mode = True
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

    def deselect_highlighted_rows(self):
        for selected_item in self.search_table.search_grid.tree.selection():
            self.search_table.search_grid.tree.selection_remove(selected_item)

    def add_row(self):
        self.old_row = []
        self.controller.frames['MainPage'].data_frame.detail_frame.input_editable()
        self.update_mode = False
        # Clear tkinter treeview selection
        self.deselect_highlighted_rows()
        # Clear detail entries
        self.detail_frame.clear_entries()
        self.controller.frames['MainPage'].data_frame.detail_frame.enable_editable()
        # Change toolbar
        self.tool_bar.change_mode(2)
        # Hide image-display button
        self.detail_frame.hide_image_button()

    def cancel_row(self):
        if not self.update_mode:
            self.detail_frame.clear_entries()
        else:
            self.detail_frame.details_struct.set_entry_strings(self.old_row)
        self.controller.frames['MainPage'].data_frame.detail_frame.disable_editable()
        self.tool_bar.change_mode(0)

    def update_database(self):
        self.update_mode = True
        self.old_row = self.detail_frame.details_struct.get_entry_strings()
        self.controller.frames['MainPage'].data_frame.detail_frame.enable_editable()
        self.tool_bar.change_mode(2)
        # Hide image-display button
        self.detail_frame.hide_image_button()

    def submit_data(self):
        global current_data_rows, displayed_data_rows
        displayed_data_rows = deepcopy(current_data_rows)
        self.tool_bar.change_mode(0)
        self.controller.frames['MainPage'].data_frame.detail_frame.disable_editable()
        current_data_rows = self.parent.equipment_table.get_rows()
        new_row = self.detail_frame.details_struct.get_entry_strings()
        row_id = new_row[0]
        test_row = deepcopy(new_row)
        test_row.pop(0)
        valid_row = self.parent.equipment_table.valid_input_row(test_row)
        print(test_row)
        # update existing row operation
        if self.update_mode and valid_row:
            # update current_data_rows
            for i in range(len(current_data_rows)):
                if current_data_rows[i][0] == row_id:
                    current_data_rows[i] = new_row

            # update database
            cols = self.parent.equipment_table.get_cols()
            # index_list = []
            columns_affected = []
            new_values = []
            for i in range(len(new_row)):
                if new_row[i] != self.old_row[i]:
                    # index_list.append(i)
                    columns_affected.append(cols[i])
                    new_values.append(new_row[i])
            self.parent.equipment_table.alter_row(columns_affected, new_values, cols[0], row_id)
            self.parent.equipment_table.commit()
            self.parent.equipment_table.print_rows()
            displayed_data_rows = deepcopy(current_data_rows)

            # update grid view
            column_list = self.parent.details_struct.get_specific_columns(self.parent.column_indices_to_retrieve)
            data_tuples_list = self.parent.MCList_values_struct.get_tuple_list(self.parent.column_indices_to_retrieve)
            self.parent.data_frame.search_table.search_grid.replace_contents(column_list, data_tuples_list)
        elif (not self.update_mode) and valid_row:
            # update current_data_rows
            for i in range(len(current_data_rows)):
                if current_data_rows[i][0] == row_id:
                    return
            current_data_rows.append(new_row)

            # update grid view
            column_list = self.parent.details_struct.get_specific_columns(self.parent.column_indices_to_retrieve)
            data_tuples_list = self.parent.MCList_values_struct.get_tuple_list(self.parent.column_indices_to_retrieve)
            self.parent.data_frame.search_table.search_grid.replace_contents(column_list, data_tuples_list)

            # update database
            new_row.pop(0)
            self.parent.equipment_table.insert_data(new_row)
            self.parent.equipment_table.print_rows()
            self.parent.equipment_table.commit()
            displayed_data_rows = deepcopy(current_data_rows)
        self.parent.search.clear_searchbar()
        self.refresh()

    def refresh(self):
        global current_data_rows, displayed_data_rows
        displayed_data_rows = current_data_rows
        current_data_rows = self.parent.equipment_table.get_rows()
        column_list = self.parent.details_struct.get_specific_columns(self.parent.column_indices_to_retrieve)
        data_tuples_list = self.parent.MCList_values_struct.get_tuple_list(self.parent.column_indices_to_retrieve)
        self.parent.data_frame.search_table.search_grid.replace_contents(column_list, data_tuples_list)
        self.parent.search.clear_searchbar()

    def remove_row(self):
        global current_data_rows, displayed_data_rows
        # get id of row to be removed
        row_id = self.detail_frame.details_struct.get_entry_strings()[0]
        # update current_data_rows
        for i in range(len(current_data_rows)):
            if current_data_rows[i][0] == row_id:
                current_data_rows.pop(i)
                break
        # TODO: Vincent, remove the row from and update the database
        column = self.parent.equipment_table.get_cols()[0]
        self.parent.equipment_table.delete_row(column, str(row_id))
        self.parent.equipment_table.commit()



        self.controller.frames['MainPage'].data_frame.detail_frame.enable_editable()
        self.detail_frame.clear_entries()
        self.controller.frames['MainPage'].data_frame.detail_frame.disable_editable()
        self.refresh()


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

        global current_data_rows, displayed_data_rows
        current_data_rows = self.equipment_table.get_rows()
        displayed_data_rows = deepcopy(current_data_rows)
        screen_name = "Equipment"

        # Child Frames
        self.search = SearchBarFrame(self, controller)
        self.search.pack(side=tk.TOP, anchor="w")
        self.data_frame = DataFrame(self, controller)
        self.data_frame.pack(side=tk.BOTTOM)

        # Grid View Data
        self.column_indices_to_retrieve = [ID_INDEX, 1, 2, 3, 4]
        self.MCList_values_struct = MCListValuesStruct(screen_name)
        self.data_tuples_list = self.MCList_values_struct.get_tuple_list(self.column_indices_to_retrieve)
        self.details_struct = DetailFrameValuesStruct(self.data_frame.frames["DetailFrame"], screen_name)
        self.column_titles = self.details_struct.get_specific_columns(self.column_indices_to_retrieve)

    def update_on_button_press(self, screen_name):
        self.equipment_table = table.dataTable(screen_name)
        # Update the global current_data_rows value based on the new table
        global current_data_rows, displayed_data_rows
        current_data_rows = self.equipment_table.get_rows()
        displayed_data_rows = deepcopy(current_data_rows)

        # Update the labels and entry boxes that appear based on the new table
        self.data_frame.detail_frame.refresh_detail_components(screen_name)

        self.column_indices_to_retrieve = [ID_INDEX, 1, 2, 3, 4]
        self.MCList_values_struct = MCListValuesStruct(screen_name)
        self.data_tuples_list = self.MCList_values_struct.get_tuple_list(self.column_indices_to_retrieve)
        self.details_struct = DetailFrameValuesStruct(self.data_frame.frames["DetailFrame"], screen_name)
        self.column_titles = self.details_struct.get_specific_columns(self.column_indices_to_retrieve)
        self.data_frame.search_table.search_grid.replace_contents(self.column_titles, self.data_tuples_list)
        self.controller.frames['MainPage'].data_frame.detail_frame.disable_editable()
        self.data_frame.tool_bar.change_mode(0)


class ToolBarFrame(tk.Frame):
    def __init__(self, parent, controller):
        global stormcloud
        tk.Frame.__init__(self, parent)
        # Initializing GUI Controller
        self.config(bg="#522B3F")
        self.controller = controller
        self.parent = parent
        self.change_mode(0)

    def change_mode(self, mode):
        global username_verify, password_verify, administrator
        if mode == 0:
            for i in range(len(self.winfo_children())-1, -1, -1):
                self.winfo_children()[i].destroy()
            self.refresh_button = tk.Button(self, text="Refresh", command=lambda: self.parent.refresh())
            self.refresh_button.grid(row=0, column=0)
            self.space_label_1 = tk.Label(self, width=1, bg="#522B3F")
            self.space_label_1.grid(row=0, column=1)
            self.add_button = tk.Button(self, text="Add Row", command=lambda: self.parent.add_row())
            self.add_button.grid(row=0, column=2)
            self.space_label_2 = tk.Label(self, width=1, bg="#522B3F")
            self.space_label_2.grid(row=0, column=3)

        elif mode == 1:
            for i in range(len(self.winfo_children())-1, -1, -1):
                self.winfo_children()[i].destroy()
            self.refresh_button = tk.Button(self, text="Refresh", command=lambda: self.parent.refresh())
            self.refresh_button.grid(row=0, column=0)
            self.space_label_1 = tk.Label(self, width=1, bg="#522B3F")
            self.space_label_1.grid(row=0, column=1)
            self.add_button = tk.Button(self, text="Add Row", command=lambda: self.parent.add_row())
            self.add_button.grid(row=0, column=2)
            self.space_label_2 = tk.Label(self, width=1, bg="#522B3F")
            self.space_label_2.grid(row=0, column=3)
            self.update_button = tk.Button(self, text="Update", command=lambda: self.parent.update_database())
            self.update_button.grid(row=0, column=4)
            self.space_label_3 = tk.Label(self, width=1, bg="#522B3F")
            self.space_label_3.grid(row=0, column=5)

            # REMOVE LOGIC PSEUDOCODE
            # TODO: Vincent, change the first two lines of the pseudocode to validate that the user who is logged in is an administrator
            # login_row = get_row(username_verify.get(), password_verify.get())
            # if login_row is administrator:
            if administrator:
               self.remove_button = tk.Button(self, text="Remove Row", command=lambda: self.parent.remove_row())
               self.remove_button.grid(row=0, column=6)

        elif mode == 2:
            for i in range(len(self.winfo_children())-1, -1, -1):
                self.winfo_children()[i].destroy()
            self.refresh_button = tk.Button(self, text="Refresh", command=lambda: self.parent.refresh())
            self.refresh_button.grid(row=0, column=0)
            self.space_label_1 = tk.Label(self, width=1, bg="#522B3F")
            self.space_label_1.grid(row=0, column=1)
            self.add_button = tk.Button(self, text="Submit", command=lambda: self.parent.submit_data())
            self.add_button.grid(row=0, column=2)
            self.space_label_2 = tk.Label(self, width=1, bg="#522B3F")
            self.space_label_2.grid(row=0, column=3)
            self.cancel_button = tk.Button(self, text="Cancel", command=lambda: self.parent.cancel_row())
            self.cancel_button.grid(row=0, column=4)
            self.space_label_3 = tk.Label(self, width=1, bg="#522B3F")
            self.space_label_3.grid(row=0, column=5)

            # REMOVE LOGIC PSEUDOCODE
            # TODO: Vincent, change the first two lines of the pseudocode to validate that the user who is logged in is an administrator
            # self.login_row = get_row(username_verify.get(), password_verify.get())
            # if login_row is administrator:
            if administrator:
               self.remove_button = tk.Button(self, text="Remove Row", command=lambda: self.parent.remove_row())
               self.remove_button.grid(row=0, column=6)


class SearchBarFrame(tk.Frame):
    def __init__(self, parent, controller):
        global stormcloud
        tk.Frame.__init__(self, parent)
        self.config(bg="#4E1220")
        # Initializing GUI Controller
        self.controller = controller
        self.parent = parent
        self.search_var = StringVar()
        self.search_text = ""
        self.search_bar = tk.Entry(self, highlightbackground="#363030", textvariable=self.search_var, highlightthickness=1,
                              width=258)
        self.search_bar.grid(row=0, column=0)

        self.search_space = tk.Label(self, width=1, bg="#280B12")
        self.search_space.grid(row=0, column=1)

        self.search_button = tk.Button(self, text="Search", command=lambda: self.search(), width=10)
        self.search_button.grid(row=0, column=2)

    def clear_searchbar(self):
        self.search_var.set("")

    def search(self):
        global current_data_rows, displayed_data_rows
        displayed_data_rows = []
        search_word = self.search_var.get()
        hits = 0
        for i in range(len(current_data_rows)):
            for j in range(len(current_data_rows[i])):
                ratio = fz.partial_ratio(str(search_word).lower(), str(current_data_rows[i][j]).lower())
                if ratio > 85:
                    hits += 1
                    displayed_data_rows.append(deepcopy(current_data_rows[i]))
                    continue
        print(displayed_data_rows)

        print("hits: " + str(hits))
        column_list = self.parent.details_struct.get_specific_columns(self.parent.column_indices_to_retrieve)
        data_tuples_list = self.parent.MCList_values_struct.get_limited_list(self.parent.column_indices_to_retrieve)
        self.parent.data_frame.search_table.search_grid.replace_contents(column_list, data_tuples_list)


class DetailFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        global SCREEN_WIDTH, SCREEN_HEIGHT, coconut, gainsboro, stormcloud

        # Initializing GUI Controller
        self.controller = controller
        #4E0717
        #280B12
        self.detail_frame = tk.Frame(self, bg="#522B3F", highlightbackground="#363030", highlightthickness=2, width=1200, height=670) #1300,670
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
        self.entry_labels = []
        self.entries_to_add = self.details_struct.get_entries()
        self.add_entries()
        self.editable = True
        self.disable_editable()

        # Variable to hold image path to be used in display
        self.image_path = ""

        # Button used to display image
        self.image_display_button = tk.Button(self.detail_frame, text="Show attached image", bg='#D84A6C', command=self.display_image) #9FAAEF
        self.image_display_button['font'] = font.Font(size=10, weight='bold')

    # Function is called when switching from one screen to another (ex. Equipment to Employees)
    def refresh_detail_components(self, new_screen_type):
        self.clear_screen_components()
        self.details_struct.clear_component_lists()
        self.details_struct.set_screen_type(new_screen_type)
        self.refresh_grid_positions()
        self.refresh_labels()
        self.update_grid_positions()
        self.refresh_entries()

        # Hide the image display button if active screen is NOT Tickets screen
        if self.details_struct.get_screen_type() != "Tickets":
            self.hide_image_button()

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

    def input_editable(self):
        for entry in self.entries_to_add:
            entry.config(state="normal")
        self.editable = True

    def enable_editable(self):
        self.entries_to_add[0].config(state="readonly")
        for entry in self.entries_to_add[1:]:
            entry.config(state="normal")
        self.editable = True

    def disable_editable(self):
        for entry in self.entries_to_add:
            entry.config(state="readonly")
        self.editable = False

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

    # Function used to update the details of a specific item when the corresponding row is clicked in the Treeview
    # NOTE: This function is called from the MCList class
    # args: item ID (such as equipment_id), passed from ID obtained from the MCList row-click
    def update_entries(self, id=-1):
        self.clear_entries()    # first clear the entry boxes' texts
        if id != -1:
            # Find the data row that matches the row clicked in the treeview (based on ID), then update the details according
            # to that specific data row
            global current_data_rows
            row_to_use = []
            for row in current_data_rows:
                if row[ID_INDEX] == id:
                    row_to_use = row

            # Insert that row's data into the entries
            for i in range(len(self.entries_to_add)):
                # Check if there is image display button should be shown
                # (if the "image" field of the Tickets table is NOT an empty string)
                if i == IMAGE_INDEX:
                    if self.details_struct.get_screen_type() == "Tickets":
                        if row_to_use[i] != "":
                            print("File name: " + row_to_use[i])
                            # Update the image path variable and set the button to a normal state
                            self.image_path = row_to_use[i]
                            self.image_display_button["state"] = "normal"
                        else:
                            print("No image file stored for this ticket...")
                            self.image_display_button["state"] = "disabled"
                self.entries_to_add[i].insert(0, row_to_use[i])

            # Show the image button if current screen is Tickets screen
            if self.details_struct.get_screen_type() == "Tickets":
                self.display_image_button()
            else:
                self.hide_image_button()


    def clear_entries(self):
        for entry in self.entries_to_add:
            entry.delete(0, len(entry.get()))

    def get_current_entries(self):
        return self.entries_to_add

    def display_image_button(self):
        self.image_display_button.tkraise()
        self.image_display_button.place(x=1014, y=335)

    def hide_image_button(self):
        self.image_display_button.place_forget()

    def display_image(self):
        print("this code will be run on button click")
        print("the current value for path is: " + self.image_path)

        source_path = "C:\\xampp\htdocs\dashboard\image_attachments\\" + self.image_path
        destination_path = os.getcwd() + "\\retrieved_image_files\\" + self.image_path

        # Retrieve connection details from file
        with open("conn_details.txt") as text_file:
            lines = text_file.read().splitlines()
        host = lines[0]
        username = lines[1]
        pw = lines[2]

        # Retrieve the file from EC2 instance to local folder
        transport = paramiko.Transport((host, 22))
        try:
            transport.connect(username=username, password=pw)
        except Exception as e:
            print(e)
            return False
        sftp = paramiko.SFTPClient.from_transport(transport)
        sftp.get(source_path, destination_path)
        sftp.close()
        print("IMAGE FILE RETRIEVED")

        # Now show the downloaded image
        image_window = Toplevel(self)
        image_window.title("Attached Image: " + self.image_path)
        downloaded_img = Image.open(destination_path)
        resized_img = downloaded_img.resize((1280,720), Image.ANTIALIAS)
        img_to_show = ImageTk.PhotoImage(resized_img)
        img_panel = Label(image_window, image=img_to_show)
        img_panel.image = img_to_show
        img_panel.pack()

# Struct used to handle creating the appropriate Label & Entry objects based on indicated screen type
class DetailFrameValuesStruct:
    # NOTE: 'frame' will always be the detail frame
    # NOTE: 'screen_type' refers to a string indicating the screen in which labels & entries are needed
    def __init__(self, frame, screen_type):
        self.frame = frame
        self.screen_type = screen_type
        self.column_titles = None
        self.entry_texts = []
        self.labels = []
        self.entries = []
        # self.equipment_columns = ["equipment_id", "category", "status", "current_user_id", "date_purchased",
        #                           "days_in_rotation", "cost", "user_first_name", "user_last_name", "department_id",
        #                           "department"]
        # self.employee_columns = ["employee_id", "first_name", "last_name", "email", "num_equipment_used", "department",
        #                         "phone_extension"]
        # self.tickets_columns = ["ticket_number", "ticket_status", "client_id", "client_first_name", "client_last_name",
        #                         "equipment_id", "ticket_category", "short_description", "full_description", "issue_scope",
        #                         "priority", "department", "image"]
        self.equipment_columns = ["Equipment ID", "Category", "Status", "Current User ID", "Date Purchased",
                                  "Days in Rotation", "Cost", "User First Name", "User Last Name", "Department ID",
                                  "Department"]
        self.employee_columns = ["Employee ID", "First Name", "Last Name", "Email", "Num. Equipment Used", "Department",
                                 "Phone Extension"]
        self.tickets_columns = ["Ticket Number", "Ticket Status", "Client ID", "Client First Name", "Client Last Name",
                                "Equipment ID", "Ticket Category", "Short Description", "Full Description",
                                "Issue Scope", "Priority", "Department", "Image"]

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
        self.screen_type = screen_type

    def get_screen_type(self):
        return self.screen_type

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
            new_label = Label(self.frame, text=title, font=("Montserrat", 14), width=25, borderwidth=2, relief='ridge', anchor='center', bg='#870524', fg=gainsboro)
            self.labels.append(new_label)
        return self.labels

    # Create Entry objects based on number of columns to be displayed in Details Subframe
    def get_entries(self):
        entry_texts = []
        for i in range(len(self.column_titles)):
            entry_texts.append(StringVar())
            new_entry = Entry(self.frame, font=("Montserrat", 14), width=80, bg='#C4A484', textvariable=entry_texts[i], borderwidth=2, relief='solid')
            # new_entry.insert(0, "test1231312215215512")
            self.entries.append(new_entry)
        self.entry_texts = entry_texts

        return self.entries

    def set_entry_strings(self, my_strings):
        print("my strings: " + str(len(my_strings)))
        print("entry texts: " + str(len(self.entry_texts)))
        if my_strings and self.entry_texts and len(my_strings) == len(self.entry_texts):
            for i in range(len(self.entry_texts)):
                self.entry_texts[i].set(my_strings[i])

    def get_entry_strings(self):
        return_strings = []
        for i in range(len(self.entry_texts)):
            return_strings.append(self.entry_texts[i].get())
        return return_strings


# Struct used to handle obtaining the database values needed for the SearchFrame (NOT the DetailFrame)
class MCListValuesStruct:
    def __init__(self, screen_type):
        self.screen_type = screen_type
        self.data_tuple_list = []
    # Function to obtain the list of tuples of data to be shown in the SearchFrame (formatted appropriately)
    # args:     list of indices to retrieve from

    def get_tuple_list(self, indices):
        global current_data_rows
        self.data_tuple_list = []
        for row in current_data_rows:
            data_list = []
            for index in indices:
                data_list.append(row[index])
            curr_tuple = tuple(data_list)
            self.data_tuple_list.append(curr_tuple)
        return self.data_tuple_list

    def get_limited_list(self, indices):
        global displayed_data_rows
        self.data_tuple_list = []
        for row in displayed_data_rows:
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

    def __init__(self, parent, controller, frames, isapp=True, name='mclistdemo', columns=None, grid=None):
        if columns is None:
            columns = []
        self.rowid = 0
        self.parent = parent
        self.controller = controller
        self.frames = frames
        self.name = name
        ttk.Frame.__init__(self, self.parent, name=self.name)
        self.config(width=10)
        self.pack(expand=Y)
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

    def replace_contents(self, columns=None, grid=None):
        self.destroy()
        ttk.Frame.__init__(self, self.parent, name=self.name)
        self.pack(expand=Y, fill=BOTH)
        if not columns:
            columns = self.dataCols
        self._create_widgets(columns, grid)

    def _delete_tree(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

    def _create_demo_panel(self, columns, grid):
        demoPanel = Frame(self)
        demoPanel.pack(side=TOP, fill=BOTH, expand=Y)

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
            item = None
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
        # NOTE: this is needed so that the entries are not re-populated after de-selection of highlighted row
        if not self.tree.selection():
            return

        self.controller.frames['MainPage'].data_frame.detail_frame.input_editable()

        curr_item = self.tree.focus()
        curr_row = (self.tree.item(curr_item))      # Obtain row as dictionary

        self.controller.frames['MainPage'].data_frame.tool_bar.change_mode(1)
        list_of_values = curr_row.get('values')
        self.frames["DetailFrame"].update_entries(list_of_values[ID_INDEX])
        self.controller.frames['MainPage'].data_frame.detail_frame.disable_editable()

def highlight_button(e):
    e.widget['background'] = "#8A1550"

def unhighlight_navigation_button(e):
    e.widget['background'] = "#540A2F"

if __name__ == "__main__":
    app = GUIController()
    app.bind("<Key>", app.key_pressed)
    app.mainloop()