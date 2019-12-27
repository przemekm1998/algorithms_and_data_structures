import unittest
from Array.stock_prices import StockPrices


class TestStockPrices(unittest.TestCase):
    def test_profit_check_exists(self):
        prices = [310, 315, 275, 295, 260, 270, 290, 230, 255, 250]
        results = StockPrices.profit_check(prices)
        self.assertEqual(results, 30)

    def test_profit_check_positive_derivative(self):
        prices = [210, 220, 230, 240]
        results = StockPrices.profit_check(prices)
        self.assertEqual(results, 30)

    def test_profit_check_negative_derivative(self):
        prices = [240, 230, 220, 210]
        results = StockPrices.profit_check(prices)
        self.assertEqual(results, 0)

    def test_profit_check_empty_prices(self):
        prices = []
        results = StockPrices.profit_check(prices)
        self.assertEqual(results, None)

    def test_profit_check_one_price(self):
        prices = [100]
        results = StockPrices.profit_check(prices)
        self.assertEqual(results, 0)


if __name__ == '__main__':
    unittest.main()
