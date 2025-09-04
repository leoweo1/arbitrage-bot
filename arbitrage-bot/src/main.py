import asyncio
from src.data_feed import DataFeed
from src.arbitrage import ArbitrageDetector

async def main():
    feed = DataFeed()
    print("🚀 Starting arbitrage monitor...")
    
    while True:
        try:
            # Fetch data from Binance and Kraken
            binance_data = await feed.fetch_orderbook('binance', 'BTC/USDT')
            kraken_data = await feed.fetch_orderbook('kraken', 'BTC/USDT')
            
            # Check for arbitrage
            opportunity = ArbitrageDetector.cross_exchange_opportunity(
                binance_data, kraken_data, 'BTC/USDT'
            )
            
            if opportunity:
                print(f"💰 ARBITRAGE FOUND: {opportunity}")
                
        except Exception as e:
            print(f"Error: {e}")
        
        await asyncio.sleep(1)  # Throttle requests

if __name__ == "__main__":
    asyncio.run(main())