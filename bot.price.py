import requests
from binance.client import Client
import json
import time

BSC_API_KEY = 'HG1TZJPJHNAMFR61UAF94QWA5KABX6YSD2'

BNC_KEY = "Binance API key"
BNC_SEC = "Binance Secret Key"


WBNB_CONTRACT = '0xbb4CdB9CBd36B01bD1cBaEBF2De08d9173bc095c'
WBNB_ADDRESS = '0xcaa6991DE146D316B15d92C33D8D07aEF972ABE2'
WBNB_DECIMA = 18


LITC_CONTRACT = '0x395678a4bab1cfe77bed9ddadca47b89a2b85dbb'
LICT_ADDRESS = '0xcaa6991DE146D316B15d92C33D8D07aEF972ABE2'
LITC_DECIMA  = 9

def getPrince(url:str, decimal: int):
    respone = requests.get(url)
    data = respone.json()['result']
    head = len(data)-decimal
    final_result = data[0:head]
    tail = data[-decimal:]
    number  = '{0}.{1}'.format(final_result,tail)
    number = round(float(number),decimal)
    return number

def getBNBPrice():
    client = Client(BNC_KEY, BNC_SEC)
    bnb_price = client.get_symbol_ticker(symbol="BNBUSDT")
    return (bnb_price['price'])

if __name__ == "__main__":
    
    while True:
        bnb_price = getBNBPrice()

        litc_request =  'https://api.bscscan.com/api?module=account&action=tokenbalance&contractaddress={0}&address={1}&tag=latest&apikey={2}'.format(LITC_CONTRACT,LICT_ADDRESS,BSC_API_KEY)
        litc_pool = getPrince(litc_request,LITC_DECIMA)

        wbnb_request = 'https://api.bscscan.com/api?module=account&action=tokenbalance&contractaddress={0}&address={1}&tag=latest&apikey={2}'.format(WBNB_CONTRACT,WBNB_ADDRESS,BSC_API_KEY)
        wbnb_pool = getPrince(wbnb_request,WBNB_DECIMA)

        last_price = (wbnb_pool/litc_pool) * round(float(bnb_price),5)
        x = ("%.16f" % float(last_price))
        #report to file
        price =  {
            "price": str(x)
        }
        print (price)
        with open("pricupdate.json",'w') as export:
                export.write(json.dumps(price,indent=2))
                export.close()
                
        time.sleep(10) #Ten seconds then run new update