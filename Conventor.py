from urllib import request
from bs4 import BeautifulSoup
import json
url = 'https://api.exchangerate-api.com/v4/latest/USD'
html = request.urlopen(url).read()
soup = BeautifulSoup(html,'html.parser')
data=json.loads(html)

Currencies = data["rates"]
 
def conveyor(summ:float, current:str, received:str)->float:
    heft = summ / Currencies[current]
    return round(heft * Currencies[received], 2)


print(conveyor(50,"UAH","USD"))
