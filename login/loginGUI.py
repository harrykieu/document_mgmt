import tkinter as tk
from login.signupGUI import SignupWindow
from login.manageDocumentGUI import DocWindow
import os

class ErrorWindow:
    def __init__(self,window):
        self.window = window
        self.window.title("Error Window")

        error_frame = tk.Frame(window)
        error_frame.pack(pady=10)

        label = tk.Label(error_frame, text="Wrong username and/or password!")
        label.grid(row=0,column=0,padx=10, pady=10)

        ok_button = tk.Button(error_frame, text="OK", command=self.window.destroy)
        ok_button.grid(row=1,column=0,padx=10, pady=10)

        window.mainloop()

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
            error_window = tk.Toplevel(window)
            error_dialog = ErrorWindow(error_window)
            self.username_input.delete(0, tk.END)
            self.password_input.delete(0, tk.END)


class LoginWindow:
    def __init__(self,window,document_manage):
        self.window = window
        self.window.title("Login Window")

        self.document_manage = document_manage

        canvas = tk.Canvas(window, width=800, height=600)
        canvas.place(x=0, y=0)

        # load the background image
        bg_image = tk.PhotoImage(file="/home/hhk/Desktop/document_mgmt/Username.png")

        # add the image to the canvas as the background
        canvas.create_image(0, 0, anchor=tk.NW, image=bg_image)
        # set window size
        window.geometry(f"{800}x{600}")
        #window.resizable(0, 0)

        login_frame = tk.Frame(window)
        login_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        label = tk.Label(login_frame, text="")
        label.place(x=200, y=0)

        username_label = tk.Label(login_frame, text="Username:")
        username_label.place(x=100, y=50)
        self.username_input = tk.Entry(login_frame)
        self.username_input.place(x=200, y=50)

        password_label = tk.Label(login_frame, text="Password:")
        password_label.place(x=100, y=100)
        self.password_input = tk.Entry(login_frame, show="*")
        self.password_input.place(x=200, y=100)

        login = Login(self.username_input, self.password_input)

        signin_button = tk.Button(login_frame, text="Sign In", command=lambda: login.signin(self.document_manage, self.window, label))
        signin_button.place(x=150, y=150)

        signup_button = tk.Button(login_frame, text="Sign Up", command=self.open_signup_window)
        signup_button.place(x=250, y=150)

        window.mainloop()


    def open_signup_window(self):
        signup_window = tk.Toplevel(self.window)
        app = SignupWindow(signup_window)

