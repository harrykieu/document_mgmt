class DocumentBase:
    def __init__(self,name,author,publisher,year_publish,note):
        self.__name = name 
        self.__author = author 
        self.__publisher = publisher 
        self.__year_publish = year_publish
        self.__note = note
        self.__content = ""
    
    def _set_name(self,name):
        self.__name = name
    
    def _get_name(self):
        return self.__name 
    
    def _set_author(self,author):
        self.__author = author
    
    def _get_author(self):
        return self.__author
    
    def _set_publisher(self,publisher):
        self.__publisher = publisher
    
    def _get_publisher(self):
        return self.__publisher
    
    def _set_yearPublish(self,year_publish):
        self.__year_publish = year_publish 
    
    def _get_yearPublish(self):
        return self.__year_publish
    
    def _set_note(self,note):
        self.__note = note
    
    def _get_note(self) :
        return self.__note
    
    def _set_content(self,content):
        self.__content = content
        
    def _get_content(self):
        return self.__content
    
    def _get_document(self):
        return [self.__name,self.__author,self.__publisher,self.__year_publish,self.__note]