import tkinter as tk
from main_classes.DocumentBase import DocumentBase
import tkinter.messagebox as messagebox
class AddGUI:
    def __init__(self,document_manage,window):

        self.window=window
        window.title("Add Document")

        # Add frame
        add_frame=tk.Frame(window)
        add_frame.grid(padx=10,pady=10)

        # Name
        name_label=tk.Label(add_frame,text="Name:",font=("",10,"bold"))
        name_label.grid(row=0,column=0,padx=10,pady=10,sticky=tk.W)
        self.name_entry=tk.Entry(add_frame)
        self.name_entry.grid(row=0,column=1,padx=10,pady=10,sticky=tk.E)

        # Author
        author_label=tk.Label(add_frame,text="Author:",font=("",10,"bold"))
        author_label.grid(row=1,column=0,padx=10,pady=10,sticky=tk.W)
        self.author_entry=tk.Entry(add_frame)
        self.author_entry.grid(row=1,column=1,padx=10,pady=10,sticky=tk.E)

        # Publisher
        publisher_label=tk.Label(add_frame,text="Publisher:",font=("",10,"bold"))
        publisher_label.grid(row=2,column=0,padx=10,pady=10,sticky=tk.W)
        self.publisher_entry=tk.Entry(add_frame)
        self.publisher_entry.grid(row=2,column=1,padx=10,pady=10,sticky=tk.E)

        # Year Publish
        yearPublish_label=tk.Label(add_frame,text="Year Publish:",font=("",10,"bold"))
        yearPublish_label.grid(row=3,column=0,padx=10,pady=10,sticky=tk.W)
        self.yearPublish_entry=tk.Entry(add_frame)
        self.yearPublish_entry.grid(row=3,column=1,padx=10,pady=10,sticky=tk.E)

        # Note
        note_label=tk.Label(add_frame,text="Note:",font=("",10,"bold"))
        note_label.grid(row=4,column=0,padx=10,pady=10,sticky=tk.W)
        self.note_entry=tk.Entry(add_frame)
        self.note_entry.grid(row=4,column=1,padx=10,pady=10,sticky=tk.E)

        # Add button
        self.add_button=tk.Button(add_frame,text="Add",width=15,height=1,command=lambda: self.add_data(document_manage))
        self.add_button.grid(row=5,column=0,padx=10,pady=10,sticky=tk.NSEW)

        # Cancel button
        self.exit_button=tk.Button(add_frame,text="Cancel",width=15,height=1,command=window.destroy)
        self.exit_button.grid(row=5,column=1,padx=10,pady=10,sticky=tk.NSEW)

        # disable resizing
        self.window.resizable(0,0)
        
        window.mainloop()

    def add_data(self,document_manage):
        # Get data from input
        year_not_int=True
        name=self.name_entry.get()
        author=self.author_entry.get()
        publisher=self.publisher_entry.get()
        year_publish=self.yearPublish_entry.get()
        note=self.note_entry.get()
        
        # Check if all fields are filled
        if name and author and publisher and year_publish:    
            try:
                year_publish=int(self.yearPublish_entry.get()) # Check if year of publish is a number
            except ValueError:
                year_not_int=False
            if year_not_int==False:
                messagebox.showerror("Add document","Error! Year of publish must be a number!")
            else:
                if note: # If note is not empty
                    # Create a Document instance based on 5 properties
                    self.document=DocumentBase(name,author,publisher,year_publish,note)
                else:
                    # Create a Document instance with no note
                    self.document=DocumentBase(name,author,publisher,year_publish,"")
                document_manage._add_document(self.document)
                messagebox.showinfo("Add document","Add success!")
        else:
            messagebox.showerror("Add document","Error! Please fill in all fields!")