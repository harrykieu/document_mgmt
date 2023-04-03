import tkinter as tk
from tkinter import messagebox
import os

class ForgetGUI:
    def __init__(self, window):

        self.window = window
        window.title("Recover Password")
        
        recover_frame = tk.Frame(window)
        recover_frame.pack(padx=10, pady=10)

        account_label = tk.Label(recover_frame, text="Username:")
        account_label.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)
        self.account_input = tk.Entry(recover_frame)
        self.account_input.grid(row=0, column=1, padx=10, pady=10, sticky=tk.W)

        recoverycode_label = tk.Label(recover_frame, text="Recovery Code:")
        recoverycode_label.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)
        self.recoverycode_input = tk.Entry(recover_frame)
        self.recoverycode_input.grid(row=1, column=1, padx=10, pady=10, sticky=tk.W)

        recover_button = tk.Button(recover_frame, text="Recover", width=10, height = 1, command=self.recover_password)
        recover_button.grid(row=2, column=0, padx=10, pady=10, sticky=tk.NSEW)

        cancel_button = tk.Button(recover_frame, text="Cancel", width=10, height = 1, command=window.destroy)
        cancel_button.grid(row=2, column=1, padx=10, pady=10, sticky=tk.NSEW)

    def read_accounts(self, filename):
        with open(filename) as f:
            data = f.read().strip()
            if "End" not in data:
                print(f"Invalid file format: {filename}")
                return [], []
            usernames, passwords = data.split("End")
            usernames = usernames.strip().split("\n")
            passwords = passwords.strip().split("\n")
            return usernames, passwords

    def recover_password(self):
        account = self.account_input.get()
        recoverycode = self.recoverycode_input.get()
        self.parent_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        
        # For Windows
        admin_usernames, admin_passwords = self.read_accounts(f"{self.parent_path}\\data\\admin.dat") 
        nonadmin_usernames, nonadmin_passwords = self.read_accounts(f"{self.parent_path}\\data\\nonadmin.dat")
        
        # For Linux
        # admin_usernames, admin_passwords = self.read_accounts(f"{self.parent_path}/data/admin.dat")
        # nonadmin_usernames, nonadmin_passwords = self.read_accounts(f"{self.parent_path}/data/nonadmin.dat")
        
        with open(f"{self.parent_path}\\data\\data.dat") as f: # For Windows
        #with open(f"{self.parent_path}/data/data.dat") as f: # For Linux
            data = f.read().strip()
            if "End" not in data:
                print("Invalid file format")
                return
            admin_recovery, nonadmin_recovery = data.split("End")
            admin_recovery = admin_recovery.strip().split("\n")
            nonadmin_recovery = nonadmin_recovery.strip().split("\n")
            
        if account in admin_usernames and recoverycode == admin_recovery[admin_usernames.index(account)]:
            password = admin_passwords[admin_usernames.index(account)]
            self.show_password(password)
        elif account in nonadmin_usernames and recoverycode == nonadmin_recovery[nonadmin_usernames.index(account)]:
            password = nonadmin_passwords[nonadmin_usernames.index(account)]
            self.show_password(password)
        else:
            messagebox.showinfo("Oh no", "Invalid recovery code")
            print("Invalid recovery code")
            return


    def show_password(self, password):
        password_window = tk.Toplevel(self.window)
        password_window.title("Recovered Password")
        password_frame = tk.Frame(password_window)
        password_frame.pack(padx=10, pady=10)
        password_label = tk.Label(password_frame, text="Password:")
        password_label.pack(padx=10, pady=10)
        password_text = tk.Text(password_frame, height=1, width=30)
        password_text.insert(tk.END, password)
        password_text.config(state="disabled")
        password_text.pack(padx=10, pady=10)
        # insert OK button
        ok_button = tk.Button(password_frame, text="OK", width=10, height = 1, command=password_window.destroy)
        ok_button.pack(padx=10, pady=10)
#enter username and recovery code to get there own password
# (recovery code is the code user use to remember like user phone number)