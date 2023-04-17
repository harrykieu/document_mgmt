import tkinter as tk
from tkinter import messagebox
import os

class ForgetGUI:
    def __init__(self,window):

        self.window=window
        window.title("Recover Password")
        
        recover_frame=tk.Frame(window)
        recover_frame.pack(padx=10,pady=10)

        prompt_user=tk.Label(recover_frame,text="• For admin account: Contact the developers.",font=("",12,"bold"))
        prompt_user.grid(row=0,column=0,columnspan=2,padx=10,pady=10,sticky=tk.W)

        prompt_user=tk.Label(recover_frame,text="• For user account:",font=("",12,"bold"))
        prompt_user.grid(row=1,column=0,columnspan=2,padx=10,pady=10,sticky=tk.W)
        
        account_label=tk.Label(recover_frame,text="Username:",font=("",10,"bold"))
        account_label.grid(row=2,column=0,columnspan=2,padx=10,pady=10,sticky=tk.W)

        self.account_input=tk.Entry(recover_frame)
        self.account_input.grid(row=3,column=0,columnspan=2,padx=10,pady=10,sticky=tk.NSEW)

        recoverycode_label=tk.Label(recover_frame,text="Recovery Code:",font=("",10,"bold"))
        recoverycode_label.grid(row=4,column=0,columnspan=2,padx=10,pady=10,sticky=tk.W)

        self.recoverycode_input=tk.Entry(recover_frame)
        self.recoverycode_input.grid(row=5,column=0,columnspan=2,padx=10,pady=10,sticky=tk.NSEW)

        recover_button=tk.Button(recover_frame,text="Recover",width=15,height=1,command=self.recover_password)
        recover_button.grid(row=6,column=0,padx=10,pady=10,sticky=tk.NSEW)

        cancel_button=tk.Button(recover_frame,text="Cancel",width=15,height=1,command=window.destroy)
        cancel_button.grid(row=6,column=1,padx=10,pady=10,sticky=tk.NSEW)

    def recover_password(self):
    # Mechanism: If the account exists and the recovery code is correct, show the password
        account=self.account_input.get()
        recoverycode=self.recoverycode_input.get()
        self.parent_path=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        
        # For Windows
        with open(f"{self.parent_path}\\data\\nonadmin.dat") as f: # For Windows
        #with open(f"{self.parent_path}/data/nonadmin.dat") as f: # For Linux
            data=f.read().strip()
            if "End" not in data:
                print(f"Invalid file format for nonadmin.dat")
                return 
            # Split the data into usernames and passwords
            nonadmin_usernames,nonadmin_passwords=data.split("End")
            nonadmin_usernames=nonadmin_usernames.strip().split("\n")
            nonadmin_passwords=nonadmin_passwords.strip().split("\n")
        
        # Get the recovery code
        with open(f"{self.parent_path}\\data\\recovercode.dat") as f: # For Windows
        #with open(f"{self.parent_path}/data/recovercode.dat") as f: # For Linux
            data=f.read().strip()
            nonadmin_recovery=data.strip().split("\n")
        
        # Check if the account exists and the recovery code is correct
        if account in nonadmin_usernames and recoverycode == nonadmin_recovery[nonadmin_usernames.index(account)]:
            password=nonadmin_passwords[nonadmin_usernames.index(account)]
            self.show_password(password)
        else:
            messagebox.showinfo("Error","Invalid recovery code")
            return

    def show_password(self,password):
        window=tk.Toplevel(self.window)
        window.title("Recovered Password")
        password_frame=tk.Frame(window)
        password_frame.pack(padx=10,pady=10)
        password_label=tk.Label(password_frame,text="Password:")
        password_label.pack(padx=10,pady=10)
        password_text=tk.Text(password_frame,height=1,width=30)
        password_text.insert(tk.END,password)
        password_text.config(state="disabled")
        password_text.pack(padx=10,pady=10)
        # insert OK button
        ok_button=tk.Button(password_frame,text="OK",width=10,height=1,command=window.destroy)
        ok_button.pack(padx=10,pady=10)
