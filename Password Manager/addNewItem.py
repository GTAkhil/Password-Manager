 # Importing the required libraries
from tkinter import *
from database import Database
from datetime import datetime

# Creating the class NewItem to add new new item
class NewItem:
    def __init__(self, mainwindow):
        self.database_obj = Database()
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

        # Creating the information label
        self.info_label = Label(self.frame,
                         bg = 'white',
                         font = ("Arial",10))

        # Function calls
        self.labels()
        self.entryBox()
        self.button()

    def labels(self):
        app_name = Label(self.frame,
                         text = "App",
                         bg = 'white',
                         fg = 'black',
                         font = ("Arial",10)
                         )
        app_name.place(x=20, y=20)

        link_name = Label(self.frame,
                         text = "Link",
                         bg = 'white',
                         fg = 'black',
                         font = ("Arial",10)
                         )
        link_name.place(x=20, y=90)

        username_name = Label(self.frame,
                         text = "Username",
                         bg = 'white',
                         fg = 'black',
                         font = ("Arial",10)
                         )
        username_name.place(x=20, y=160)

        password_name = Label(self.frame,
                         text = "Password",
                         bg = 'white',
                         fg = 'black',
                         font = ("Arial",10)
                         )
        password_name.place(x=20, y=230)

    def entryBox(self):
        self.app_input_box = Entry(self.frame,
                              bg = 'white',
                              fg = 'black',
                              font = ("Arial",10),
                              borderwidth = 2,
                              width = 40
                              )
        self.app_input_box.place(x=19, y=50)

        self.link_input_box = Entry(self.frame,
                              bg = 'white',
                              fg = 'black',
                              font = ("Arial",10),
                              borderwidth = 2,
                              width = 40
                              )
        self.link_input_box.place(x=19, y=120)

        self.username_input_box = Entry(self.frame,
                              bg = 'white',
                              fg = 'black',
                              font = ("Arial",10),
                              borderwidth = 2,
                              width = 40
                              )
        self.username_input_box.place(x=19, y=190)

        self.password_input_box = Entry(self.frame,
                              bg = 'white',
                              fg = 'black',
                              font = ("Arial",10),
                              borderwidth = 2,
                              width = 40
                              )
        self.password_input_box.place(x=19, y=260)

    # Button to add the item
    def button(self):
        add_button = Button(self.frame,
                            text='Add',
                            bg='#36454f',
                            fg='white',
                            activebackground='#36454f',
                            activeforeground='white',
                            cursor='hand2',
                            font=('Arial',10),
                            width=4,
                            height=1,
                            command = self.additem
                            )
        add_button.place(x=320, y=300)

    # Function to add the item
    def additem(self):
        app = self.app_input_box.get()
        link = self.link_input_box.get()
        username = self.username_input_box.get()
        password = self.password_input_box.get()
        date = datetime.now().date()
        fav = False
        sql_querry = 'insert into Akhil values(%s,%s,%s,%s,%s,%s)'
        try:
            if app!='' and link!='' and username!='' and password!='':
                self.database_obj.cursor.execute(sql_querry, (link, username, password, date, app, fav))
                self.database_obj.connection.commit()
                self.info_label.config(text='Item added successfully', fg='green')

            else:
                self.info_label.config(text='Please provide all the details', fg='red')

            self.info_label.place(x=100, y=10)

        except Exception as e:

            self.info_label.config(text='Something went wrong!', fg='red')
            self.info_label.place(x=100, y=10)


