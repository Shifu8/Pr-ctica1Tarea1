from controls.tda.linked.node import Node
from controls.exception.arrayPositionException import ArrayPositionException
from controls.exception.linkedEmpty import LinkedEmpty

class Linked_List(object):
    def __init__(self):
        self.__head = None  
        self.__last = None
        self.__lenght = 0

    @property
    def _lenght(self):
        return self.__lenght

    @_lenght.setter
    def _lenght(self, value):
        self.__lenght = value
        
        
    def is_empty(self):
        return self.__head is None 
    
    def size(self):
        current = self.__head
        count = 0
        while current:
            count += 1
            current = current._next
        return count
    
    
    #Metodo privado para aregar un primer nodo
    def __addFirst__(self, data):
        if self.isEmpty:
            node = Node(data)
            self.__head = node  
            self.__last = node
            self.__lenght += 1
        else:
            headOld = self.__head  
            node = Node(data, headOld)
            self.__head = node  
            self.__lenght += 1
            
            
    #Metodo privado para aregar un nodo al final
    def __addLast__(self, data):
        if self.isEmpty:
           self.__addFirst__(data)
        else:
            node = Node(data)
            self.__last._next = node
            self.__last = node
            self.__lenght += 1

    #Vacía la lista, o la reinicia a su estado vacío 
    @property
    def clear(self):
        self.__head = None
        self.__last = None
        self.__lenght = 0


    # """""""""""""Obtiene el nodo"""""""""""""""
    def getNode(self, pos):
        if self.isEmpty:
            raise LinkedEmpty("List empty")
        elif pos < 0 or pos >= self._lenght:
            raise ArrayPositionException("Index out range")
        elif pos == 0:
            return self.__head
        elif pos == (self.__lenght - 1):
            return self.__last
        else:
            node = self.__head
            cont = 0
            while cont < pos:
                cont += 1
                node = node._next
            return node
    # --------------------------------------------
        
        
    #insetar un nodo con data en una posicion         
    def add(self, data, pos = 0):
        if pos == 0:
            self.__addFirst__(data)
        elif pos == self.__lenght:
            self.__addLast__(data)
        else:
            node_preview = self.getNode(pos - 1)
            node_last = node_preview._next #self.getNode(pos)
            node = Node(data, node_last)
            node_preview._next = node
            self.__lenght += 1
    
    #Permite Modificar un dato en el nodo en la posicion pos
    def edit(self, data, pos = 0):
        if pos == 0:
            self.__head._data = data 
        elif pos == self.__lenght:
            self.__last._data = data
        else:
            node = self.getNode(pos)  
            node._data = data

    #Eliminar el nodo en la posiciión pos 
    def delete(self, pos = 0):
        if pos == 0:
            self._head = self.head._next if self._head else None
            self._last = None if self.head is None else self._last
        else:
            node = self.__head
            for _ in range(pos - 1):
                if node:
                    node = node._next
            if node and node._next:
                node._next = node._next._next
            if pos == self.__lenght - 1:
                self.__last = node
        self.__lenght -= 1
    
        
    # """""""""" Obtiene la data del nodo """""""""""
    # * lo utilizamos para el dao adapter
    def get(self, pos):
        
        if self.isEmpty:
            raise LinkedEmpty("List empty")
        elif pos < 0 or pos >= self._lenght:
            raise ArrayPositionException("Index out range")
        elif pos == 0:
            return self.__head._data
        elif pos == (self.__lenght - 1):
            return self.__last._data
        else:
            node = self.__head
            cont = 0
            while cont < pos:
                cont += 1
                node = node._next
            return node._data
    # ------------------------------------------------
    
    @property
    def print(self):
        node = self.__head
        data = ""
        while node != None:
            data += str(node._data)+"    "
            node = node._next
        print("Lista de datos")
        print(data)

    @property
    def isEmpty(self):
        return self.__head == None or self.__lenght == 0  
    
    def __str__(self) -> str:
        out = ""
        if self.isEmpty:
            return "List is Empty"
        else:
            node = self.__head 
            while node != None:
                out += str(node._data) + "\t"
                node = node._next          
        return out
    