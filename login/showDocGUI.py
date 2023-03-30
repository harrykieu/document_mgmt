import tkinter as tk
import os
import tkinter.messagebox as messagebox
from tkinter import ttk

class ShowGUI:
    def __init__(self, document_manager, window):
        # get the data 
        self.documents = document_manager._get_all_documents()
        if self.documents == None:
            messagebox.showerror("Error", "No document found!")
            window.destroy()
            # exit
            return
        
        # create a window
        self.window = window
        window.title("All Documents")

        self.tabledoc = ttk.Treeview(window, columns=("Name", "Author", "Publisher", "Year Published", "Note"))
        self.tabledoc.pack(padx=10, pady=10)

        # set the column width
        self.tabledoc.column("#0", width=50, stretch=tk.NO)
        self.tabledoc.column("Name", width=200, stretch=tk.NO)
        self.tabledoc.column("Author", width=200, stretch=tk.NO)
        self.tabledoc.column("Year Published", width=200, stretch=tk.NO)
        self.tabledoc.column("Publisher", width=200, stretch=tk.NO)
        self.tabledoc.column("Note", width=300, stretch=tk.NO)

        # create the table headers
        self.tabledoc.heading("#0", text="ID", anchor=tk.CENTER)
        self.tabledoc.heading("Name", text="Name", anchor=tk.CENTER)
        self.tabledoc.heading("Author", text="Author", anchor=tk.CENTER)
        self.tabledoc.heading("Year Published", text="Year Published", anchor=tk.CENTER)
        self.tabledoc.heading("Publisher", text="Publisher", anchor=tk.CENTER)
        self.tabledoc.heading("Note", text="Note", anchor=tk.CENTER)
        
        # display the data in the table
        for i, document in enumerate(self.documents):
            self.tabledoc.insert(parent="", index=i+1, text=i+1, values=(document._get_name(), document._get_author(), document._get_publisher(), document._get_yearPublish(), document._get_note()))

        self.window.mainloop()