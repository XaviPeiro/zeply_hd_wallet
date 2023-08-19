from src.domain.entitites.coins.bitcoin import Bitcoin, Coin
from src.domain.entitites.coins.ethereum import Ethereum


class CoinFactory:
    @staticmethod
    def create_coin(coin_code: str) -> Coin:
        coins = {
            "ETH": Ethereum,
            "BTC": Bitcoin
        }

        return coins.get(coin_code)()
