import tkinter as tk
from tkinter import messagebox
import os

class Signup:
    def __init__(self, username_input, password_input, recovery_code_input):
        self.username_input = username_input
        self.password_input = password_input
        self.recovery_code_input = recovery_code_input

    def create_account(self):
        username = self.username_input.get()
        password = self.password_input.get()
        recovery_code = self.recovery_code_input.get()
        self.parent_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


        with open(f"{self.parent_path}/data/nonadmin.dat") as f:
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

        with open(f"{self.parent_path}/data/nonadmin.dat", "w") as f:
            f.write("\n".join(usernames) + "\nEnd\n" + "\n".join(passwords))

        with open(f"{self.parent_path}/data/data.dat") as f:
            data = f.read().strip()
            if "\nEnd\n" not in data:
                print("Invalid file format")
                return
            admin_codes, user_codes = data.split("\nEnd\n")
            user_codes = user_codes.strip().split("\n")

        user_codes.append(recovery_code)

        with open(f"{self.parent_path}/data/data.dat", "w") as f:
            f.write(admin_codes + "\nEnd\n" + "\n".join(user_codes))

        messagebox.showinfo("Success", "Account created successfully.")

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

        recovery_code_label = tk.Label(signup_frame, text="Recovery Code:")
        recovery_code_label.grid(row=2,column=0,padx=10, pady=10)
        self.recovery_code_input = tk.Entry(signup_frame)
        self.recovery_code_input.grid(row=2,column=1,padx=10, pady=10)

        signup = Signup(self.username_input, self.password_input, self.recovery_code_input)
        signup_button = tk.Button(signup_frame, text="Sign up", width=10, height = 1, command=signup.create_account)
        signup_button.grid(row=3,column=0,padx=10, pady=10, sticky=tk.NSEW)

        cancel_button = tk.Button(signup_frame, text="Cancel",  width=10, height = 1, command=window.destroy)
        cancel_button.grid(row=3,column=1,padx=10, pady=10, sticky=tk.NSEW)