from function import showDocument
import Document

class DocumentManage(Document):
    def __init__(self) -> None:
        self.__document_list = []
    
    def _get_total_document(self) -> int:
        return len(self.__document_list)
    
    def _add_document(self,document) -> None:
        # Make a document
        self.__docu = Document()
        self.__document_list.append(self.__docu)
    
    def _show_all_document(self) -> None:
        if self._get_total_document() != 0:
            for document in self.__document_list:
                showDocument(document)

    