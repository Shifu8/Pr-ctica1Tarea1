from models.factura import Factura
from models.personaEmisora import PersonaEmisora
from controls.tda.linked.linkedList import Linked_List

class FacturaControl:
    def __init__(self):
        self.__factura = None
        self.__id_counter = 0
        self.__lista = Linked_List()
        
    @property
    def _factura(self):
        if self.__factura == None:
            self.__factura = Factura()
        return self.__factura

    @_factura.setter
    def _factura(self, value):
        self.__factura = value
        
    @property
    def _lista(self):
        return self.__lista

    @_lista.setter
    def _lista(self, value):
        self.__lista = value 
    
    def save(self):
        self._factura._id = self.__id_counter
        self._lista.add(self._factura, self._lista._lenght)
        
    def eliminar(self, pos):
        self._lista.delete(pos)

    def modificar(self, pos, numero, dniPersonaEmisora, fechaEmision, montoTotal, ruc):
        self._lista.edit(pos, numero, dniPersonaEmisora, fechaEmision, montoTotal, ruc)
    