# Importing the required libraries
from tkinter import *
import random
from send_otp import SendOTP
from change_password import ChangePassword

# Class to forgot password hyperlink
class VerifyOTP:
    def __init__(self, mainwindow, email): # Runs the class when an instance of the class is created
        # Global variables
        self.mainwindow = mainwindow
        self.vOTP = Frame(self.mainwindow)
        self.email = email
        self.canva = Canvas(self.vOTP, width=1000, height=550, bg='#ebecf0')
        self.otp = random.randint(100000, 200000)
        print(self.otp)

        # Verified otp information
        self.information_otp_text = Label(self.vOTP, fg="red", bg='#ebecf0', font = ("italic", 10))

        # otp entry box
        self.otp_input_box = Entry(self.vOTP, bg='white', fg='black', font=('Arial', 11), borderwidth=0, width=43)
        self.otp_input_box.place(x=245, y=200)

         # Features
        self.vOTP.config(background='#d3d3d3')
        self.canva.place(x=20, y=20)
        self.vOTP.place(x=100, y=50, width=1050, height=600)

        # Function calls
        self.voLabels()
        SendOTP.send_email(self.email, self.otp)

    # Function to add the labels to the forgot password frame
    def voLabels(self):

        # Verify OTP, send to your email id text
        self.vo_labels = Label(self.vOTP, text='Verify OTP, send to your email id', bg='#ebecf0', fg='black', font=("Arial", 13))
        self.vo_labels.place(x=250, y=160)

        # Edit email id
        self.vo_edit = Label(self.vOTP, text='Edit email id',  fg="#000040", bg='#ebecf0', font = ("bold", 11), cursor='hand2')
        self.vo_edit.place(x=400, y=250)
        self.vo_edit.bind("<Button-1>", self.editEmailPressed)

        # verify otp hyperlink in forgot password frame
        self.vo_verify = Label(self.vOTP, text='verify otp >', fg="#000040", bg='#ebecf0', font = ("bold", 11), cursor='hand2')
        self.vo_verify.place(x=600, y=250)
        self.vo_verify.bind("<Button-1>", self.verifyOTPPressed)

        # Back to login page hyperlink in forgot password frame
        self.vo_back_to_login= Label(self.vOTP, text='< Go back', fg="#000040", bg='#ebecf0', font = ("italic", 10), cursor='hand2')
        self.vo_back_to_login.place(x=250, y=250)
        self.vo_back_to_login.bind("<Button-1>", self.backToLoginFrame)

        # Resend otp hyperlink
        self.resend_otp = Label(self.vOTP, text='Resend OTP', fg="#000040", bg='#ebecf0', font = ("bold", 9), cursor='hand2')
        self.resend_otp.place(x=600, y=160)
        self.resend_otp.bind("<Button-1>",self.resendOTP)


    # Function to resend otp
    def resendOTP(self, event):
        self.otp = random.randint(100000, 200000)
        SendOTP.send_email(self.email, self.otp)


    # If the hyperlink verify otp is pressed
    def verifyOTPPressed(self, event):
        otp_input = int(self.otp_input_box.get())
        try:
            # Checking if the otp_input is not an empty box
            if otp_input != "":
                # If the otp_input is same as self.otp
                if otp_input == self.otp:
                    ChangePassword(self.mainwindow)
                # If the otp_input is not same as self.otp
                else:
                    self.information_otp_text.config(text="OTP entered is not correct", fg='red')
            # If the otp_input is empty
            else:
                self.information_otp_text.config(text="Please provide the OTP", fg='red')
            self.information_otp_text.place(x=690, y=200)

        except ValueError as verr:
            self.information_otp_text.config(text="Please provide the OTP", fg='red')
            self.information_otp_text.place(x=690, y=200)


    # Function to go back to login page when the go back hyperlink is pressed
    def backToLoginFrame(self, event):
        self.vOTP.destroy()
        from login_frame import Login
        Login(self.mainwindow)

    # Function to go back to forgo password when the edit email id hyperlink is pressed
    def editEmailPressed(self, event):
        self.vOTP.destroy()
        from forgot_pass_frame import ForgotPassword
        ForgotPassword(self.mainwindow)
