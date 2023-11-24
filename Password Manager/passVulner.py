# Importing the required libraires
from tkinter import *

# Class vulerability to find the password_get is vulerable or not
class Vulnerability:
    def __init__(self, mainwindow):
        # Adding the top level window
        self.topwidgit_ni = Toplevel(mainwindow)

        # Adding the features of the top level window
        self.topwidgit_ni.title("New Item")
        self.topwidgit_ni.geometry("600x500")
        self.topwidgit_ni.config(background='#36454f')
        self.topwidgit_ni.resizable(False, False)

        # Adding the frame to the window
        self.frame = Frame(self.topwidgit_ni, bg='white')
        self.frame.place(x=30, y=30, width=500, height=400)

        # Adding a label to the frame
        self.info_label = Label(self.frame, bg='white', font=("Arial", 9))

        # Adding the password_get text
        password_get_text = Label(self.frame, fg='black', bg='white', text='Enter your password_get', font=("Arial", 13))
        password_get_text.place(x=20, y=50)

        # Adding the password_get input box
        self.password_get_input = Entry(self.frame, fg='black', bg='white', font=("Arial",11), width=40, borderwidth=0, show="*")
        self.password_get_input.place(x=19, y=90)

        # Adding the check button
        check_button = Button(self.frame,
                              fg='white',
                              bg='#36454f',
                              activebackground = '#36454f',
                              activeforeground = 'white',
                              text='check',
                              width = 4,
                              height = 1,
                              font=("Arial", 10),
                              command = self.check,
                              cursor = 'hand2'
                              )
        check_button.place(x=360, y=120)

    # Creating the function to check the password_get strength
    def check(self):
        # Getting the inputed password_get
        password_get = self.password_get_input.get()
        special_char = "!@#$%^&*()_+/*<>,.:;?/{}[]~`"
        self.lowercase = False
        self.uppercase = False
        self.number = False
        self.special = False
        self.common_pass = True

        for i in password_get:
            if i.islower():
                self.lowercase = True
            if i.isupper():
                self.uppercase = True
            if i.isdigit():
                self.number = True
            for j in special_char:
                if i in j:
                    self.special = True

        with open('common_password.txt', 'r') as file:
            common_passwords = file.read().splitlines()

        for cp in common_passwords:
            if cp == password_get:
                self.common_pass = False
                break  # No need to continue checking once a match is found

        # Fucnction call
        self.status()

    # Function to check the status
    def status(self):
        if (self.common_pass==True and self.lowercase==True and self.uppercase==True and self.number==True and self.special==True):
            self.info_label.config(text='Your password is strong', fg='green')
        else:
            self.info_label.config(text='Your password is not strong', fg='red')
        self.info_label.place(x=40, y=120)

