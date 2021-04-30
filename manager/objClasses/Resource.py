class Resource:
    ##Method __init__
    ##constructor for object class Resource
    ##builds the generic Resource Object with minimal information
    def __init__(self,title,id):
        self.__title = title
        self.__id = id

    ##Getter and setter Methods
    ##standard methods to get singular values and set those to a provide value
    def getTitle(self):
        return self.__title
    def setTitle(self,title):
        self.__title=title
    
    def getId(self):
        return self.__id
    def setId(self,id):
        self.__id=id
        
    ##Method that prints the Resource info
    ##if called the function repr() or str() on the Resource object
    def __repr__(self):
        title="Title: "+self.__title
        code="Code: '"+self.__id+"'"
        return title+", "+code
    def __str__(self):
        title="Title: "+self.__title
        code="Code: '"+self.__id+"'"
        return title+", "+code
