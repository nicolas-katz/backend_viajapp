from flask import Flask, render_template
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

def getDatabase():
    with open('./plans.json', 'r') as file:
        data = json.loads(file.read())
    return data

@app.route('/')
def index():
    return render_template('./index.html')

@app.route('/api/v1/plans', methods=["GET"])
def getAllPlans():
    try:
        data = getDatabase()
        if len(data) > 0:
            return data
        else:
            return 'No existe ningún plan actualmente.'
    except:
        return 'Hubo un error buscando todos los planes.'

@app.route('/api/v1/plans/<int:plan_id>', methods=["GET"])
def getPlanById(plan_id):
    try:
        filteredData = ''
        data = getDatabase()
        if len(data) > 0:
            for item in data:
                if item["id"] == plan_id:
                    filteredData = item
                else:
                    return 'No existe un plan con el id: ' + str(plan_id)
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
        if len(data) > 0:
            for item in data:
                if item["offer"]:
                    filteredData.append(item)
                else:
                    'Hubo un error buscando todos los planes con oferta.'
            return filteredData
        else:
            return 'No existe ningún plan actualmente.'
    except:
        return 'Hubo un error buscando todos los planes con oferta.'

@app.route('/api/v1/create_plan', methods=["POST"])
def createPlan():
    return 'en proceso'

@app.route('/api/v1/edit_plan/<int:plan_id>', methods=["PUT"])
def editPlan(plan_id):
    return 'en proceso'

@app.route('/api/v1/plans/<int:plan_id>', methods=["DELETE"])
def deletePlan(plan_id):
    try:
        filteredData = []
        data = getDatabase()
        if len(data) > 0:
            for item in data:
                if item["id"] != plan_id:
                    filteredData.append(item)
            with open('./plans.json', 'w') as file:
                file.write(str(filteredData))
            return 'El plan con id ' + str(plan_id) + ' ha sido eliminado correctamente.'
        else:
            return 'No existe ningún plan actualmente.'
    except:
        return 'Hubo un error eliminando el plan con id: ' + str(plan_id)

if __name__ == '__main__':
    app.run(None, 3000, True)