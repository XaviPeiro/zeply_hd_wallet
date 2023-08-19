from pydantic import BaseModel, Field

from src.domain.entitites.coins.coins_code import CoinsCode


# TODO: Add enum
class CreateAddressSchema(BaseModel):
    coin_code: CoinsCode


class ReadAddressSchema(BaseModel):
    address: str
    index: int
    coin: str

    class Config:
        orm_mode = True


class ListReadAddressSchema(BaseModel):
    __root__: list[ReadAddressSchema]

    class Config:
        orm_mode = True
