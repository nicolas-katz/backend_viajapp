import flask
from flask import Flask, render_template
from flask_cors import CORS
import json
import uuid

app = Flask(__name__)
CORS(app)

def getDatabase():
    with open('plans.json', 'r') as file:
        data = file.read()
    if data:
        return json.loads(data)
    else:
        return []
@app.route('/')
def index():
    return render_template('./index.html')

@app.route('/api/v1/plans', methods=["GET"])
def getAllPlans():
    try:
        data = getDatabase()
        if len(data) == 0:
            with open('plans.json', 'w') as file:
                file.write(str(data))
        return data
    except:
        return 'Hubo un error buscando todos los planes.'

@app.route('/api/v1/plans/<plan_id>', methods=["GET"])
def getPlanById(plan_id):
    try:
        filteredData = []
        data = getDatabase()
        if type(data) == list and len(data) > 0:
            for item in data:
                if item["id"] == plan_id:
                    filteredData = item
            return filteredData
        else:
            return 'No existe ningún plan actualmente.'
    except:
        return 'Hubo un error buscando el plan con id ' + plan_id + "."

@app.route('/api/v1/plans/offers', methods=["GET"])
def getPlansWithOffers():
    try:
        filteredData = []
        data = getDatabase()
        if data:
            for item in data:
                if item["offer"]:
                    filteredData.append(item)
            return filteredData
        else:
            return 'No existe ningún plan actualmente.'
    except:
        return 'Hubo un error buscando todos los planes con oferta.'

@app.route('/api/v1/plans', methods=["POST"])
def createPlan():
    try:
        data = getDatabase()
        body = json.loads(flask.request.data)
        body["id"] = uuid.uuid1().hex
        if type(data) == list:
            data.append(body)
            with open('plans.json', 'w') as file:
                file.write(str(data))
        else:
            with open('plans.json', 'w') as file:
                file.write(str(list(body)))
        return 'El plan se ha creado correctamente.'
    except:
        return 'Hubo un error creando un plan.'

@app.route('/api/v1/plans/<plan_id>', methods=["PUT"])
def editPlan(plan_id):
    try:
        data = getDatabase()
        body = json.loads(flask.request.data)
        if type(data) == list and len(data) > 0:
            for item in data:
                if item["id"] == plan_id:
                    item["name"] = body["name"]
                    item["offer"] = body["offer"]
            with open('./plans.json', 'w') as file:
                file.write(str(data))
            return 'El plan se ha editado correctamente.'
        else:
            return 'No existe ningún plan actualmente.'
    except:
        return 'Hubo un error editando el plan con id: ' + plan_id

@app.route('/api/v1/plans/<plan_id>', methods=["DELETE"])
def deletePlan(plan_id):
    try:
        filteredData = []
        data = getDatabase()
        if len(data) > 0:
            for item in data:
                if item["id"] == plan_id:
                    filteredData.append(item)
                    with open('plans.json', 'w') as file:
                        file.write(str(filteredData))
                    return 'El plan con id ' + plan_id + ' ha sido eliminado correctamente.'
                else:
                    return []
        else:
            return 'No existe ningún plan actualmente.'
    except:
        return 'Hubo un error eliminando el plan con id: ' + plan_id

if __name__ == '__main__':
    app.run(None, 3000, True)