import tkinter as tk
from login.showDocumentGUI import ShowUp
from main_classes import DocumentManage as DocManage
from main_classes import DocumentBase as Document
#class DocManage:
"""    def __init__(self, file_path):
        self.file_path = file_path

    def add(self, data):
        with open(self.file_path, 'a') as f:
            f.write(data + '\n')

    def remove(self, data):
        with open(self.file_path, 'r') as f:
            lines = f.readlines()
        with open(self.file_path, 'w') as f:
            for line in lines:
                if line.strip() != data:
                    f.write(line)

    def display(self):
        with open(self.file_path, 'r') as f:
            lines = f.readlines()
        print("Document Contents:")
        for line in lines:
            print(line.strip())
"""
class DocWindow:
    def __init__(self, document_manager, admin):
        self.admin = admin
        window = tk.Tk()
        window.title("Document Manager")

        # Add
        add_frame = tk.Frame(window)
        add_frame.pack(padx=10, pady=10)

        # Name
        name_label = tk.Label(add_frame, text="Name:")
        name_label.pack(side=tk.LEFT, padx=10, pady=10)
        self.add_entry = tk.Entry(add_frame)
        self.add_entry.pack(side=tk.LEFT, padx=10, pady=10)
        if not self.admin:
            self.add_entry.configure(state='disabled')

        # Author
        author_label = tk.Label(add_frame, text="Author:")
        author_label.pack(side=tk.LEFT, padx=10, pady=10)
        self.author_entry = tk.Entry(add_frame)
        if not self.admin:
            self.author_entry.configure(state='disabled')
        self.author_entry.pack(side=tk.LEFT, padx=10, pady=10)

        # Publisher
        publisher_label = tk.Label(add_frame, text="Publisher:")
        publisher_label.pack(side=tk.LEFT, padx=10, pady=10)
        self.publisher_entry = tk.Entry(add_frame)
        if not self.admin:
            self.publisher_entry.configure(state='disabled')
        self.publisher_entry.pack(side=tk.LEFT, padx=10, pady=10)

        # Year Publish
        yearPublish_label = tk.Label(add_frame, text="Year Publish:")
        yearPublish_label.pack(side=tk.LEFT, padx=10, pady=10)
        self.yearPublish_entry = tk.Entry(add_frame)
        if not self.admin:
            self.yearPublish_entry.configure(state='disabled')
        self.yearPublish_entry.pack(side=tk.LEFT, padx=10, pady=10)

        # Note
        note_label = tk.Label(add_frame, text="Note:")
        note_label.pack(side=tk.LEFT, padx=10, pady=10)
        self.note_entry = tk.Entry(add_frame)
        if not self.admin:
            self.note_entry.configure(state='disabled')
        self.note_entry.pack(side=tk.LEFT, padx=10, pady=10)

        # Add data
        if self.admin:
            self.add_button = tk.Button(add_frame, text="Add", command=lambda: self.add_data(document_manager))
            self.add_button.pack(side=tk.LEFT, padx=10, pady=10)


        # Remove
        remove_frame = tk.Frame(window)
        remove_frame.pack(padx=10, pady=10)
        remove_label = tk.Label(remove_frame, text="Remove Data:")
        remove_label.pack(side=tk.LEFT, padx=10, pady=10)
        self.remove_entry = tk.Entry(remove_frame)
        self.remove_entry.pack(side=tk.LEFT, padx=10, pady=10)
        if self.admin:
            self.remove_button = tk.Button(remove_frame, text="Remove", command=lambda: self.remove_data(document_manager))
            self.remove_button.pack(side=tk.LEFT, padx=10, pady=10)
        if not self.admin:
            self.remove_entry.configure(state='disabled')

        # Display
        display_frame = tk.Frame(window)
        display_frame.pack(padx=10, pady=10)
        self.display_button = tk.Button(display_frame, text="Display Contents", command=lambda: self.display_data(document_manager))
        self.display_button.pack(padx=10, pady=10)

        if not self.admin:
            if self.display_button:
                self.display_button.configure(text="Display", command=self.dispnonadmin)

        window.mainloop()

    def add_data(self,document_manager):
        name = self.add_entry.get()
        author = self.author_entry.get()
        publisher = self.publisher_entry.get()
        yearPublish = self.yearPublish_entry.get()
        note = self.note_entry.get()
        if name and author and publisher and yearPublish and note:    
            # Create a Document instance based on 5 properties
            self.document = Document(name,author,publisher,yearPublish,note)

            #data = f"{name}, {author}, {publisher}, {yearPublish}, {note}"
            
            document_manager._add_document(self.document)

    def remove_data(self,document_manager):
        remove_name = self.remove_entry.get()
        document_manager._del_document(remove_name)

    def display_data(self):
        displayscr = tk.Toplevel()
        app = ShowUp(displayscr)
    def dispnonadmin(self):
        displayscr = tk.Toplevel()
        app = ShowUp(displayscr)
