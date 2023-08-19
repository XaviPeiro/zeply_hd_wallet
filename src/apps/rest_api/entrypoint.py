from typing import List

from fastapi import FastAPI, Depends
from pydantic import parse_obj_as
from sqlalchemy.orm import Session

from src.apps.rest_api.database import SessionLocal
from src.apps.rest_api.orm.models import Address
from src.apps.rest_api.schemas.schemas import CreateAddressSchema, ReadAddressSchema, ListReadAddressSchema
from src.domain.entitites.coins.coins_code import CoinsCode
from src.domain.services.generate_address import GenerateAddressService

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_all_addresses(db: Session) -> List[Address]:
    return db.query(Address).all()


def get_address_by_index(db: Session, index: int) -> Address:
    return db.query(Address).filter_by(index=index).one()


@app.get(path="/")
def root():
    return { "title": "Welcome to your wallet. Visit http://localhost:8081/docs.", }


@app.post(path="/address", status_code=201)
def create_address(coin_code: CreateAddressSchema, db: Session = Depends(get_db)):
    # Service to create address
    GenerateAddressService(session=db)(coin_code=coin_code.coin_code)


@app.get(path="/address/{id}", status_code=200, response_model=ReadAddressSchema)
def get_address(id:int, db: Session = Depends(get_db)):
    return get_address_by_index(db=db, index=id)


@app.get(path="/address", status_code=200, response_model=ListReadAddressSchema)
def list_addresses(db: Session = Depends(get_db)):
    addresses = get_all_addresses(db=db)
    return addresses

