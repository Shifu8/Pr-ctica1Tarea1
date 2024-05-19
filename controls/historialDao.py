from controls.dao.daoAdapter import DaoAdapter
from models.historialRetenciones import HistorialRetenciones

class HistorialDao(DaoAdapter):
    def __init__(self):
        super().__init__(HistorialRetenciones)
        self.__historial = None

    @property
    def _historial(self):
        if self.__historial == None:
            self.__historial = HistorialRetenciones() 
        return self.__historial

    @_historial.setter
    def _historial(self, value):
        self.__historial = value

    @property
    def _lista(self):
        return self._list()
    
    @property
    def save(self):
        self._historial._idRetencion = self._lista._lenght + 1
        self._save(self._historial)
    
    def merge(self, pos):
        self._merge(self._historial, pos)
        
       
