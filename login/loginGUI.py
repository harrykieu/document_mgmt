import tkinter as tk
from login.signupGUI import SignupWindow
from login.manageDocumentGUI import DocWindow
import os

class Login:
    def __init__(self, username_input, password_input):
        self.username_input = username_input
        self.password_input = password_input
        self.parent_path = (os.path.dirname(os.path.abspath(__file__)))

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

    def signin(self,document_manage,window,label):
        username = self.username_input.get()
        password = self.password_input.get()

        if Login.check_user_pass(f"{self.parent_path}/admin.dat", username, password):
            window.destroy()
            window = DocWindow(document_manage, admin=True)
            window.show_options()
        elif Login.check_user_pass(f"{self.parent_path}/nonadmin.dat", username, password):
            window.destroy()
            window = DocWindow(document_manage, admin=False)
            window.show_options()
        else:
            self.username_input.delete(0, tk.END)
            self.password_input.delete(0, tk.END)
            label.config(text="Invalid username or password! Please try again.")


class LoginWindow:
    def __init__(self, window,document_manage):
        self.window = window
        self.window.title("Login Window")

        # Create a DocumentManage instance that will be passed later
        self.document_manage = document_manage

        login_frame = tk.Frame(window)
        login_frame.pack(side=tk.TOP, padx=100, pady=100)

        label = tk.Label(login_frame, text="")
        label.pack(side=tk.TOP, padx=100, pady=100)

        username_label = tk.Label(login_frame, text="Username:")
        username_label.pack(padx=10, pady=10)
        self.username_input = tk.Entry(login_frame)
        self.username_input.pack(padx=10, pady=10)

        password_label = tk.Label(login_frame, text="Password:")
        password_label.pack(padx=10, pady=10)
        self.password_input = tk.Entry(login_frame, show="*")
        self.password_input.pack(padx=10, pady=10)

        login = Login(self.username_input, self.password_input)

        signin_button = tk.Button(login_frame, text="Sign In", command=lambda: login.signin(self.document_manage,self.window,label))
        signin_button.pack(padx=10, pady=10)       

        signup_button = tk.Button(login_frame, text="Sign Up", command=self.open_signup_window)
        signup_button.pack(padx=10, pady=10)

        window.mainloop()

    def open_signup_window(self):
        signup_window = tk.Toplevel(self.window)
        app = SignupWindow(signup_window)

