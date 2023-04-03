import tkinter as tk
import login # to import the loginGUI.py file later
from login.showDocGUI import ShowGUI
from login.addGUI import AddGUI
from login.removeGUI import RemoveGUI
from login.findGUI import FindGUI
import os
import tkinter.messagebox as messagebox
import tkinter.filedialog as filedialog

class DocWindow:
    def __init__(self, document_manage, admin):
        # get the admin status
        self.admin = admin

        # create a new window
        self.window = tk.Tk()
        
        # set custom window title
        if (self.admin==True):
            self.window.title("Document Management System - Admin")
        else:
            self.window.title("Document Management System - User")

        # get the root folder path
        self.root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

        # get document_manage instance from the main.py file
        self.document_manage = document_manage

        # load the background image
        #bg_image = tk.PhotoImage(file=f"{self.root_path}\\backgr.png") # For Windows
        bg_image = tk.PhotoImage(file=f"{self.root_path}/backgr.png") # For Linux

        # create a label with the background image as its content
        bg_label = tk.Label(self.window, image=bg_image)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # create a frame to hold the login form
        login_frame = tk.Frame(self.window,bg="white")
        login_frame.place(relx=0.5,rely=0.5,anchor=tk.CENTER)
        #login_frame.pack(padx=10, pady=10)

        # create welcome label
        self.welcome_label = tk.Label(login_frame, text="Welcome to Document Management System!", font=("Arial", 20),bg="white")
        self.welcome_label.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

        # create the sub welcome label
        self.sub_welcome_label = tk.Label(login_frame, text="Please select an option from the list below:", font=("Arial", 15),bg="white")
        self.sub_welcome_label.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

        # Add button
        self.add_button = tk.Button(login_frame, text="Add", width=15, height=2, command=lambda: self._add_data(document_manage))
        self.add_button.grid(row=2, column=0, padx=10, pady=10)
        if not (self.admin):
            self.add_button.config(state=tk.DISABLED) # disable the button if the user is not an admin

        # Remove button
        self.remove_button = tk.Button(login_frame, text="Remove", width=15, height=2, command=lambda: self._remove_data(document_manage))
        self.remove_button.grid(row=2, column=1, padx=10, pady=10)
        if not (self.admin):
            self.remove_button.config(state=tk.DISABLED) # disable the button if the user is not an admin

        # Import button
        self.import_button = tk.Button(login_frame, text="Import from CSV", width=15, height=2, command=lambda: self._import_data(document_manage))
        self.import_button.grid(row=2, column=2, padx=10, pady=10)
        if not (self.admin):
            self.import_button.config(state=tk.DISABLED) # disable the button if the user is not an admin
        
        # Display button
        self.display_button = tk.Button(login_frame, text="Display", width=15, height=2, command=lambda: self._display_data(document_manage))
        self.display_button.grid(row=3, column=0, padx=10, pady=10)

        # Find button
        self.find_button = tk.Button(login_frame, text="Find", width=15, height=2, command=lambda: self._find_data(document_manage))
        self.find_button.grid(row=3, column=1, padx=10, pady=10)

        # Export button
        self.export_button = tk.Button(login_frame, text="Export to CSV", width=15, height=2, command=lambda: self._export_data(document_manage))
        self.export_button.grid(row=3, column=2, padx=10, pady=10)
        
        # Logout button
        self.logout_button = tk.Button(login_frame, text="Logout",  width=15, height=2, command=lambda: self._logout(self.document_manage,self.window))
        self.logout_button.grid(row=4, column=1, padx=10, pady=10)

        # set window size and disable resizing
        self.window.geometry(f"{bg_image.width()}x{bg_image.height()}")
        self.window.resizable(0, 0)

        self.window.mainloop()

    def _add_data(self,document_manage):
        displayscr = tk.Toplevel()
        app = AddGUI(document_manage,displayscr)

    def _remove_data(self,document_manage):
        displayscr = tk.Toplevel()
        app = RemoveGUI(document_manage,displayscr)

    def _display_data(self,document_manage):
        if document_manage._get_total_document() == 0:
            messagebox.showerror("Error", "No document to display!")
            return # no document to export
        displayscr = tk.Toplevel()
        app = ShowGUI(document_manage,displayscr)

    def _find_data(self,document_manage):
        if document_manage._get_total_document() == 0:
            messagebox.showerror("Error", "No document to find!")
            return # no document to export
        displayscr = tk.Toplevel()
        app = FindGUI(document_manage,displayscr)

    def _export_data(self,document_manage):
        if document_manage._get_total_document() == 0:
            messagebox.showerror("Error", "No document to export!")
            return # no document to export
        self.file_path = filedialog.asksaveasfilename(title = "Save As", filetypes = (("CSV files","*.csv"),), defaultextension = ".csv")
        if self.file_path == "":
            return # user cancelled
        else:
            document_manage._export_csv(self.file_path)
            messagebox.showinfo("Success", f"Export successful!")
    
    def _import_data(self,document_manage):
        self.file_path = filedialog.askopenfilename(title = "Open", filetypes = (("CSV files","*.csv"),), defaultextension = ".csv")
        if self.file_path == "":
            return # user cancelled
        else:
            self.success = document_manage._import_csv(self.file_path)
            if self.success == False:
                messagebox.showerror("Error", f"Import unsuccessful! Please check CSV file.")
            else:
                messagebox.showinfo("Success", f"Import successful!")

    def _logout(self,document_manage,window):
        window.destroy()
        displayscr = tk.Tk()
        window = login.loginGUI.LoginGUI(document_manage,displayscr) # avoid circular import