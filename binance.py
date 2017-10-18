import hmac
import hashlib
import requests
import time
import sys

class Binance():
    def __init__(self, key, secret, base_url = 'https://www.binance.com'):
        self.key = key
        self.secret = secret
        self.base_url = base_url


    def public_url(self, method, api_url, **payload):
        r_url = self.base_url + api_url
        try:
            # r = requests.get(r_url, payload)
            r = requests.request(method, r_url, params=payload)
            r.raise_for_status()
        except requests.exceptions.HTTPError as err:
            print err
            sys.exit(1)

        if r.status_code == 200:
            return r.json()



    def signed_url(self, method, api_url, **payload):

        r_url = self.base_url + api_url

        timestamp = self.get_server_time()
        payload['timestamp'] = timestamp
        signature = self.get_signed(payload)
        payload['signature'] = signature

        headers = {
            'X-MBX-APIKEY': self.key,
        }


        try:

            r = requests.request(method, r_url, headers = headers, params=payload)
            r.raise_for_status()
        except requests.exceptions.HTTPError as err:
            print err
            print r.text
            sys.exit(1)
        if r.status_code == 200:
            return r.json()


    def get_signed(self, payload):

        param = ''
        for k in payload:
            param += '&' + k + '=' + str(payload[k])
        param = param.lstrip('&')

        signature = hmac.new(self.secret, param, digestmod=hashlib.sha256).hexdigest()

        return signature


    def get_server_time(self):
        """Get server time"""
        # time_url = '/api/v1/time'
        # r = self.public_url('GET', time_url)
        # server_time = r.json()
        # return server_time['serverTime']
        return self.public_url('GET','/api/v1/time')['serverTime']


    def get_all_orders(self, symbol):
        allOrders_url = '/api/v3/allOrders'

        r = self.signed_url('GET', allOrders_url, symbol = symbol)
        print r.json()

    def get_balance(self, coin='all'):

        return self.public_url('GET', '/api/v3/account')
        # account_url = '/api/v3/account'
        # 
        # r = self.signed_url('GET', account_url)
        #
        # if coin == 'all':
        #     return r.json()
        # else:
        #     for c in r.json()['balances']:
        #         if c['asset'] == coin:
        #             return c

    def get_allPrices(self):
        allPrice_url = '/api/v1/ticker/allPrices'
        r = self.public_url('GET', allPrice_url)
        return r.json()


if __name__ == '__main__':
    api_key = 'Mts9Gpk2qIYCXtnZPyGVejo1remzEvjxwHPJXeABAEZzfCVElOGrCaFbgKozCXmc'
    secret_key = 'tZi9agXXmtqw4suiZZQruHcqT1dwI91zOScC6d6u4tsZE7C0wBIseCF2DB3lDD5X'
    # base_url = 'https://www.binance.com'
    binance = Binance(api_key, secret_key)



    # binance.get_server_time()
    # binance.get_all_orders()
    binance.get_balance('BNB')
    # print binance.get_allPrices()
    # time_url = '/api/v1/time'
    # r = binance.public_url('GET', time_url)
    # print r.json()
    #
    # ticker24hr_url = '/api/v1/ticker/24hr'
    # r = binance.public_url('GET', ticker24hr_url, symbol='LTCBTC')
    # print r.json()



