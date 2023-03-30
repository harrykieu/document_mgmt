import tkinter as tk
import os
import tkinter.messagebox as messagebox

class ShowGUI:
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



