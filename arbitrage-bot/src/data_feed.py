import ccxt
import asyncio

class DataFeed:
    def __init__(self):
        self.exchanges = {
            'binance': ccxt.binance(),
            'kraken': ccxt.kraken()
        }
    
    async def fetch_orderbook(self, exchange, symbol):
        """Fetch real-time order book data."""
        try:
            ob = await self.exchanges[exchange].fetch_order_book(symbol)
            return {
                'bid': ob['bids'][0][0] if ob['bids'] else None,
                'ask': ob['asks'][0][0] if ob['asks'] else None,
                'timestamp': ob['timestamp']
            }
        except Exception as e:
            print(f"Error fetching {exchange} {symbol}: {e}")
            await asyncio.sleep(5)