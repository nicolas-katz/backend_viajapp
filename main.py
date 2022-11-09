from flask import Flask, render_template
from flask_cors import CORS
from db.manager_db import load_plans, load_budgets

import os
import flask
import uuid
import json

app = Flask(__name__)
CORS(app)
plans = load_plans()
budgets = load_budgets()

@app.route('/')
def index():
    return render_template('./index.html')


@app.route('/api/v1/plans', methods=["GET"])
def get_all_plans():
    try:
        return plans
    except:
        return []


@app.route('/api/v1/plans/<plan_id>', methods=["GET"])
def get_plan_by_id(plan_id):
    try:
        founded_data = {}
        for item in plans:
            if item["id"] == plan_id:
                founded_data = item
        return founded_data
    except:
        return {}


@app.route('/api/v1/plans/offers', methods=["GET"])
def get_offers_plans():
    try:
        founded_data = []
        for item in plans:
            if item["offer"]:
                founded_data.append(item)
        return founded_data
    except:
        return []


@app.route('/api/v1/plans/popular', methods=["GET"])
def get_popular_plans():
    try:
        founded_data = []
        for item in plans:
            if item["popular"]:
                if len(founded_data) < 4:
                    founded_data.append(item)
        return founded_data
    except:
        return []


@app.route('api/v1/budgets', methods=["GET"])
def get_all_budgets():
    try:
        return budgets
    except:
        return []


@app.route('/api/v1/budgets', methods=["POST"])
def create_budget():
    try:
        body = json.loads(flask.request.data)
        body["id"] = uuid.uuid1().hex
        budgets.append(body)
        with open('{0}\\db\\budgets.txt'.format(os.getcwd()), 'w') as file:
            file.write(str(budgets))
        return budgets
    except:
        return []


@app.route('/api/v1/plans', methods=["POST"])
def create_plan():
    try:
        body = json.loads(flask.request.data)
        body["id"] = uuid.uuid1().hex
        plans.append(body)
        with open('{0}\\db\\plans.txt'.format(os.getcwd()), 'w') as file:
            file.write(str(plans))
        return plans
    except:
        return []


@app.route('/api/v1/plans/<plan_id>', methods=["PUT"])
def edit_plan(plan_id):
    try:
        body = json.loads(flask.request.data)
        if len(plans) > 0:
            for item in plans:
                if item["id"] == plan_id:
                    item["title"] = body["title"]
                    item["offer"] = body["offer"]
                    item["popular"] = body["popular"]
                    with open('{0}\\db\\plans.txt'.format(os.getcwd()), 'w') as file:
                        file.write(str(plans))
                    return plans
        else:
            return {}
    except:
        return {}


@app.route('/api/v1/plans/<plan_id>', methods=["DELETE"])
def delete_plan(plan_id):
    try:
        if len(plans) > 0:
            for item in plans:
                if item["id"] == plan_id:
                    plans.remove(item)
                    with open('{0}\\db\\plans.txt'.format(os.getcwd()), 'w') as file:
                        file.write(str(plans))
                    return plans
        else:
            return {}
    except:
        return {}


if __name__ == '__main__':
    app.run(None, 3000, True)
