import tkinter as tk
from tkinter import ttk

# Create a Tkinter window
root = tk.Tk()

# Create a Treeview widget
table = ttk.Treeview(root)

# Define columns
table["columns"] = ("Name", "Age", "City")

# Column formatting
table.column("#0", width=0, stretch=tk.NO)
table.column("Name", width=100, anchor=tk.W)
table.column("Age", width=50, anchor=tk.CENTER)
table.column("City", width=100, anchor=tk.W)

# Add column headings
table.heading("#0", text="", anchor=tk.W)
table.heading("Name", text="Name", anchor=tk.W)
table.heading("Age", text="Age", anchor=tk.CENTER)
table.heading("City", text="City", anchor=tk.W)

# Add data rows
table.insert("", "end", text="1", values=("John", 30, "New York"))
table.insert("", "end", text="2", values=("Mary", 25, "Los Angeles"))
table.insert("", "end", text="3", values=("Bob", 40, "Chicago"))

# Pack the table into the window
table.pack(fill=tk.BOTH, expand=1)

# Start the main event loop
root.mainloop()
