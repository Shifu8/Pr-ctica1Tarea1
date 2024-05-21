from flask import Blueprint, abort , request, render_template, redirect, url_for, jsonify
from flask import flash
from flask import Flask
from controls.personaDaoControl import PersonaDaoControl
from models.personaEmisora import PersonaEmisora
from controls.facturaDaoControl import FacturaDaoControl
from models.factura import Factura
from controls.historialDao import HistorialDao
from models.historialRetenciones import HistorialRetenciones
from controls.personaControl import PersonaControl
from controls.facturaControl import FacturaControl
from models.enumTipoRuc import EnumTipoRuc
from flask_cors import CORS
import json


app = Flask(__name__)
app.secret_key = '1234'

cors = CORS(app)

router = Blueprint('router', __name__)

import secrets

app.secret_key = secrets.token_hex(16)  # Genera una cadena hexadecimal de 16 bytes



#CORS(api)
cors = CORS(router, resource={
    r"/*":{
        "origins":"*"
    }
})

@router.route('/') #SON GETS
def home():
    return render_template('templatepersonas.html')

@router.route('/') #SON GETS
def home1():
    return render_template('templatefacturas.html')

@router.route('/') #SON GETS
def home2():
    return render_template('templateretenciones.html')


@router.route('/personas')
def lista_personas():
    pc = PersonaDaoControl()
    return render_template('personas/listapersonas.html', lista = pc.to_dict())


@router.route('/facturas')
def lista_facturas():
    fc = FacturaDaoControl()
    return render_template('facturas/listafacturas.html', lista = fc.to_dict())

@router.route('/retenciones')
def lista_retenciones():
    hd = HistorialDao()
    return render_template('retenciones/listaretenciones.html', lista = hd.to_dict())



@router.route('/personas/ver')
def ver_personas():
   return render_template('personas/guardarpersonas.html')

@router.route('/facturas/ver')
def ver_facturas():
    dni = request.args.get('dni')
    ruc = request.args.get('ruc')
    return render_template('facturas/guardarfacturas.html', dni=dni, ruc=ruc)

@router.route('/retenciones/ver')
def ver_retenciones():
   return render_template('retenciones/guardarretenciones.html')




@router.route('/personas/guardar', methods=["POST"])
def guardar_personas():
    pd = PersonaDaoControl()
    data = request.form

    if not all(key in data for key in ["apellidos", "nombres", "direccion", "dni", "telefono", "tipoRuc"]):
        abort(400, "Faltan datos necesarios")

    nueva_persona = PersonaEmisora()
    nueva_persona._apellidos = str(data["apellidos"])
    nueva_persona._nombres = str(data["nombres"])
    nueva_persona._direccion = str(data["direccion"])
    nueva_persona._dni = str(data["dni"])
    nueva_persona._telefono = str(data["telefono"])
    
    # Validar y asignar el tipo de RUC
    tipo_ruc = str(data["tipoRuc"])
    if tipo_ruc not in ["8", "10"]:
        abort(400, "Valor de RUC no válido")
    
    tipo_ruc_enum = EnumTipoRuc(int(tipo_ruc))
    nueva_persona._tipoRuc = tipo_ruc_enum.name  # Guardar el nombre del Enum en lugar del valor numérico

    # Obtener la lista de personas para determinar el nuevo ID
    lista_personas = pd._list()
    nuevo_id = lista_personas._lenght + 1  # ID único basado en la longitud de la lista más 1
    nueva_persona._id = nuevo_id

    pd._save(nueva_persona)

    return redirect("/personas", code=302)

@router.route('/facturas/guardar', methods=["POST"])
def guardar_facturas():
    fd = FacturaDaoControl()
    data = request.form
    
    # Validar si los datos mínimos están presentes
    if not all(key in data for key in ["numero", "dniPersonaEmisora", "nombreReceptor", "fechaEmision", "montoTotal", "ruc"]):
        abort(400, "Faltan datos necesarios")

    nueva_factura = Factura()
    nueva_factura._numero = str(data["numero"])
    nueva_factura._dniPersonaEmisora = str(data["dniPersonaEmisora"])  
    nueva_factura._nombreReceptor = str(data["nombreReceptor"])
    nueva_factura._fechaEmision = str(data["fechaEmision"])
    nueva_factura._montoTotal = str(data["montoTotal"])
    nueva_factura._ruc = str(data["ruc"])


    # Obtener la lista de personas para determinar el nuevo ID
    lista_facturas = fd._list()
    nuevo_id = lista_facturas._lenght + 1  # ID único basado en la longitud de la lista más 1
    nueva_factura._id = nuevo_id
    
    fd._save(nueva_factura)

    return redirect("/facturas", code=302)

@router.route('/retenciones/guardar', methods=["POST"])
def guardar_retenciones():
    hd = HistorialDao()
    data = request.form

    if not all(key in data for key in ["fecha", "numeroFactura", "porcentaje", "montoRetenido"]):
        abort(400, "Faltan datos necesarios")

    nuevo_historial = HistorialRetenciones()
    nuevo_historial._fecha = str(data["fecha"])
    nuevo_historial._numeroFactura = str(data["numeroFactura"])
    nuevo_historial._porcentaje = str(data["porcentaje"])
    nuevo_historial._montoRetenido = str(data["montoRetenido"])
    
    # Obtener la lista de personas para determinar el nuevo ID
    lista_retenciones = hd._list()
    nuevo_id = lista_retenciones._lenght + 1  # ID único basado en la longitud de la lista más 1
    nuevo_historial._idRetencion = nuevo_id
    
    hd._save(nuevo_historial)

    return redirect("/retenciones", code=302)


@router.route('/personas/eliminar/<int:persona_id>', methods=["POST"])
def eliminar_persona(persona_id):
    pc = PersonaControl()
    try:
        pc.eliminar(persona_id)
        
        # Eliminar la persona del JSON
        with open('data/personaemisora.json', 'r') as file:
            personas = json.load(file)
        personas = [persona for persona in personas if persona['id'] != persona_id]
        with open('data/personaemisora.json', 'w') as file:
            json.dump(personas, file, indent=4)

        return jsonify({"message": "Persona eliminada correctamente.", "persona_id": persona_id}), 200
    except Exception as e:
        return jsonify({"error": f"No se pudo eliminar la persona: {str(e)}"}), 500
 
 
    
@router.route('/facturas/eliminar/<int:factura_id>', methods=["POST"])
def eliminar_factura(factura_id):
    fc = FacturaControl()
    try:
        fc.eliminar(factura_id)
        
        # Eliminar la persona del JSON
        with open('data/factura.json', 'r') as file:
            facturas = json.load(file)
        facturas = [factura for factura in facturas if factura['id'] != factura_id]
        with open('data/factura.json', 'w') as file:
            json.dump(facturas, file, indent=4)

        return jsonify({"message": "Factura eliminada correctamente.", "factura_id": factura_id}), 200
    except Exception as e:
        return jsonify({"error": f"No se pudo eliminar la factura: {str(e)}"}), 500




@router.route('/personas/editar/<pos>')
def ver_editar(pos):
    pd = PersonaDaoControl()
    nene = pd._list().getNode(int(pos)-1)
    print(nene)
    return render_template("personas/editarpersonas.html", data = nene )



@router.route('/personas/modificar', methods=["POST"])
def modificar_personas():
    pd = PersonaDaoControl()
    data = request.form
    pos = data["id"]
    nene = pd._list().getNode(int(pos)-1)   #nene = pd._list().getNode(int(data["id"]) -1)
    
    if not "apellidos" in data.keys():
        abort(400)
        
    #TODO ...Validar
    pd._persona = nene
    pd._persona._apellidos = data["apellidos"]
    pd._persona._nombres = data["nombres"]
    pd._persona._direccion = data["direccion"]
    pd._persona._dni = data["dni"]
    pd._persona._telefono = data["telefono"]
    pd._persona._tipoRuc = str(data["tipoRuc"])

    pd.merge(int(pos)-1)
    return redirect("/personas", code=302)
