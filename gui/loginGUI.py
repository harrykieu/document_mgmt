import tkinter as tk
from gui.signupGUI import SignupGUI
from gui.manageGUI import DocWindow
from gui.forgetGUI import ForgetGUI
import os
import tkinter.messagebox as messagebox

class LoginLogic:
    def __init__(self,username_input,password_input):
        self.username_input = username_input
        self.password_input = password_input
        self.parent_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    def check_user_pass(file_path,username,password):
        # Check the format of data.dat file
        with open(file_path) as f:
            data = f.read().strip()
            if "End" not in data:
                print(f"Invalid file format of {file_path}")
                return False
            usernames,passwords = data.split("End")
            usernames = usernames.strip().split("\n")
            passwords = passwords.strip().split("\n")
        # Check if the username and password are correct
        for i in range(len(usernames)):
            if usernames[i] == username and passwords[i] == password:
                return True
        return False

    def signin(self,document_manage,window):
        # get the username and password from the input fields
        username = self.username_input.get()
        password = self.password_input.get()
        if username == "" or password == "":
            # Display the error message on new window
            tk.messagebox.showerror("Error","Wrong username and/or password!")
            self.username_input.delete(0,tk.END)
            self.password_input.delete(0,tk.END)
            return

        # get the parent path
        self.parent_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        
        # File admin.dat always exists, so check if the username and password are correct
        # For admin user
        #if LoginLogic.check_user_pass(f"{self.parent_path}/data/admin.dat",username,password): # For Linux
        if LoginLogic.check_user_pass(f"{self.parent_path}\\data\\admin.dat",username,password): # For Windows
            window.destroy()
            window = DocWindow(document_manage,admin=True)
        else:
            # Check if file nonadmin.dat not exists, then display the error message 

            #if not os.path.exists(f"{self.parent_path}/data/nonadmin.dat"): # For Linux
            if not os.path.exists(f"{self.parent_path}\\data\\nonadmin.dat"): # For Windows
                # display the error message on new window
                tk.messagebox.showerror("Error","No users available! You must sign up first!")
                self.username_input.delete(0,tk.END)
                self.password_input.delete(0,tk.END)
                return
            
            # If file nonadmin.dat exists, then check if the username and password are correct

            #if LoginLogic.check_user_pass(f"{self.parent_path}/data/nonadmin.dat",username,password): # For Linux
            if LoginLogic.check_user_pass(f"{self.parent_path}\\data\\nonadmin.dat",username,password): # For Windows
                window.destroy()
                window = DocWindow(document_manage,admin=False)
            else:
                # Display the error message on new window
                tk.messagebox.showerror("Error","Wrong username and/or password!")
                self.username_input.delete(0,tk.END)
                self.password_input.delete(0,tk.END)
            
class LoginGUI:
    def __init__(self,document_manage,window):
        self.window = window
        self.window.title("Login")

        # get the root folder path
        self.parent_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

        # get document_manage instance from the main.py file
        self.document_manage = document_manage

        # load the background image
        bg_image = tk.PhotoImage(file=f"{self.parent_path}\\backgr.png") # For Windows
        #bg_image = tk.PhotoImage(file=f"{self.parent_path}/backgr.png") # For Linux

        # create a label with the background image as its content
        bg_label = tk.Label(self.window,image=bg_image)
        bg_label.place(x=0,y=0,relwidth=1,relheight=1)

        # create a frame to hold the login form
        login_frame = tk.Frame(self.window,bg="white")
        login_frame.place(relx=0.5,rely=0.5,anchor=tk.CENTER)

        # create the Document Management System label
        dms_label = tk.Label(login_frame,text="DOCUMENT MANAGEMENT SYSTEM",bg="white",font=("",20,"bold"))
        dms_label.grid(row=0,column=0,columnspan=2,padx=10,pady=10,sticky=tk.NSEW)

        # create the login form elements: username, password, login button, signup button, "forgot password" link
        username_label = tk.Label(login_frame,text="Username:",bg="white",font=("",12,"bold"))
        username_label.grid(row=1,column=0,padx=10,pady=10,sticky=tk.W)
        self.username_input = tk.Entry(login_frame,width=60)
        self.username_input.grid(row=1,column=1,padx=10,pady=10,sticky=tk.NSEW)

        password_label = tk.Label(login_frame,text="Password:",bg="white",font=("",12,"bold"))
        password_label.grid(row=2,column=0,padx=10,pady=10,sticky=tk.W)
        self.password_input = tk.Entry(login_frame,show="*",width=60) # hide the password
        self.password_input.grid(row=2,column=1,padx=10,pady=10,sticky=tk.NSEW)

        # create the Login instance
        login = LoginLogic(self.username_input,self.password_input)

        # create the login button
        login_button = tk.Button(login_frame,text="SIGN IN",font=("",12,"bold"),height=2,background="#1E88E5",foreground="white",command=lambda: login.signin(self.document_manage,self.window))
        login_button.grid(row=3,column=0,columnspan=2,padx=10,pady=10,sticky=tk.NSEW)

        # create the "sign up" link
        signup_link = tk.Label(login_frame,text="No account? Sign up here.",bg="white",font=("",12),cursor="hand2",fg="blue")
        signup_link.grid(row=4,column=0,columnspan=2,padx=10,pady=10,sticky=tk.NSEW)
        signup_link.bind("<Button-1>",self._open_signup_window)

        # create the "forgot password" link
        forget_label = tk.Label(login_frame,text="Forget password?",bg="white",font=("",12),cursor="hand2",fg="blue")
        forget_label.grid(row=5,column=0,columnspan=2,padx=10,pady=10,sticky=tk.NSEW)
        forget_label.bind("<Button-1>",self._open_forget_window)

        # Credit
        credit_label = tk.Label(login_frame,text="© 2023 DQ/USTH",bg="white",font=("",8,"bold"),cursor="hand2",fg="blue")
        credit_label.grid(row=6,column=0,columnspan=2,padx=10,pady=10,sticky=tk.NSEW)
        credit_label.bind("<Button-1>",self._open_credit_window)

        # set window size the same as image size and disable resizing
        self.window.geometry(f"{bg_image.width()}x{bg_image.height()}")
        self.window.resizable(0,0)

        self.window.mainloop()

    def _open_signup_window(self,event):
        signup_window = tk.Toplevel(self.window)
        app = SignupGUI(signup_window)

    def _open_forget_window(self,event):
        forget_window = tk.Toplevel(self.window)
        app = ForgetGUI(forget_window)

    def _open_credit_window(self,event):
        messagebox.showinfo("Credit","""This application is developed by:
    - Doan Tri Tien - BI12-435
    - Kieu Huy Hai - BI12-149
    - Vu Duc Hieu - BI12-162
    - Bui Cong Hoang - BI12-169
    - Le Trong Tan - BI12-395
P/S: Plz give us extra points ;)""")

