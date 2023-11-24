# Importing the required libraries
from tkinter import *
from database import Database
from PIL import Image, ImageTk

# Class to when the person is loged in
class LogedIn:
    def __init__(self, username, window): # Runs the class when an instance of the class is created
        # Global variables
        self.mainwindow = window
        self.database_obj = Database()
        self.username = username
        # self.showed_data = None
        # self.username_showed_data = None

        # Frames
        self.mainframe2 = Frame(self.mainwindow, bg='white')
        self.mainframe2.place(x=332, y=0, width=400, height=700)
        self.mainframe3 = Frame(self.mainframe2, bg='white')
        self.mainframe4 = Frame(self.mainframe2, bg='white')
        self.mainframe5 = Frame(self.mainwindow, bg='white')
        self.mainframe5.place(x=734, y=0, width=600, height=700)
        self.mainframe6 = Frame(self.mainframe2, bg='#36454f')
        self.mainframe6.place(x=0, y=45, width=400, height=2)

        #Canvas
        self.canvas = Canvas(self.mainframe5, width=450, height=340, bg='white')
        self.canvas.place(x=30, y=110)

        # Funtion calls
        self.frame1(username = username)
        self.frame2()
        self.frame5()
        self.appIsOpened()

    # Function to add a left side frame to the main window
    def frame1(self, username):
        # Creating the frame
        self.mainframe = Frame(self.mainwindow, bg='white')
        self.mainframe.place(x=0, y=0, height=700, width=330)

        # Adding labels to the frame
        avtar_image = Image.open('Images/account_akhil.png')
        resize_avtar_image = avtar_image.resize((20,20))
        avtar_photo_image = ImageTk.PhotoImage(resize_avtar_image)
        avtar_label = Label(self.mainframe,
                            bg='white',
                            image=avtar_photo_image,
                            text=f'  Welcome {username}',
                            font=("bold", 13),
                            compound = 'left'
                            )
        avtar_label.image = avtar_photo_image
        avtar_label.place(x=30, y=30)

        # Adding the Features text to the frame
        features_text = Label(self.mainframe, text='Features', bg='white', fg='#999090', font=('Arial',10))
        features_text.place(x=30, y=100)

        # Adding hyperlinks to the frame
        # all items hyperlink
        all_items_hyperlink_image = Image.open('Images/allItems.png')
        resize_all_items_hyperlink_image = all_items_hyperlink_image.resize((20,20))
        all_items_photo_image = ImageTk.PhotoImage(resize_all_items_hyperlink_image)
        all_items_hyperlink = Label(self.mainframe,
                                    bg='white',
                                    image=all_items_photo_image,
                                    text='   All items',
                                    cursor='hand2',
                                    font=('bold', 10),
                                    compound = 'left'
                                    )
        all_items_hyperlink.image = all_items_photo_image
        all_items_hyperlink.bind("<Button-1>", self.allItems)
        all_items_hyperlink.place(x=30, y=140)

        # Adding the favourite item hyperlink
        favourite_item_hyperlink_image = Image.open('Images/favouriteItem.png')
        resize_favourite_item_hyperlink_image = favourite_item_hyperlink_image.resize((30,30))
        favourite_item_photo_image = ImageTk.PhotoImage(resize_favourite_item_hyperlink_image)
        favourite_item_hyperlink = Label(self.mainframe,
                                         bg="white",
                                         text="  Favourite item",
                                         cursor = 'hand2',
                                         font=("bold", 10),
                                         image = favourite_item_photo_image,
                                         compound = 'left'
                                         )
        favourite_item_hyperlink.image = favourite_item_photo_image
        favourite_item_hyperlink.bind("<Button-1>", self.favouriteItem)
        favourite_item_hyperlink.place(x=25, y=170)

        # Adding the password vulnerability hyperlink
        pass_vulnerability_image = Image.open('Images/passVulnerability.jpg')
        resize_pass_vulnerability_image = pass_vulnerability_image.resize((30,30))
        pass_vulnerability_image_photo = ImageTk.PhotoImage(resize_pass_vulnerability_image)
        pass_vulnerability_label = Label(self.mainframe,
                                         bg="white",
                                         text="  Check password vulnerability",
                                         cursor = 'hand2',
                                         font=("bold", 10),
                                         image = pass_vulnerability_image_photo,
                                         compound = 'left'
                                         )
        pass_vulnerability_label.image = pass_vulnerability_image_photo
        pass_vulnerability_label.bind("<Button-1>", self.passVulnerability)
        pass_vulnerability_label.place(x=25, y=205)

        # Adding the strong password hyperlink
        strong_password_image = Image.open('Images/strongPass.png')
        resize_strong_password_image = strong_password_image.resize((30,30))
        photo_strong_password_image = ImageTk.PhotoImage(resize_strong_password_image)
        strong_password_label = Label(self.mainframe,
                                      bg="white",
                                      text="  Create strong password",
                                      cursor = 'hand2',
                                      font=("bold", 10),
                                      image = photo_strong_password_image,
                                      compound = 'left'
                                      )
        strong_password_label.image = photo_strong_password_image
        strong_password_label.bind("<Button-1>", self.strongPass)
        strong_password_label.place(x=25, y=240)

        # Adding the Others text to the frame
        others_text = Label(self.mainframe, text='Others', bg='white', fg='#999090', font=('Arial',10))
        others_text.place(x=30, y=300)

        # Adding the logout hyperlink
        logout_image = Image.open('Images/logout.png')
        resize_logout_image = logout_image.resize((30,30))
        photo_logout_image = ImageTk.PhotoImage(resize_logout_image)
        logout_label = Label(self.mainframe,
                             bg="white",
                             text="  Logout",
                             cursor = 'hand2',
                             font=("bold", 10),
                             image = photo_logout_image,
                             compound = 'left'
                             )
        logout_label.image = photo_logout_image
        logout_label.bind("<Button-1>",self.logout)
        logout_label.place(x=25, y=330)
#--------------------------------------------------------------------------------------------------------------------------------
# Left side frame(frame1) completed
#--------------------------------------------------------------------------------------------------------------------------------

    # Function to make the widgets for the middle frame
    def frame2(self):
        # Adding a search box
        self.search_box = Entry(self.mainframe2,
                           text='Search all items',
                           bg='white',
                           fg='grey',
                           font=("Arial",12),
                           width=25,
                           borderwidth=0
                           )
        self.search_box.insert(0, 'Search all items')
        self.search_box.place(x=10, y=5)

        # Adding a search hyperlink
        search_hyperlink_image = Image.open('Images/searchIcon.png')
        resize_search_hyperlink_image = search_hyperlink_image.resize((25,25))
        photo_search_hyperlink_image = ImageTk.PhotoImage(resize_search_hyperlink_image)
        search_hyperlink = Label(self.mainframe2,
                         bg = 'white',
                         image=photo_search_hyperlink_image,
                         borderwidth=0,
                         cursor = "hand2"
                         )
        search_hyperlink.image = photo_search_hyperlink_image
        search_hyperlink.bind("<Button-1>", self.searchItem)
        search_hyperlink.bind("<Return>", self.searchItem)
        search_hyperlink.place(x=300, y=5)

        # Adding a hyperlink new item
        new_item_image = Image.open('Images/newItem.png')
        resize_new_item_image = new_item_image.resize((25,24))
        photo_new_item_image = ImageTk.PhotoImage(resize_new_item_image)
        new_item_hyperlink = Label(self.mainframe2,
                                 bg = 'white',
                                 fg = '#000040',
                                 image = photo_new_item_image,
                                 font = ("bold",10),
                                 cursor = "hand2"
                                 )
        new_item_hyperlink.image = photo_new_item_image
        new_item_hyperlink.bind("<Button-1>", self.newItem)
        new_item_hyperlink.place(x=340, y=5)

#------------------------------------------------------------------------------------------------------------------------------
# Middle frame that is Frame 2 is completed
#------------------------------------------------------------------------------------------------------------------------------

    # Function to add the widgets to the right side frame or frame5
    def frame5(self):
        # Item information text
        item_information_label = Label(self.mainframe5, bg="white", fg='#999090', font=("bold", 14), text="ITEM INFORMATION")
        item_information_label.place(x=30, y=40)

        # Coordinates of the top-left and bottom-right corners of the rectangle
        x1, y1 = 1, 1
        x2, y2 = 450, 340
        line_x1, line_y1 = 1, 70
        line_x2, line_y2 = 450, 70

        # Draw the rectangle and the line on the canvas
        self.canvas.create_rectangle(x1, y1, x2, y2, outline='#999090', width=1, fill='white')
        for i in range(0,4):
            self.canvas.create_line(line_x1, line_y1, line_x2, line_y2, width=1, fill='#999090')
            line_y1+=70
            line_y2+=70

        # Labels
        # label to add the App name text
        label1 = Label(self.mainframe5, text='App', font=("Arial" ,9), fg="#999090", bg='white')
        label1.place(x=40, y=115)

        # label to add the link name text
        label2 = Label(self.mainframe5, text='Link', font=("Arial" ,9), fg="#999090", bg='white')
        label2.place(x=40, y=185)

        # label to add the username name text
        label3 = Label(self.mainframe5, text='Username', font=("Arial" ,9), fg="#999090", bg='white')
        label3.place(x=40, y=255)

        # label to add the password name text
        label4 = Label(self.mainframe5, text='password', font=("Arial" ,9), fg="#999090", bg='white')
        label4.place(x=40, y=325)

         # label to add the Last modified at name text
        label5 = Label(self.mainframe5, text='Last modified at', font=("Arial" ,9), fg="#999090", bg='white')
        label5.place(x=40, y=395)

#------------------------------------------------------------------------------------------------------------------------------
# Right side frame that is frame 5 is completed
#------------------------------------------------------------------------------------------------------------------------------


    # Function to add the all the items in the window to show when the application is opened
    def appIsOpened(self):
        if hasattr(self, 'mainframe3'):
            self.mainframe3.destroy()

        self.mainframe4 = Frame(self.mainframe2, bg='white')
        self.mainframe4.place(x=2, y=50, width=500, height=700)

        x = 10
        y = 10
        x1 = 10
        y1 = 40
        try:
            sql_querry = f"select App from {self.username}"
            self.database_obj.cursor.execute(sql_querry)
            data = self.database_obj.cursor.fetchall()

            sql_querry2 = f'select Username from {self.username}'
            self.database_obj.cursor.execute(sql_querry2)
            data2 = self.database_obj.cursor.fetchall()
            if data is not None:
                for i in range(len(data)):
                    self.showed_data = data[i]
                    self.username_showed_data = data2[i]

                    allItem_label = Label(self.mainframe4, bg='white', fg='black', font=("bold", 12), cursor = "hand2")
                    allItem_label.bind("<Button-1>", self.getdata)
                    user_allItem_label = Label(self.mainframe4, bg='white', fg='#999090', font=("Arial", 9), cursor = "hand2")

                    allItem_label.config(text=self.showed_data)
                    user_allItem_label.config(text=self.username_showed_data)
                    user_allItem_label.place(x=x1, y=y1)
                    allItem_label.place(x=x, y=y)
                    y+=60
                    y1 = y + 30
            else:
                print("None")
        except Exception as e:
            print(e)

#------------------------------------------------------------------------------------------------------------------------------
# All the functions which are connected throught bind() method starts here for all the frames
#------------------------------------------------------------------------------------------------------------------------------
    # Function to bind with the all_items_hyperlink
    def allItems(self, event):
        # Variables for this class
        x = 10
        y = 10
        x1 = 10
        y1 = 40
        line_x1 = 0
        line_y1 = 60
        line_x2 = 400
        line_y2 = 60

        self.search_box.delete(0, END)
        self.search_box.insert(0, "Search all items")
        if hasattr(self, 'mainframe3'):
            self.mainframe3.destroy()

        self.mainframe4 = Frame(self.mainframe2, bg='white')
        self.mainframe4.place(x=2, y=50, width=500, height=700)


        try:
            sql_querry = f"select App from {self.username}"
            self.database_obj.cursor.execute(sql_querry)
            data = self.database_obj.cursor.fetchall()

            sql_querry2 = f'select Username from {self.username}'
            self.database_obj.cursor.execute(sql_querry2)
            data2 = self.database_obj.cursor.fetchall()

            if data is not None:
                for i in range(len(data)):
                    self.showed_data = data[i]
                    self.username_showed_data = data2[i]

                    allItem_label = Label(self.mainframe4, bg='white', fg='black', font=("bold", 12), cursor="hand2")
                    allItem_label.bind("<Button-1>", self.getdata)
                    user_allItem_label = Label(self.mainframe4, bg='white', fg='#999090', font=("Arial", 9), cursor="hand2")

                    allItem_label.config(text=self.showed_data)
                    user_allItem_label.config(text=self.username_showed_data)

                    user_allItem_label.place(x=x1, y=y1)
                    allItem_label.place(x=x, y=y)

                    y += 60
                    y1 = y + 30
            else:
                print("None")

        except Exception as e:
            print(e)

    # Function to bind with the favourite_item_hyperlink
    def favouriteItem(self, event):
        # Variables for this class
        x = 10
        y = 10
        x1 = 10
        y1 = 40

        self.search_box.delete(0, END)
        self.search_box.insert(0, "Search favourites")

        if hasattr(self, 'mainframe4'):
            self.mainframe4.destroy()

        self.mainframe3 = Frame(self.mainframe2, bg='white')
        self.mainframe3.place(x=2, y=50, width=500, height=700)

        try:
            sql_querry = f"select App from {self.username} where Favourite = True"
            self.database_obj.cursor.execute(sql_querry)
            data = self.database_obj.cursor.fetchall()

            sql_querry2 = f'select Username from {self.username} where Favourite = True'
            self.database_obj.cursor.execute(sql_querry2)
            data2 = self.database_obj.cursor.fetchall()

            if data is not None:
                for i in range(len(data)):
                    self.showed_data = data[i]
                    self.username_showed_data = data2[i]

                    favouriteItem_label = Label(self.mainframe3, bg='white', fg='black', font=("bold", 12), cursor="hand2")
                    favouriteItem_label.bind("<Button-1>", self.getdata)
                    user_favouriteItem_label = Label(self.mainframe3, bg='white', fg='#999090', font=("Arial", 9), cursor="hand2")

                    favouriteItem_label.config(text=self.showed_data)
                    user_favouriteItem_label.config(text=self.username_showed_data)

                    user_favouriteItem_label.place(x=x1, y=y1)
                    favouriteItem_label.place(x=x, y=y)

                    y += 60
                    y1 = y + 30
            else:
                print("None")

        except Exception as e:
            print(e)


    # Function to get the data and add to the information label
    def getdata(self, event):
       string_showed_data = str(self.showed_data[0])
       string_username_showed_data = str(self.username_showed_data[0])

       sql_querry = f"select id from {self.username} where App = %s and Username = %s"
       self.database_obj.cursor.execute(sql_querry, (string_showed_data, string_username_showed_data))
       data = self.database_obj.cursor.fetchall()
       for i in data:
           sql_querry2 = f"select * from {self.username} where id = %s"
           self.database_obj.cursor.execute(sql_querry2, (i[0], ))
           data2 = self.database_obj.cursor.fetchone()
           self.setData(data2)
           break

    # Function to set the item information into the frame
    def setData(self, data2):
        # label to add the App name text
        label1 = Label(self.mainframe5, text=data2[4], font=("Arial" ,11), fg="black", bg='white')
        label1.place(x=40, y=140)

        # label to add the link text
        label2 = Label(self.mainframe5, text=data2[0], font=("Arial" ,11), fg="black", bg='white')
        label2.place(x=40, y=210)

        # label to add the username text
        label3 = Label(self.mainframe5, text=data2[1], font=("Arial" ,11), fg="black", bg='white')
        label3.place(x=40, y=280)

        # label to add the password text
        label4 = Label(self.mainframe5, text=data2[2], font=("Arial" ,11), fg="black", bg='white')
        label4.place(x=40, y=350)

        # label to add the password text
        label5 = Label(self.mainframe5, text=data2[3], font=("Arial" ,11), fg="black", bg='white')
        label5.place(x=40, y=420)




    # Function to bind with the logout hyperlink
    def logout(self, event):
        self.mainframe.destroy()
        self.mainframe2.destroy()
        self.mainframe5.destroy()
        from login_frame import Login
        Login(self.mainwindow)


    # Function to bind with the password vulnerability hyperlink
    def passVulnerability(self, event):
        from passVulner import Vulnerability
        Vulnerability(self.mainwindow)


    # Function to bind with the strong password hyperlink
    def strongPass(self, event):
        from create_strong import StrongPassword
        StrongPassword(self.mainwindow)

    # Function to bind with the search item hyperlink
    def searchItem(self, event):
        # Variables for this class
        x = 10
        y = 10
        x1 = 10
        y1 = 40

        search = self.search_box.get()

        sql_querry = f"select App from {self.username} where App = %s"
        sql_querry2 = f"select Username from {self.username} where App = %s"

        if search!='Search all items' or search!="Search favourite" or search!='':
            if hasattr(self, 'self.mainframe3') or hasattr(self, 'self.mainframe4'):
                self.mainframe3.destroy()
                self.mainframe4.destroy()

            self.mainframe7 = Frame(self.mainframe2, bg = "white")
            self.mainframe7.place(x=2, y=50, width=500, height=700)

            # Running the sql command
            self.database_obj.cursor.execute(sql_querry, (search, ))
            data = self.database_obj.cursor.fetchall()

            self.database_obj.cursor.execute(sql_querry2, (search, ))
            data2 = self.database_obj.cursor.fetchall()

            try:
                if data is not None:
                    for i in range(len(data)):
                        favouriteItem_label = Label(self.mainframe7, bg='white', fg='black', font=("bold", 12), cursor = "hand2")
                        user_favouriteItem_label = Label(self.mainframe7, bg='white', fg='#999090', font=("Arial", 9), cursor = "hand2")

                        showed_data = data[i]
                        username_showed_data = data2[i]

                        favouriteItem_label.config(text=showed_data)
                        user_favouriteItem_label.config(text=username_showed_data)

                        user_favouriteItem_label.place(x=x1, y=y1)
                        favouriteItem_label.place(x=x, y=y)

                        y+=60
                        y1 = y + 30
                else:
                    favouriteItem_label.config(text="Could not found the data")
                    favouriteItem_label.place(x=x, y=y)

            except Exception as e:
                print(e)

    # Function to bind with the new Item hyperlink
    def newItem(self, event):
        from addNewItem import NewItem
        NewItem(self.mainwindow)
