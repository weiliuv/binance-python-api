# Python Binance API
This project is designed for [Binance API)(https://www.binance.com/restapipub.html),you can use it as you will.it include http api and websocket.

#### Installation
```
clone this repository,and copy requirements,binance.py in you project.
pip install -r requirements.txt
```

#### Getting started
```python
binance = Binance(api_key='your_api_key', secret_key = 'your_api_secret')
```

#### Getting all symbol latest price ,or get price by symbol like get_allPrices('ETHBTH')
```python
print pythonon.dumps(binance.get_allPrices(), indent = 2)
```
<details>
 <summary>View Response</summary>

```python
[                                                                                                                                    
  {                                                                                                                                  
    "symbol": "ETHBTC",                                                                                                              
    "price": "0.04853400"                                                                                                            
  },                                                                                                                                 
  {                                                                                                                                  
    "symbol": "LTCBTC",                                                                                                              
    "price": "0.00919000"                                                                                                            
  },                                                                                                                                 
  {                                                                                                                                  
    "symbol": "BNBBTC",                                                                                                              
    "price": "0.00020770"                                                                                                            
  },                                                                                                                                 
  {                                                                                                                                  
    "symbol": "NEOBTC",                                                                                                              
    "price": "0.00469900"                                                                                                            
  },                                                                                                                                 
  {                                                                                                                                  
    "symbol": "123456",                                                                                                              
    "price": "0.00030000"                                                                                                            
  },                                                                                                                                 
  {                                                                                                                                  
    "symbol": "QTUMETH",                                                                                                             
    "price": "0.03466000"                                                                                                            
  }, 
  .....
]
```
</details>


#### Getting list of current balances, or only one asset like get_balance("ETH"
```python
print pythonon.dumps(binance.get_balance(), indent = 2)
```
<details>
 <summary>View Response</summary>

```python
{                                                                                                                                    
  "buyerCommission": 0,                                                                                                              
  "canWithdraw": true,                                                                                                               
  "takerCommission": 10,                                                                                                             
  "canTrade": true,                                                                                                                  
  "makerCommission": 10,                                                                                                             
  "sellerCommission": 0, 
  "canDeposit": true,
  "balances": [                                                                                                                      
    {                                                                                                                                
      "locked": "0.00000000",                                                                                                        
      "asset": "BTC",                                                                                                                
      "free": "0.00001660"                                                                                                           
    },                                                                                                                               
    {                                                                                                                                
      "locked": "0.00000000",                                                                                                        
      "asset": "LTC",                                                                                                                
      "free": "0.00000000"                                                                                                           
    },                                                                                                                               
    {                                                                                                                                
      "locked": "0.00000000",                                                                                                        
      "asset": "ETH",                                                                                                                
      "free": "0.29785000"                                                                                                           
    }, 
    .....
}
```
</details>

#### Getting bid/ask prices for all symbol, or only one symbol like get_all_bookticker('MCOETH')
```python
json.dumps(binance.get_all_bookticker(), indent=2) 
```

<details>
 <summary>View Response</summary>

```python
[
  {
    "bidQty": "4.05800000", 
    "symbol": "ETHBTC", 
    "askQty": "7.29300000", 
    "bidPrice": "0.04844900", 
    "askPrice": "0.04855600"
  }, 
  {
    "bidQty": "21.65000000", 
    "symbol": "LTCBTC", 
    "askQty": "71.21000000", 
    "bidPrice": "0.00916300", 
    "askPrice": "0.00919800"
  }, 
  {
    "bidQty": "50.00000000", 
    "symbol": "BNBBTC", 
    "askQty": "46.00000000", 
    "bidPrice": "0.00020801", 
    "askPrice": "0.00020930"
  }, 
  {
    "bidQty": "10.00000000", 
    "symbol": "NEOBTC", 
    "askQty": "6.89000000", 
    "bidPrice": "0.00465200", 
    "askPrice": "0.00467400"
  }, 
  ...
]
```
</details>

#### Get market depth for a symbol
```python
print json.dumps(binance.get_depth("LTCBTC"), indent = 2)
```
<details>
 <summary>View Response</summary>

```python
market depth for LTCBTC
{
  "lastUpdateId": 9322003, 
  "bids": [
    [
      "0.00915500", 
      "2.14000000", 
      []
    ], 
    [
      "0.00915100", 
      "26.52000000", 
      []
    ], 
    [
      "0.00915000", 
      "241.49000000", 
      []
    ], 
    [
      "0.00912000", 
      "1.00000000", 
      []
    ], 
    [
      "0.00911800", 
      "596.36000000", 
      []
    ], 
    [
      "0.00910400", 
      "22.18000000", 
      []
    ], 
    [
      "0.00910000", 
      "10.01000000", 
      []
    ], 
    [
      "0.00904500", 
      "73.82000000", 
      []
    ], 
    [
      "0.00903300", 
      "68.80000000", 
      []
    ], 
    [
      "0.00902900", 
      "0.63000000", 
      []
    ], 
    [
      "0.00901900", 
      "1.46000000", 
      []
    ], 
    [
      "0.00900100", 
      "0.23000000", 
      []
    ], 
    [
      "0.00900000", 
      "5.61000000", 
      []
    ], 
    [
      "0.00895000", 
      "0.25000000", 
      []
    ], 
    [
      "0.00892600", 
      "58.80000000", 
      []
    ], 
    [
      "0.00885200", 
      "42.00000000", 
      []
    ], 
    [
      "0.00872300", 
      "54.80000000", 
      []
    ], 
    [
      "0.00870500", 
      "8.28000000", 
      []
    ], 
    [
      "0.00864600", 
      "0.61000000", 
      []
    ], 
    [
      "0.00862900", 
      "57.61000000", 
      []
    ], 
    [
      "0.00856500", 
      "0.62000000", 
      []
    ], 
    [
      "0.00854100", 
      "42.00000000", 
      []
    ], 
    [
      "0.00845500", 
      "21.20000000", 
      []
    ], 
    [
      "0.00844500", 
      "0.63000000", 
      []
    ], 
    [
      "0.00833000", 
      "74.80000000", 
      []
    ], 
    [
      "0.00829100", 
      "0.64000000", 
      []
    ], 
    [
      "0.00820800", 
      "75.21000000", 
      []
    ], 
    [
      "0.00810900", 
      "39.61000000", 
      []
    ], 
    [
      "0.00806800", 
      "50.80000000", 
      []
    ], 
    [
      "0.00804700", 
      "2.00000000", 
      []
    ], 
    [
      "0.00801900", 
      "58.40000000", 
      []
    ], 
    [
      "0.00793500", 
      "58.40000000", 
      []
    ], 
    [
      "0.00788900", 
      "37.21000000", 
      []
    ], 
    [
      "0.00779100", 
      "69.60000000", 
      []
    ], 
    [
      "0.00769600", 
      "10.00000000", 
      []
    ], 
    [
      "0.00700000", 
      "5.00000000", 
      []
    ], 
    [
      "0.00500000", 
      "3.00000000", 
      []
    ], 
    [
      "0.00487700", 
      "1.08000000", 
      []
    ], 
    [
      "0.00100000", 
      "2.00000000", 
      []
    ], 
    [
      "0.00000200", 
      "660.16000000", 
      []
    ], 
    [
      "0.00000100", 
      "1000.00000000", 
      []
    ]
  ], 
  "asks": [
    [
      "0.00920200", 
      "1.49000000", 
      []
    ], 
    [
      "0.00922100", 
      "0.41000000", 
      []
    ], 
    [
      "0.00924900", 
      "24.89000000", 
      []
    ], 
    [
      "0.00930700", 
      "79.95000000", 
      []
    ], 
    [
      "0.00930800", 
      "60.00000000", 
      []
    ], 
    [
      "0.00931600", 
      "6.44000000", 
      []
    ], 
    [
      "0.00938000", 
      "0.55000000", 
      []
    ], 
    [
      "0.00940000", 
      "0.20000000", 
      []
    ], 
    [
      "0.00940400", 
      "40.00000000", 
      []
    ], 
    [
      "0.00942500", 
      "9.24000000", 
      []
    ], 
    [
      "0.00944900", 
      "10.00000000", 
      []
    ], 
    [
      "0.00948800", 
      "5.40000000", 
      []
    ], 
    [
      "0.00949600", 
      "2.38000000", 
      []
    ], 
    [
      "0.00950500", 
      "0.23000000", 
      []
    ], 
    [
      "0.00950700", 
      "52.00000000", 
      []
    ], 
    [
      "0.00959500", 
      "0.23000000", 
      []
    ], 
    [
      "0.00960000", 
      "0.20000000", 
      []
    ], 
    [
      "0.00960400", 
      "22.00000000", 
      []
    ], 
    [
      "0.00962100", 
      "4.31000000", 
      []
    ], 
    [
      "0.00970000", 
      "25.30000000", 
      []
    ], 
    [
      "0.00970600", 
      "49.21000000", 
      []
    ], 
    [
      "0.00973100", 
      "0.23000000", 
      []
    ], 
    [
      "0.00977600", 
      "5.67000000", 
      []
    ], 
    [
      "0.00982100", 
      "13.38000000", 
      []
    ], 
    [
      "0.00990000", 
      "33.24000000", 
      []
    ], 
    [
      "0.00991200", 
      "0.23000000", 
      []
    ], 
    [
      "0.00993600", 
      "61.61000000", 
      []
    ], 
    [
      "0.00999700", 
      "15.66000000", 
      []
    ], 
    [
      "0.01000000", 
      "114.50000000", 
      []
    ], 
    [
      "0.01000100", 
      "57.61000000", 
      []
    ], 
    [
      "0.01002700", 
      "0.65000000", 
      []
    ], 
    [
      "0.01008600", 
      "1.00000000", 
      []
    ], 
    [
      "0.01011500", 
      "30.81000000", 
      []
    ], 
    [
      "0.01020000", 
      "0.10000000", 
      []
    ], 
    [
      "0.01022600", 
      "28.81000000", 
      []
    ], 
    [
      "0.01027500", 
      "123.86000000", 
      []
    ], 
    [
      "0.01027600", 
      "250.27000000", 
      []
    ], 
    [
      "0.01027700", 
      "125.14000000", 
      []
    ], 
    [
      "0.01029000", 
      "194.95000000", 
      []
    ], 
    [
      "0.01029100", 
      "0.24000000", 
      []
    ], 
    [
      "0.01029500", 
      "1.04000000", 
      []
    ], 
    [
      "0.01033000", 
      "66.00000000", 
      []
    ], 
    [
      "0.01033300", 
      "10.00000000", 
      []
    ], 
    [
      "0.01040000", 
      "0.10000000", 
      []
    ], 
    [
      "0.01043500", 
      "30.81000000", 
      []
    ], 
    [
      "0.01044400", 
      "10.00000000", 
      []
    ], 
    [
      "0.01049700", 
      "20.81000000", 
      []
    ], 
    [
      "0.01049900", 
      "24.41000000", 
      []
    ], 
    [
      "0.01050000", 
      "42.18000000", 
      []
    ], 
    [
      "0.01053400", 
      "0.33000000", 
      []
    ], 
    [
      "0.01055500", 
      "10.00000000", 
      []
    ], 
    [
      "0.01057000", 
      "35.14000000", 
      []
    ], 
    [
      "0.01057200", 
      "5.00000000", 
      []
    ], 
    [
      "0.01060000", 
      "11.88000000", 
      []
    ], 
    [
      "0.01062900", 
      "5.97000000", 
      []
    ], 
    [
      "0.01066600", 
      "10.00000000", 
      []
    ], 
    [
      "0.01067700", 
      "56.00000000", 
      []
    ], 
    [
      "0.01067800", 
      "7.82000000", 
      []
    ], 
    [
      "0.01077600", 
      "0.10000000", 
      []
    ], 
    [
      "0.01077700", 
      "10.00000000", 
      []
    ], 
    [
      "0.01078900", 
      "39.21000000", 
      []
    ], 
    [
      "0.01079900", 
      "2.40000000", 
      []
    ], 
    [
      "0.01080000", 
      "0.10000000", 
      []
    ], 
    [
      "0.01080500", 
      "0.93000000", 
      []
    ], 
    [
      "0.01087700", 
      "56.40000000", 
      []
    ], 
    [
      "0.01088800", 
      "10.00000000", 
      []
    ], 
    [
      "0.01089200", 
      "13.52000000", 
      []
    ], 
    [
      "0.01089900", 
      "4.79000000", 
      []
    ], 
    [
      "0.01091100", 
      "7.69000000", 
      []
    ], 
    [
      "0.01092800", 
      "21.80000000", 
      []
    ], 
    [
      "0.01098100", 
      "25.20000000", 
      []
    ], 
    [
      "0.01099900", 
      "31.40000000", 
      []
    ], 
    [
      "0.01100000", 
      "11.64000000", 
      []
    ], 
    [
      "0.01105000", 
      "0.89000000", 
      []
    ], 
    [
      "0.01108300", 
      "3.93000000", 
      []
    ], 
    [
      "0.01110000", 
      "1.10000000", 
      []
    ], 
    [
      "0.01119800", 
      "13.00000000", 
      []
    ], 
    [
      "0.01120000", 
      "5.10000000", 
      []
    ], 
    [
      "0.01129100", 
      "1.36000000", 
      []
    ], 
    [
      "0.01130000", 
      "0.10000000", 
      []
    ], 
    [
      "0.01139900", 
      "20.00000000", 
      []
    ], 
    [
      "0.01140000", 
      "0.10000000", 
      []
    ], 
    [
      "0.01140500", 
      "3.00000000", 
      []
    ], 
    [
      "0.01149900", 
      "20.00000000", 
      []
    ], 
    [
      "0.01150000", 
      "10.50000000", 
      []
    ], 
    [
      "0.01155000", 
      "35.31000000", 
      []
    ], 
    [
      "0.01155500", 
      "3.89000000", 
      []
    ], 
    [
      "0.01159900", 
      "20.00000000", 
      []
    ], 
    [
      "0.01160000", 
      "0.10000000", 
      []
    ], 
    [
      "0.01161400", 
      "0.97000000", 
      []
    ], 
    [
      "0.01169900", 
      "20.00000000", 
      []
    ], 
    [
      "0.01170000", 
      "1.88000000", 
      []
    ], 
    [
      "0.01180000", 
      "1.88000000", 
      []
    ], 
    [
      "0.01183500", 
      "8.04000000", 
      []
    ], 
    [
      "0.01190000", 
      "0.10000000", 
      []
    ], 
    [
      "0.01193900", 
      "0.40000000", 
      []
    ], 
    [
      "0.01199900", 
      "4.99000000", 
      []
    ], 
    [
      "0.01200000", 
      "758.75000000", 
      []
    ], 
    [
      "0.01206400", 
      "1.79000000", 
      []
    ], 
    [
      "0.01210000", 
      "0.10000000", 
      []
    ]
  ]
}

```

```
</details>

#### Placing a LIMIT order
```python
payload = {
    'symbol': "MCOETH",
    'side': "BUY",
    'type': "LIMIT",
    'quantity': 10,
    'price': 0.005,
    'timeInForce': 'GTC'
}
binance.new_order(**payload)
```

#### Placing a MARKET order
```python
// These orders will be executed at current market price.
payload = { 
    'symbol': "MCOETH",
    'side': "BUY",
    'type': "LIMIT",
    'quantity': 10 
}
binance.new_order(**payload)
```

#### Cancel an order
```python
orderid = "1071476"
binance.cancel_order("WTCETH",orderid)
```

#### Getting list of open orders
```python
binance.get_open_orders("ETHBTC")
```

#### Check an order's status
```python
orderid = "1071559";
binance.query_order("WTCETH",orderid)
```

#### Trade history
```python
print json.dumps(binance.get_mytrade("MCOETH"))
```
<details>
 <summary>View Response</summary>

```python
[
  {
    "orderId": 849113, 
    "isBuyer": true, 
    "price": "0.03100000", 
    "isMaker": true, 
    "qty": "22.40000000", 
    "commission": "0.07880677", 
    "time": 1506651726069, 
    "commissionAsset": "BNB", 
    "id": 91983, 
    "isBestMatch": true
  }, 
  {
    "orderId": 851069, 
    "isBuyer": true, 
    "price": "0.02800800", 
    "isMaker": true, 
    "qty": "23.33000000", 
    "commission": "0.07605135", 
    "time": 1506692087009, 
    "commissionAsset": "BNB", 
    "id": 93503, 
    "isBestMatch": true
  }, 
  {
    "orderId": 911636, 
    "isBuyer": false, 
    "price": "0.02747900", 
    "isMaker": false, 
    "qty": "10.68000000", 
    "commission": "0.03247898", 
    "time": 1506836764731, 
    "commissionAsset": "BNB", 
    "id": 100716, 
    "isBestMatch": true
  }, 
  {
    "orderId": 911636, 
    "isBuyer": false, 
    "price": "0.02747800", 
    "isMaker": false, 
    "qty": "18.00000000", 
    "commission": "0.05473662", 
    "time": 1506836764731, 
    "commissionAsset": "BNB", 
    "id": 100717, 
    "isBestMatch": true
  }, 
  {
    "orderId": 911636, 
    "isBuyer": false, 
    "price": "0.02747800", 
    "isMaker": true, 
    "qty": "3.35000000", 
    "commission": "0.01018592", 
    "time": 1506836764814, 
    "commissionAsset": "BNB", 
    "id": 100718, 
    "isBestMatch": true
  }, 
  {
    "orderId": 911636, 
    "isBuyer": false, 
    "price": "0.02747800", 
    "isMaker": true, 
    "qty": "3.36000000", 
    "commission": "0.01021691", 
    "time": 1506836764820, 
    "commissionAsset": "BNB", 
    "id": 100719, 
    "isBestMatch": true
  }, 
  {
    "orderId": 911636, 
    "isBuyer": false, 
    "price": "0.02747800", 
    "isMaker": true, 
    "qty": "2.22000000", 
    "commission": "0.00675173", 
    "time": 1506836774654, 
    "commissionAsset": "BNB", 
    "id": 100720, 
    "isBestMatch": true
  }, 
  {
    "orderId": 911636, 
    "isBuyer": false, 
    "price": "0.02747800", 
    "isMaker": true, 
    "qty": "3.71000000", 
    "commission": "0.01130078", 
    "time": 1506836781936, 
    "commissionAsset": "BNB", 
    "id": 100721, 
    "isBestMatch": true
  }, 
  {
    "orderId": 911655, 
    "isBuyer": false, 
    "price": "0.02746000", 
    "isMaker": false, 
    "qty": "4.41000000", 
    "commission": "0.01340129", 
    "time": 1506836810913, 
    "commissionAsset": "BNB", 
    "id": 100728, 
    "isBestMatch": true
  }, 
  {
    "orderId": 1958157, 
    "isBuyer": true, 
    "price": "0.02842900", 
    "isMaker": false, 
    "qty": "1.00000000", 
    "commission": "0.00332065", 
    "time": 1508754171909, 
    "commissionAsset": "BNB", 
    "id": 164976, 
    "isBestMatch": true
  }
]
```

</details>

#### Get all account orders; active, canceled, or filled.
```python
binance.get_all_orders("LTCBTC")
```

#### Getting 24hr ticker price change statistics for a symbol
```python
binance.get_24hr_ticker("WTCETH")
```

#### Get Kline/candlestick data for a symbol
```python
// Periods: 1m,3m,5m,15m,30m,1h,2h,4h,6h,8h,12h,1d,3d,1w,1M
binance.get_klines("WTCETH", "1h")
```

# WebSockets Implementation

#### Get Candlestick Updates via WebSocket
```python
// Periods: 1m,3m,5m,15m,30m,1h,2h,4h,6h,8h,12h,1d,3d,1w,1M
def on_message(ws, message):
    print 'web socket message doing'
    print message
ws = binance.ws_kline('ETHBTC', '1m', on_message)
ws.on_message = on_message
ws.run_forever()

```

#### Get Trade Updates via WebSocket
```python
def on_message(ws, message):
    print 'web socket message doing'
    print message
ws = binance.ws_aggTrade('ethbTC')
ws.on_message = on_message
ws.run_forever()
```

#### User Data: Account Balance Updates, Trade Updates, New Orders, Filled Orders, Cancelled Orders via WebSocket
```python
def on_message(ws, message):
    print 'web socket message doing'
    print message
ws = binance.ws_aggTrade('ethbTC')
ws.on_message = on_message
ws.run_forever()
```

#### Get Market Depth via WebSocket
```python

```

#### Maintain Market Depth Cache Locally via WebSocket
```python
def on_message(ws, message):
    print 'web socket message doing'
    print message
ws = binance.ws_depth('ethbTC')
ws.on_message = on_message
ws.run_forever()
```
