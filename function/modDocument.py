# Must return a DocumentBase
from main_classes import DocumentBase as DocumentBase
def modify_DocumentBase(DocumentBaseBase, name=None, author=None, publisher=None, yearPublish=None, note=None):
# Modify the specified attributes of the DocumentBase
    if name is not None:
        DocumentBase.set_name()
        DocumentBase.get_name()
    if author is not None:
        DocumentBase.set_author()
        DocumentBase.get_author()
    if publisher is not None:
        DocumentBase.set_publisher()
        DocumentBase.get_publisher()
    if yearPublish is not None:
        DocumentBase.set_yearPublish()
        DocumentBase.get_yearPublish()
    if note is not None:
        DocumentBase.set_note()
        DocumentBase.get_note()
    return DocumentBase
# fix lai ham 