from models.personaEmisora import PersonaEmisora

class Factura:
    def __init__(self):
        self.__id = 0
        self.__numero = ''
        self.__dniPersonaEmisora = ''
        self.__nombreReceptor = ''
        self.__fechaEmision = ''
        self.__montoTotal = 0.0
        self.__ruc = ''

    @property
    def _ruc(self):
        return self.__ruc

    @_ruc.setter
    def _ruc(self, value):
        self.__ruc = value

    @property
    def _id(self):
        return self.__id

    @_id.setter
    def _id(self, value):
        self.__id = value

    @property
    def _numero(self):
        return self.__numero

    @_numero.setter
    def _numero(self, value):
        self.__numero = value

    @property
    def _dniPersonaEmisora(self):
        return self.__dniPersonaEmisora

    @_dniPersonaEmisora.setter
    def _dniPersonaEmisora(self, value):
        self.__dniPersonaEmisora = value

    @property
    def _nombreReceptor(self):
        return self.__nombreReceptor

    @_nombreReceptor.setter
    def _nombreReceptor(self, value):
        self.__nombreReceptor = value

    @property
    def _fechaEmision(self):
        return self.__fechaEmision

    @_fechaEmision.setter
    def _fechaEmision(self, value):
        self.__fechaEmision = value

    @property
    def _montoTotal(self):
        return self.__montoTotal

    @_montoTotal.setter
    def _montoTotal(self, value):
        self.__montoTotal = value

    @property
    def serializable(self):
        return {
            "id": self.__id,
            "numero": self.__numero,
            "dniPersonaEmisora": self.__dniPersonaEmisora,
            "nombreReceptor": self.__nombreReceptor,
            "fechaEmision": self.__fechaEmision,
            "montoTotal": self.__montoTotal,
            "ruc": self.__ruc
        }
    
    def deserializar(data):
        factura = Factura()
        factura._id = data["id"]
        factura._numero = data["numero"]
        factura._dniPersonaEmisora = data["dniPersonaEmisora"]
        factura._nombreReceptor = data["nombreReceptor"] 
        factura._fechaEmision = data["fechaEmision"]
        factura._montoTotal = data["montoTotal"]
        factura._ruc = data["ruc"]
        return factura
    
    def __str__(self):
        return f"ID: {self._id}, Número: {self._numero}, DNI Persona Emisora: {self._dniPersonaEmisora}, Nombre Receptor: {self._nombreReceptor}, Fecha Emisión: {self._fechaEmision}, Monto Total: {self._montoTotal}, RUC: {self._ruc}"
