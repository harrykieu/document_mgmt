# Must return a Document
# Must return a Document
def modify_document(Document, name=None, author=None, publisher=None, yearPublish=None, note=None):
# Modify the specified attributes of the document
    if name is not None:
        Document.set_name()
        Document.get_name()
    if author is not None:
        Document.set_author()
        Document.get_author()
    if publisher is not None:
        Document.set_publisher()
        Document.get_publisher()
    if yearPublish is not None:
        Document.set_yearPublish()
        Document.get_yearPublish()
    if note is not None:
        Document.set_note()
        Document.get_note()
    return Document
