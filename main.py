from tradingview_ta import TA_Handler, Interval, Exchange
import time

last_order = "sell"

handler = TA_Handler(
    symbol='AAPL',
    exchange="NASDAQ",
    screener="america",
    interval=Interval.INTERVAL_1_DAY,
)

i=1
while i==1:
    
    rec = handler.get_analysis().summary['RECOMMENDATION']

    
    
    if "BUY" in rec and last_order == "sell":
        print('buy')

        last_order = "buy"
    elif "SELL" in rec and last_order == "buy":
        print('sell')

        last_order = "sell"
    else:
        print('Condition_not-satisfied_Process_restarted')
   
    time.sleep(1)