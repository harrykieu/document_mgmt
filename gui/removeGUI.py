import tkinter as tk
from main_classes.DocumentManage import DocumentManage
import tkinter.messagebox as messagebox

class RemoveGUI:
    def __init__(self, document_manage, window):

        self.window = window
        window.title("Remove Document")

        # Add frame
        add_frame = tk.Frame(window)
        add_frame.grid(padx=10, pady=10)

        # Prompt to enter document name
        name_label = tk.Label(add_frame, text="Enter the name of the document you want to delete:")
        name_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky=tk.NSEW)
        
        # Name input
        self.name_entry = tk.Entry(add_frame)
        self.name_entry.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky=tk.NSEW)

        # Remove button
        self.remove_button = tk.Button(add_frame, text="Remove", width=15, height=1, command=lambda: self.remove_data(document_manage))
        self.remove_button.grid(row=2, column = 0, padx=10, pady=10,sticky=tk.NSEW)

        # Cancel button
        self.exit_button = tk.Button(add_frame, text="Cancel", width=15, height=1, command=window.destroy)
        self.exit_button.grid(row=2, column = 1, padx=10, pady=10,sticky=tk.NSEW)

        window.mainloop()

    def remove_data(self,document_manage):
        # Get data from input
        name = self.name_entry.get()
        
        # Delete the document
        if (document_manage._delete_document(name)):
            messagebox.showinfo("Success", "Document deleted successfully!")
        else:
            messagebox.showerror("Error", "Document not found!")