from models.enumTipoRuc import EnumTipoRuc

class PersonaEmisora:
    def __init__(self):
        self.__id = 0
        self.__apellidos = ''
        self.__nombres = ''
        self.__dni = ''
        self.__direccion = ''
        self.__telefono = ''
        self.__tipoRuc = ''

    @property
    def _id(self):
        return self.__id

    @_id.setter
    def _id(self, value):
        self.__id = value

    @property
    def _apellidos(self):
        return self.__apellidos

    @_apellidos.setter
    def _apellidos(self, value):
        self.__apellidos = value

    @property
    def _nombres(self):
        return self.__nombres

    @_nombres.setter
    def _nombres(self, value):
        self.__nombres = value

    @property
    def _dni(self):
        return self.__dni

    @_dni.setter
    def _dni(self, value):
        self.__dni = value

    @property
    def _direccion(self):
        return self.__direccion

    @_direccion.setter
    def _direccion(self, value):
        self.__direccion = value

    @property
    def _telefono(self):
        return self.__telefono

    @_telefono.setter
    def _telefono(self, value):
        self.__telefono = value
        
    @property
    def _tipoRuc(self):
        return self.__tipoRuc

    @_tipoRuc.setter
    def _tipoRuc(self, value):
        self.__tipoRuc = value
    
    @property
    def serializable(self):
        return {
            "id": self.__id,
            "apellidos": self.__apellidos,
            "nombres": self.__nombres,
            "direccion": self.__direccion,
            "dni": self.__dni,
            "telefono": self.__telefono,
            "tipoRuc":self.__tipoRuc
        }
    
    def deserializar(data):
        persona = PersonaEmisora()
        persona._id = data ["id"]
        persona._apellidos = data ["apellidos"]
        persona._nombres = data ["nombres"]
        persona._direccion = data ["direccion"]
        persona._dni = data ["dni"]
        persona._telefono = data ["telefono"]
        persona._tipoRuc = data ["tipoRuc"]
        return persona
        
    def __str__(self):
        return f"ID: {self.__id}, Apellidos: {self.__apellidos}, Nombres: {self.__nombres}, Dirección: {self.__direccion}, DNI: {self.__dni}, Teléfono: {self.__telefono}, TipoRuc: {self.__tipoRuc}"

    
