import os
import flask
from flask import Flask, render_template
from flask_cors import CORS
import json
import uuid
from db.manager_db import load_plans

app = Flask(__name__)
CORS(app)
data = load_plans()


@app.route('/')
def index():
    return render_template('./index.html')


@app.route('/api/v1/plans', methods=["GET"])
def get_all_plans():
    try:
        return data
    except:
        return 'Hubo un error buscando todos los planes.'


@app.route('/api/v1/plans/<plan_id>', methods=["GET"])
def get_plan_by_id(plan_id):
    try:
        founded_data = {}
        for item in data:
            if item["id"] == plan_id:
                founded_data = item
        return founded_data
    except:
        return 'Hubo un error buscando el plan con id ' + plan_id + "."


@app.route('/api/v1/plans/popular', methods=["GET"])
def get_popular_plans():
    try:
        founded_data = []
        for item in data:
            if item["popular"]:
                founded_data.append(item)
        return founded_data
    except:
        return 'Hubo un error buscando todos los planes populares.'


@app.route('/api/v1/plans', methods=["POST"])
def create_plan():
    try:
        body = json.loads(flask.request.data)
        body["id"] = uuid.uuid1().hex
        data.append(body)
        with open('{0}\\db\\plans.txt'.format(os.getcwd()), 'w') as file:
            file.write(str(data))
        return 'El plan se ha creado correctamente.'
    except:
        return 'Hubo un error creando un plan.'


@app.route('/api/v1/plans/<plan_id>', methods=["PUT"])
def edit_plan(plan_id):
    try:
        body = json.loads(flask.request.data)
        if len(data) > 0:
            for item in data:
                if item["id"] == plan_id:
                    item["title"] = body["title"]
                    item["offer"] = body["offer"]
                    item["popular"] = body["popular"]
                    with open('{0}\\db\\plans.txt'.format(os.getcwd()), 'w') as file:
                        file.write(str(data))
                    return 'El plan se ha editado correctamente.'
        else:
            return 'No hay ningún plan cargado en nuestra base de datos.'
    except:
        return 'Hubo un error editando el plan con id: ' + plan_id


@app.route('/api/v1/plans/<plan_id>', methods=["DELETE"])
def delete_plan(plan_id):
    try:
        if len(data) > 0:
            for item in data:
                if item["id"] == plan_id:
                    data.remove(item)
                    with open('{0}\\db\\plans.txt'.format(os.getcwd()), 'w') as file:
                        file.write(str(data))
                    return 'El plan con id ' + plan_id + ' ha sido eliminado correctamente.'
        else:
            return 'No hay ningún plan cargado en nuestra base de datos.'
    except:
        return 'Hubo un error eliminando el plan con id: ' + plan_id


if __name__ == '__main__':
    app.run(None, 3000, True)
