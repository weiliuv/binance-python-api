from binance import Binance
import json

if __name__ == '__main__':
    api_key = 'kAm3kdMZKkr3TJMqptR8S8BOahI7NWApblknS78eM3ezWsBcr00upMBldfskb88y'
    secret_key = 'Rjl8ObbJv90bgLhyxXs8NtOsYHsOKRnfTKasmdxgTyuXVSDZBaHp3rBv9nPQ3FrE'
    binance = Binance(api_key, secret_key)
    # hitbtc_address = '0xae4bb570ba78e5f45581e125d0e24d634e4c52fb'
    # print binance.withdraw('ETH', hitbtc_address, 0.1)
    # print binance.get_allPrices()
    #print binance.get_balance('ETH')
    #print json.dumps(binance.get_withdraw_history(asset='ETH'), indent = 2)
    #print json.dumps(binance.get_deposit_history(), indent = 2)

    # for deposit in binance.get_deposit_history(asset='eth')['depositList']:
    #     print json.dumps(deposit, indent = 2)
    # print json.dumps(binance.get_deposit_history(), indent = 2 )

    # def on_message(ws, message):
    #     print 'dodooo'
    #     print message
    #
    # ws = binance.ws_depth('ethbTC')
    # ws = binance.ws_kline('MCOETH', '1m')
    # ws.on_message = on_message
    # ws.run_forever()

    # binance.ws_kline('ETHBTC', '1m', on_message)
    # binance.ws_aggTrade('ETHBTC', on_message)
    # binance.ws_user_data(on_message)
    # binance.get_server_time()
    # print binance.get_all_orders("LTCBTC")
    #print json.dumps(binance.get_balance(), indent = 2)
    # print json.dumps(binance.get_allPrices(), indent = 2)
    # print json.dumps(binance.get_depth("LTCBTC"), indent = 2)
    #payload = {
    #    'symbol': "MCOETH",
    #    'side': "BUY",
    #    'type': "LIMIT",
    #    'quantity': 10,
    #    'price': 0.005,
    #    'timeInForce': 'GTC'
    #}
    #print binance.new_order(**payload)
    # print binance.new_order_test('LTCBTC', 'BUY', 'LIMIT', 10, 0.001)
    # binance.new_order_test('WTCETH', 'BUY', 'LIMIT', 10, 0.005)
    # binance.cancel_order("WTCETH",1071476)
    # for order in  binance.get_open_orders("WTCETH"):
    #     print json.dumps(order, indent=4)
    # for trade in binance.get_aggTrades("WTCETH"):
    #     print json.dumps(trade, indent=2)
    # print binance.get_klines("WTCETH", "1h")
    # print json.dumps(binance.get_24hr_ticker("WTCETH"),indent=2)
    print json.dumps(binance.get_all_ticker('MCOETH'), indent=2)
    #print json.dumps(binance.get_all_bookticker('MCOETH'), indent=2)
    # print json.dumps(binance.query_order("WTCETH",1071559), indent=2)
    # print json.dumps(binance.get_mytrade("WTCETH"))
    # print json.dumps(binance.get_mytrade("MCOETH"), indent = 2)
    # listenKey = binance.start_userdata_stream()['listenKey']


    # binance.keepalive_userdata_stream(listenKey)
    # print listenKey
    # binance.close_userdata_stream(listenKey)
