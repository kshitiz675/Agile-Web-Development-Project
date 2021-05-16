from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

class PriceLoader():
    url = 'https://api.coingecko.com/api/v3/coins/markets'
    parameters = {
    'per_page':'10',
    'page':'1',
    'vs_currency':'aud'
    }
    headers = {
    'Accepts': 'application/json'
    }

    def getPriceData(self):
        session = Session()
        session.headers.update(self.headers)
        coinList = []
        try:
            with session.get(self.url, params=self.parameters) as response:
                data = json.loads(response.text)
                for coin in data:
                    coinList.append((coin['name'], coin['symbol'], coin['image'], coin['current_price'], coin['price_change_percentage_24h']))

            session.close()   
            return coinList

        except (ConnectionError, Timeout, TooManyRedirects) as e:
            print(e)