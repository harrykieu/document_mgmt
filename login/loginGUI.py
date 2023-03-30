import tkinter as tk
from login.signupGUI import SignupGUI
from login.manageGUI import DocWindow
from login.forgetGUI import ForgetGUI
import os

class LoginLogic:
    def __init__(self, username_input, password_input):
        self.username_input = username_input
        self.password_input = password_input
        self.root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    def check_user_pass(file_path, username, password):
        with open(file_path) as f:
            data = f.read().strip()
            if "\nEnd\n" not in data:
                print("Invalid file format")
                return False
            usernames, passwords = data.split("\nEnd\n")
            usernames = usernames.strip().split("\n")
            passwords = passwords.strip().split("\n")

        for i in range(len(usernames)):
            if usernames[i] == username and passwords[i] == password:
                return True
        return False

    def signin(self,document_manage,window):
        # get the username and password from the input fields
        username = self.username_input.get()
        password = self.password_input.get()

        # check if the username and password are correct
        if LoginLogic.check_user_pass(f"{self.root_path}/data/admin.dat", username, password): # For Linux
        # if LoginLogic.check_user_pass(f"{self.root_path}\\data\\admin.dat", username, password): # For Windows
            window.destroy()
            window = DocWindow(document_manage, admin=True)
        elif LoginLogic.check_user_pass(f"{self.root_path}/data/nonadmin.dat", username, password): # For Linux
        # elif LoginLogic.check_user_pass(f"{self.root_path}\\data\\nonadmin.dat", username, password): # For Windows
            window.destroy()
            window = DocWindow(document_manage, admin=False)
        else:
            # display the error message on new window
            tk.messagebox.showerror("Error", "Wrong username and/or password!")
            self.username_input.delete(0, tk.END)
            self.password_input.delete(0, tk.END)


class LoginGUI:
    def __init__(self, document_manage, window):
        self.window = window
        self.window.title("Login    ")

        # get the root folder path
        self.root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

        # get document_manage instance from the main.py file
        self.document_manage = document_manage

        # load the background image
        # bg_image = tk.PhotoImage(file=f"{self.root_path}\\backgr.png") # For Windows
        bg_image = tk.PhotoImage(file=f"{self.root_path}/backgr.png") # For Linux

        # create a label with the background image as its content
        bg_label = tk.Label(self.window, image=bg_image)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # create a frame to hold the login form
        login_frame = tk.Frame(self.window)
        login_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        # create the login form elements: username, password, login button, signup button, "forgot password" link
        username_label = tk.Label(login_frame, text="Username:")
        username_label.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)
        self.username_input = tk.Entry(login_frame)
        self.username_input.grid(row=0, column=1, padx=10, pady=10)

        password_label = tk.Label(login_frame, text="Password:")
        password_label.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)
        self.password_input = tk.Entry(login_frame, show="*")
        self.password_input.grid(row=1, column=1, padx=10, pady=10)

        # create the Login instance
        login = LoginLogic(self.username_input, self.password_input)

        # create the login button
        login_button = tk.Button(login_frame, text="Sign In", command=lambda: login.signin(self.document_manage, self.window))
        login_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky=tk.NSEW)

        # create the "sign up" link
        signup_link = tk.Label(login_frame, text="No account? Sign up here.", cursor="hand2", fg="blue")
        signup_link.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky=tk.NSEW)
        signup_link.bind("<Button-1>", self.open_signup_window)

        # create the "forgot password" link
        forget_label = tk.Label(login_frame, text="Forget password?", cursor="hand2", fg="blue")
        forget_label.grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky=tk.NSEW)
        forget_label.bind("<Button-1>", self.open_forget_window)

        # set window size and disable resizing
        self.window.geometry(f"{bg_image.width()}x{bg_image.height()}")
        self.window.resizable(0, 0)

        self.window.mainloop()

    def open_signup_window(self,event):
        signup_window = tk.Toplevel(self.window)
        app = SignupGUI(signup_window)

    def open_forget_window(self, event):
        forget_window = tk.Toplevel(self.window)
        app = ForgetGUI(forget_window)



