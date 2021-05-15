from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

class PriceLoader():
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    parameters = {
    'start':'1',
    'limit':'10',
    'convert':'AUD'
    }
    headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': '7453c0d6-667a-47de-a640-44856f624494',
    }

    def getPriceData(self):
        session = Session()
        session.headers.update(self.headers)

        try:
            response = session.get(self.url, params=self.parameters)
            data = json.loads(response.text)
            priceData = data['data']
            for coin in priceData:
                print(coin['name'])
                print(coin['symbol'])
                print(coin['quote']['AUD']['price'])
                print(coin['quote']['AUD']['percent_change_24h'])

        except (ConnectionError, Timeout, TooManyRedirects) as e:
            print(e)