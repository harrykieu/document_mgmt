from function import addDocument,delDocument,modDocument,showDocument
class Document:
    def __init__(self,name,author,publisher,yearPublish,note):
        self.name = name 
        self.author = author 
        self.publisher = publisher 
        self.yearPublish = yearPublish
        self.note = note
    def set_name(self,name):
        self.name = name
    def get_name(self):
        return self.name 
    def set_author(self,author):
        self.author = author
    def get_author(self):
        return self.author
    def set_publisher(self,publisher):
        self.publisher = publisher
    def get_publisher(self):
        return self.publisher
    def set_yearPublisher(self,yearPublisher):
        self.yearPublisher = yearPublisher 
    def get_yearPublish(self):
        return self.yearPublish
    def set_note(self,note):
        self.note = note
    def get_note(self) :
        return self.note
    