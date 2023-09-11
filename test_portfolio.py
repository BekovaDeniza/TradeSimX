import unittest
from main import AssetPrice, Portfolio
from decimal import Decimal


class TestPortfolio(unittest.TestCase):
    def setUp(self):
        # Создаем портфель с начальными средствами 10,000 перед каждым тестом
        self.portfolio = Portfolio(10000)

    def test_buy(self):
        # Покупка активов
        self.portfolio.buy("AAPL", 5)
        # Проверка остатка средств и количества активов
        self.assertEqual(self.portfolio.cash, 10000 - AssetPrice.AAPL.value * 5)
        self.assertEqual(self.portfolio.assets["AAPL"], 5)

    def test_sell(self):
        # Покупка активов
        self.portfolio.buy("AAPL", 5)
        # Продажа части активов
        self.portfolio.sell("AAPL", 3)
        # Проверка остатка средств и количества активов
        self.assertEqual(self.portfolio.cash, 10000 - AssetPrice.AAPL.value * 2)
        self.assertEqual(self.portfolio.assets["AAPL"], 2)

    def test_portfolio_value(self):
        # Покупка активов
        self.portfolio.buy("AAPL", 5)
        self.portfolio.buy("GOOGL", 2)

        # Рассчитываем ожидаемую оценку портфеля
        expected_value = self.portfolio.cash
        for asset, quantity in self.portfolio.assets.items():
            asset_price = AssetPrice.get_price(asset)
            expected_value += asset_price * Decimal(quantity)

        # Проверка оценки портфеля
        self.assertEqual(self.portfolio.portfolio_value, expected_value)


if __name__ == "__main__":
    unittest.main()
