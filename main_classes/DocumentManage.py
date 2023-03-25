from function import showDocument
import csv

class DocumentManage():
    def __init__(self) -> None:
        self.__document_list = []
    
    def _get_document_list(self) -> int:
        return self.__document_list
    
    def _get_total_document(self) -> int:
        return len(self.__document_list)
    
    def _add_document(self,document) -> None:
        # Make a document
        self.__document = document
        self.__document_list.append(self.__document)
    
    def _show_all_document(self) -> None:
        if self._get_total_document() != 0:
            for document in self.__document_list:
                showDocument(document)

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
        with open("document.csv", "w", newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Name", "Author", "Publisher", "Year Publish", "Note"])
            for document in self.__document_list:
                writer.writerow(document._to_csv())

    def _backup_data(self) -> None:
        # add content
    # bo sung ham luu data thanh file