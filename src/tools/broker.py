import requests
import json
from dotenv import load_dotenv
from datetime import datetime
import pandas as pd 
import threading
from ibapi.client import EClient
from ibapi.wrapper import EWrapper
# enum side 
load_dotenv()
BUY = 'BUY'
SELL = 'SELL'


class Broker(EClient, EWrapper):

#      POST https://api.ibkr.com/v1/api/iserver/account/{accountId}/orders
#      GET  https://api.ibkr.com/v1/api//trsrv/stocks?symbols={symbol}

    def __init__(self, price, quantity, tif ):
      EClient.__init__(self, self)
      self.side = BUY or SELL 
      self.price = price
      self.quantity = quantity
      self.tif = tif
      order_type = 'LMT' # limit order 


def run_loop():
    app.run()

app = Broker()
app.connect('192.168.1.125', 7496, 'DU3360345')
# Establishes the connection to the API
# Substitute 192.168.1.120 for your own machine's IP
# Substitute 7496 for your own Socket port number if required.
# For paper accounts, the Socket port number is typically set to 7497
# Substitute 123 for your own client ID that you set earlier.

# Confirm successful connection
print("Connected to the API successfully.")

# Start the socket in a thread
api_thread = threading.Thread(target=run_loop, daemon=True)
api_thread.start()
# This starts the API