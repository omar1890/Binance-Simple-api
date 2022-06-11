from flask import Flask, render_template,jsonify
from binance.client import Client


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
# socket = SocketIO(app,cors_allowed_origins="*")

api_key = 'g5Sbm9dEa32nYv0E6dZ0ydpteWoFnDLDcLg2PsQ1XjCnUE3vp8jQcNC3CWzoeJnC'
api_secret = 'IAT3DKg6G2bNboN9vCgRTDm4UbkqGVgQi7oWc5v3sVTi0K0tl14XJX7qyROC49qO'
client = Client(api_key, api_secret)
client.API_URL = 'https://testnet.binance.vision/api'


# def btc_trade_history(msg):
#     ''' define how to process incoming WebSocket messages '''
#     if msg['e'] != 'error':
#         return msg['c']


@app.route('/')
def index():
    # init and start the WebSocket
    # bsm = ThreadedWebsocketManager()
    # bsm.start()
    # # subscribe to a stream
    # msg = bsm.start_symbol_ticker_socket(callback=btc_trade_history, symbol='BTCUSDT')
    symbol = client.get_symbol_ticker(symbol="BTCUSDT")
    return render_template('index.html',symbol=symbol)

#Get historical data for a specific BTCUSDT type for 1 day and view it in data table
@app.route('/history')
def history():
    candlesticks = client.get_historical_klines('BTCUSDT', '1d', limit=1000)
    history_data = []

    for data in candlesticks:
        candlestick = { 
            "open": data[1],
            "high": data[2], 
            "low": data[3], 
            "close": data[4]
        }

        history_data.append(candlestick)

    return render_template('history.html',history_data=history_data)


if __name__ == '__main__':
    app.run(debug=True)