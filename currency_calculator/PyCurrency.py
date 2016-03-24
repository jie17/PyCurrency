# import requests
import json
import urllib.request

class PyCurrency:
    @staticmethod
    def get(src, dst):
        url = "http://free.currencyconverterapi.com/api/v3/convert?q={}_{}&compact=y".format(src,dst)
        with urllib.request.urlopen(url) as f:
            rate = json.loads(f.read().decode())["{}_{}".format(src,dst)]["val"]
            return rate
        # r = requests.get(
        # "http://free.currencyconverterapi.com/api/"
        # "v3/convert?q={}_{}&compact=y".format(src,dst))
        # rate = json.loads(r.content.decode())["{}_{}".format(src,dst)]["val"]
        # return rate

    @staticmethod
    def convert(src, dst):
        currency = src[-3:]
        amount = float(src[:-3])
        rate = PyCurrency.get(currency, dst)
        return amount*rate

def get(src, dst=None):
    if dst:
        return PyCurrency.get(src, dst)
    else:
        return PyCurrency.get(src[:3], src[3:])

def convert(src, dst):
    return PyCurrency.convert(src, dst)
