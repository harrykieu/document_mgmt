# Must return a Document
def delDocument(document_list, name):
    # Find the document with the given name
    for document in document_list:
        if document.get_name() == name:
            # Remove all properties of the document
            document.set_name(None)
            document.set_author(None)
            document.set_publisher(None)
            document.set_yearPublish(None)
            document.set_note(None)

            # Return the modified document object
            return document

    # If the document was not found, return None
    return None
