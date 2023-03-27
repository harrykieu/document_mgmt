# Must return a Document
from document import Document

def addDocument(dm):
    # Prompt the user for metadata
    __title = input("Enter the title of the document: ")
    __author = input("Enter the author of the document: ")
    __publisher = input("Enter the publisher of the document: ")
    __year = input("Enter the year of publication: ")
    __note = input("Enter any notes about the document: ")

    # Create a new Document object and add it to the list
    new_document = DocumentBase(__title, __author, __publisher, __year, __note)
    dm._add_document(new_document)

    # Return the new document object
    return new_document
