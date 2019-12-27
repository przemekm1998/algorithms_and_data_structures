class StockPrices:
    @staticmethod
    def profit_check(prices):
        if len(prices) == 0:
            return None

        min_buy_price = max(prices) + 1
        max_profit = 0

        for price in prices:
            min_buy_price = min(min_buy_price, price)
            compare_profit = price - min_buy_price
            max_profit = max(max_profit, compare_profit)

        return max_profit
