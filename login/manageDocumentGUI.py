import tkinter as tk
from login.showDocumentGUI import ShowUp
from login.addGUI import AddWindow
from main_classes.DocumentBase import DocumentBase as Document

class DocWindow:
    def __init__(self, document_manager, admin):
        self.admin = admin
        window = tk.Tk()
        window.title("Document Manager")

        frame = tk.Frame(window)
        frame.grid(padx=10, pady=10)

        # Add data
        if self.admin:
            self.add_button = tk.Button(frame, text="Add", command=lambda: self.add_data(document_manager))
            self.add_button.grid(row=0, column=0, padx=10, pady=10)

        # Remove button
        self.remove_button = tk.Button(frame, text="Remove", command=lambda: self.remove_data(document_manager))
        self.remove_button.grid(row=0, column=1, padx=10, pady=10)

        # Display button
        self.display_button = tk.Button(frame, text="Display", command=lambda: self.display_data(document_manager))
        self.display_button.grid(row=0, column=2, padx=10, pady=10)

        window.mainloop()

    def add_data(self,document_manager):
        displayscr = tk.Toplevel()
        app = AddWindow(document_manager,displayscr)

    def remove_data(self,document_manager):
        remove_name = self.remove_entry.get()
        document_manager._del_document(remove_name)

    def display_data(self,document_manager):
        displayscr = tk.Toplevel()
        app = ShowUp(document_manager,displayscr)

