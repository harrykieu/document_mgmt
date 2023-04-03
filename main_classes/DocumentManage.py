import csv
from main_classes.DocumentBase import DocumentBase

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
                document._set_yearPublish(None)
                document._set_note(None)
            
                # Remove the document from the list
                self._get_document_list().remove(document)
                return True
        return False
            
    def _find_by_condition(self,choice,keyword) -> list:
        self.__document_list_found = []
        if self._get_total_document() != 0:
            for document in self.__document_list:
                # Find by name
                if choice == "name":
                    if keyword == document._get_name():
                        self.__document_list_found.append(document)
                # Find by author
                elif choice == "author":
                    if keyword == document._get_author():
                        self.__document_list_found.append(document)
                # Find by publisher
                elif choice == "publisher":
                    if keyword == document._get_publisher():
                        self.__document_list_found.append(document)
                # Find by year publish
                elif choice == "yearPublish":
                    if keyword == document._get_yearPublish():
                        self.__document_list_found.append(document)
            return self.__document_list_found
        else:
            return None # No document found

    def _export_csv(self,file_path) -> bool:
        self.csvpath = file_path
        with open(self.csvpath, "w", newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Name", "Author", "Publisher", "Year Publish", "Note"])
            for document in self.__document_list:
                writer.writerow(document._get_document())
    
    def _import_csv(self,file_path) -> bool:
        self.csvpath = file_path
        with open(self.csvpath, "r") as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if len(row) != 5:
                    return False # Invalid file format
                if row[0] != "Name":
                    self._add_document(DocumentBase(row[0],row[1],row[2],row[3],row[4]))
            return True # Success