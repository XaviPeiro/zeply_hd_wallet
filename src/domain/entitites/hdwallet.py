from abc import abstractmethod, ABC
from typing import Self

from bitcoinlib.keys import HDKey
from bitcoinlib.mnemonic import Mnemonic

from src.domain.entitites.coins.coin_factory import CoinFactory


class Wallet(ABC):

    @abstractmethod
    def generate_address(self, coin_code: str):
        ...


class HDWallet:
    _master_key: HDKey
    _index: int

    def __init__(self):
        self._master_key = HDKey()

    @property
    def master_key(self):
        return self._master_key.wif_private()

    @classmethod
    def create_with_mnemonic_words(cls, mnemonic_words: str = "") -> Self:
        mnemo = Mnemonic()
        mnemonic_words = mnemonic_words or mnemo.generate(strength=128)

        seed = mnemo.to_seed(mnemonic_words)
        master_key = HDKey.from_seed(seed)

        self = HDWallet()
        self._set_master_key(master_key=master_key)

        return self

    @classmethod
    def create_with_master_key(cls, wif_master_key: str):
        master_key = HDKey(wif_master_key)
        self = HDWallet()
        self._set_master_key(master_key=master_key)

        return self

    def _set_master_key(self, master_key: HDKey):
        self._master_key = master_key

    def get_child_private_key(self, index: int) -> str:
        self._index = index
        return self._master_key.child_private(index=index).private_hex

    def get_next_child_private_key(self) -> str:
        self._index += 1
        return self._master_key.child_private(index=self._index).private_hex

    def create_crypto_address(self, coin_code: str, private_key: str) -> str:
        coin = CoinFactory.create_coin(coin_code=coin_code)
        return coin.generate_address(private_key=private_key)

