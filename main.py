from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve

app=Flask(__name__)
cors = CORS(app)
from Controladores.ControladorCandidato import ControladorCandidato
from Controladores.ControladorMesa import ControladorMesa
from Controladores.ControladorPartido import ControladorPartido
from Controladores.ControladorResultado import ControladorResultado
miControladorCandidato=ControladorCandidato()
miControladorMesa=ControladorMesa()
miControladorPartido=ControladorPartido()
miControladorResultado=ControladorResultado()
###################################################################################
@app.route("/",methods=['GET'])
def test():
    json = {}
    json["message"]="Server running ..."
    return jsonify(json)
###################################################################################
@app.route("/candidato",methods=['GET'])
def getCandidatos():
    json=miControladorCandidato.index()
    return jsonify(json)
@app.route("/candidato",methods=['POST'])
def crearCandidato():
    data = request.get_json()
    json=miControladorCandidato.create(data)
    return jsonify(json)
@app.route("/candidato/<string:id>",methods=['GET'])
def getCandidato(id):
    json=miControladorCandidato.show(id)
    return jsonify(json)
@app.route("/candidato/<string:id>",methods=['PUT'])
def modificarCandidato(id):
    data = request.get_json()
    json=miControladorCandidato.update(id,data)
    return jsonify(json)
@app.route("/candidato/<string:id>",methods=['DELETE'])
def eliminarCandidato(id):
    json=miControladorCandidato.delete(id)
    return jsonify(json)
###################################################################################
@app.route("/mesa",methods=['GET'])
def getMesas():
    json=miControladorMesa.index()
    return jsonify(json)
@app.route("/mesa/<string:id>",methods=['GET'])
def getMesa(id):
    json=miControladorMesa.show(id)
    return jsonify(json)
@app.route("/mesa",methods=['POST'])
def crearmesa():
    data = request.get_json()
    json=miControladorMesa.create(data)
    return jsonify(json)
@app.route("/mesa/<string:id>",methods=['PUT'])
def modificarmesa(id):
    data = request.get_json()
    json=miControladorMesa.update(id,data)
    return jsonify(json)
@app.route("/mesa/<string:id>",methods=['DELETE'])
def eliminarMesa(id):
    json=miControladorMesa.delete(id)
    return jsonify(json)
###################################################################################
@app.route("/partido",methods=['GET'])
def getPartidos():
    json=miControladorPartido.index()
    return jsonify(json)
@app.route("/partido/<string:id>",methods=['GET'])
def getPartido(id):
    json=miControladorPartido.show(id)
    return jsonify(json)
@app.route("/partido",methods=['POST'])
def crearPartido():
    data = request.get_json()
    json=miControladorPartido.create(data)
    return jsonify(json)
@app.route("/partido/<string:id>",methods=['PUT'])
def modificarPartido(id):
    data = request.get_json()
    json=miControladorPartido.update(id,data)
    return jsonify(json)
@app.route("/partido/<string:id>",methods=['DELETE'])
def eliminarPartido(id):
    json=miControladorPartido.delete(id)
    return jsonify(json)
@app.route("/partido/<string:id>/mesa/<string:id_mesa>",methods=['PUT'])
def asignarMesaAPartido(id,id_mesa):
    json=miControladorPartido.asignarMesa(id,id_mesa)
    return jsonify(json)
###################################################################################
@app.route("/resultado",methods=['GET'])
def getResultados():
    json=miControladorResultado.index()
    return jsonify(json)
@app.route("/resultado/<string:id>",methods=['GET'])
def getResultado(id):
    json=miControladorResultado.show(id)
    return jsonify(json)
@app.route("/resultado/candidato/<string:id_candidato>/partido/<string:id_partido>",methods=['POST'])
def crearResultado(id_candidato,id_partido):
    data = request.get_json()
    json=miControladorResultado.create(data,id_candidato,id_partido)
    return jsonify(json)
@app.route("/resultados/<string:id_resultado>/candidato/<string:id_candidato>/partido/<string:id_partido>",methods=['PUT'])
def modificarResultado(id_resultado,id_candidato,id_partido):
    data = request.get_json()
    json=miControladorResultado.update(id_resultado,data,id_candidato,id_partido)
    return jsonify(json)
@app.route("/resultado/<string:id_resultado>",methods=['DELETE'])
def eliminarResultado(id_resultado):
    json=miControladorResultado.delete(id_resultado)
    return jsonify(json)
@app.route("/resultado/partido/<string:id_partido>",methods=['GET'])
def inscritosEnPartido(id_partido):
    json=miControladorResultado.listarResultadosEnPartido(id_partido)
    return jsonify(json)
@app.route("/inscripciones/notas_mayores",methods=['GET'])
def getVotosMayores():
    json=miControladorResultado.votosMasAltosPorMesa()
    return jsonify(json)
@app.route("/resultado/promedio_votos/partido/<string:id_partido>",methods=['GET'])
def getPromedioVotosEnPartido(id_partido):
    json=miControladorResultado.promedioVotosEnPartido(id_partido)
    return jsonify(json)
###################################################################################
def loadFileConfig():
    with open('config.json') as f:
        data = json.load(f)
    return data

if __name__=='__main__':
    dataConfig = loadFileConfig()
    print("Server running : "+"http://"+dataConfig["url-backend"]+":" + str(dataConfig["port"]))
    serve(app,host=dataConfig["url-backend"],port=dataConfig["port"])