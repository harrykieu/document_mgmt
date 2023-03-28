import tkinter as tk
import os
import sys
import subprocess
import tkinter.messagebox as messagebox

class ShowUp:
    def __init__(self, document_manager, window):
        self.window = window
        window.title("All Documents")

        # create a table to display the data
        self.listdoc = tk.Frame(window)
        self.listdoc.pack(padx=10, pady=10)

        # get the root folder path
        self.root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

        # create the table headers
        self.name_label = tk.Label(self.listdoc, text="Name")
        self.name_label.grid(row=0, column=0, padx=10, pady=10, sticky=tk.NSEW)

        self.author_label = tk.Label(self.listdoc, text="Author")
        self.author_label.grid(row=0, column=1, padx=10, pady=10, sticky=tk.NSEW)

        self.publisher_label = tk.Label(self.listdoc, text="Publisher")
        self.publisher_label.grid(row=0, column=2, padx=10, pady=10, sticky=tk.NSEW)

        self.yearPublish_label = tk.Label(self.listdoc, text="Year Published")
        self.yearPublish_label.grid(row=0, column=3, padx=10, pady=10, sticky=tk.NSEW)

        self.note_label = tk.Label(self.listdoc, text="Note")
        self.note_label.grid(row=0, column=4, padx=10, pady=10, sticky=tk.NSEW)

        # get the data 
        self.documents = document_manager._get_all_documents()
        if self.documents == None:
            messagebox.showerror("Error", "No document found!")
            window.destroy()
            # exit
            return
        
        # display the data in the table
        for i, document in enumerate(self.documents):
            name_label = tk.Label(self.listdoc, text=document._get_name())
            name_label.grid(row=i+1, column=0, padx=10, pady=10, sticky=tk.NSEW)

            author_label = tk.Label(self.listdoc, text=document._get_author())
            author_label.grid(row=i+1, column=1, padx=10, pady=10, sticky=tk.NSEW)

            publisher_label = tk.Label(self.listdoc, text=document._get_publisher())
            publisher_label.grid(row=i+1, column=2, padx=10, pady=10, sticky=tk.NSEW)

            yearPublish_label = tk.Label(self.listdoc, text=document._get_yearPublish())
            yearPublish_label.grid(row=i+1, column=3, padx=10, pady=10, sticky=tk.NSEW)

            note_label = tk.Label(self.listdoc, text=document._get_note())
            note_label.grid(row=i+1, column=4, padx=10, pady=10, sticky=tk.NSEW)

        # create a list to store the filenames
        self.filenames = []

        # display the filenames in a listbox
        self.listbox = tk.Listbox(window, height=10)
        self.listbox.pack(padx=10, pady=10)

        for document in self.documents:
            # add the filename to the list
            self.filenames.append(document._get_name())

            # add the filename to the listbox
            self.listbox.insert(tk.END, document._get_name())

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



