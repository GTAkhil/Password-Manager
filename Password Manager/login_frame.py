# Importing the required libraries
from tkinter import *
from database import Database

# Class to login to the system
class Login:
    def __init__(self, mainwindow):

        # Global Variables
        self.mainwindow = mainwindow
        self.database_obj = Database()
        self.lf = Frame(self.mainwindow)
        self.canva = Canvas(self.lf, width=400, height=550, bg='#ebecf0')

        # Login information text
        self.login_information_text = Label(self.lf, bg='#ebecf0', fg='red', font=("bold", 9))

        # Features
        self.lf.config(background='#d3d3d3')
        self.canva.place(x=20, y=20)
        self.lf.place(x=100, y=50, width=1050, height=600)

        # Function calls
        self.loginLabels()
        self.loginInputBox()
        self.loginButton()


    # Fucntion to change the frame to singup frame
    def changeToSignupFrame(self, event):
        self.lf.destroy()
        from signup_frame import SignUp
        SignUp(self.mainwindow)

    # Function to change the frame to forgot passsword frame
    def changeToForgotPassword(self, event):
        self.lf.destroy()
        from forgot_pass_frame import ForgotPassword
        ForgotPassword(self.mainwindow)

    # Function to add all labels to the login frame
    def loginLabels(self):
        # Login text
        login_text = Label(self.lf, text="LOGIN", bg='#ebecf0', font=("bold", 13))
        login_text.place(x=40, y=40)

        # Dosen't have an account text
        signup_text = Label(self.lf, text="Dosen't have an account?", bg='#ebecf0', font=("bold", 9))
        signup_text.place(x=40, y=78)

        # Sign Up hyperlink text
        signup_hyperlink_text = Label(self.lf, text="Sign Up", bg='#ebecf0',fg='#000040', font=('bold', 9), cursor='hand2')
        signup_hyperlink_text.bind("<Button-1>", self.changeToSignupFrame)
        signup_hyperlink_text.place(x=230, y=78)

        # Forgot Password hyperlink text
        fotgot_password_hyperlink_text = Label(self.lf, text="Forgot Password?", bg='#ebecf0',fg='#000040', font=('bold', 9), cursor='hand2')
        fotgot_password_hyperlink_text.bind("<Button-1>", self.changeToForgotPassword)
        fotgot_password_hyperlink_text.place(x=40, y=300)

        # Master username text
        master_username_text = Label(self.lf, text="Master Username", bg='#ebecf0', font=("Arial", 11))
        master_username_text.place(x=40, y=140)

        # Master Password text
        master_password_text = Label(self.lf, text="Master Password", bg='#ebecf0', font=("Arial", 11))
        master_password_text.place(x=40, y=220)


    # Function to add entry box to the login frame
    def loginInputBox(self):

        # Master Username input box
        self.master_username_input_box = Entry(self.lf, bg='white', fg='black', font=("Arial", 11), width=35, borderwidth=0)
        self.master_username_input_box.place(x=38, y=170)

        # Master Password input box
        self.master_password_input_box = Entry(self.lf, bg='white', fg='black', font=("Arial", 11), width=35, borderwidth=0, show="*")
        self.master_password_input_box.place(x=38, y=260)

    # Function to add login button to the login frame
    def loginButton(self):
        login_button = Button(self.lf, text='LOGIN', bg='#36454f', fg='white', activeforeground='white', activebackground='#36454f', width=6, height=1, cursor="hand2", command = self.loginButtonPressed)
        login_button.place(x=305, y=300)


    # Function to connected to the login button which login to the password manager
    def loginButtonPressed(self):
        # Getting the input from the input boxes
        master_username = self.master_username_input_box.get()
        master_password = self.master_password_input_box.get()

        try:
            # Running the sql command to get the password
            sql_querry = "select Master_Password from login where Master_Username=%s"
            self.database_obj.cursor.execute(sql_querry, (master_username, ))
            db_master_passwrod = self.database_obj.cursor.fetchone()

            # Checking if the password is not none
            if db_master_passwrod is not None:
                # Login Successful
                if db_master_passwrod[0] == master_password:
                    master_username = self.master_username_input_box.get()
                    self.lf.destroy()
                    from logedin_frame import LogedIn
                    LogedIn(master_username, self.mainwindow)
                # Login Unsuccessful
                else:
                    self.login_information_text.config(text='Invlaid login details!')
                    self.login_information_text.place(x=150, y=110)
            # Login Unsuccessful
            else:
                self.login_information_text.config(text='Invlaid login details!')
                self.login_information_text.place(x=150, y=110)

        # If any error occurs
        except Exception as e:
            print(e)
