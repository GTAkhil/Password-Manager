# Importing the required library
from tkinter import *
import random
import string

class StrongPassword:
    def __init__(self, window):
        self.toplevel = Toplevel(window)

        # Features
        self.toplevel.title("Generate password")
        self.toplevel.geometry("600x500")
        self.toplevel.config(background='#36454f')
        self.toplevel.resizable(False, False)

         # Adding the frame to the window
        self.frame = Frame(self.toplevel, bg='white')
        self.frame.place(x=30, y=30, width=500, height=400)

        # your generated password text
        generate_password = Label(self.frame,
                                  fg='black',
                                  bg='white',
                                  text = 'Your generated password',
                                  font = ("Arial", 10)
                                  )
        generate_password.place(x=20, y=40)

        # Adding the entry filed
        self.entry_field = Entry(self.frame,
                               fg = 'black',
                               bg = 'white',
                               width = 35,
                               font=("Arial",10),
                               borderwidth = 0
                               )
        self.entry_field.place(x=19, y=90)

        # Function calls
        self.generate_password()

    def generate_password(self, length=12):
        # Define character sets for different types of characters
        lowercase_letters = string.ascii_lowercase
        uppercase_letters = string.ascii_uppercase
        digits = string.digits
        special_characters = string.punctuation

        # Combine all character sets
        all_characters = lowercase_letters + uppercase_letters + digits + special_characters

        # Ensure the password has at least one character from each set
        password = [
            random.choice(lowercase_letters),
            random.choice(uppercase_letters),
            random.choice(digits),
            random.choice(special_characters)
        ]

        # Generate the remaining characters randomly
        for _ in range(length - 4):
            password.append(random.choice(all_characters))

        # Shuffle the characters to make the password more random
        random.shuffle(password)

        # Convert the list of characters to a string
        password_str = ''.join(password)
        self.entry_field.insert(0, password_str)
