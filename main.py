from decimal import Decimal
from enum import Enum


class AssetPrice(Enum):
    LKOH = Decimal(5896)
    SBER = Decimal(250)
    AAPL = Decimal(150)
    MSFT = Decimal(300)
    GOOGL = Decimal(2500)
    TSLA = Decimal(700)

    @classmethod
    def get_price(cls, asset):
        return cls[asset].value


class Portfolio:
    def __init__(self, initial_cash):
        self.cash = Decimal(initial_cash)
        self.assets = {}  # Словарь для отслеживания количества каждого актива

    def buy(self, asset, quantity):
        # Метод для выполнения покупки активов
        asset_price = self.get_asset_price(asset)
        total_cost = asset_price * Decimal(quantity)

        if total_cost > self.cash:
            raise ValueError("Insufficient funds")

        if asset in self.assets:
            self.assets[asset] += quantity
        else:
            self.assets[asset] = quantity

        self.cash -= total_cost

    def sell(self, asset, quantity):
        # Метод для выполнения продажи активов
        asset_quantity = self.assets.get(asset, 0)
        if asset_quantity < quantity:
            raise ValueError("Not enough of this asset to sell")

        asset_price = self.get_asset_price(asset)
        total_value = asset_price * Decimal(quantity)

        self.assets[asset] -= quantity
        self.cash += total_value

    @property
    def portfolio_value(self):
        # Метод для вычисления стоимости портфеля
        total_value = self.cash

        for asset, quantity in self.assets.items():
            asset_price = self.get_asset_price(asset)
            total_value += asset_price * Decimal(quantity)

        return total_value

    @staticmethod
    def get_asset_price(asset):
        # Метод для получения цены актива из класса AssetPrice
        return AssetPrice.get_price(asset)

    def get_assets_list(self):
        # Метод для получения списка активов в портфеле
        return list(self.assets.keys())
