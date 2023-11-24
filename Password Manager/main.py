# Importing the required libraries
from tkinter import *
from login_frame import Login

# Function to add the edit the window
def windowFeatures():
    window.geometry("1250x700+400+170")
    window.resizable(False, False)
    window.title("Password Manager")
    window.config(background='#36454f')
    # Icon image
    icon_image = PhotoImage(file='Images/windowIcon.png')
    window.iconphoto(False, icon_image)

# Function to create and add frame login to the window
def frames():
    # creating the loginframe
    login_obj = Login(window) # object for login class


# if the file is this then run it
if __name__=="__main__":
    window = Tk() # Creating a simple gui winodw
    windowFeatures()
    frames()
    window.mainloop() # Showing and running the gui window
