# Must return a Document
def delDocument(dm, name):
    # Find the document with the given name
    for DocumentBase in dm._get_document_list():
        if DocumentBase._get_name() == name:
            # Remove all properties of the document
            DocumentBase._set_name(None)
            DocumentBase._set_author(None)
            DocumentBase._set_publisher(None)
            DocumentBase._set_yearPublisher(None)
            DocumentBase._set_note(None)
            
            # Remove the document from the list
            dm._get_document_list().remove(DocumentBase)

            # Return the modified document object
            return DocumentBase

    # If the document was not found, return None
    return None
