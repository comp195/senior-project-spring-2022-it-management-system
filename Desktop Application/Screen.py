from playsound import playsound
from tkinter import *
from re import *


class Ticket_Screen:
    def __init__(self):
        """===================================== CONFIGURATIONS ====================================="""

        self.window_title = "Window"
        self.resolution = "400x400"

        """===================================== GUI COMPONENTS ====================================="""

        self.root = Tk()
        self.root.title(self.window_title)
        self.root.geometry(self.resolution)
        self.email_entry = Entry(self.root, width=50)
        self.invalid_email_label = Label(self.root, width=50)
        self.ticket_title = Entry(self.root, width=50)
        # self.ticket_dropdown = OptionMenu(self.root)
        self.description_box = Entry(self.root, width=50)
        self.submission_button = Button(self.root, text="Submit", command=self.on_ticket_submission)

    def draw_screen(self):
        print("Put items on screen")

    def on_ticket_submission(self):
        email = self.email_entry.get()
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if not re.fullmatch(regex, email):
            # Execute code to make invalid_email_label pop up and play error sound
            # playsound("[Error Noise]")
            print("Invalid Email Address")



        print("Perform Ticket Operations")

    def is_valid_email(self):
        print("Use Regex to validate email in correct format")


def main():
    ticket_screen = Ticket_Screen()
    ticket_screen.root.mainloop()
    #Testing git

if __name__ == "__main__":
    main()