from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import mapped_column
from sqlalchemy_utils import StringEncryptedType
from ..database import Base


# Super secret encryption key that should not be here.
_encryption_key = b"ZaDfcTF7_60GrrY167zrrrd67pEvs0aGOa2oasOM1Pg="


class MasterKey(Base):
    __tablename__ = "master_key"

    id = Column(Integer, primary_key=True, index=True)
    # _master_key = Column(StringEncryptedType, name="master_key", unique=True, nullable=False)
    master_key = Column(StringEncryptedType(String, length=255, key=_encryption_key))


class Address(Base):
    __tablename__ = "addresses"

    address = Column(String, unique=True, nullable=False, primary_key=True)
    private_key = Column(String, nullable=False)
    master_key = mapped_column(ForeignKey("master_key.id"))
    index = Column(Integer, nullable=False)
    coin = mapped_column(String)
