from config import settings

class ArbitrageDetector:
    @staticmethod
    def cross_exchange_opportunity(exchange_a, exchange_b, symbol):
        """Detect arbitrage between two exchanges."""
        bid_a = exchange_a['bid']
        ask_b = exchange_b['ask']
        
        if not all([bid_a, ask_b]):
            return None

        gross_profit = bid_a - ask_b
        total_fee = settings.EXCHANGES['binance']['fee'] + settings.EXCHANGES['kraken']['fee']
        net_profit = gross_profit - (ask_b * total_fee)
        profit_pct = net_profit / ask_b

        if profit_pct > settings.MIN_PROFIT:
            return {
                'symbol': symbol,
                'profit_pct': profit_pct * 100,
                'buy_exchange': 'kraken',
                'sell_exchange': 'binance',
                'buy_price': ask_b,
                'sell_price': bid_a
            }
        return None