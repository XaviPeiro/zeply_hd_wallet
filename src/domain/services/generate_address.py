from dataclasses import dataclass
from typing import Optional

from sqlalchemy.orm import Session

from src.apps.rest_api.orm.models import MasterKey, Address
from src.domain.entitites.hdwallet import HDWallet


def get_last_master_key_address(session: Session) -> Optional[Address]:
    return session.query(Address).order_by(Address.index.desc()).first()


def get_or_create_master_key(session: Session) -> MasterKey:
    secrets_manager_cli = lambda x: None

    master_key = session.query(MasterKey).first()
    if master_key:
        return master_key
    else:
        master_key = HDWallet().master_key
        instance = MasterKey(master_key=master_key)
        session.add(instance)
        session.commit()
        return instance


def persist_address(session: Session, address: Address):
    session.add(address)
    session.commit()


@dataclass
class GenerateAddressService:
    session: Session

    def __call__(self, coin_code: str):
        # Get coin
        # get or create a private key
        master_key = get_or_create_master_key(session=self.session)
        last_master_key_address = get_last_master_key_address(session=self.session)
        next_index = 0 if not last_master_key_address else last_master_key_address.index + 1

        # create address from master private key
        wallet = HDWallet.create_with_master_key(wif_master_key=master_key.master_key)
        child_private_key = wallet.get_child_private_key(index=next_index)
        address_value = wallet.create_crypto_address(
            coin_code=coin_code,
            private_key=child_private_key
        )

        address = Address(
            index=next_index,
            private_key=child_private_key,
            address=address_value,
            master_key=master_key.id,
            coin=coin_code
        )

        # store data
        persist_address(session=self.session, address=address)

        return address
