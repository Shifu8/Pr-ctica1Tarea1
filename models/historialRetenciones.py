from models.factura import Factura

class HistorialRetenciones:
    def __init__(self):
        self.__idRetencion = 0
        self.__fecha = ''
        self.__numeroFactura = ''
        self.__porcentaje = 0
        self.__montoRetenido = 0.0

    @property
    def _idRetencion(self):
        return self.__idRetencion

    @_idRetencion.setter
    def _idRetencion(self, value):
        self.__idRetencion = value

    @property
    def _fecha(self):
        return self.__fecha

    @_fecha.setter
    def _fecha(self, value):
        self.__fecha = value

    @property
    def _numeroFactura(self):
        return self.__numeroFactura

    @_numeroFactura.setter
    def _numeroFactura(self, value):
        self.__numeroFactura = value

    @property
    def _porcentaje(self):
        return self.__porcentaje

    @_porcentaje.setter
    def _porcentaje(self, value):
        self.__porcentaje = value

    @property
    def _montoRetenido(self):
        return self.__montoRetenido

    @_montoRetenido.setter
    def _montoRetenido(self, value):
        self.__montoRetenido = value

    @property
    def serializable(self):
        return {
            "idRetencion": self.__idRetencion,
            "fecha": self.__fecha,
            "numeroFactura": self.__numeroFactura,
            "porcentaje": self.__porcentaje,
            "montoRetenido": self.__montoRetenido, 
        }
    
    def deserializar(data):
        historial = HistorialRetenciones()
        historial._idRetencion = data ["idRetencion"]
        historial._fecha = data ["fecha"]
        historial._numeroFactura = data ["numeroFactura"]
        historial._porcentaje = data ["porcentaje"] 
        historial._montoRetenido = data ["montoRetenido"]
        return historial

    def __str__(self):
        return f"ID Retención: {self.__idRetencion}, Fecha: {self.__fecha}, Número de Factura: {self.__numeroFactura}, Porcentaje: {self.__porcentaje}, Monto Retenido: {self.__montoRetenido}"
