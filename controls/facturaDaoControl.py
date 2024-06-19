from controls.dao.daoAdapter import DaoAdapter
from models.factura import Factura

class FacturaDaoControl(DaoAdapter):
    def __init__(self):
        super().__init__(Factura)
        self.__factura = None

    @property
    def _factura(self):
        if self.__factura == None:
            self.__factura = Factura()   
        return self.__factura

    @_factura.setter
    def _factura(self, value):
        self.__factura = value

    def _lista(self):
        return self._list()
    
    @property
    def save(self):
        self._factura._id = self._lista + 1
        self._save(self._factura)
    
    def merge(self, pos):
        self._merge(self._factura, pos)