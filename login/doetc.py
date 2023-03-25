import tkinter as tk

class DocManage:
    def __init__(self, file_path):
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

    def sort(self):
        with open(self.file_path, 'r') as f:
            lines = f.readlines()
        lines.sort()
        with open(self.file_path, 'w') as f:
            for line in lines:
                f.write(line)

class DocWindow:
    def __init__(self, admin):
        self.admin = admin

        master = tk.Tk()
        master.title("Document Manager")

        # Add
        add_frame = tk.Frame(master)
        add_frame.pack(padx=10, pady=10)
        add_label = tk.Label(add_frame, text="Add Data:")
        add_label.pack(side=tk.LEFT, padx=10, pady=10)
        self.add_entry = tk.Entry(add_frame)
        self.add_entry.pack(side=tk.LEFT, padx=10, pady=10)
        if self.admin:
            self.add_button = tk.Button(add_frame, text="Add", command=self.add_data)
            self.add_button.pack(side=tk.LEFT, padx=10, pady=10)

        # Remove
        remove_frame = tk.Frame(master)
        remove_frame.pack(padx=10, pady=10)
        remove_label = tk.Label(remove_frame, text="Remove Data:")
        remove_label.pack(side=tk.LEFT, padx=10, pady=10)
        self.remove_entry = tk.Entry(remove_frame)
        self.remove_entry.pack(side=tk.LEFT, padx=10, pady=10)
        if self.admin:
            self.remove_button = tk.Button(remove_frame, text="Remove", command=self.remove_data)
            self.remove_button.pack(side=tk.LEFT, padx=10, pady=10)

        # Display
        display_frame = tk.Frame(master)
        display_frame.pack(padx=10, pady=10)
        self.display_button = tk.Button(display_frame, text="Display Contents", command=self.display_data)
        self.display_button.pack(padx=10, pady=10)

        if not self.admin:
            self.add_entry.configure(state='disabled')
            self.remove_entry.configure(state='disabled')
            if self.display_button:
                self.display_button.configure(text="Display", command=self.dispnonadmin)

        master.mainloop()

    def add_data(self):
        data = self.add_entry.get()
        if data:
            document_manager = DocManage("manage.txt")
            document_manager.add(data)
            self.add_entry.delete(0, tk.END)

    def remove_data(self):
        data = self.remove_entry.get()
        if data:
            document_manager = DocManage("manage.txt")
            document_manager.remove(data)
            self.remove_entry.delete(0, tk.END)

    def display_data(self):
        document_manager = DocManage("manage.txt")
        document_manager.display()

    def dispnonadmin(self):
        document_manager = DocManage("manage.txt")
        document_manager.display()


root = tk.Tk()
app = DocWindow(root)
root.mainloop()
