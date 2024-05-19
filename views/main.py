import sys
sys.path.append('../')
from controls.personaDaoControl import PersonaDaoControl
from controls.facturaDaoControl import FacturaDaoControl
from controls.historialDao import HistorialDao


pcd = PersonaDaoControl()
fcd = FacturaDaoControl()
hd = HistorialDao()

pcd._persona._apellidos = "Criollo"
pcd._persona._nombres = "Angy"
pcd._persona._telefono = "0964209135"
pcd._persona.__dni = "1111111111"
pcd.save

pcd._persona._apellidos = "Criollo"
pcd._persona._nombres = "sAngy"
pcd._persona._telefono = "0964209135"
pcd.save

fcd._factura._dniPersonaEmisora = "1111111111"
fcd._factura._numero = "2024-05-20"
fcd._factura._nombreReceptor = "Lucho"
fcd._factura._montoTotal = 1000
fcd.save

hd._historial._idRetencion = 1
hd._historial._fecha = "fecha"
hd._historial._numeroFactura = "numeroFactura"
hd._historial._porcentaje = "porcentaje"
hd._historial._montoRetenido = "montoRetenido"
hd.save

