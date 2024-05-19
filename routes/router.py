from flask import Blueprint, abort , request, render_template, redirect, url_for
from controls.personaDaoControl import PersonaDaoControl
from controls.facturaDaoControl import FacturaDaoControl
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
    return render_template('template.html')


#Ver la lista de las personas
@router.route('/personas')
def lista_personas():
    pc = PersonaDaoControl()
    return render_template('personas/lista.html', lista = pc.to_dict())


#Ver la lista de las facturas
#@router.route('/facturas')
#def lista_facturas():
 #   fc = FacturaDaoControl()
  #  return render_template('facturas/lista.html', lista=fc.to_dict())



#ver la interfaz de guardar persona
@router.route('/personas/ver')
def ver_personas():
   return render_template('personas/guardar.html')

#ver la interfaz de guardar factura
#@router.route('/facturas/ver')
#def ver_facturas():
 #   return render_template('factura/guardar.html')


@router.route('/personas/editar/<pos>')
def ver_editar(pos):
    pd = PersonaDaoControl()
    persona = pd._list().getNode(int(pos)-1)
    print(persona)
    return render_template("personas/editar.html", data = persona )


#GUARDAR PERSONAS
@router.route('/personas/guardar', methods=["POST"])
def guardar_personas():
    pd = PersonaDaoControl()
    data = request.form
    
    if not "apellidos" in data.keys():
        abort(400)
        
    #TODO ...Validar
    pd._persona._apellidos = data["apellidos"]
    pd._persona._nombres = data["nombres"]
    pd._persona._direccion = data["direccion"]
    pd._persona._dni = data["dni"]
    pd._persona._telefono = data["telefono"]
    pd._persona._tipoRuc = "EDUCATIVO"
    pd.save
    return redirect("/personas", code=302)


#MODIFICAR PERSONAS
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
    pd._persona._tipoIdentificacion = "CEDULA"

    pd.merge(int(pos)-1)
    return redirect("/personas", code=302)