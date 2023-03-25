# Must return a Document
def addDocument(document_list):
    _title = input("Enter the title of the document: ")
    _author = input("Enter the author of the document: ")
    _publisher = input("Enter the publisher of the document: ")
    _year = input("Enter the year of publication: ")
    _note = input("Enter any notes about the document: ")

    # Create a new Document object and add it to the list
    new_document = Document(_title, _author, _publisher, _year, _note)
    document_list.append(new_document)

    # Return the new document object
    return new_document
