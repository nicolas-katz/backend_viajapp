import os
import json


def load_plans():
    try:
        with open('{0}\\db\\plans.txt'.format(os.getcwd()), 'r') as file:
            data = file.read()
        if data:
            return json.loads(data)
        else:
            return []
    except:
        return 'Hubo un error cargando todos los planes.'

def load_budgets():
    try:
        with open('{0}\\db\\budgets.txt'.format(os.getcwd()), 'r') as file:
            data = file.read()
        if data:
            return json.loads(data)
        else:
            return []
    except:
        return 'Hubo un error cargando todos los planes.'