from controls.tda.linked.linkedList import Linked_List
from controls.exception.linkedEmpty import LinkedEmpty

class QueueOperation(Linked_List):
    def _init_(self, tope):
        super().__init__()
        self.__tope = tope

    @property
    def _tope(self):
        return self.__tope

    @_tope.setter
    def _tope(self, value):
        self.__tope = value

    @property
    def verifyTop(self):
        print(self._lenght)
        return self._lenght < self._tope
    
    def queue(self, data):
        if self.verifyTop:
            self.add(data, self._lenght)
        else:
            raise LinkedEmpty("Queue full")
    
    @property
    def dequeue(self):
        if self.isEmpty:
            raise LinkedEmpty("Queue empty")
        else:
            return self.delete(0)
        
    