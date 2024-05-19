from models.personaEmisora import PersonaEmisora
from controls.tda.linked.linkedList import Linked_List

class PersonaControl:
    def __init__(self):
        self.__persona = None
        self.__id_counter = 0
        self.__lista = Linked_List()
    
    @property
    def _persona(self):
        if self.__persona == None:
            self.__persona = PersonaEmisora()
        return self.__persona

    @_persona.setter
    def _persona(self, value):
        self.__persona = value

    @property
    def _lista(self):
        return self.__lista

    @_lista.setter
    def _lista(self, value):
        self.__lista = value
        
    
    def save(self):
        self._persona._id = self.__id_counter
        self._lista.add(self._persona, self._lista._lenght)
       
    def eliminar(self, pos):
        self._lista.delete(pos)

    def modificar(self, pos, apellidos, nombres, direccion, dni, telefono, tipoRuc):
        self._lista.edit(pos, apellidos, nombres, direccion, dni, telefono, tipoRuc)

