import tkinter as tk
from main_classes.DocumentBase import DocumentBase
from main_classes.DocumentManage import DocumentManage
class AddWindow:
    def __init__(self, document_manage, window):

        self.window = window
        window.title("Add Document")

        # Add frame
        add_frame = tk.Frame(window)
        add_frame.grid(padx=10, pady=10)

        # Add a big title to the window with the string "Document signup"
        title = tk.Label(add_frame, text="Add Document", font=("Helvetica", 16))
        title.grid(row=0, column=0, columnspan=2, sticky='nsew')

        # Add success label
        self.add_success_label = tk.Label(add_frame, text="")
        self.add_success_label.grid(row=1, column=0, columnspan=2, sticky='nsew')

        # Name
        name_label = tk.Label(add_frame, text="Name:")
        name_label.grid(row=2, column=0, padx=10, pady=10, sticky=tk.W)
        self.name_entry = tk.Entry(add_frame)
        self.name_entry.grid(row=2, column=1, padx=10, pady=10, sticky=tk.E)

        # Author
        author_label = tk.Label(add_frame, text="Author:")
        author_label.grid(row=3, column=0, padx=10, pady=10, sticky=tk.W)
        self.author_entry = tk.Entry(add_frame)
        self.author_entry.grid(row=3, column=1, padx=10, pady=10, sticky=tk.E)

        # Publisher
        publisher_label = tk.Label(add_frame, text="Publisher:")
        publisher_label.grid(row=4, column=0, padx=10, pady=10, sticky=tk.W)
        self.publisher_entry = tk.Entry(add_frame)
        self.publisher_entry.grid(row=4, column=1, padx=10, pady=10, sticky=tk.E)

        # Year Publish
        yearPublish_label = tk.Label(add_frame, text="Year Publish:")
        yearPublish_label.grid(row=5, column=0, padx=10, pady=10, sticky=tk.W)
        self.yearPublish_entry = tk.Entry(add_frame)
        self.yearPublish_entry.grid(row=5, column=1, padx=10, pady=10, sticky=tk.E)

        # Note
        note_label = tk.Label(add_frame, text="Note:")
        note_label.grid(row=6, column=0, padx=10, pady=10, sticky=tk.W)
        self.note_entry = tk.Entry(add_frame)
        self.note_entry.grid(row=6, column=1, padx=10, pady=10, sticky=tk.E)

        # Content
        content_label = tk.Label(add_frame,text="Content:")
        content_label.grid(row=7, column=0, padx=10, pady=10, sticky=tk.W)
        self.content_entry = tk.Entry(add_frame) # 20 chars wide, 5 lines 
        self.content_entry.grid(row=7, column=1, padx=10, pady=10, sticky=tk.E)

        # Add button
        self.add_button = tk.Button(add_frame, text="Add", command=lambda: self.add_data(document_manage))
        self.add_button.grid(row=8, column = 0, padx=30, pady=10)

        # Exit button
        self.exit_button = tk.Button(add_frame, text="Exit", command=window.destroy)
        self.exit_button.grid(row=8, column = 1, padx=10, pady=10)
        window.mainloop()

    def add_data(self,document_manage):
        name = self.name_entry.get()
        author = self.author_entry.get()
        publisher = self.publisher_entry.get()
        yearPublish = self.yearPublish_entry.get()
        note = self.note_entry.get()
        content = self.content_entry.get()

        if name and author:    
            # Create a Document instance based on 6 properties
            self.document = DocumentBase(name,author,publisher,yearPublish,note,content)
            document_manage._add_document(self.document)
            self.add_success_label.config(text="Add success!")
        else:
            self.add_success_label.config(text="Add failed! Try again!")
            self.name_entry.delete(0, tk.END)
            self.author_entry.delete(0, tk.END)
            self.publisher_entry.delete(0, tk.END)
            self.yearPublish_entry.delete(0, tk.END)
            self.note_entry.delete(0, tk.END)
            self.content_entry.delete(0, tk.END)