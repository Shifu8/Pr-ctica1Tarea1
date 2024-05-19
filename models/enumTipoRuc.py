import enum
class EnumTipoRuc(enum.Enum):
    
    EDUCATIVO = 8
    PROFESIONAL = 10

    def getValue(self):
        return self.value
    
    @classmethod
    def from_str(cls, value):
        for enum_type in cls:
            if enum_type.value == value:
                return enum_type
        raise ValueError(f"Invalid value for EnumTipoIdentificacion: {value}")