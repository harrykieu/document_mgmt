import tkinter as tk
import os
import sys
import subprocess
import tkinter.messagebox as messagebox

class ShowUp:
    def __init__(self, document_manager, window):
        self.window = window
        window.title("Document Manager")

        # create a table to display the data
        self.table = tk.Frame(window)
        self.table.pack(padx=10, pady=10)

        # create the headers
        self.name_label = tk.Label(self.table, text="Name")
        self.name_label.grid(row=0, column=0)

        self.author_label = tk.Label(self.table, text="Author")
        self.author_label.grid(row=0, column=1)

        self.publisher_label = tk.Label(self.table, text="Publisher")
        self.publisher_label.grid(row=0, column=2)

        self.yearPublish_label = tk.Label(self.table, text="Year Published")
        self.yearPublish_label.grid(row=0, column=3)

        self.note_label = tk.Label(self.table, text="Note")
        self.note_label.grid(row=0, column=4)

        # get the data 
        self.documents = document_manager._get_all_documents()

        # display the data in the table
        for i, document in enumerate(self.documents):
            name_label = tk.Label(self.table, text=document._get_name())
            name_label.grid(row=i+1, column=0)

            author_label = tk.Label(self.table, text=document._get_author())
            author_label.grid(row=i+1, column=1)

            publisher_label = tk.Label(self.table, text=document._get_publisher())
            publisher_label.grid(row=i+1, column=2)

            yearPublish_label = tk.Label(self.table, text=document._get_yearPublish())
            yearPublish_label.grid(row=i+1, column=3)

            note_label = tk.Label(self.table, text=document._get_note())
            note_label.grid(row=i+1, column=4)

              # create a list to store the filenames
        self.filenames = []

        # display the filenames in a listbox
        self.listbox = tk.Listbox(window, height=10)
        self.listbox.pack(padx=10, pady=10)

        for document in self.documents:
            # add the filename to the list
            self.filenames.append(document["name"])

            # add the filename to the listbox
            self.listbox.insert(tk.END, document["name"])

        # bind the listbox to a function that opens the selected file
        self.listbox.bind("<Double-Button-1>", self.open_file)

    def open_file(self, event):
        # get the selected filename from the listbox
        selected_index = self.listbox.curselection()
        if selected_index:
            selected_filename = self.filenames[selected_index[0]]

            # check if the file exists
            if os.path.exists(selected_filename):
                # open the file using the default application for its file type
                opener = "open" if sys.platform == "darwin" else "xdg-open"
                subprocess.call([opener, selected_filename])
            else:
                # display an error message if the file does not exist
                tk.messagebox.showerror("Error", "File not found!")



