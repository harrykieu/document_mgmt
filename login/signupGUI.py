import tkinter as tk
from tkinter import messagebox
import os
import random
import string

class Signup:
    def __init__(self, username_input, password_input):
        self.username_input = username_input
        self.password_input = password_input
        self.recovery_code = ''

    def create_account(self):
        username = self.username_input.get()
        password = self.password_input.get()
        self.recovery_code = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(4))
        self.parent_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        

        if not all([username, password]):
            messagebox.showerror("Error", "Please fill in all fields.")
            return


        with open(f"{self.parent_path}/data/nonadmin.dat") as f: # For Linux
        # with open(f"{self.parent_path}\data\nonadmin.dat") as f: # For Windows
            data = f.read().strip()
            if "\nEnd\n" not in data:
                print("Invalid file format")
                return
            usernames, passwords = data.split("\nEnd\n")
            usernames = usernames.strip().split("\n")
            passwords = passwords.strip().split("\n")

        if username in usernames:
            print("Username is already taken.")
            return

        usernames.append(username)
        passwords.append(password)

        with open(f"{self.parent_path}/data/nonadmin.dat", "w") as f: # For Linux
        # with open(f"{self.parent_path}\data\nonadmin.dat", "w") as f: # For Windows
            f.write("\n".join(usernames) + "\nEnd\n" + "\n".join(passwords))

        with open(f"{self.parent_path}/data/data.dat") as f: # For Linux
        # with open(f"{self.parent_path}\data\data.dat") as f: # For Windows
            data = f.read().strip()
            if "\nEnd\n" not in data:
                print("Invalid file format")
                return
            admin_codes, user_codes = data.split("\nEnd\n")
            user_codes = user_codes.strip().split("\n")

        with open(f"{self.parent_path}/data/data.dat", "w") as f: # For Linux
        # with open(f"{self.parent_path}\data\data.dat", "w") as f: # For Windows
            f.write(admin_codes + "\nEnd\n" + "\n".join(user_codes))

        with open(f"{self.parent_path}/data/data.dat") as f:
            data = f.read().strip()
            if "\nEnd\n" not in data:
                print("Invalid file format")
                return
            admin_codes, user_codes = data.split("\nEnd\n")
            user_codes = user_codes.strip().split("\n")

        user_codes.append(self.recovery_code)

        with open(f"{self.parent_path}/data/data.dat", "w") as f:
            f.write(admin_codes + "\nEnd\n" + "\n".join(user_codes))

        messagebox.showinfo("Success", f"Account created successfully.\nRecovery code: {self.recovery_code}")

class SignupGUI:
    def __init__(self, window):
        self.window = window
        window.title("Signup")
        window.resizable(0,0)

        signup_frame = tk.Frame(window)
        signup_frame.pack(padx=10, pady=10)

        username_label = tk.Label(signup_frame, text="Username:")
        username_label.grid(row=0,column=0,padx=10, pady=10)
        self.username_input = tk.Entry(signup_frame)
        self.username_input.grid(row=0,column=1,padx=10, pady=10)

        password_label = tk.Label(signup_frame, text="Password:")
        password_label.grid(row=1,column=0,padx=10, pady=10)
        self.password_input = tk.Entry(signup_frame, show="*")
        self.password_input.grid(row=1,column=1,padx=10, pady=10)

        forget_label = tk.Label(signup_frame, text="(After signup i will give you recovery code to use when you forget password)", cursor="hand2", fg="blue")
        forget_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky=tk.NSEW)

        signup = Signup(self.username_input, self.password_input)
        signup_button = tk.Button(signup_frame, text="Sign up", width=10, height = 1, command=signup.create_account)
        signup_button.grid(row=4,column=0,padx=10, pady=10, sticky=tk.NSEW)

        cancel_button = tk.Button(signup_frame, text="Cancel",  width=10, height = 1, command=window.destroy)
        cancel_button.grid(row=4,column=1,padx=10, pady=10, sticky=tk.NSEW)