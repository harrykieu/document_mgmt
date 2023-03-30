import tkinter as tk
import tkinter.messagebox as messagebox
from tkinter import ttk

class FindGUI:
    def __init__(self,document_manage,window):
        
        self.window = window
        window.title("Find Document")
        window.resizable(0,0)

        self.document_manage = document_manage

        # Create frame
        find_frame = tk.Frame(self.window)
        find_frame.pack(padx=10,pady=10)

        # Create string var for holding choice
        self.choice = tk.StringVar()

        # Create criteria label
        criteria_label = tk.Label(find_frame,text="Criteria:")
        criteria_label.grid(row=0,column=0,padx=10,pady=10,sticky=tk.W)
        
        # Create name choice
        name_choice = tk.Radiobutton(find_frame,text="Name",variable=self.choice,value="name")
        name_choice.grid(row=1,column=0,columnspan=2,padx=10,pady=10,sticky=tk.W)

        # Create author choice
        author_choice = tk.Radiobutton(find_frame,text="Author",variable=self.choice,value="author")
        author_choice.grid(row=2,column=0,columnspan=2,padx=10,pady=10,sticky=tk.W)

        # Create year choice
        year_choice = tk.Radiobutton(find_frame,text="Year Publish",variable=self.choice,value="yearPublish")
        year_choice.grid(row=3,column=0,columnspan=2,padx=10,pady=10,sticky=tk.W)

        # Create publisher choice
        publisher_choice = tk.Radiobutton(find_frame,text="Publisher",variable=self.choice,value="publisher")
        publisher_choice.grid(row=4,column=0,columnspan=2,padx=10,pady=10,sticky=tk.W)

        # Create keyword input
        find_prompt = tk.Label(find_frame,text="Keyword:")
        find_prompt.grid(row=5,column=0,padx=10,pady=10,sticky=tk.W)
        self.find_entry = tk.Entry(find_frame)
        self.find_entry.grid(row=5,column=1,padx=10,pady=10,sticky=tk.W)

        # Create find and cancel button
        find_button = tk.Button(find_frame,text="Find",command=lambda: self._find_by_condition(self.document_manage,self.choice.get(),self.find_entry.get()))
        find_button.grid(row=6,column=0,padx=10,pady=10,sticky=tk.NSEW)

        cancel_button = tk.Button(find_frame,text="Cancel",command=window.destroy)
        cancel_button.grid(row=6,column=1,padx=10,pady=10,sticky=tk.NSEW)

        self.window.mainloop()

    def _find_by_condition(self,document_manage,choice,keyword):
        self.__document_found =  document_manage._find_by_condition(choice,keyword)
        if self.__document_found == None:
            messagebox.showerror("Error","No document found!")
        else:
            window = tk.Toplevel(self.window)
            result_gui = ResultGUI(self.__document_found,window)

class ResultGUI:
    def __init__(self,document_found,window):
        self.window = window
        window.title("Result")

        # create a window
        self.window = window
        window.title("All Documents")

        # Create frame
        result_frame = tk.Frame(self.window)
        result_frame.pack(padx=10,pady=5)

        # Create result label
        result_label = tk.Label(result_frame,text=f"Found {len(document_found)} result(s): ")
        result_label.grid(row=0,column=0, columnspan=5, padx=10, pady=10, sticky=tk.W)

        # Create table
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
        
        # get the data
        self.documents = document_found

        # display the data in the table
        for i, document in enumerate(self.documents):
            self.tabledoc.insert(parent="", index=i+1, text=i+1, values=(document._get_name(), document._get_author(), document._get_publisher(), document._get_yearPublish(), document._get_note()))
          
        # add ok button
        ok_button = tk.Button(window,text="OK",command=window.destroy)
        ok_button.pack(padx=10,pady=10,side=tk.RIGHT)
