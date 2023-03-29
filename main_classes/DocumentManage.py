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
            
    def _find_by_condition(self,choice,keyword) -> list:
        self.__document_list_found = []
        if self._get_total_document() != 0:
            for document in self.__document_list:
                if choice == "name":
                    if keyword == document._get_name():
                        self.__document_list_found.append(document)
                elif choice == "author":
                    if keyword == document._get_author():
                        self.__document_list_found.append(document)
                elif choice == "publisher":
                    if keyword == document._get_publisher():
                        self.__document_list_found.append(document)
                elif choice == "yearPublish":
                    if keyword == document._get_yearPublish():
                        self.__document_list_found.append(document)
            return self.__document_list_found
        else:
            return None

    def _export_csv(self) -> str:
        self.parent_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.csvpath = f"{self.parent_path}/document.csv" # For Linux
        #self.csvpath = f"{self.parent_path}\\document.csv" # For Windows
        #with open(self.csvpath, "w", newline='') as csvfile: # For Windows
        with open(self.csvpath, "w", newline='') as csvfile: # For Linux
            writer = csv.writer(csvfile)
            writer.writerow(["Name", "Author", "Publisher", "Year Publish", "Note"])
            for document in self.__document_list:
                writer.writerow(document._get_document())
        return self.csvpath