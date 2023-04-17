import tkinter as tk
from tkinter import messagebox
import os
import random
import string

class Signup:
    def __init__(self,username_input,password_input):
        self.username_input=username_input
        self.password_input=password_input
        self.recovery_code=''

    def create_account(self,window):
        # Get the parent path
        self.parent_path=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        
        # Get the username and password from input
        username=self.username_input.get()
        password=self.password_input.get()

        # Generate a recovery code
        self.recovery_code=''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(6))
        
        # Check if user fill in all the fields
        if not all([username,password]):
            messagebox.showerror("Error","Please fill in all fields.")
            return
        
        # All the non-admin users data are stored in data/nonadmin.dat
        # Format of the file: username1\nusername2\n...\nEnd\npassword1\npassword2\n...\nEnd
        # Check if file nonadmin.dat exists,if not then create a new one
        
        #if not os.path.exists(f"{self.parent_path}/data/nonadmin.dat"): # For Linux
        if not os.path.exists(f"{self.parent_path}\\data\\nonadmin.dat"): # For Windows
            #with open(f"{self.parent_path}/data/nonadmin.dat","w") as f: # For Linux
            with open(f"{self.parent_path}\\data\\nonadmin.dat","w") as f:
                print("No nonadmin.dat file found,creating a new one...") # Log
                f.write("End")

        # Check if the nonadmin.dat file has the correct format
        
        #with open(f"{self.parent_path}/data/nonadmin.dat") as f: # For Linux
        with open(f"{self.parent_path}\\data\\nonadmin.dat") as f: # For Windows
            data=f.read()
            if "End" not in data:
                print("Invalid file format for nonadmin.dat") # Log
                return
            # Split the data into usernames and passwords
            usernames,passwords=data.split("End")
            usernames=usernames.strip().split("\n")
            passwords=passwords.strip().split("\n")
            # If there is no user signed up before,then the last element of the list is an empty string,so we remove it
            if usernames[-1] == "":
                usernames.pop()
                passwords.pop()

        # Check if the username is already taken
        if username in usernames:
            messagebox.showerror("Error","Username is already taken.")
            return
        
        # Add the new user to the data file
        usernames.append(username)
        passwords.append(password)

        #with open(f"{self.parent_path}/data/nonadmin.dat","w") as f: # For Linux
        with open(f"{self.parent_path}\\data\\nonadmin.dat","w") as f: # For Windows
            if len(usernames) >1 and len(passwords) >1:
                f.write("\n".join(usernames) + "\nEnd\n" + "\n".join(passwords)) # If there is more than one user,then use newline character to separate the usernames and passwords
            else:
                f.write(usernames[0] + "\nEnd\n" + passwords[0]) # If there is only one user,then there is no newline character

        # File recovercode.dat stores all the recovery codes
        # Check if the file exists,if not then create a new one
        
        #if not os.path.exists(f"{self.parent_path}/data/recovercode.dat"): # For Linux
        if not os.path.exists(f"{self.parent_path}\\data\\recovercode.dat"): # For Windows
            #with open(f"{self.parent_path}/data/recovercode.dat","w") as f: # For Linux
            with open(f"{self.parent_path}\\data\\recovercode.dat","w") as f: # For Windows
                print("No recovercode.dat file found,creating a new one...") # Log
                f.write("")

        # Read the data file
        #with open(f"{self.parent_path}/data/recovercode.dat") as f: # For Linux
        with open(f"{self.parent_path}\\data\\recovercode.dat") as f: # For Windows
            data=f.read().strip()
            user_codes=data.strip().split("\n")
            # If there is no user signed up before,then the last element of the list is an empty string,so we remove it
            if user_codes[-1] == "":
                user_codes.pop()

        # Add the new user's recovery code to the data file
        user_codes.append(self.recovery_code)

        # Save the recover codes to file
        #with open(f"{self.parent_path}/data/recovercode.dat","w") as f: # For Linux
        with open(f"{self.parent_path}\\data\\recovercode.dat","w") as f: # For Windows
            if len(user_codes) > 1:
                f.write("\n".join(user_codes)) # If there is more than one user,then use newline character to separate the codes
            else:
                f.write(user_codes[0]) # If there is only one user,then there is no newline character
            
            
        # Close the signup windows
        window.destroy()

        # Show the recovery code
        messagebox.showinfo("Success",f"Account created successfully.\nRecovery code: {self.recovery_code}")

class SignupGUI:
    def __init__(self,window):
        self.window=window
        window.title("Sign up")
        window.resizable(0,0)

        signup_frame=tk.Frame(window)
        signup_frame.pack(padx=10,pady=10)

        forget_label=tk.Label(signup_frame,text="After signed up, keep the recovery code safe!",font=("",12,"bold"))
        forget_label.grid(row=0,column=0,columnspan=2,padx=10,pady=10,sticky=tk.NSEW)

        username_label=tk.Label(signup_frame,text="Username:",font=("",10,"bold"))
        username_label.grid(row=1,column=0,columnspan=2,padx=10,pady=10,sticky=tk.W)
        self.username_input=tk.Entry(signup_frame,width=15)
        self.username_input.grid(row=2,column=0,columnspan=2,padx=10,pady=10,sticky=tk.NSEW)

        password_label=tk.Label(signup_frame,text="Password:",font=("",10,"bold"))
        password_label.grid(row=3,column=0,columnspan=2,padx=10,pady=10,sticky=tk.W)
        self.password_input=tk.Entry(signup_frame,show="*",width=15)
        self.password_input.grid(row=4,column=0,columnspan=2,padx=10,pady=10,sticky=tk.NSEW)

        signup=Signup(self.username_input,self.password_input)

        signup_button=tk.Button(signup_frame,text="Sign up",width=20,height=1,command=lambda: signup.create_account(window))
        signup_button.grid(row=5,column=0,padx=10,pady=10,sticky=tk.NSEW)

        cancel_button=tk.Button(signup_frame,text="Cancel",width=20,height=1,command=window.destroy)
        cancel_button.grid(row=5,column=1,padx=10,pady=10,sticky=tk.NSEW)