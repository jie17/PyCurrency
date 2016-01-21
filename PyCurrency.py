import requests
import json

class PyCurrency:
    @staticmethod
    def get(A, B):
        r = requests.get(
        "http://free.currencyconverterapi.com/api/"
        "v3/convert?q={}_{}&compact=y".format(A,B))
        rate = json.loads(r.content.decode())["{}_{}".format(A,B)]["val"]
        return rate

    @staticmethod
    def convert(A, B):
        currency = A[-3:]
        amount = float(A[:-3])
        rate = PyCurrency.get(currency, B)
        return amount*rate

def get(A, B=None):
    if B:
        return PyCurrency.get(A, B)
    else:
        return PyCurrency.get(A[:3], A[3:])

def convert(A, B):
    return PyCurrency.convert(A, B)