import tkinter as tk

class Result:
    def get_documents():
        documents = []
        with open("manage.txt", "r") as file:
            for line in file:
                document = line.strip().split(",")
                documents.append({
                    "name": document[0],
                    "author": document[1],
                    "publisher": document[2],
                    "yearPublish": document[3],
                    "note": document[4]
                })
        return documents

class ShowUp:
    def __init__(self, master):
        self.master = master
        master.title("Document Manager")

        # create a table to display the data
        self.table = tk.Frame(master)
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

        # get the data from the manage.txt file
        self.documents = Result.get_documents()

        # display the data in the table
        for i, document in enumerate(self.documents):
            name_label = tk.Label(self.table, text=document["name"])
            name_label.grid(row=i+1, column=0)

            author_label = tk.Label(self.table, text=document["author"])
            author_label.grid(row=i+1, column=1)

            publisher_label = tk.Label(self.table, text=document["publisher"])
            publisher_label.grid(row=i+1, column=2)

            yearPublish_label = tk.Label(self.table, text=document["yearPublish"])
            yearPublish_label.grid(row=i+1, column=3)

            note_label = tk.Label(self.table, text=document["note"])
            note_label.grid(row=i+1, column=4)

if __name__ == '__main__':
    root = tk.Tk()
    showup = ShowUp(root)
    root.mainloop()
