from tradingview_ta import TA_Handler, Interval, Exchange

tesla = TA_Handler(
    symbol="BTCUSDT",
    screener="Crypto",
    exchange="Binance",
    interval=Interval.INTERVAL_1_DAY
)

print(tesla.get_analysis().indicators)
