import csv
import os


def load_plans():
    plans = []
    try:
        with open('{0}\\db\\plans.csv'.format(os.getcwd()), 'r') as file:
            rows = csv.DictReader(file)

            for row in rows:
                plans.append(row)

            return plans
    except:
        return 'Ocurrio un error.'


def save_plan(plan):
    with open('{0}\\db\\plans.csv'.format(os.getcwd()), 'a') as file:
        header = ["id", "title", "price", "offer", "popular", "description", "img"]

        writer = csv.DictWriter(file, fieldnames=header)

        if file.tell() == 0:
            writer.writeheader()

        writer.writerow(plan)


def update_plan(plan_id, body):
    try:
        plans = load_plans()

        with open('{0}\\db\\plans.csv'.format(os.getcwd()), 'w') as file:
            header = ["id", "title", "price", "offer", "popular", "description", "img"]

            writer = csv.DictWriter(file, fieldnames=header)

            if file.tell() == 0:
                writer.writeheader()

            for item in plans:
                if item["id"] == plan_id:
                    item["title"] = body["title"]
                    item["price"] = body["price"]
                    item["offer"] = body["offer"]
                    item["popular"] = body["popular"]
                    item["description"] = body["description"]
                    item["img"] = body["img"]

            writer.writerow(item)
            print({"status": "ok"})
    except:
        return {}


def remove_plan(plans):
    try:
        with open('{0}\\db\\plans.csv'.format(os.getcwd()), 'w') as file:
            header = ["id", "title", "price", "offer", "popular", "description", "img"]

            writer = csv.DictWriter(file, fieldnames=header)

            if file.tell() == 0:
                writer.writeheader()

            for item in plans:
                writer.writerow(item)
            print({"status": "ok"})
    except:
        return {}


def load_budgets():
    budgets = []
    try:
        with open('{0}\\db\\budgets.csv'.format(os.getcwd()), 'r') as file:
            rows = csv.DictReader(file)

            for row in rows:
                budgets.append(row)

            return budgets
    except:
        return 'Ocurrio un error.'


def save_budget(budget):
    with open('{0}\\db\\budgets.csv'.format(os.getcwd()), 'a') as file:
        header = ["id", "name", "email", "phone", "budget", "plan", "message"]

        writer = csv.DictWriter(file, fieldnames=header)

        if file.tell() == 0:
            writer.writeheader()

        writer.writerow(budget)
