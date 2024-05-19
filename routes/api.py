from flask import Blueprint, jsonify, make_response, request
from controls.personaDaoControl import PersonaDaoControl
from flask_cors import CORS
api = Blueprint('api', __name__)




#CORS(api)
cors = CORS(api, resource={
    r"/*":{
        "origins":"*"
    }
})

#GET: PARA PRESENTAR DATOS
#POST: GUARDA DATOS, MODIFICA DATOS Y EL INICIO DE SESION, EVIAR DATOS AL SERVIDOR

@api.route('/') #SON GETS
def home():
    return make_response(
        jsonify({"msg":"Hola mundo", "code": 200}),
        200
    )


#LISTA PERSONAS
@api.route('/api/personas')
def lista_personas():
    pc = PersonaDaoControl()
    return make_response(
        
        jsonify({"msg":"OK", "code": 200, "data": pc.to_dict()}),
        200
    )

#GUARDAR PERSONAS
@api.route('/api/personas/guardar', methods=['POST'])
def guardar_personas():
    pc = PersonaDaoControl()
    data = request.json  #obtener datos del cliente, arquitectura cliente servidor
    print(type(data))
    if not "apellidos" in data.keys():
        return make_response(
            jsonify({"msg":"Faltan datos", "code": 400, "data": []}),
            400
        )
    
    #TODO... VALIDAR DATOS 
    pc._persona._apellidos = data["apellidos"]
    pc._persona._nombres = data["nombres"]
    pc._persona._telefono = data["telefono"]
    pc._persona._direccion = data["direccion"]
    pc._persona._dni = data["dni"]
    pc._persona._tipoRuc = data["tipoIdentificacion"]
    pc.save
    pc._persona = None

    return make_response(
        
        jsonify({"msg":"OK, se ha registrado correctamente", "code": 200, "data": []}),
        200
    )