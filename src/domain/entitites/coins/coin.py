from abc import ABC, abstractmethod


class Coin(ABC):
    @abstractmethod
    def generate_address(self, private_key) -> str:
        ...

