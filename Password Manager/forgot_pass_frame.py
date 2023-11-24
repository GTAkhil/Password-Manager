# Importing the required libraries
from tkinter import *
from mac import GetMac
from otp import VerifyOTP
from database import Database
import time

# Class to forgot password hyperlink
class ForgotPassword:
    def __init__(self, mainwindow): # Runs the class when an instance of the class is created
        # Global variables
        self.mainwindow = mainwindow
        self.database_obj = Database()
        self.fpf = Frame(self.mainwindow)
        self.canva = Canvas(self.fpf, width=1000, height=550, bg='#ebecf0')

        # phone number entry box
        self.email_input_box = Entry(self.fpf, bg='white', fg='black', font=('Arial', 11), borderwidth=0, width=43)
        self.email_input_box.place(x=245, y=200)

         # Features
        self.fpf.config(background='#d3d3d3')
        self.canva.place(x=20, y=20)
        self.fpf.place(x=100, y=50, width=1050, height=600)

        # Function calls
        self.fpLabels()


    # Function to add the labels to the forgot password frame
    def fpLabels(self):

        # Email text
        self.fp_labels = Label(self.fpf, text='Verify your email id', bg='#ebecf0', fg='black', font=("Arial", 13))
        self.fp_labels.place(x=255, y=160)

        # verify hyperlink in forgot password frame
        self.fp_verify = Label(self.fpf, text='verify >', fg="#000040", bg='#ebecf0', font = ("bold", 11), cursor='hand2')
        self.fp_verify.place(x=605, y=230)
        self.fp_verify.bind("<Button-1>", self.verifyButtonPressed)

        # Back to login page hyperlink in forgot password frame
        self.fp_back_to_login= Label(self.fpf, text='< Go back', fg="#000040", bg='#ebecf0', font = ("italic", 10), cursor='hand2')
        self.fp_back_to_login.place(x=250, y=230)
        self.fp_back_to_login.bind("<Button-1>", self.backToLoginFrame)

        # Verified email information
        self.information_email_text = Label(self.fpf, fg="red", bg='#ebecf0', font = ("italic", 10))


    # If verify button pressed
    def verifyButtonPressed(self, event):
        mac_address = GetMac.get_mac_address()
        email = self.email_input_box.get()
        sql_querry = "select Email from login where Mac=%s"
        # Getting the registered email
        self.database_obj.cursor.execute(sql_querry, (mac_address, ))
        db_email = self.database_obj.cursor.fetchone()

        try:
            # Checking if the email is not none
            if email != "" and db_email is not None:
                # Checking if the email is equal to the db_email
                if email == db_email[0]:
                    VerifyOTP(self.mainwindow, email)
                    time.sleep(1)
                    self.fpf.destroy()

                else:
                    self.information_email_text.config(text="Email id doesn't match")
            else:
                self.information_email_text.config(text="Please provide registered Email id")
            self.information_email_text.place(x=680, y=200)

        # if any error occurs
        except Exception as e:
            print(e)

    # If user want to go back to login frame
    def backToLoginFrame(self, event):
        self.fpf.destroy()
        from login_frame import Login
        Login(self.mainwindow)















