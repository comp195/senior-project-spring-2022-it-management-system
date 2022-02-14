from playsound import playsound
from tkinter import *
from re import *


class Ticket:
    def __init__(self, email, title, category, description):
        self.email = email
        self.title = title
        self.category = category
        self.description = description


class Ticket_Screen:
    def __init__(self):
        """===================================== CONFIGURATIONS ====================================="""

        self.window_title = "Window"
        self.resolution = "400x400"
        self.dropdown_options = ["Computer Issue",
                                 "Computer Upgrade",
                                 "VoIP Phone Configuration",
                                 "Equipment Request",
                                 "Other"]

        """===================================== GUI COMPONENTS ====================================="""

        # Window
        self.root = Tk()
        self.root.title(self.window_title)
        self.root.geometry(self.resolution)

        # Email Entry
        self.email_label = Label(self.root, width=20, text="Email")
        self.email_entry = Entry(self.root, width=50)
        self.invalid_email_label = Label(self.root, width=50, text="Please enter a valid email.", fg="red")

        # Ticket Title Entry
        self.title_label = Label(self.root, width=20, text="Title")
        self.ticket_title = Entry(self.root, width=50)

        # Ticket Category Dropdown
        self.category_label = Label(self.root, width=20, text="Category")
        self.dropdown_selection = StringVar(self.root)
        self.dropdown_selection.set(self.dropdown_options[0])
        self.ticket_dropdown = OptionMenu(self.root, self.dropdown_selection, self.dropdown_options[0], *self.dropdown_options[1:])

        # Ticket Description Box
        self.description_label = Label(self.root, width=20, text="Description")
        self.description_box = Entry(self.root, width=50)

        # Ticket Submission Button
        self.submission_button = Button(self.root, text="Submit", command=self.on_ticket_submission)

    def draw_screen(self):
        print("Put items on screen")
        self.email_label.pack()
        self.email_entry.pack()
        self.title_label.pack()
        self.ticket_title.pack()
        self.category_label.pack()
        self.ticket_dropdown.pack()
        self.description_label.pack()
        self.description_box.pack()
        self.submission_button.pack()

    def setMaxWidth(self, element):
        # f = tkFont.nametofont(element.cget("font"))
        # zerowidth = f.measure("0")
        # w = max([f.measure(i) for i in self.dropdown_options]) / zerowidth
        # element.config(width=w)
        print("Make it so that width of dropdown list is equal to longest element")

    def on_ticket_submission(self):

        email = self.email_entry.get()
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if not re.fullmatch(regex, email):
            self.invalid_email_label.pack()
            # Execute code to make invalid_email_label pop up and play error sound
            # playsound("[Error Noise]")
            print("Invalid Email Address")
            return
        self.invalid_email_label.destroy()
        self.submission_button['state'] = 'disabled'
        title = self.ticket_title.get()
        category = self.dropdown_selection.get()
        description = self.description_box.get()
        ticket = Ticket(email, title, category, description)

    def is_valid_email(self):
        print("Use Regex to validate email in correct format")


def main():
    ticket_screen = Ticket_Screen()
    ticket_screen.draw_screen()
    ticket_screen.root.mainloop()
    #Testing git


if __name__ == "__main__":
    main()