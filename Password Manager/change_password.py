# Importing the required libraries
from tkinter import *
from database import Database
from mac import GetMac

# Class to change the password
class ChangePassword:
    def __init__(self, mainwindow):
        # Global variables
        self.mainwindow = mainwindow
        self.cpFrame = Frame(self.mainwindow)
        self.database_obj = Database()

        # Update information text
        self.update_informantion_text = Label(self.cpFrame, bg='#ebecf0', font=('bold', 11))

        # Settingup the frame
        self.cpFrame.config(bg='#ebecf0')
        self.cpFrame.place(x=100, y=50, width=1050, height=600)

        # Function calls
        self.cpLabels()
        self.inputBox()

     # Function to add the input box to the chang password frame
    def inputBox(self):
        # Master Password input box
        self.master_password_input_box = Entry(self.cpFrame, bg='white', fg='black', font = ("Arial", 11), width=43, borderwidth=0, show='*')
        self.master_password_input_box.place(x=245, y=190)

        # Re type master password
        self.retype_master_password_input_box = Entry(self.cpFrame, bg='white', fg='black', font =("Arial", 11), width=43, borderwidth=0, show='*')
        self.retype_master_password_input_box.place(x=245, y=270)


    # Function to add all the labels to the change password frame
    def cpLabels(self):
        # Reconfigure your password text
        reconfigure_text = Label(self.cpFrame, text='Reconfigure your master password', bg='#ebecf0', font=("bold", 14))
        reconfigure_text.place(x=245, y=100)

        # Master Password text
        master_password_text = Label(self.cpFrame, text="Master Password", bg='#ebecf0', font=("Arial", 11))
        master_password_text.place(x=245, y=160)


        # Re type Master Password text
        retype_master_password_text = Label(self.cpFrame, text="Re-type master password", bg='#ebecf0', font=("Arial", 11))
        retype_master_password_text.place(x=245, y=240)

        # Go back hyperlink
        go_back_hyperlink = Label(self.cpFrame, text="< Go back", bg='#ebecf0', fg='#000040', font=("Arial", 10), cursor="hand2")
        go_back_hyperlink.bind("<Button-1>", self.goBackHyperlinkPressed)
        go_back_hyperlink.place(x=245, y=310)

        # Update button
        update_button = Button(self.cpFrame, text='Update', bg='#36454f', fg='white', activeforeground='white', activebackground='#36454f', width=6, height=1, cursor="hand2", command = self.updateButtonPressed)
        update_button.place(x=590, y=310)


    # Functon to update the password to the database
    def updateButtonPressed(self):
        master_password = self.master_password_input_box.get()
        retype_master_password = self.retype_master_password_input_box.get()
        mac_address = GetMac.get_mac_address()
        sql_querry = '''UPDATE login SET Master_Password = %s WHERE Mac = %s;'''
        try:
            if master_password == retype_master_password:
                self.database_obj.cursor.execute(sql_querry, (master_password, mac_address))
                self.database_obj.connection.commit()
                self.update_informantion_text.config(text='Updated Successfully', fg='green')
            else:
                self.update_informantion_text.config(text="Password doesn't not matched", fg='red')
            self.update_informantion_text.place(x=400, y=350)

        except Exception as e:
            print(e)

    # Function to go back to the signup frame
    def goBackHyperlinkPressed(self, event):
        from signup_frame import SignUp
        SignUp(self.mainwindow)
