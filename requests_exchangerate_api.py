# -*- coding: utf-8 -*-
"""requests_ExchangeRate-API

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1rwX-CuGQq8oTgvS2tBkgr9spKtzrB5Rl
"""

import requests

import json

api_key="0884b75794eac9a6ff9feca0"
api_url=f"https://v6.exchangerate-api.com/v6/{api_key}/latest/"

sold_curr=input("Sold Currency (USD-TRY): ")
purchased_curr=input("Purchased Currency: ")
amount=float(input(f"How much {sold_curr} do you want to change?: "))

result=requests.get(api_url + sold_curr)
#print(result.text)

data=json.loads(result.text)

result_curr=amount* data['conversion_rates'][purchased_curr]

print("1 {0} = {1} {2}".format(sold_curr,data["conversion_rates"][purchased_curr],purchased_curr))
print(f"{amount} {sold_curr} is equal to {result_curr} {purchased_curr}")