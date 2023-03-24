# Must return a Document
def delDocument(self, name) -> bool:
        # Find the document with the specified name and remove it from the list
        for document in self.__document_list:
            if document.get_name() == name:
                self.__document_list.remove(document)
                return True
        return False
