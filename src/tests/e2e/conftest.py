import logging

import pytest
from sqlalchemy import create_engine, StaticPool
from sqlalchemy.orm import sessionmaker
from starlette.testclient import TestClient
import src.apps.rest_api.entrypoint as rest_entrypoint
from src.apps.rest_api.database import Base


@pytest.fixture(scope="session")
def client():
    SQLALCHEMY_DATABASE_URL = "sqlite://"

    engine = create_engine(
        SQLALCHEMY_DATABASE_URL,
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )
    TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    Base.metadata.create_all(bind=engine)

    def override_get_db():
        try:
            db = TestingSessionLocal()
            yield db
        finally:
            db.close()

    rest_entrypoint.app.dependency_overrides[rest_entrypoint.get_db] = override_get_db

    client = TestClient(rest_entrypoint.app)

    test_client = TestClient(rest_entrypoint.app)
    return test_client
