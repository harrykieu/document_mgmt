import tkinter as tk
from submit import Login
from signup import SignupWindow

class LoginWindow:
    def __init__(self, master):
        self.master = master
        master.title("Login Window")

        logo_image = tk.PhotoImage(file="3.png")
        logo_label = tk.Label(master, image=logo_image)
        logo_label.pack(side=tk.LEFT, padx=10, pady=10)

        login_frame = tk.Frame(master)
        login_frame.pack(side=tk.RIGHT, padx=10, pady=10)

        username_label = tk.Label(login_frame, text="Username:")
        username_label.pack(padx=10, pady=10)
        self.username_input = tk.Entry(login_frame)
        self.username_input.pack(padx=10, pady=10)

        password_label = tk.Label(login_frame, text="Password:")
        password_label.pack(padx=10, pady=10)
        self.password_input = tk.Entry(login_frame, show="*")
        self.password_input.pack(padx=10, pady=10)

        login = Login(self.username_input, self.password_input)
        signin_button = tk.Button(login_frame, text="Sign In", command=login.signin)
        signin_button.pack(padx=10, pady=10)       

        signup_button = tk.Button(login_frame, text="Sign Up", command=self.open_signup_window)
        signup_button.pack(padx=10, pady=10)
        
    def open_signup_window(self):
        signup_window = tk.Toplevel(self.master)
        app = SignupWindow(signup_window)

root = tk.Tk()
app = LoginWindow(root)
root.mainloop()
