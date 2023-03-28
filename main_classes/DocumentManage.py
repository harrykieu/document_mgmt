import csv
import os

class DocumentManage():
    def __init__(self) -> None:
        self.__document_list = []
    
    def _get_document_list(self) -> list:
        return self.__document_list
    
    def _get_total_document(self) -> int:
        return len(self.__document_list)
    
    def _add_document(self,document) -> None:
        # Make a document
        self.__document = document
        self.__document_list.append(self.__document)
    
    def _get_all_documents(self) -> list:
        if self._get_total_document() != 0:
            return self.__document_list
    
    def _delete_document(self,name) -> bool:
        for document in self.__document_list:
            if name == document._get_name():
                document._set_name(None)
                document._set_author(None)
                document._set_publisher(None)
                document._set_yearPublisher(None)
                document._set_note(None)
            
                # Remove the document from the list
                self._get_document_list().remove(document)
                return True
        return False
            
    def _sort_document(self,condition) -> list:
        self.__sorted_list = self.__document_list.copy()
        if condition == "name":
            self.__sorted_list.sort(key=lambda x: x._get_name())
        elif condition == "author":
            self.__sorted_list.sort(key=lambda x: x._get_author())
        elif condition == "publisher":
            self.__sorted_list.sort(key=lambda x: x._get_publisher())
        elif condition == "yearPublish":
            self.__sorted_list.sort(key=lambda x: x._get_yearPublish())
        elif condition == "note":
            self.__sorted_list.sort(key=lambda x: x._get_note())
        else:
            print("Invalid condition")
        return self.__sorted_list

    def _export_csv(self) -> None:
        self.parent_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        with open(f"{self.parent_path}\\document.csv", "w", newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Name", "Author", "Publisher", "Year Publish", "Note"])
            for document in self.__document_list:
                writer.writerow(document._get_document())
