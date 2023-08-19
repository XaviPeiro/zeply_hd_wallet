from src.domain.entitites.coins.coin import Coin
from eth_account import Account


class Ethereum(Coin):
    code = "ETH"

    def generate_address(self, private_key: str) -> str:
        account = Account.from_key(private_key)
        address = account.address
        return address

