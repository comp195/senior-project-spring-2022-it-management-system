from tkinter import *
from re import *


class Ticket_Screen:
    def __init__(self):
        self.root = Tk()
        self.email_entry = Entry(self.root, width=50)
        self.ticket_title = Entry(self.root, width=50)
        # self.ticket_dropdown = OptionMenu(self.root)
        self.description_box = Entry(self.root, width=50)
        self.submission_button = Button(self.root, text="Submit", command=self.on_ticket_submission)

    def on_ticket_submission(self):
        print("Perform Ticket Operations")

    def is_valid_email(self):
        print("Use Regex to validate email in correct format")


def main():
    ticket_screen = Ticket_Screen()
    ticket_screen.root.mainloop()


if __name__ == "__main__":
    main()