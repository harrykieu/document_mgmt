import tkinter as tk
from login.showDocGUI import ShowUp
from login.addGUI import AddGUI
from login.removeGUI import RemoveGUI
from main_classes.DocumentBase import DocumentBase as Document
import os
import tkinter.messagebox as messagebox

class DocWindow:
    def __init__(self, document_manage, admin):
        # get the admin status
        self.admin = admin

        # create a new window
        self.window = tk.Tk()
        self.window.title("Document Manager")

        # get the root folder path
        self.root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

        # get document_manage instance from the main.py file
        self.document_manage = document_manage

        # load the background image
        bg_image = tk.PhotoImage(file=f"{self.root_path}\\backgr.png")

        # create a label with the background image as its content
        bg_label = tk.Label(self.window, image=bg_image)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # create a frame to hold the login form
        login_frame = tk.Frame(self.window)
        login_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        # create welcome label
        self.welcome_label = tk.Label(login_frame, text="Welcome to Document Manager!", font=("Helvetica", 20))
        self.welcome_label.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        # create the sub welcome label
        self.sub_welcome_label = tk.Label(login_frame, text="Please select an option from the list below:", font=("Helvetica", 15))
        self.sub_welcome_label.grid(row=1, column=0, columnspan=4, padx=10, pady=10)

        # Add button
        self.add_button = tk.Button(login_frame, text="Add", width=15, height=1, command=lambda: self._add_data(document_manage))
        self.add_button.grid(row=2, column=0, padx=10, pady=10)
        if not (self.admin):
            self.add_button.config(state=tk.DISABLED)

        # Remove button
        self.remove_button = tk.Button(login_frame, text="Remove", width=15, height=1, command=lambda: self._remove_data(document_manage))
        self.remove_button.grid(row=2, column=1, padx=10, pady=10)
        if not (self.admin):
            self.remove_button.config(state=tk.DISABLED)

        # Display button
        self.display_button = tk.Button(login_frame, text="Display", width=15, height=1, command=lambda: self._display_data(document_manage))
        self.display_button.grid(row=2, column=2, padx=10, pady=10)

        # Export button
        self.export_button = tk.Button(login_frame, text="Export to CSV", width=15, height=1, command=lambda: self._export_data(document_manage))
        self.export_button.grid(row=2, column=3, padx=10, pady=10)

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
        displayscr = tk.Toplevel()
        app = ShowUp(document_manage,displayscr)

    def _export_data(self,document_manage):
        document_manage._export_csv()
        messagebox.showinfo("Success", "Export successful!")