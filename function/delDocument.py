# Must return a Document
def delDocument(dm, name):
    # Find the document with the given name
    for document in dm._get_document_list():
        if document._get_name() == name:
            # Remove all properties of the document
            document._set_name(None)
            document._set_author(None)
            document._set_publisher(None)
            document._set_yearPublisher(None)
            document._set_note(None)
            
            # Remove the document from the list
            dm._get_document_list().remove(document)

            # Return the modified document object
            return document

    # If the document was not found, return None
    return None
