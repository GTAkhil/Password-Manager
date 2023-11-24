# Importing the required libraries
from tkinter import *
from database import Database
from mac import GetMac

# Creating the class to make the signup page
class SignUp:
    def __init__(self, mainwindow):

        # Global variables
        self.database_obj = Database()
        self.mainwindow = mainwindow
        self.sf = Frame(self.mainwindow)
        self.canva = Canvas(self.sf, width=400, height=550, bg='#ebecf0')

        # Features
        self.sf.config(background='#d3d3d3')
        self.canva.place(x=20, y=20)
        self.sf.place(x=100, y=50, width=1050, height=600)
        # Signup information text
        self.signup_infromation_text = Label(self.sf, bg='#ebecf0', fg='red', font=("Arial", 9))


        # Function calls
        self.signupLabels()
        self.signupInputBox()
        self.signupButton()


    # function to switch frame to the login frame
    def changeToLoginFrame(self, event):
        self.sf.destroy()
        from login_frame import Login
        Login(self.mainwindow)

    # Function to add all labels to the signup frame
    def signupLabels(self):
        # Sign Up text
        signup_text = Label(self.sf, text="Sign Up", bg='#ebecf0', font=("bold", 13))
        signup_text.place(x=40, y=40)

        # Already have an account text
        signup_text = Label(self.sf, text="Already have an account?", bg='#ebecf0', font=("bold", 9))
        signup_text.place(x=40, y=78)

        # Login hyperlink text
        login_hyperlink_text = Label(self.sf, text="Login", bg='#ebecf0',fg='#000040', font=('bold', 9), cursor='hand2')
        login_hyperlink_text.bind("<Button-1>", self.changeToLoginFrame)
        login_hyperlink_text.place(x=230, y=78)

        # Email text
        Email = Label(self.sf, text="Email ID", bg='#ebecf0', font=("Arial", 11))
        Email.place(x=40, y=130)

        # Master username text
        master_username_text = Label(self.sf, text="Master Username", bg='#ebecf0', font=("Arial", 11))
        master_username_text.place(x=40, y=210)

        # Master Password text
        master_password_text = Label(self.sf, text="Master Password", bg='#ebecf0', font=("Arial", 11))
        master_password_text.place(x=40, y=280)

        # Re-Type Master Password text
        re_type_master_password_text = Label(self.sf, text="Re-Type Master Password", bg='#ebecf0', font=("Arial", 11))
        re_type_master_password_text.place(x=40, y=350)


    # Function to add entry box to the signup frame
    def signupInputBox(self):
        # email input box
        self.email_input_box = Entry(self.sf, bg='white', fg='black', font=("Arial", 11), width=35, borderwidth=0)
        self.email_input_box.place(x=38, y=160)

        # Master Username input box
        self.master_username_input_box = Entry(self.sf, bg='white', fg='black', font=("Arial", 11), width=35, borderwidth=0)
        self.master_username_input_box.place(x=38, y=240)

        # Master Password input box
        self.master_password_input_box = Entry(self.sf, bg='white', fg='black', font=("Arial", 11), width=35, borderwidth=0, show="*")
        self.master_password_input_box.place(x=38, y=310)

        # Re Type Master Password box
        self.re_type_master_password_input_box = Entry(self.sf, bg='white', fg='black', font=("Arial", 11), width=35, borderwidth=0, show="*")
        self.re_type_master_password_input_box.place(x=38, y=380)


    # Function to add sign up button to the signup frame
    def signupButton(self):
        signup_button = Button(self.sf, text='Sign Up', bg='#36454f', fg='white', activeforeground='white', activebackground='#36454f', width=6, height=1, cursor="hand2", command=self.signupButtonPressed)
        signup_button.place(x=305, y=430)


    # Function that connect to the signup button when the signup button is pressed
    def signupButtonPressed(self):
        # Taking the input from the user and inserting them into the variables
        email = self.email_input_box.get()
        master_username = self.master_username_input_box.get()
        master_password = self.master_password_input_box.get()
        retyped_master_password = self.re_type_master_password_input_box.get()
        mac_address = GetMac.get_mac_address()
        sql_querry = "insert into login values (%s, %s, %s, %s)"

        sql_querry_2 = f'''create table {master_username}(Link varchar(40) not null, Username varchar(20),Password varchar(20),Last_Modified date)'''

        tabel_check_querry = f'''SELECT "login" FROM information_schema.tables WHERE table_schema = "accounts" AND table_name ="{master_username}";'''
        self.database_obj.cursor.execute(tabel_check_querry)
        db_tabel_check = self.database_obj.cursor.fetchone()

        try:
            if db_tabel_check:
                pass
            else:
                # Checking if the master_password is not empty
                if master_password != "" or email != "" or master_username != "":
                    # Checking if the master_password is same as retyped_master_password or not
                    if (master_password == retyped_master_password):
                        self.database_obj.cursor.execute(sql_querry,(master_username, master_password, mac_address, email))
                        self.database_obj.cursor.execute(sql_querry_2)
                        self.database_obj.connection.commit()

                    # If the master_password and the retyped_master_password is not same
                    else:
                        self.signup_infromation_text.config(text="Password dosen't match")

                # If any or all the details are empty
                else:
                    self.signup_infromation_text.config(text='Please provide all the details')
                self.signup_infromation_text.place(x=150, y=110)

        # If any error occurs in database related command
        except self.database_obj.err as err:
            if err.errno == 1062:
                self.signup_infromation_text.config(text='Master Username already exist')
                self.signup_infromation_text.place(x=150, y=110)
            else:
                print(err)

        # If any other exception or error occurs
        except Exception as e:
            print(e)
