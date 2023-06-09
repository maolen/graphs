import pymongo
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://zhakupovakamila:<password>@cluster0.t5f8buz.mongodb.net/?retryWrites=true&w=majority")

db = cluster["monthly_reports"]
collection = db["expense_data"]


# insert period as a document inside our mongodb
def insert_period(period, incomes, expenses, comment):
    return collection.insert_one({"key": period, "incomes": incomes, "expenses": expenses, "comment": comment})


def fetch_all_periods():
    res = collection.find()
    return res


def get_period(period):
    if not isinstance(period, dict):
        period = {"key": period}

    return collection.find(period)
