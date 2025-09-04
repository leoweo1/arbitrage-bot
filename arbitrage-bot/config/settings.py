from dotenv import load_dotenv
import os

load_dotenv()  # Load .env file

EXCHANGES = {
    'binance': {
        'api_key': os.getenv('BINANCE_API_KEY'),
        'secret': os.getenv('BINANCE_SECRET'),
        'fee': 0.001  # 0.1% taker fee
    },
    'kraken': {
        'api_key': os.getenv('KRAKEN_API_KEY'),
        'secret': os.getenv('KRAKEN_SECRET'),
        'fee': 0.0026  # 0.26% fee
    }
}

SYMBOLS = ['BTC/USDT', 'ETH/USDT']
MIN_PROFIT = 0.002  # Minimum profit threshold (0.2%)