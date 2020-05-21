from abc import ABC, abstractmethod

class Subject(ABC):
    
    def __init__(self,name):
        self.name = name
       
    
    @abstractmethod
    def get_comfort(self,home):
        pass
    
class Daddy(Subject):
    
    def __init__(self):
        super().__init__("Daddy")
        
    def get_comfort(self,home):
        consumption_ratio = home.get_consumption_ratio()
        return 1 - consumption_ratio
    
    def __repr__(self):
        return self.name