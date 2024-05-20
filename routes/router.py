from flask import Blueprint, abort , request, render_template, redirect, url_for
from flask import flash
from controls.personaDaoControl import PersonaDaoControl
from models.personaEmisora import PersonaEmisora
from controls.facturaDaoControl import FacturaDaoControl
from models.factura import Factura
from flask_cors import CORS


router = Blueprint('router', __name__)



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


#Ver la lista de las personas
@router.route('/personas')
def lista_personas():
    pc = PersonaDaoControl()
    return render_template('personas/listapersonas.html', lista = pc.to_dict())

#Ver la lista de las personas
@router.route('/facturas')
def lista_facturas():
    fc = FacturaDaoControl()
    return render_template('facturas/listafacturas.html', lista = fc.to_dict())


#ver la interfaz de guardar persona
@router.route('/personas/ver')
def ver_personas():
   return render_template('personas/guardarpersonas.html')

#ver la interfaz de guardar persona
@router.route('/facturas/ver')
def ver_facturas():
   return render_template('facturas/guardarfacturas.html')

@router.route('/personas/guardar', methods=["POST"])
def guardar_personas():
    pd = PersonaDaoControl()
    data = request.form
    
    # Validar si los datos mínimos están presentes
    if not all(key in data for key in ["apellidos", "nombres", "direccion", "dni", "telefono"]):
        abort(400, "Faltan datos necesarios")

    # Crear una nueva instancia de PersonaEmisora con los datos del formulario
    nueva_persona = PersonaEmisora()
    nueva_persona._apellidos = str(data["apellidos"])
    nueva_persona._nombres = str(data["nombres"])
    nueva_persona._direccion = str(data["direccion"])
    nueva_persona._dni = str(data["dni"])
    nueva_persona._telefono = str(data["telefono"])
    nueva_persona._tipoRuc = "EDUCATIVO"  # Se define el tipo de RUC aquí, puedes modificarlo según tus necesidades

    # Guardar la nueva persona utilizando el método save de PersonaDaoControl
    pd._save(nueva_persona)

    return redirect("/personas", code=302)


@router.route('/facturas/guardar', methods=["POST"])
def guardar_facturas():
    fd = FacturaDaoControl()
    data = request.form
    
    # Validar si los datos mínimos están presentes
    if not all(key in data for key in ["numero", "dniPersonaEmisora", "nombreReceptor", "fechaEmision", "montoTotal"]):
        abort(400, "Faltan datos necesarios")

    # Crear una nueva instancia de Factura con los datos del formulario
    nueva_factura = Factura()
    nueva_factura._numero = str(data["numero"])
    nueva_factura._dniPersonaEmisora = str(data["dniPersonaEmisora"])
    nueva_factura._nombreReceptor = str(data["nombreReceptor"])
    nueva_factura._fechaEmision = str(data["fechaEmision"])
    nueva_factura._montoTotal = str(data["montoTotal"])

    # Guardar la nueva factura utilizando el método save de FacturaDaoControl
    fd._save(nueva_factura)

    return redirect("/facturas", code=302)


@router.route('/personas/editar/<int:id>', methods=["GET"])
def ver_editarPersonas(id):
    pd = PersonaDaoControl()
    lista_personas = pd._lista
    if lista_personas.is_empty():
        abort(404, "No hay personas para editar")
    
    if id < 0 or id > lista_personas.size():
        abort(404, "El ID de la persona está fuera de rango")

    persona = lista_personas.getNode(id)  # Restar 1 porque los índices comienzan desde 0
    if persona:
        return render_template("personas/editarpersonas.html", data=persona)
    else:
        abort(404, "Persona no encontrada")


@router.route('/personas/modificar', methods=["POST"])
def modificar_personas():
    pd = PersonaDaoControl()
    data = request.form

    persona_id = data.get("id")
    if not persona_id:
         abort(400, "ID de persona no proporcionado")
    try:
        persona_id = int(persona_id)
    except ValueError:
        abort(400, "ID de persona no válido")


    # Obtener la persona correspondiente al ID
    persona = pd._lista.getNode(persona_id)  # Restar 1 porque los índices comienzan desde 0

    # Verificar si la persona existe
    if not persona:
        abort(404, "Persona no encontrada")

    # Actualizar los datos de la persona con los valores del formulario
    if "apellidos" in data:
        persona._apellidos = str(data["apellidos"])
    if "nombres" in data:
        persona._nombres = str(data["nombres"])
    if "direccion" in data:
        persona._direccion = str(data["direccion"])
    if "dni" in data:
        persona._dni = str(data["dni"])
    if "telefono" in data:
        persona._telefono = str(data["telefono"])
    if "tipoRuc" in data:
        persona._tipoRuc = str(data["tipoRuc"])

    # Guardar los cambios en la base de datos
    pd._merge(persona, persona_id - 1)  # Restar 1 porque los índices comienzan desde 0

    # Redirigir a la página de personas después de modificar
    return redirect("/personas", code=302)



@router.route('/personas/eliminar/<int:id>', methods=['DELETE'])
def eliminar_persona(id):
    pd = PersonaDaoControl()
    pd.delete(id)
    flash("La persona ha sido eliminada exitosamente", "success")
    return redirect("/personas")

