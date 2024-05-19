from flask import Blueprint, jsonify, abort , request, render_template, redirect
from controls.personaDaoControl import PersonaDaoControl
from flask_cors import CORS
router = Blueprint('router', __name__)




#CORS(api)
cors = CORS(router, resource={
    r"/*":{
        "origins":"*"
    }
})

#GET: PARA PRESENTAR DATOS
#POST: GUARDA DATOS, MODIFICA DATOS Y EL INICIO DE SESION, EVIAR DATOS AL SERVIDOR

@router.route('/') #SON GETS
def home():
    return render_template('template.html')


#LISTA PERSONAS
@router.route('/personas')
def lista_personas():
    pc = PersonaDaoControl()
    return render_template('nene/lista.html', lista=pc.to_dic())

#LISTA PERSONAS
@router.route('/personas/ver')
def ver_personas():
    return render_template('nene/guardar.html')





@router.route('/personas/editar/<pos>')
def ver_editar(pos):
    pd = PersonaDaoControl()
    nene = pd._list().getNode(int(pos)-1)
    print(nene)
    return render_template("nene/editar.html", data = nene )


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
    pd._persona._tipoIdentificacion = "CEDULA"
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