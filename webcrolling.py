from bs4 import BeautifulSoup
from datetime import datetime
import requests
import time
import sys
import pandas as pd
import openpyxl


f = open('stock.txt', 'w')
n = 0

def get_code(company_code):
    url ='https://finance.naver.com/item/main.nhn?code=' + company_code
    result = requests.get(url)
    bs_obj = BeautifulSoup(result.content, "html.parser")
    return bs_obj

def get_price(company_code):
    bs_obj = get_code(company_code)
    no_today = bs_obj.find("p", {"class": "no_today"})
    blind = no_today.find("span", {"class": "blind"})
    now_price = blind.text
    return now_price

company_code = ["005930", "373220", "035720", "035420"]
now = datetime.now()
df = pd.DataFrame([get_price(company_code[0]), get_price(company_code[1]), get_price(company_code[2]), get_price(company_code[3])],
                  index=[company_code[0], company_code[1], company_code[2], company_code[3]], columns=[now])


df.to_excel('C:\KGW\PythonWorkSpace\stockpractice.xlsx')
i = 1
while True:
    now = datetime.now()
    df.insert(1,now,[get_price(company_code[0]), get_price(company_code[1]), get_price(company_code[2]), get_price(company_code[3])])
    df.sort_index(axis=1)
    i += 1
    df.to_excel('C:\KGW\PythonWorkSpace\stockpractice.xlsx')
    time.sleep(3)


df.to_excel('C:\KGW\PythonWorkSpace\stockpractice.xlsx')


f.close()

