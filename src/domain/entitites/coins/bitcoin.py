import cryptos

from src.domain.entitites.coins.coin import Coin


class Bitcoin(Coin):
    code = "BTC"
    net: cryptos.Bitcoin

    def __init__(self):
        self.net = cryptos.Bitcoin(testnet=False)

    def generate_address(self, private_key) -> str:
        public_key = self.net.privtopub(private_key)
        address = self.net.pubtoaddr(public_key)

        return address
