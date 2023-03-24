# Must return a Document
def addDocument(document_list):
    # Get the details of the new document from the user
    title = input("Enter the title of the document: ")
    author = input("Enter the author of the document: ")
    publisher = input("Enter the publisher of the document: ")
    year = input("Enter the year of publication: ")
    note = input("Enter any notes about the document: ")

    # Create a new Document object and add it to the list
    new_document = Document(title, author, publisher, year, note)
    document_list.append(new_document)
